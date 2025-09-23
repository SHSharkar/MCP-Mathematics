import ast
import datetime
import hashlib
import logging
import math
import operator
import re
import signal
import sys
import time
from typing import Any, Union

from mcp.server import FastMCP

MAX_EXPRESSION_LENGTH = 1000
MAX_EXPRESSION_DEPTH = 10
MAX_HISTORY_SIZE = 100
MAX_FACTORIAL_INPUT = 170
MAX_POWER_EXPONENT = 1000

COMPUTATION_TIMEOUT = 50.0
ENABLE_AUDIT_LOGGING = True

MAX_COMPUTATION_TIME = 20.0
MAX_RECURSIVE_CALLS = 1000
ENABLE_RATE_LIMITING = True
RATE_LIMIT_WINDOW = 60
MAX_REQUESTS_PER_WINDOW = 100000
ENABLE_INPUT_HASHING = True

FORBIDDEN_PATTERNS = [
    r'import\s+',
    r'exec\s*\(',
    r'eval\s*\(',
    r'__.*__',
    r'globals\s*\(',
    r'locals\s*\(',
    r'getattr\s*\(',
    r'setattr\s*\(',
    r'delattr\s*\(',
    r'hasattr\s*\(',
]

_request_history: dict[str, list[float]] = {}
_computation_stats: dict[str, dict[str, Any]] = {}

_expression_cache: dict[str, tuple[str, float]] = {}
_ast_cache: dict[str, ast.AST] = {}
CACHE_TTL = 300
MAX_CACHE_SIZE = 1000

logger = logging.getLogger(__name__)

security_logger = logging.getLogger(f"{__name__}.security")
security_logger.setLevel(logging.INFO)

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

MATH_FUNCTIONS = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "atan2": math.atan2,
    "sinh": math.sinh,
    "cosh": math.cosh,
    "tanh": math.tanh,
    "asinh": math.asinh,
    "acosh": math.acosh,
    "atanh": math.atanh,
    "log": math.log,
    "log10": math.log10,
    "log2": math.log2,
    "exp": math.exp,
    "sqrt": math.sqrt,
    "pow": math.pow,
    "fabs": math.fabs,
    "factorial": math.factorial,
    "ceil": math.ceil,
    "floor": math.floor,
    "trunc": math.trunc,
    "degrees": math.degrees,
    "radians": math.radians,
    "gcd": math.gcd,
    "lcm": getattr(math, "lcm", None),
    "isqrt": getattr(math, "isqrt", None),
    "hypot": math.hypot,
    "copysign": math.copysign,
    "fmod": math.fmod,
    "remainder": math.remainder,
    "modf": math.modf,
    "frexp": math.frexp,
    "ldexp": math.ldexp,
    "isfinite": math.isfinite,
    "isinf": math.isinf,
    "isnan": math.isnan,
    "isclose": math.isclose,
    "comb": getattr(math, "comb", None),
    "perm": getattr(math, "perm", None),
    "erf": math.erf,
    "erfc": math.erfc,
    "gamma": math.gamma,
    "lgamma": math.lgamma,
    "cbrt": getattr(math, "cbrt", None),
    "exp2": getattr(math, "exp2", None),
    "expm1": math.expm1,
    "log1p": math.log1p,
    "nextafter": getattr(math, "nextafter", None),
    "ulp": getattr(math, "ulp", None),
}

MATH_CONSTANTS = {
    "pi": math.pi,
    "e": math.e,
    "tau": math.tau,
    "inf": math.inf,
    "nan": math.nan,
}

MATH_FUNCTIONS = {k: v for k, v in MATH_FUNCTIONS.items() if v is not None}


class CalculationHistory:
    def __init__(self, max_size: int = MAX_HISTORY_SIZE):
        self.history: list[dict[str, Any]] = []
        self.max_size = max_size

    def add(self, expression: str, result: str) -> None:
        entry = {
            "expression": expression,
            "result": result,
            "timestamp": datetime.datetime.now().isoformat(),
        }
        self.history.append(entry)
        if len(self.history) > self.max_size:
            self.history.pop(0)

        if ENABLE_AUDIT_LOGGING:
            logger.info(f"Added calculation: {expression} = {result}")

    def get_recent(self, limit: int = 10) -> list[dict[str, Any]]:
        return self.history[-limit:]

    def clear(self) -> None:
        if ENABLE_AUDIT_LOGGING:
            logger.info("Calculation history cleared")
        self.history.clear()


calculation_history = CalculationHistory()


def validate_input_security(expression: str, client_id: str = "default") -> bool:
    current_time = time.time()

    if ENABLE_RATE_LIMITING:
        if client_id not in _request_history:
            _request_history[client_id] = []

        _request_history[client_id] = [
            req_time for req_time in _request_history[client_id]
            if current_time - req_time < RATE_LIMIT_WINDOW
        ]

        if len(_request_history[client_id]) >= MAX_REQUESTS_PER_WINDOW:
            security_logger.warning(f"Rate limit exceeded for client: {client_id}")
            raise PermissionError(
                f"Rate limit exceeded: {MAX_REQUESTS_PER_WINDOW} requests per {RATE_LIMIT_WINDOW} seconds"
            )

        _request_history[client_id].append(current_time)

    for pattern in FORBIDDEN_PATTERNS:
        if re.search(pattern, expression, re.IGNORECASE):
            security_logger.error(f"Forbidden pattern detected in expression: {pattern}")
            raise ValueError(f"Expression contains forbidden pattern: {pattern}")

    suspicious_chars = ['\\x00', '\\n', '\\r', '\\t', '\\b', '\\f', '\\v']
    if any(char in expression for char in suspicious_chars):
        security_logger.error(f"Control characters detected in expression")
        raise ValueError("Expression contains invalid control characters")

    normalized = expression.encode('ascii', 'ignore').decode('ascii')
    if len(normalized) != len(expression):
        security_logger.warning(f"Non-ASCII characters detected in expression")

    if ENABLE_INPUT_HASHING:
        input_hash = hashlib.sha256(expression.encode()).hexdigest()[:16]
        security_logger.info(f"Processing expression hash: {input_hash}")

    return True


def monitor_computation_performance(expression: str, start_time: float, end_time: float) -> None:
    computation_time = end_time - start_time
    expression_hash = hashlib.sha256(expression.encode()).hexdigest()[:16]

    if expression_hash not in _computation_stats:
        _computation_stats[expression_hash] = {
            "count": 0,
            "total_time": 0.0,
            "max_time": 0.0,
            "first_seen": start_time,
            "last_seen": end_time
        }

    stats = _computation_stats[expression_hash]
    stats["count"] += 1
    stats["total_time"] += computation_time
    stats["max_time"] = max(stats["max_time"], computation_time)
    stats["last_seen"] = end_time

    if computation_time > MAX_COMPUTATION_TIME:
        security_logger.warning(
            f"Slow computation detected: {computation_time:.3f}s for expression hash {expression_hash}"
        )

    if ENABLE_AUDIT_LOGGING and computation_time > 0.1:
        logger.info(
            f"Performance: {computation_time:.3f}s for expression hash {expression_hash} "
            f"(count: {stats['count']}, avg: {stats['total_time']/stats['count']:.3f}s)"
        )


def cleanup_caches() -> None:
    current_time = time.time()

    expired_keys = [
        key for key, (_, timestamp) in _expression_cache.items()
        if current_time - timestamp > CACHE_TTL
    ]
    for key in expired_keys:
        del _expression_cache[key]

    if len(_expression_cache) > MAX_CACHE_SIZE:
        sorted_items = sorted(
            _expression_cache.items(),
            key=lambda x: x[1][1]
        )
        items_to_remove = len(_expression_cache) - MAX_CACHE_SIZE
        for key, _ in sorted_items[:items_to_remove]:
            del _expression_cache[key]

    if len(_ast_cache) > MAX_CACHE_SIZE:
        keys_to_remove = list(_ast_cache.keys())[: len(_ast_cache) // 2]
        for key in keys_to_remove:
            del _ast_cache[key]

    if len(_computation_stats) > MAX_CACHE_SIZE * 2:
        oldest_keys = sorted(
            _computation_stats.keys(),
            key=lambda k: _computation_stats[k]["last_seen"]
        )[: len(_computation_stats) // 2]
        for key in oldest_keys:
            del _computation_stats[key]


def get_cached_result(expression: str) -> str | None:
    if expression not in _expression_cache:
        return None

    result, timestamp = _expression_cache[expression]
    if time.time() - timestamp > CACHE_TTL:
        del _expression_cache[expression]
        return None

    return result


def cache_result(expression: str, result: str) -> None:
    _expression_cache[expression] = (result, time.time())

    if len(_expression_cache) % 100 == 0:
        cleanup_caches()


def get_cached_ast(expression: str) -> ast.AST | None:
    return _ast_cache.get(expression)


def cache_ast(expression: str, tree: ast.AST) -> None:
    _ast_cache[expression] = tree


def sanitize_expression(expr: str) -> str:
    sanitized = ''.join(char for char in expr if ord(char) >= 32 or char in ' \\t')

    sanitized = ' '.join(sanitized.split())

    dangerous_sequences = ['..', '__', '$$', '@@', '##']
    for seq in dangerous_sequences:
        sanitized = sanitized.replace(seq, '')

    return sanitized


def preprocess_expression(expr: str) -> str:
    expr = expr.replace("×", "*")
    expr = expr.replace("÷", "/")
    expr = expr.replace("^", "**")
    return expr


def validate_ast_node(node: ast.AST, depth: int = 0) -> bool:
    if depth > MAX_EXPRESSION_DEPTH:
        raise ValueError(f"Expression too complex (max depth: {MAX_EXPRESSION_DEPTH})")
    if isinstance(node, ast.Expression):
        return validate_ast_node(node.body, depth + 1)

    if isinstance(node, ast.Constant):
        return isinstance(node.value, (int, float, complex))

    if isinstance(node, ast.Name):
        return node.id in MATH_CONSTANTS or node.id in MATH_FUNCTIONS

    if isinstance(node, ast.UnaryOp):
        return type(node.op) in OPERATORS and validate_ast_node(node.operand, depth + 1)

    if isinstance(node, ast.BinOp):
        return (
            type(node.op) in OPERATORS
            and validate_ast_node(node.left, depth + 1)
            and validate_ast_node(node.right, depth + 1)
        )

    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            return False
        if node.func.id not in MATH_FUNCTIONS:
            return False
        if node.keywords:
            return False
        return all(validate_ast_node(arg, depth + 1) for arg in node.args)

    return False


def eval_node(node: ast.AST) -> int | float | complex:
    if isinstance(node, ast.Expression):
        return eval_node(node.body)

    if isinstance(node, ast.Constant):
        return node.value

    if isinstance(node, ast.Name):
        if node.id in MATH_CONSTANTS:
            return MATH_CONSTANTS[node.id]
        raise ValueError(f"Unknown constant: {node.id}")

    if isinstance(node, ast.UnaryOp):
        op = OPERATORS[type(node.op)]
        operand = eval_node(node.operand)
        return op(operand)

    if isinstance(node, ast.BinOp):
        op = OPERATORS[type(node.op)]
        left = eval_node(node.left)
        right = eval_node(node.right)

        if isinstance(node.op, ast.Pow) and abs(right) > MAX_POWER_EXPONENT:
            raise ValueError(f"Power exponent too large (max: {MAX_POWER_EXPONENT})")

        try:
            return op(left, right)
        except (OverflowError, ZeroDivisionError) as e:
            raise ValueError(f"Mathematical operation failed: {str(e)}") from e

    if isinstance(node, ast.Call):
        func_name = node.func.id
        func = MATH_FUNCTIONS[func_name]
        args = [eval_node(arg) for arg in node.args]

        if func_name == "factorial" and len(args) == 1:
            if args[0] > MAX_FACTORIAL_INPUT:
                raise ValueError(f"Factorial input too large (max: {MAX_FACTORIAL_INPUT})")
            if args[0] < 0 or not isinstance(args[0], int):
                raise ValueError("Factorial requires non-negative integer")

        elif func_name == "pow" and len(args) == 2:
            if abs(args[1]) > MAX_POWER_EXPONENT:
                raise ValueError(f"Power exponent too large (max: {MAX_POWER_EXPONENT})")

        try:
            return func(*args)
        except (OverflowError, ValueError) as e:
            raise ValueError(f"Mathematical operation failed: {str(e)}") from e

    raise ValueError(f"Unsupported node type: {type(node).__name__}")


def evaluate(expression: str) -> str:
    start_time = time.time()

    try:
        if ENABLE_AUDIT_LOGGING:
            logger.info(f"Evaluating expression: {expression}")

        validate_input_security(expression)

        expression = expression.strip()
        if not expression:
            raise SyntaxError("Empty expression")

        if len(expression) > MAX_EXPRESSION_LENGTH:
            raise ValueError(f"Expression too long (max: {MAX_EXPRESSION_LENGTH} characters)")

        original_expression = expression

        cached_result = get_cached_result(original_expression)
        if cached_result is not None:
            if ENABLE_AUDIT_LOGGING:
                logger.info(f"Cache hit for expression: {original_expression}")
            return cached_result

        expression = sanitize_expression(expression)
        expression = preprocess_expression(expression)

        tree = get_cached_ast(expression)
        if tree is None:
            try:
                tree = ast.parse(expression, mode="eval")
                cache_ast(expression, tree)
            except SyntaxError as e:
                raise SyntaxError(f"Invalid mathematical expression: {str(e)}") from e
        else:
            if ENABLE_AUDIT_LOGGING:
                logger.info(f"AST cache hit for expression: {expression}")

        if not validate_ast_node(tree):
            raise ValueError("Expression contains unsupported operations")

        result = eval_node(tree)

        has_division = "/" in original_expression or "÷" in original_expression
        has_float_operand = "." in original_expression

        if (
            isinstance(result, float)
            and result.is_integer()
            and not has_division
            and not has_float_operand
        ):
            result_str = str(int(result))
        else:
            result_str = str(result)

        calculation_history.add(original_expression, result_str)

        cache_result(original_expression, result_str)

        end_time = time.time()

        monitor_computation_performance(original_expression, start_time, end_time)

        if ENABLE_AUDIT_LOGGING:
            logger.info(f"Successfully evaluated: {original_expression} = {result_str}")

        return result_str

    except (SyntaxError, ValueError, ZeroDivisionError, TypeError, AttributeError) as e:
        if ENABLE_AUDIT_LOGGING:
            logger.warning(f"Evaluation failed for '{expression}': {str(e)}")
        raise e
    except Exception as e:
        if ENABLE_AUDIT_LOGGING:
            logger.error(f"Unexpected error evaluating '{expression}': {str(e)}")
        raise ValueError(f"Calculation error: {str(e)}") from e


async def evaluate_expression(expression: str) -> str:
    return evaluate(expression)


_shutdown_requested = False
_active_computations = 0


def signal_handler(signum: int, frame: Any) -> None:
    global _shutdown_requested
    _shutdown_requested = True

    signal_name = signal.Signals(signum).name
    logger.info(f"Received {signal_name} signal, initiating graceful shutdown")

    if _active_computations > 0:
        logger.info(f"Waiting for {_active_computations} active computations to complete")
    else:
        logger.info("No active computations, shutting down immediately")


signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

mcp = FastMCP("MCP Math")


@mcp.tool()
async def get_system_metrics() -> str:
    current_time = time.time()
    metrics = ["MCP Math System Metrics:"]
    metrics.append("="*40)

    total_computations = sum(stats["count"] for stats in _computation_stats.values())
    total_time = sum(stats["total_time"] for stats in _computation_stats.values())
    avg_time = total_time / total_computations if total_computations > 0 else 0

    metrics.append(f"Total Computations: {total_computations}")
    metrics.append(f"Average Computation Time: {avg_time:.3f}s")
    metrics.append(f"Active Computations: {_active_computations}")

    active_clients = len(_request_history)
    total_requests = sum(len(requests) for requests in _request_history.values())
    metrics.append(f"Active Clients: {active_clients}")
    metrics.append(f"Total Requests (current window): {total_requests}")

    history_size = len(calculation_history.history)
    metrics.append(f"History Entries: {history_size}/{MAX_HISTORY_SIZE}")

    metrics.append(f"Security Monitoring: {'Enabled' if ENABLE_AUDIT_LOGGING else 'Disabled'}")
    metrics.append(f"Rate Limiting: {'Enabled' if ENABLE_RATE_LIMITING else 'Disabled'}")

    metrics.append("\\nConfiguration:")
    metrics.append(f"  Max Expression Length: {MAX_EXPRESSION_LENGTH}")
    metrics.append(f"  Max Expression Depth: {MAX_EXPRESSION_DEPTH}")
    metrics.append(f"  Max Computation Time: {MAX_COMPUTATION_TIME}s")
    metrics.append(f"  Available Functions: {len(MATH_FUNCTIONS)}")

    return "\\n".join(metrics)


@mcp.tool()
async def get_security_status() -> str:
    current_time = time.time()
    security_info = ["MCP Math Security Status:"]
    security_info.append("="*35)

    security_info.append("Rate Limiting:")
    security_info.append(f"  Status: {'Enabled' if ENABLE_RATE_LIMITING else 'Disabled'}")
    security_info.append(f"  Window: {RATE_LIMIT_WINDOW}s")
    security_info.append(f"  Max Requests: {MAX_REQUESTS_PER_WINDOW}")
    security_info.append(f"  Active Clients: {len(_request_history)}")

    security_info.append("\\nThreat Detection:")
    security_info.append(f"  Forbidden Patterns: {len(FORBIDDEN_PATTERNS)}")
    security_info.append(f"  Input Hashing: {'Enabled' if ENABLE_INPUT_HASHING else 'Disabled'}")

    security_info.append("\\nAudit Configuration:")
    security_info.append(f"  Audit Logging: {'Enabled' if ENABLE_AUDIT_LOGGING else 'Disabled'}")
    security_info.append(f"  Security Logger: Active")

    security_info.append("\\nResource Limits:")
    security_info.append(f"  Max Factorial: {MAX_FACTORIAL_INPUT}")
    security_info.append(f"  Max Power Exponent: {MAX_POWER_EXPONENT}")
    security_info.append(f"  Max Recursive Calls: {MAX_RECURSIVE_CALLS}")

    return "\\n".join(security_info)


@mcp.tool()
async def calculate(expression: str) -> str:
    global _active_computations

    if _shutdown_requested:
        return "Error: Server is shutting down, not accepting new requests"

    _active_computations += 1

    try:
        result = evaluate(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        _active_computations -= 1


@mcp.tool()
async def batch_calculate(expressions: list[str]) -> str:
    results = []
    for expr in expressions:
        try:
            result = evaluate(expr)
            results.append(f"{expr} = {result}")
        except Exception as e:
            results.append(f"{expr} = Error: {str(e)}")
    return "\\n".join(results)


@mcp.tool()
async def get_calculation_history(limit: int = 10) -> str:
    if limit > MAX_HISTORY_SIZE:
        limit = MAX_HISTORY_SIZE

    history = calculation_history.get_recent(limit)
    if not history:
        return "No calculation history available."

    lines = ["Recent Calculations:"]
    for entry in history:
        lines.append(f"  {entry['expression']} = {entry['result']} ({entry['timestamp']})")
    return "\\n".join(lines)


@mcp.tool()
async def clear_history() -> str:
    calculation_history.clear()
    return "Calculation history cleared successfully"


@mcp.tool()
async def list_functions() -> str:
    lines = ["Available Mathematical Functions and Constants:"]
    lines.append("\\nFunctions:")
    for func in sorted(MATH_FUNCTIONS.keys()):
        lines.append(f"  {func}")
    lines.append("\\nConstants:")
    for const in sorted(MATH_CONSTANTS.keys()):
        lines.append(f"  {const}")
    lines.append("\\nOperators:")
    lines.append("  +, -, *, /, //, %, **, ×, ÷, ^")
    return "\\n".join(lines)


@mcp.resource("history://recent")
async def get_recent_history() -> str:
    history = calculation_history.get_recent(20)
    if not history:
        return "No calculation history available."

    lines = ["Recent Calculations:"]
    for entry in history:
        lines.append(f"  {entry['expression']} = {entry['result']}")
    return "\\n".join(lines)


@mcp.resource("functions://available")
async def get_available_functions() -> str:
    lines = ["Available Mathematical Functions:"]

    lines.append("\\nTrigonometric:")
    for func in ["sin", "cos", "tan", "asin", "acos", "atan"]:
        if func in MATH_FUNCTIONS:
            lines.append(f"  {func}")

    lines.append("\\nHyperbolic:")
    for func in ["sinh", "cosh", "tanh", "asinh", "acosh", "atanh"]:
        if func in MATH_FUNCTIONS:
            lines.append(f"  {func}")

    lines.append("\\nLogarithmic:")
    for func in ["log", "log10", "log2", "exp"]:
        if func in MATH_FUNCTIONS:
            lines.append(f"  {func}")

    lines.append("\\nOther:")
    other_funcs = sorted(
        set(MATH_FUNCTIONS.keys())
        - {
            "sin",
            "cos",
            "tan",
            "asin",
            "acos",
            "atan",
            "sinh",
            "cosh",
            "tanh",
            "asinh",
            "acosh",
            "atanh",
            "log",
            "log10",
            "log2",
            "exp",
        }
    )
    for func in other_funcs:
        lines.append(f"  {func}")

    return "\\n".join(lines)


@mcp.resource("constants://math")
async def get_math_constants() -> str:
    lines = ["Mathematical Constants:"]
    lines.append(f"  pi = {math.pi}")
    lines.append(f"  e = {math.e}")
    lines.append(f"  tau = {math.tau}")
    lines.append("  inf = infinity")
    lines.append("  nan = not a number")
    return "\\n".join(lines)


@mcp.prompt()
async def scientific_calculation() -> str:
    return """I need help with scientific calculations. Here are some examples:

Basic Operations:
- Addition: 2 + 3
- Subtraction: 10 - 4
- Multiplication: 5 * 6 or 5 × 6
- Division: 15 / 3 or 15 ÷ 3
- Power: 2 ** 3 or 2 ^ 3

Scientific Functions:
- Trigonometry: sin(pi/2), cos(0), tan(pi/4)
- Logarithms: log(10), log10(100), log2(8)
- Square root: sqrt(16)
- Exponential: exp(1)

What calculation would you like me to perform?"""


@mcp.prompt()
async def batch_calculation() -> str:
    return """I need to process multiple calculations at once.

Example: ["2 + 2", "sin(pi/2)", "sqrt(16) * cos(0)", "factorial(5)", "log10(1000)"]

What expressions would you like to calculate?"""


def main() -> None:
    if ENABLE_AUDIT_LOGGING:
        logger.info("Starting MCP Math server with production configuration")
        logger.info(f"Available functions: {len(MATH_FUNCTIONS)}")
        logger.info(f"Security limits: expression_length={MAX_EXPRESSION_LENGTH}, depth={MAX_EXPRESSION_DEPTH}")

    try:
        mcp.run()
    except Exception as e:
        if ENABLE_AUDIT_LOGGING:
            logger.critical(f"Failed to start MCP Math server: {str(e)}")
        raise


if __name__ == "__main__":
    main()