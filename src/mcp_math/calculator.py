import ast
import math
import operator
from typing import Any

from mcp.server import FastMCP

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
    def __init__(self, max_size: int = 100):
        self.history: list[dict[str, Any]] = []
        self.max_size = max_size

    def add(self, expression: str, result: str) -> None:
        import datetime

        entry = {
            "expression": expression,
            "result": result,
            "timestamp": datetime.datetime.now().isoformat(),
        }
        self.history.append(entry)
        if len(self.history) > self.max_size:
            self.history.pop(0)

    def get_recent(self, limit: int = 10) -> list[dict[str, Any]]:
        return self.history[-limit:]

    def clear(self) -> None:
        self.history.clear()


calculation_history = CalculationHistory()


def preprocess_expression(expr: str) -> str:
    expr = expr.replace("×", "*")
    expr = expr.replace("÷", "/")
    expr = expr.replace("^", "**")
    return expr


def validate_ast_node(node: ast.AST) -> bool:
    if isinstance(node, ast.Expression):
        return validate_ast_node(node.body)

    if isinstance(node, ast.Constant):
        return isinstance(node.value, (int, float, complex))

    if isinstance(node, ast.Name):
        return node.id in MATH_CONSTANTS or node.id in MATH_FUNCTIONS

    if isinstance(node, ast.UnaryOp):
        return type(node.op) in OPERATORS and validate_ast_node(node.operand)

    if isinstance(node, ast.BinOp):
        return (
            type(node.op) in OPERATORS
            and validate_ast_node(node.left)
            and validate_ast_node(node.right)
        )

    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            return False
        if node.func.id not in MATH_FUNCTIONS:
            return False
        if node.keywords:
            return False
        return all(validate_ast_node(arg) for arg in node.args)

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
        return op(left, right)

    if isinstance(node, ast.Call):
        func_name = node.func.id
        func = MATH_FUNCTIONS[func_name]
        args = [eval_node(arg) for arg in node.args]
        return func(*args)

    raise ValueError(f"Unsupported node type: {type(node).__name__}")


def evaluate(expression: str) -> str:
    try:
        expression = expression.strip()
        if not expression:
            raise SyntaxError("Empty expression")

        original_expression = expression
        expression = preprocess_expression(expression)
        tree = ast.parse(expression, mode="eval")

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

        calculation_history.add(expression, result_str)
        return result_str

    except (SyntaxError, ValueError, ZeroDivisionError, TypeError, AttributeError) as e:
        raise e
    except Exception as e:
        raise ValueError(f"Calculation error: {str(e)}") from e


async def evaluate_expression(expression: str) -> str:
    return evaluate(expression)


mcp = FastMCP("MCP Math")


@mcp.tool()
async def calculate(expression: str) -> str:
    """Evaluate a mathematical expression."""
    try:
        result = evaluate(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
async def batch_calculate(expressions: list[str]) -> str:
    """Process multiple mathematical expressions."""
    results = []
    for expr in expressions:
        try:
            result = evaluate(expr)
            results.append(f"{expr} = {result}")
        except Exception as e:
            results.append(f"{expr} = Error: {str(e)}")
    return "\n".join(results)


@mcp.tool()
async def get_calculation_history(limit: int = 10) -> str:
    """Retrieve recent calculation history."""
    history = calculation_history.get_recent(limit)
    if not history:
        return "No calculation history available."

    lines = ["Recent Calculations:"]
    for entry in history:
        lines.append(f"  {entry['expression']} = {entry['result']} ({entry['timestamp']})")
    return "\n".join(lines)


@mcp.tool()
async def clear_history() -> str:
    """Clear the calculation history."""
    calculation_history.clear()
    return "Calculation history cleared successfully"


@mcp.tool()
async def list_functions() -> str:
    """List available mathematical functions and constants."""
    lines = ["Available Mathematical Functions and Constants:"]
    lines.append("\nFunctions:")
    for func in sorted(MATH_FUNCTIONS.keys()):
        lines.append(f"  {func}")
    lines.append("\nConstants:")
    for const in sorted(MATH_CONSTANTS.keys()):
        lines.append(f"  {const}")
    lines.append("\nOperators:")
    lines.append("  +, -, *, /, //, %, **, ×, ÷, ^")
    return "\n".join(lines)


@mcp.resource("history://recent")
async def get_recent_history() -> str:
    """Access recent calculation history as a resource."""
    history = calculation_history.get_recent(20)
    if not history:
        return "No calculation history available."

    lines = ["Recent Calculations:"]
    for entry in history:
        lines.append(f"  {entry['expression']} = {entry['result']}")
    return "\n".join(lines)


@mcp.resource("functions://available")
async def get_available_functions() -> str:
    """Get list of all available mathematical functions."""
    lines = ["Available Mathematical Functions:"]

    lines.append("\nTrigonometric:")
    for func in ["sin", "cos", "tan", "asin", "acos", "atan"]:
        if func in MATH_FUNCTIONS:
            lines.append(f"  {func}")

    lines.append("\nHyperbolic:")
    for func in ["sinh", "cosh", "tanh", "asinh", "acosh", "atanh"]:
        if func in MATH_FUNCTIONS:
            lines.append(f"  {func}")

    lines.append("\nLogarithmic:")
    for func in ["log", "log10", "log2", "exp"]:
        if func in MATH_FUNCTIONS:
            lines.append(f"  {func}")

    lines.append("\nOther:")
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

    return "\n".join(lines)


@mcp.resource("constants://math")
async def get_math_constants() -> str:
    """Get all available mathematical constants."""
    lines = ["Mathematical Constants:"]
    lines.append(f"  pi = {math.pi}")
    lines.append(f"  e = {math.e}")
    lines.append(f"  tau = {math.tau}")
    lines.append("  inf = infinity")
    lines.append("  nan = not a number")
    return "\n".join(lines)


@mcp.prompt()
async def scientific_calculation() -> str:
    """Template for scientific calculations."""
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
    """Template for batch calculations."""
    return """I need to process multiple calculations at once.

Example: ["2 + 2", "sin(pi/2)", "sqrt(16) * cos(0)", "factorial(5)", "log10(1000)"]

What expressions would you like to calculate?"""


def main():
    mcp.run()


if __name__ == "__main__":
    main()
