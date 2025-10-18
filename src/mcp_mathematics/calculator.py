import ast
import cmath
import datetime
import math
import operator
import re
import resource
import statistics
import threading
import time
from collections import OrderedDict, deque
from contextlib import contextmanager
from dataclasses import dataclass, field
from threading import RLock
from typing import Annotated, Any

from fastmcp import Context, FastMCP
from mcp.types import ToolAnnotations


@dataclass
class MatrixOperationChoice:
    matrix_operation_type: str


@dataclass
class NumberTheoryOperationChoice:
    number_theory_operation_type: str


@dataclass
class StatisticsOperationChoice:
    statistical_operation_type: str


MAXIMUM_MATHEMATICAL_EXPRESSION_CHARACTER_LIMIT = 1000
MAXIMUM_AST_NODE_DEPTH_LIMIT = 10
CALCULATION_HISTORY_ENTRY_LIMIT = 100
FACTORIAL_COMPUTATION_UPPER_BOUND = 300
EXPONENTIATION_SAFETY_THRESHOLD = 10000
MAXIMUM_COMPUTATION_RESULT_CHARACTER_LIMIT = 10000
MAXIMUM_MEMORY_USAGE_MEGABYTES = 512
MAXIMUM_LIST_ELEMENT_COUNT_LIMIT = 10000

MATHEMATICAL_OPERATION_TIMEOUT_SECONDS = 15.0
SECURITY_AUDIT_LOGGING_ENABLED = True

MAXIMUM_COMPUTATION_DURATION_SECONDS = 20.0
MAXIMUM_RECURSIVE_FUNCTION_CALL_DEPTH = 1000
ENABLE_RATE_LIMITING = True
RATE_LIMIT_WINDOW = 60
MAXIMUM_CLIENT_REQUESTS_PER_TIME_WINDOW = 1000000
ENABLE_INPUT_HASHING = True

FORBIDDEN_PATTERNS = [
    r"import\s+",
    r"exec\s*\(",
    r"eval\s*\(",
    r"__.*__",
    r"globals\s*\(",
    r"locals\s*\(",
    r"getattr\s*\(",
    r"setattr\s*\(",
    r"delattr\s*\(",
    r"hasattr\s*\(",
]

_expression_cache_lock = RLock()
_computation_metrics_lock = RLock()
_calculation_history_lock = RLock()
_session_variables_lock = RLock()
_rate_limiting_lock = RLock()

CACHE_TIME_TO_LIVE_SECONDS = 300
MAXIMUM_CACHE_SIZE = 1000
MAXIMUM_SESSION_TIME_TO_LIVE_SECONDS = 3600
MAXIMUM_SESSIONS = 100
MAXIMUM_COMPUTATION_STATISTICS = 500
SESSION_CLEANUP_INTERVAL = 600

_memory_cleanup_timer = None


class LRUExpressionCache:
    def __init__(self, max_size: int = MAXIMUM_CACHE_SIZE):
        self.max_size = max_size
        self.cache = OrderedDict()
        self.lock = RLock()

    def get(self, key: str) -> Any:
        with self.lock:
            if key not in self.cache:
                return None
            self.cache.move_to_end(key)
            return self.cache[key]

    def set(self, key: str, value: Any) -> None:
        with self.lock:
            if key in self.cache:
                self.cache.move_to_end(key)
            elif len(self.cache) >= self.max_size:
                self.cache.popitem(last=False)
            self.cache[key] = value

    def clear(self) -> None:
        with self.lock:
            self.cache.clear()

    def size(self) -> int:
        with self.lock:
            return len(self.cache)


class TTLResultCache:
    def __init__(
        self, max_size: int = MAXIMUM_CACHE_SIZE, time_to_live: float = CACHE_TIME_TO_LIVE_SECONDS
    ):
        self.max_size = max_size
        self.time_to_live = time_to_live
        self.cache = OrderedDict()
        self.lock = RLock()

    def get(self, key: str) -> Any:
        with self.lock:
            if key not in self.cache:
                return None
            value, timestamp = self.cache[key]
            if time.time() - timestamp > self.time_to_live:
                del self.cache[key]
                return None
            self.cache.move_to_end(key)
            return value

    def set(self, key: str, value: Any) -> None:
        with self.lock:
            current_time = time.time()
            if key in self.cache:
                self.cache.move_to_end(key)
            elif len(self.cache) >= self.max_size:
                self.cache.popitem(last=False)
            self.cache[key] = (value, current_time)

    def cleanup_expired(self) -> int:
        with self.lock:
            current_time = time.time()
            expired_keys = [
                key
                for key, (_, timestamp) in self.cache.items()
                if current_time - timestamp > self.time_to_live
            ]
            for key in expired_keys:
                del self.cache[key]
            return len(expired_keys)

    def clear(self) -> None:
        with self.lock:
            self.cache.clear()

    def size(self) -> int:
        with self.lock:
            return len(self.cache)


class CalculationSessionManager:
    def __init__(
        self,
        max_sessions: int = MAXIMUM_SESSIONS,
        session_time_to_live: float = MAXIMUM_SESSION_TIME_TO_LIVE_SECONDS,
    ):
        self.max_sessions = max_sessions
        self.session_time_to_live = session_time_to_live
        self.sessions = OrderedDict()
        self.session_timestamps = {}
        self.lock = RLock()
        self.started = False

    def _ensure_started(self):
        if not self.started:
            self.started = True

    def create_session(self, session_id: str, variables: dict[str, float | complex] = None) -> None:
        with self.lock:
            current_time = time.time()
            if len(self.sessions) >= self.max_sessions:
                oldest_session = next(iter(self.sessions))
                del self.sessions[oldest_session]
                del self.session_timestamps[oldest_session]

            self.sessions[session_id] = variables or {}
            self.session_timestamps[session_id] = current_time

    def get_session(self, session_id: str) -> dict[str, float | complex] | None:
        with self.lock:
            if session_id not in self.sessions:
                return None
            current_time = time.time()
            if current_time - self.session_timestamps[session_id] > self.session_time_to_live:
                del self.sessions[session_id]
                del self.session_timestamps[session_id]
                return None
            self.session_timestamps[session_id] = current_time
            self.sessions.move_to_end(session_id)
            return self.sessions[session_id]

    def update_session(self, session_id: str, key: str, value: float | complex) -> bool:
        with self.lock:
            session = self.get_session(session_id)
            if session is None:
                return False
            session[key] = value
            return True

    def delete_session(self, session_id: str) -> bool:
        with self.lock:
            if session_id in self.sessions:
                del self.sessions[session_id]
                del self.session_timestamps[session_id]
                return True
            return False

    def cleanup_expired(self) -> int:
        with self.lock:
            current_time = time.time()
            expired_sessions = [
                session_id
                for session_id, timestamp in self.session_timestamps.items()
                if current_time - timestamp > self.session_time_to_live
            ]
            for session_id in expired_sessions:
                del self.sessions[session_id]
                del self.session_timestamps[session_id]
            return len(expired_sessions)

    def shutdown(self) -> None:
        pass

    def get_stats(self) -> dict[str, Any]:
        with self.lock:
            return {
                "active_sessions": len(self.sessions),
                "max_sessions": self.max_sessions,
                "session_time_to_live": self.session_time_to_live,
            }


_expression_cache = None
_parsed_expression_ast_cache = None
_computation_stats = None
_session_manager = None


def _get_expression_cache():
    global _expression_cache
    if _expression_cache is None:
        _expression_cache = TTLResultCache(MAXIMUM_CACHE_SIZE, CACHE_TIME_TO_LIVE_SECONDS)
    return _expression_cache


def _get_parsed_cache():
    global _parsed_expression_ast_cache
    if _parsed_expression_ast_cache is None:
        _parsed_expression_ast_cache = LRUExpressionCache(MAXIMUM_CACHE_SIZE)
    return _parsed_expression_ast_cache


def _get_computation_stats():
    global _computation_stats
    if _computation_stats is None:
        _computation_stats = LRUExpressionCache(MAXIMUM_COMPUTATION_STATISTICS)
    return _computation_stats


def _get_session_manager():
    global _session_manager
    if _session_manager is None:
        _session_manager = CalculationSessionManager()
    return _session_manager


@dataclass
class ExpressionEvaluationResult:
    success: bool
    expression: str
    result: float | complex | bool | tuple | list | None = None
    error: dict[str, Any] | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self):
        return {
            "success": self.success,
            "expression": self.expression,
            "result": str(self.result) if self.result is not None else None,
            "error": self.error,
            "metadata": self.metadata,
        }

    def to_string(self):
        if self.success:
            return f"Result: {self.result}"
        else:
            return f"Error: {self.error.get('message', 'Unknown error')}"


class ComputationRateLimiter:
    def __init__(self, max_requests: int, window: int, max_clients: int = 1000):
        self.max_requests = max_requests
        self.window = window
        self.max_clients = max_clients
        self.requests = OrderedDict()
        self.lock = RLock()

    def check_rate_limit(self, client_id: str) -> bool:
        current_time = time.time()
        with self.lock:
            if client_id not in self.requests:
                if len(self.requests) >= self.max_clients:
                    oldest_client = next(iter(self.requests))
                    del self.requests[oldest_client]
                self.requests[client_id] = deque()

            client_requests = self.requests[client_id]
            while client_requests and client_requests[0] < current_time - self.window:
                client_requests.popleft()

            if len(client_requests) >= self.max_requests:
                return False

            client_requests.append(current_time)
            self.requests.move_to_end(client_id)
            return True

    def cleanup_expired(self) -> int:
        current_time = time.time()
        with self.lock:
            expired_clients = []
            for client_id, client_requests in self.requests.items():
                while client_requests and client_requests[0] < current_time - self.window:
                    client_requests.popleft()
                if not client_requests:
                    expired_clients.append(client_id)

            for client_id in expired_clients:
                del self.requests[client_id]
            return len(expired_clients)


mathematical_computation_rate_limiter = ComputationRateLimiter(
    MAXIMUM_CLIENT_REQUESTS_PER_TIME_WINDOW, RATE_LIMIT_WINDOW
)


@contextmanager
def mathematical_computation_timeout(seconds: float):
    from threading import Timer

    timeout_occurred = threading.Event()

    def timeout_callback():
        timeout_occurred.set()

    timer = Timer(seconds, timeout_callback)
    timer.start()

    try:
        yield timeout_occurred
    finally:
        timer.cancel()
        if timeout_occurred.is_set():
            raise TimeoutError(f"Computation exceeded {seconds}s limit")


@contextmanager
def mathematical_computation_memory_limit(mb: int):
    try:
        soft, hard = resource.getrlimit(resource.RLIMIT_AS)
        new_limit = mb * 1024 * 1024

        if new_limit < soft and new_limit < hard:
            resource.setrlimit(resource.RLIMIT_AS, (new_limit, hard))
            try:
                yield
            finally:
                resource.setrlimit(resource.RLIMIT_AS, (soft, hard))
        else:
            yield
    except (ValueError, OSError):
        yield


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
    ast.BitXor: operator.xor,
    ast.BitOr: operator.or_,
    ast.BitAnd: operator.and_,
    ast.LShift: operator.lshift,
    ast.RShift: operator.rshift,
}

COMPARISON_OPS = {
    ast.Eq: operator.eq,
    ast.NotEq: operator.ne,
    ast.Lt: operator.lt,
    ast.LtE: operator.le,
    ast.Gt: operator.gt,
    ast.GtE: operator.ge,
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
    "abs": lambda x: abs(x),
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

STATISTICS_FUNCTIONS = {
    "mean": statistics.mean,
    "median": statistics.median,
    "mode": statistics.mode,
    "stdev": statistics.stdev,
    "pstdev": statistics.pstdev,
    "variance": statistics.variance,
    "pvariance": statistics.pvariance,
    "harmonic_mean": statistics.harmonic_mean,
    "geometric_mean": getattr(statistics, "geometric_mean", None),
    "quantiles": getattr(statistics, "quantiles", None),
}

COMPLEX_FUNCTIONS = {
    "phase": cmath.phase,
    "polar": cmath.polar,
    "rect": cmath.rect,
    "csin": cmath.sin,
    "ccos": cmath.cos,
    "ctan": cmath.tan,
    "cexp": cmath.exp,
    "clog": cmath.log,
    "clog10": cmath.log10,
    "csqrt": cmath.sqrt,
}

UNIT_CONVERSIONS = {
    "length": {
        "m": 1.0,
        "km": 1000.0,
        "cm": 0.01,
        "mm": 0.001,
        "mi": 1609.344,
        "yd": 0.9144,
        "ft": 0.3048,
        "in": 0.0254,
        "nmi": 1852.0,
        "ly": 9.4607e15,
        "AU": 1.496e11,
        "pc": 3.0857e16,
        "angstrom": 1e-10,
        "micron": 1e-6,
        "nm": 1e-9,
    },
    "mass": {
        "kg": 1.0,
        "g": 0.001,
        "mg": 1e-6,
        "lb": 0.453592,
        "oz": 0.0283495,
        "ton": 1000.0,
        "t": 1000.0,
        "ton_us": 907.185,
        "ton_uk": 1016.05,
        "st": 6.35029,
        "ct": 0.0002,
        "gr": 6.47989e-5,
        "amu": 1.66054e-27,
    },
    "time": {
        "s": 1.0,
        "ms": 0.001,
        "us": 1e-6,
        "ns": 1e-9,
        "min": 60.0,
        "h": 3600.0,
        "d": 86400.0,
        "wk": 604800.0,
        "mo": 2592000.0,
        "yr": 31536000.0,
        "decade": 315360000.0,
        "century": 3153600000.0,
        "ps": 1e-12,
        "fortnight": 1209600.0,
        "millennium": 31536000000.0,
    },
    "temperature": {
        "K": lambda x: x,
        "C": lambda x: x + 273.15,
        "F": lambda x: (x - 32) * 5 / 9 + 273.15,
    },
    "area": {
        "m2": 1.0,
        "km2": 1e6,
        "cm2": 1e-4,
        "mm2": 1e-6,
        "ft2": 0.092903,
        "yd2": 0.836127,
        "in2": 0.00064516,
        "mi2": 2.59e6,
        "acre": 4046.86,
        "hectare": 10000.0,
        "are": 100.0,
        "sqch": 404.686,
    },
    "volume": {
        "L": 0.001,
        "mL": 1e-6,
        "m3": 1.0,
        "cm3": 1e-6,
        "gal": 0.00378541,
        "qt": 0.000946353,
        "pt": 0.000473176,
        "fl_oz": 2.95735e-5,
        "gal_uk": 0.00454609,
        "qt_uk": 0.00113652,
        "pt_uk": 0.000568261,
        "cup": 0.000236588,
        "tbsp": 1.47868e-5,
        "tsp": 4.92892e-6,
        "ft3": 0.0283168,
        "in3": 1.63871e-5,
    },
    "speed": {
        "m/s": 1.0,
        "km/h": 0.277778,
        "mph": 0.44704,
        "ft/s": 0.3048,
        "knot": 0.514444,
        "mach": 340.29,
        "cm/s": 0.01,
        "mi/min": 26.8224,
        "in/s": 0.0254,
        "c": 299792458.0,
    },
    "data": {
        "B": 1.0,
        "KB": 1000.0,
        "MB": 1e6,
        "GB": 1e9,
        "TB": 1e12,
        "PB": 1e15,
        "EB": 1e18,
        "ZB": 1e21,
        "bit": 0.125,
        "Kbit": 125.0,
        "Mbit": 125000.0,
        "Gbit": 1.25e8,
        "Tbit": 1.25e11,
        "KiB": 1024.0,
        "MiB": 1048576.0,
        "GiB": 1073741824.0,
    },
    "pressure": {
        "Pa": 1.0,
        "kPa": 1000.0,
        "MPa": 1e6,
        "atm": 101325.0,
        "bar": 100000.0,
        "mbar": 100.0,
        "psi": 6894.76,
        "torr": 133.322,
        "mmHg": 133.322,
        "inHg": 3386.39,
    },
    "energy": {
        "J": 1.0,
        "kJ": 1000.0,
        "MJ": 1e6,
        "cal": 4.184,
        "kcal": 4184.0,
        "Wh": 3600.0,
        "kWh": 3.6e6,
        "BTU": 1055.06,
        "eV": 1.60218e-19,
        "ft_lb": 1.35582,
        "erg": 1e-7,
        "therm": 1.055e8,
    },
    "power": {
        "W": 1.0,
        "kW": 1000.0,
        "MW": 1e6,
        "hp": 745.7,
        "PS": 735.499,
        "BTU/h": 0.293071,
        "ft_lb/s": 1.35582,
        "cal/s": 4.184,
        "erg/s": 1e-7,
        "ton_refrigeration": 3516.85,
    },
    "force": {
        "N": 1.0,
        "kN": 1000.0,
        "lbf": 4.44822,
        "kgf": 9.80665,
        "dyne": 1e-5,
        "pdl": 0.138255,
        "ozf": 0.278014,
        "tonf": 9806.65,
    },
    "angle": {
        "deg": 1.0,
        "rad": 57.2958,
        "grad": 0.9,
        "arcmin": 0.0166667,
        "arcsec": 0.000277778,
        "turn": 360.0,
    },
    "frequency": {
        "Hz": 1.0,
        "kHz": 1000.0,
        "MHz": 1e6,
        "GHz": 1e9,
        "rpm": 0.0166667,
        "rad/s": 0.159155,
    },
    "fuel_economy": {
        "mpg": 1.0,
        "mpg_uk": 1.20095,
        "L/100km": 235.215,
        "km/L": 2.35215,
        "mi/L": 3.78541,
        "gal/100mi": 100.0,
    },
}

UNIT_ALIASES = {
    "meters": "m",
    "meter": "m",
    "metres": "m",
    "metre": "m",
    "kilometers": "km",
    "kilometer": "km",
    "kilometres": "km",
    "kilometre": "km",
    "centimeters": "cm",
    "centimeter": "cm",
    "centimetres": "cm",
    "centimetre": "cm",
    "millimeters": "mm",
    "millimeter": "mm",
    "millimetres": "mm",
    "millimetre": "mm",
    "miles": "mi",
    "mile": "mi",
    "yards": "yd",
    "yard": "yd",
    "feet": "ft",
    "foot": "ft",
    "inches": "in",
    "inch": "in",
    "kilograms": "kg",
    "kilogram": "kg",
    "grams": "g",
    "gram": "g",
    "milligrams": "mg",
    "milligram": "mg",
    "pounds": "lb",
    "pound": "lb",
    "lbs": "lb",
    "ounces": "oz",
    "ounce": "oz",
    "tons": "ton",
    "seconds": "s",
    "second": "s",
    "sec": "s",
    "secs": "s",
    "milliseconds": "ms",
    "millisecond": "ms",
    "millisec": "ms",
    "millisecs": "ms",
    "microseconds": "us",
    "microsecond": "us",
    "microsec": "us",
    "microsecs": "us",
    "nanoseconds": "ns",
    "nanosecond": "ns",
    "nanosec": "ns",
    "nanosecs": "ns",
    "minutes": "min",
    "minute": "min",
    "mins": "min",
    "hours": "h",
    "hour": "h",
    "hrs": "h",
    "hr": "h",
    "days": "d",
    "day": "d",
    "weeks": "wk",
    "week": "wk",
    "months": "mo",
    "month": "mo",
    "years": "yr",
    "year": "yr",
    "yrs": "yr",
    "decades": "decade",
    "centuries": "century",
    "celsius": "C",
    "centigrade": "C",
    "fahrenheit": "F",
    "fahr": "F",
    "kelvin": "K",
    "liters": "L",
    "liter": "L",
    "litres": "L",
    "litre": "L",
    "milliliters": "mL",
    "milliliter": "mL",
    "millilitres": "mL",
    "millilitre": "mL",
    "gallons": "gal",
    "gallon": "gal",
    "quarts": "qt",
    "quart": "qt",
    "pints": "pt",
    "pint": "pt",
    "cups": "cup",
    "tablespoons": "tbsp",
    "tablespoon": "tbsp",
    "teaspoons": "tsp",
    "teaspoon": "tsp",
    "bytes": "B",
    "byte": "B",
    "kilobytes": "KB",
    "kilobyte": "KB",
    "megabytes": "MB",
    "megabyte": "MB",
    "gigabytes": "GB",
    "gigabyte": "GB",
    "terabytes": "TB",
    "terabyte": "TB",
    "petabytes": "PB",
    "petabyte": "PB",
    "bits": "bit",
    "kilobits": "Kbit",
    "kilobit": "Kbit",
    "megabits": "Mbit",
    "megabit": "Mbit",
    "gigabits": "Gbit",
    "gigabit": "Gbit",
    "pascals": "Pa",
    "pascal": "Pa",
    "kilopascals": "kPa",
    "kilopascal": "kPa",
    "megapascals": "MPa",
    "megapascal": "MPa",
    "atmospheres": "atm",
    "atmosphere": "atm",
    "bars": "bar",
    "millibars": "mbar",
    "millibar": "mbar",
    "joules": "J",
    "joule": "J",
    "kilojoules": "kJ",
    "kilojoule": "kJ",
    "megajoules": "MJ",
    "megajoule": "MJ",
    "calories": "cal",
    "calorie": "cal",
    "kilocalories": "kcal",
    "kilocalorie": "kcal",
    "watts": "W",
    "watt": "W",
    "kilowatts": "kW",
    "kilowatt": "kW",
    "megawatts": "MW",
    "megawatt": "MW",
    "horsepower": "hp",
    "newtons": "N",
    "newton": "N",
    "kilonewtons": "kN",
    "kilonewton": "kN",
    "degrees": "deg",
    "degree": "deg",
    "radians": "rad",
    "radian": "rad",
    "hertz": "Hz",
    "kilohertz": "kHz",
    "megahertz": "MHz",
    "gigahertz": "GHz",
}

MATH_CONSTANTS = {
    "pi": math.pi,
    "e": math.e,
    "tau": math.tau,
    "inf": math.inf,
    "nan": math.nan,
    "phi": (1 + math.sqrt(5)) / 2,
    "euler": 0.5772156649,
}

MATH_FUNCTIONS = {k: v for k, v in MATH_FUNCTIONS.items() if v is not None}
STATISTICS_FUNCTIONS = {k: v for k, v in STATISTICS_FUNCTIONS.items() if v is not None}

ALL_FUNCTIONS = {**MATH_FUNCTIONS, **STATISTICS_FUNCTIONS, **COMPLEX_FUNCTIONS}


class MathematicalCalculationHistory:
    def __init__(self, max_size: int = CALCULATION_HISTORY_ENTRY_LIMIT):
        self.history: list[dict[str, Any]] = []
        self.max_size = max_size
        self.lock = RLock()

    def add(self, expression: str, result: str) -> None:
        with self.lock:
            entry = {
                "expression": expression,
                "result": result,
                "timestamp": datetime.datetime.now().isoformat(),
            }
            self.history.append(entry)
            if len(self.history) > self.max_size:
                self.history.pop(0)

    def get_recent(self, limit: int = 10) -> list[dict[str, Any]]:
        with self.lock:
            return self.history[-limit:]

    def clear(self) -> None:
        with self.lock:
            self.history.clear()


mathematical_calculation_history = MathematicalCalculationHistory()


def compute_expression_fingerprint(expression: str) -> str:
    return str(hash(expression))


def validate_expression_security_constraints(expression: str, client_id: str = "default") -> bool:
    if ENABLE_RATE_LIMITING and not mathematical_computation_rate_limiter.check_rate_limit(
        client_id
    ):
        raise PermissionError(
            f"Rate limit exceeded: {MAXIMUM_CLIENT_REQUESTS_PER_TIME_WINDOW} requests per {RATE_LIMIT_WINDOW} seconds"
        )

    for pattern in FORBIDDEN_PATTERNS:
        if re.search(pattern, expression, re.IGNORECASE):
            raise ValueError("Expression contains forbidden pattern")

    suspicious_chars = ["\\x00", "\\n", "\\r", "\\b", "\\f", "\\v"]
    filtered_expr = "".join(ch for ch in expression if ch not in suspicious_chars)

    if len(filtered_expr) != len(expression):
        raise ValueError("Expression contains invalid control characters")

    return True


def track_mathematical_operation_performance(
    expression: str, start_time: float, end_time: float
) -> None:
    with _computation_metrics_lock:
        computation_time = end_time - start_time
        expression_hash = compute_expression_fingerprint(expression)

        existing_stats = _get_computation_stats().get(expression_hash)
        if existing_stats is None:
            stats = {
                "count": 1,
                "total_time": computation_time,
                "max_time": computation_time,
                "first_seen": start_time,
                "last_seen": end_time,
            }
        else:
            stats = existing_stats.copy()
            stats["count"] += 1
            stats["total_time"] += computation_time
            stats["max_time"] = max(stats["max_time"], computation_time)
            stats["last_seen"] = end_time

        _get_computation_stats().set(expression_hash, stats)


def cleanup_expired_cache_entries() -> dict[str, int]:
    cleanup_stats = {
        "expression_cache_expired": 0,
        "sessions_expired": 0,
        "rate_limiter_expired": 0,
    }

    cleanup_stats["expression_cache_expired"] = _get_expression_cache().cleanup_expired()
    cleanup_stats["sessions_expired"] = _get_session_manager().cleanup_expired()
    cleanup_stats["rate_limiter_expired"] = mathematical_computation_rate_limiter.cleanup_expired()

    return cleanup_stats


def get_memory_usage_stats() -> dict[str, Any]:
    import os

    import psutil

    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()

    return {
        "process_memory_mb": round(memory_info.rss / 1024 / 1024, 2),
        "virtual_memory_mb": round(memory_info.vms / 1024 / 1024, 2),
        "expression_cache_size": _get_expression_cache().size(),
        "ast_cache_size": _get_parsed_cache().size(),
        "computation_stats_size": _get_computation_stats().size(),
        "active_sessions": _get_session_manager().get_stats()["active_sessions"],
        "rate_limiter_clients": len(mathematical_computation_rate_limiter.requests),
        "history_entries": len(mathematical_calculation_history.history),
    }


def shutdown_memory_management() -> None:
    global _memory_cleanup_timer
    if _memory_cleanup_timer:
        _memory_cleanup_timer.cancel()
    _get_session_manager().shutdown()


def retrieve_cached_computation_result(expression: str) -> str | None:
    return _get_expression_cache().get(expression)


def persist_computation_result_in_cache(expression: str, result: str) -> None:
    _get_expression_cache().set(expression, result)


def retrieve_cached_abstract_syntax_tree(expression: str) -> ast.AST | None:
    return _get_parsed_cache().get(expression)


def store_parsed_expression(expression: str, tree: ast.AST) -> None:
    _get_parsed_cache().set(expression, tree)


def sanitize_expression(expr: str) -> str:
    sanitized = "".join(char for char in expr if ord(char) >= 32 or char in " \\t")
    sanitized = " ".join(sanitized.split())

    dangerous_sequences = ["..", "__", "$$", "@@", "##"]
    for seq in dangerous_sequences:
        sanitized = sanitized.replace(seq, "")

    return sanitized


def preprocess_expression(expr: str) -> str:
    expr = expr.replace("×", "*")
    expr = expr.replace("÷", "/")
    expr = expr.replace("^", "**")
    return expr


def validate_ast_node(node: ast.AST, depth: int = 0, session_vars: dict | None = None) -> bool:
    if depth > MAXIMUM_AST_NODE_DEPTH_LIMIT:
        raise ValueError(f"Expression too complex (max depth: {MAXIMUM_AST_NODE_DEPTH_LIMIT})")

    if isinstance(node, ast.Expression):
        return validate_ast_node(node.body, depth + 1, session_vars)

    if isinstance(node, ast.Constant):
        return isinstance(node.value, (int, float, complex, str))

    if isinstance(node, ast.Name):
        if session_vars and node.id in session_vars:
            return True
        return node.id in MATH_CONSTANTS or node.id in ALL_FUNCTIONS

    if isinstance(node, ast.UnaryOp):
        return type(node.op) in OPERATORS and validate_ast_node(
            node.operand, depth + 1, session_vars
        )

    if isinstance(node, ast.BinOp):
        return (
            type(node.op) in OPERATORS
            and validate_ast_node(node.left, depth + 1, session_vars)
            and validate_ast_node(node.right, depth + 1, session_vars)
        )

    if isinstance(node, ast.Compare):
        if len(node.ops) != 1 or len(node.comparators) != 1:
            return False
        return (
            type(node.ops[0]) in COMPARISON_OPS
            and validate_ast_node(node.left, depth + 1, session_vars)
            and validate_ast_node(node.comparators[0], depth + 1, session_vars)
        )

    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            return False
        if node.func.id not in ALL_FUNCTIONS:
            return False
        if node.keywords:
            return False
        return all(validate_ast_node(arg, depth + 1, session_vars) for arg in node.args)

    if isinstance(node, ast.List):
        if len(node.elts) > MAXIMUM_LIST_ELEMENT_COUNT_LIMIT:
            raise ValueError(f"List too large (max size: {MAXIMUM_LIST_ELEMENT_COUNT_LIMIT})")
        return all(validate_ast_node(elt, depth + 1, session_vars) for elt in node.elts)

    return False


def evaluate_mathematical_node(node: ast.AST, session_vars: dict | None = None) -> Any:
    if isinstance(node, ast.Expression):
        return evaluate_mathematical_node(node.body, session_vars)

    if isinstance(node, ast.Constant):
        if isinstance(node.value, str):
            if node.value.endswith("j"):
                return complex(node.value)
            return node.value
        return node.value

    if isinstance(node, ast.Name):
        if session_vars and node.id in session_vars:
            return session_vars[node.id]
        if node.id in MATH_CONSTANTS:
            return MATH_CONSTANTS[node.id]
        raise ValueError(f"Unknown variable: {node.id}")

    if isinstance(node, ast.UnaryOp):
        op = OPERATORS[type(node.op)]
        operand = evaluate_mathematical_node(node.operand, session_vars)
        return op(operand)

    if isinstance(node, ast.BinOp):
        op = OPERATORS[type(node.op)]
        left = evaluate_mathematical_node(node.left, session_vars)
        right = evaluate_mathematical_node(node.right, session_vars)

        if isinstance(node.op, ast.Pow) and abs(right) > EXPONENTIATION_SAFETY_THRESHOLD:
            raise ValueError(f"Power exponent too large (max: {EXPONENTIATION_SAFETY_THRESHOLD})")

        try:
            return op(left, right)
        except (OverflowError, ZeroDivisionError) as e:
            raise ValueError(f"Mathematical operation failed: {str(e)}") from e

    if isinstance(node, ast.Compare):
        left = evaluate_mathematical_node(node.left, session_vars)
        op = COMPARISON_OPS[type(node.ops[0])]
        right = evaluate_mathematical_node(node.comparators[0], session_vars)
        return op(left, right)

    if isinstance(node, ast.Call):
        func_name = node.func.id
        func = ALL_FUNCTIONS[func_name]
        args = [evaluate_mathematical_node(arg, session_vars) for arg in node.args]

        if func_name == "factorial" and len(args) == 1:
            if args[0] > FACTORIAL_COMPUTATION_UPPER_BOUND:
                raise ValueError(
                    f"Factorial input too large (max: {FACTORIAL_COMPUTATION_UPPER_BOUND})"
                )
            if args[0] < 0 or not isinstance(args[0], int):
                raise ValueError("Factorial requires a non-negative integer")

        elif func_name == "pow" and len(args) == 2:
            if abs(args[1]) > EXPONENTIATION_SAFETY_THRESHOLD:
                raise ValueError(
                    f"Power exponent too large (max: {EXPONENTIATION_SAFETY_THRESHOLD})"
                )

        try:
            return func(*args)
        except (OverflowError, ValueError, statistics.StatisticsError) as e:
            raise ValueError(f"Mathematical operation failed: {str(e)}") from e

    if isinstance(node, ast.List):
        return [evaluate_mathematical_node(elt, session_vars) for elt in node.elts]

    raise ValueError(f"Unsupported node type: {type(node).__name__}")


def compute_expression(
    expression: str, session_id: str | None = None
) -> ExpressionEvaluationResult:
    start_time = time.time()

    try:
        validate_expression_security_constraints(expression)

        expression = expression.strip()
        if not expression:
            raise SyntaxError("Empty expression")

        if len(expression) > MAXIMUM_MATHEMATICAL_EXPRESSION_CHARACTER_LIMIT:
            raise ValueError(
                f"Expression too long (max: {MAXIMUM_MATHEMATICAL_EXPRESSION_CHARACTER_LIMIT} characters)"
            )

        original_expression = expression

        session_vars = {}
        if session_id:
            session_vars = _get_session_manager().get_session(session_id) or {}

        cached_result = retrieve_cached_computation_result(original_expression)
        if cached_result is not None:
            return ExpressionEvaluationResult(
                success=True,
                expression=original_expression,
                result=cached_result,
                metadata={"cache_hit": True, "computation_time": 0},
            )

        expression = sanitize_expression(expression)
        expression = preprocess_expression(expression)

        tree = retrieve_cached_abstract_syntax_tree(expression)
        if tree is None:
            try:
                tree = ast.parse(expression, mode="eval")
                store_parsed_expression(expression, tree)
            except SyntaxError as e:
                raise SyntaxError(f"Invalid mathematical expression: {str(e)}") from e

        try:
            if not validate_ast_node(tree, session_vars=session_vars):
                raise ValueError("Expression contains unsupported operations")
        except Exception as e:
            if "unsupported operations" in str(e).lower():
                raise ValueError(f"Unsupported mathematical operation detected: {str(e)}") from e
            raise

        def compute_result(timeout_event=None):
            with mathematical_computation_memory_limit(MAXIMUM_MEMORY_USAGE_MEGABYTES):
                if timeout_event and timeout_event.is_set():
                    raise TimeoutError(
                        f"Computation exceeded {MATHEMATICAL_OPERATION_TIMEOUT_SECONDS}s limit"
                    )
                result = evaluate_mathematical_node(tree, session_vars)
                if timeout_event and timeout_event.is_set():
                    raise TimeoutError(
                        f"Computation exceeded {MATHEMATICAL_OPERATION_TIMEOUT_SECONDS}s limit"
                    )
                return result

        with mathematical_computation_timeout(
            MATHEMATICAL_OPERATION_TIMEOUT_SECONDS
        ) as timeout_event:
            result = compute_result(timeout_event)

        if isinstance(result, (int, float, complex)) and abs(result) > 10**200:
            result_magnitude = abs(result)
            if result_magnitude == float("inf"):
                raise ValueError("Result is infinite - consider using smaller values")
            else:
                raise ValueError(
                    f"Result magnitude ({result_magnitude:.2e}) exceeds safe computational limits"
                )

        result_str = format_calculation_output(result, original_expression)

        if len(result_str) > MAXIMUM_COMPUTATION_RESULT_CHARACTER_LIMIT:
            raise ValueError(
                f"Result too large (max length: {MAXIMUM_COMPUTATION_RESULT_CHARACTER_LIMIT})"
            )

        mathematical_calculation_history.add(original_expression, result_str)
        persist_computation_result_in_cache(original_expression, result_str)

        end_time = time.time()
        track_mathematical_operation_performance(original_expression, start_time, end_time)

        return ExpressionEvaluationResult(
            success=True,
            expression=original_expression,
            result=result,
            metadata={"computation_time": end_time - start_time, "cache_hit": False},
        )

    except (
        SyntaxError,
        ValueError,
        ZeroDivisionError,
        TypeError,
        AttributeError,
        TimeoutError,
    ) as e:
        return ExpressionEvaluationResult(
            success=False,
            expression=expression,
            error={"type": type(e).__name__, "message": str(e)},
        )
    except Exception as e:
        return ExpressionEvaluationResult(
            success=False,
            expression=expression,
            error={"type": "UnexpectedError", "message": f"Calculation error: {str(e)}"},
        )


def execute_mathematical_computation(expression: str, session_id: str | None = None) -> str:
    result = compute_expression(expression, session_id)
    if result.success:
        return format_calculation_output(result.result, expression)
    else:
        error_msg = result.error.get("message", "Unknown error")
        if "division by zero" in error_msg.lower():
            raise ValueError("Cannot divide by zero")
        elif "invalid" in error_msg.lower() or "unsupported" in error_msg.lower():
            raise ValueError(error_msg)
        elif "empty" in error_msg.lower():
            raise SyntaxError(error_msg)
        else:
            raise ValueError(error_msg)


def format_calculation_output(result: Any, original_expression: str) -> str:
    if isinstance(result, bool):
        return str(result)

    if isinstance(result, complex):
        if result.imag == 0:
            return format_calculation_output(result.real, original_expression)
        return str(result)

    if isinstance(result, (list, tuple)):
        return str(result)

    if isinstance(result, (float, int)):
        has_division = "/" in original_expression or "÷" in original_expression
        has_float_operand = "." in original_expression
        has_statistics_func = any(
            func in original_expression
            for func in ["mean", "median", "stdev", "pstdev", "variance", "pvariance"]
        )

        is_integer_result = isinstance(result, int) or (
            isinstance(result, float) and result.is_integer()
        )

        if "nextafter" in original_expression or "ulp" in original_expression:
            return f"{result:.17g}"

        if has_statistics_func and is_integer_result:
            return f"{float(result):.1f}"

        if is_integer_result and not has_division and not has_float_operand:
            return str(int(result))

        if abs(result) < 1e-10 and result != 0:
            return f"{result:.10e}"
        elif abs(result) > 1e10:
            return f"{result:.6e}"
        else:
            return str(round(result, 10))

    return str(result)


def matrix_multiply(
    first_matrix: list[list[float]], second_matrix: list[list[float]]
) -> list[list[float]]:
    first_matrix_rows, first_matrix_cols = len(first_matrix), (
        len(first_matrix[0]) if first_matrix else 0
    )
    second_matrix_rows, second_matrix_cols = len(second_matrix), (
        len(second_matrix[0]) if second_matrix else 0
    )

    if first_matrix_cols != second_matrix_rows:
        raise ValueError(f"Cannot multiply matrices: {first_matrix_cols} != {second_matrix_rows}")

    result = [[0 for _ in range(second_matrix_cols)] for _ in range(first_matrix_rows)]

    for row_index in range(first_matrix_rows):
        for column_index in range(second_matrix_cols):
            for inner_index in range(first_matrix_cols):
                result[row_index][column_index] += (
                    first_matrix[row_index][inner_index] * second_matrix[inner_index][column_index]
                )

    return result


def matrix_determinant(matrix: list[list[float]]) -> float:
    matrix_dimension = len(matrix)
    if matrix_dimension == 0 or matrix_dimension != len(matrix[0]):
        raise ValueError("Matrix must be square")

    if matrix_dimension == 1:
        return matrix[0][0]

    if matrix_dimension == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant_value = 0
    for column_index in range(matrix_dimension):
        minor = [row[:column_index] + row[column_index + 1 :] for row in matrix[1:]]
        determinant_value += (
            ((-1) ** column_index) * matrix[0][column_index] * matrix_determinant(minor)
        )

    return determinant_value


def matrix_inverse(matrix: list[list[float]]) -> list[list[float]]:
    matrix_size = len(matrix)
    determinant_value = matrix_determinant(matrix)

    if abs(determinant_value) < 1e-10:
        raise ValueError("Matrix is singular (determinant equals zero)")

    if matrix_size == 2:
        return [
            [matrix[1][1] / determinant_value, -matrix[0][1] / determinant_value],
            [-matrix[1][0] / determinant_value, matrix[0][0] / determinant_value],
        ]

    raise ValueError("Matrix inverse is only implemented for 2x2 matrices")


def is_prime(candidate_number: int) -> bool:
    if candidate_number < 2:
        return False
    if candidate_number == 2:
        return True
    if candidate_number % 2 == 0:
        return False

    return all(
        candidate_number % potential_divisor != 0
        for potential_divisor in range(3, int(math.sqrt(candidate_number)) + 1, 2)
    )


def prime_factors(input_number: int) -> list[int]:
    factor_list = []
    trial_divisor = 2
    while trial_divisor * trial_divisor <= input_number:
        while input_number % trial_divisor == 0:
            factor_list.append(trial_divisor)
            input_number //= trial_divisor
        trial_divisor += 1
    if input_number > 1:
        factor_list.append(input_number)
    return factor_list


def parse_natural_language_conversion(text: str) -> tuple[float, str, str, str] | None:
    """Parse natural language conversion queries.

    Args:
        text (str): Natural language conversion request

    Returns:
        tuple[float, str, str, str] | None: Parsed conversion data or None
    """
    import re

    text = text.lower().strip()

    patterns = [
        r"(?:convert|change)\s+(\d*\.?\d+)\s+(\w+)\s+(?:to|into)\s+(\w+)",
        r"(?:what\s+is\s+)?(\d*\.?\d+)\s+(\w+)\s+(?:in|to|as)\s+(\w+)",
        r"(\d*\.?\d+)\s+(\w+)\s*->\s*(\w+)",
        r"(\d*\.?\d+)\s+(\w+)\s+equals?\s+how\s+many\s+(\w+)",
        r"from\s+(\d*\.?\d+)\s+(\w+)\s+to\s+(\w+)",
    ]

    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            try:
                value = float(match.group(1))
                from_unit = match.group(2).strip()
                to_unit = match.group(3).strip()

                from_unit_resolved = resolve_unit_alias(from_unit)
                resolve_unit_alias(to_unit)

                unit_type = detect_unit_type(from_unit_resolved)
                if unit_type:
                    return value, from_unit, to_unit, unit_type

            except (ValueError, IndexError):
                continue

    return None


def convert_unit(value: float, from_unit: str, to_unit: str, unit_type: str) -> float:
    if unit_type not in UNIT_CONVERSIONS:
        raise ValueError(f"Unknown unit type: {unit_type}")

    conversions = UNIT_CONVERSIONS[unit_type]

    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError(f"Unknown unit in {unit_type}: {from_unit} or {to_unit}")

    if unit_type == "temperature":
        kelvin = conversions[from_unit](value)
        if to_unit == "K":
            return kelvin
        elif to_unit == "C":
            return kelvin - 273.15
        elif to_unit == "F":
            return (kelvin - 273.15) * 9 / 5 + 32
    elif unit_type == "fuel_economy":
        if (
            from_unit == "mpg"
            and to_unit == "L/100km"
            or from_unit == "L/100km"
            and to_unit == "mpg"
        ):
            return 235.215 / value
        elif (
            from_unit == "mpg_uk"
            and to_unit == "L/100km"
            or from_unit == "L/100km"
            and to_unit == "mpg_uk"
        ):
            return 282.481 / value
        elif (
            from_unit == "km/L"
            and to_unit == "L/100km"
            or from_unit == "L/100km"
            and to_unit == "km/L"
        ):
            return 100.0 / value
        elif from_unit == "mpg" and to_unit == "mpg_uk":
            return value / 1.20095
        elif from_unit == "mpg_uk" and to_unit == "mpg":
            return value * 1.20095
        elif from_unit == "mpg" and to_unit == "km/L":
            return value * 0.425144
        elif from_unit == "km/L" and to_unit == "mpg":
            return value * 2.35215
        else:
            base_value = value * conversions[from_unit]
            return base_value / conversions[to_unit]
    else:
        base_value = value * conversions[from_unit]
        return base_value / conversions[to_unit]


class UnitConversionHistory:
    def __init__(self, max_size: int = 100):
        self.history: list[dict[str, Any]] = []
        self.max_size = max_size
        self.lock = RLock()

    def add(self, value: float, from_unit: str, to_unit: str, result: float) -> None:
        with self.lock:
            entry = {
                "value": value,
                "from_unit": from_unit,
                "to_unit": to_unit,
                "result": result,
                "timestamp": datetime.datetime.now().isoformat(),
            }
            self.history.append(entry)
            if len(self.history) > self.max_size:
                self.history.pop(0)

    def get_recent(self, limit: int = 10) -> list[dict[str, Any]]:
        with self.lock:
            return self.history[-limit:]

    def clear(self) -> None:
        with self.lock:
            self.history.clear()


conversion_history = UnitConversionHistory()


def resolve_unit_alias(unit: str) -> str:
    unit_lower = unit.lower()
    return UNIT_ALIASES.get(unit_lower, unit)


def detect_unit_type(unit: str) -> str | None:
    unit = resolve_unit_alias(unit)
    for unit_type, units in UNIT_CONVERSIONS.items():
        if unit in units:
            return unit_type
    return None


def format_scientific_notation(value: float, precision: int = 4) -> str:
    if abs(value) < 1e-10 or abs(value) > 1e10:
        return f"{value:.{precision}e}"
    return str(value)


def convert_with_history(value: float, from_unit: str, to_unit: str, precision: int = 10) -> float:
    from_unit = resolve_unit_alias(from_unit)
    to_unit = resolve_unit_alias(to_unit)

    unit_type = detect_unit_type(from_unit)
    if not unit_type:
        raise ValueError(f"Unknown unit: {from_unit}")

    if to_unit not in UNIT_CONVERSIONS[unit_type]:
        raise ValueError(f"Unknown unit: {to_unit}")

    result = convert_unit(value, from_unit, to_unit, unit_type)
    result = round(result, precision)

    conversion_history.add(value, from_unit, to_unit, result)
    return result


def parse_compound_unit(unit_str: str) -> tuple[list[str], list[str]]:
    unit_str = unit_str.replace("·", "*").replace("/", " / ").replace("*", " * ")

    parts = unit_str.split()
    numerator = []
    denominator = []
    current_list = numerator

    for part in parts:
        if part == "/":
            current_list = denominator
        elif part not in ["*", "·"]:
            if "^" in part or part[-1].isdigit():
                base_unit = "".join(c for c in part if not c.isdigit() and c != "^")
                power = "".join(c for c in part if c.isdigit())
                power = int(power) if power else 1
                for _ in range(abs(power)):
                    if power > 0:
                        current_list.append(base_unit)
                    else:
                        (denominator if current_list == numerator else numerator).append(base_unit)
            else:
                current_list.append(part)

    return numerator, denominator


def calculate_percentage(value: float, percentage: float) -> float:
    return value * (percentage / 100)


def calculate_percentage_of(part: float, whole: float) -> float:
    if whole == 0:
        raise ValueError("Cannot calculate percentage of zero")
    return (part / whole) * 100


def calculate_percentage_change(old_value: float, new_value: float) -> float:
    if old_value == 0:
        raise ValueError("Cannot calculate percentage change from zero")
    return ((new_value - old_value) / old_value) * 100


def split_bill(total: float, people: int, tip_percent: float = 0) -> dict[str, float]:
    if people <= 0:
        raise ValueError("Number of people must be positive")

    tip_amount = calculate_percentage(total, tip_percent)
    total_with_tip = total + tip_amount
    per_person = total_with_tip / people

    return {
        "total": total,
        "tip_amount": tip_amount,
        "total_with_tip": total_with_tip,
        "per_person": per_person,
        "people": people,
    }


def calculate_tax(amount: float, tax_rate: float, is_inclusive: bool = False) -> dict[str, float]:
    if is_inclusive:
        base_amount = amount / (1 + tax_rate / 100)
        tax_amount = amount - base_amount
    else:
        tax_amount = calculate_percentage(amount, tax_rate)
        base_amount = amount

    return {
        "base_amount": base_amount,
        "tax_rate": tax_rate,
        "tax_amount": tax_amount,
        "total_amount": base_amount + tax_amount,
    }


def calculate_tip(amount: float, tip_percent: float) -> dict[str, float]:
    tip_amount = calculate_percentage(amount, tip_percent)
    return {
        "base_amount": amount,
        "tip_percent": tip_percent,
        "tip_amount": tip_amount,
        "total_amount": amount + tip_amount,
    }


def calculate_compound_interest(
    principal: float, rate: float, time: float, compounds_per_year: int = 1
) -> dict[str, float]:
    rate_decimal = rate / 100
    amount = principal * (1 + rate_decimal / compounds_per_year) ** (compounds_per_year * time)
    interest = amount - principal

    return {
        "principal": principal,
        "rate": rate,
        "time": time,
        "compounds_per_year": compounds_per_year,
        "interest": interest,
        "amount": amount,
    }


def calculate_simple_interest(principal: float, rate: float, time: float) -> dict[str, float]:
    rate_decimal = rate / 100
    interest = principal * rate_decimal * time
    amount = principal + interest

    return {
        "principal": principal,
        "rate": rate,
        "time": time,
        "interest": interest,
        "amount": amount,
    }


def calculate_loan_payment(
    principal: float, annual_rate: float, years: float, payments_per_year: int = 12
) -> dict[str, float]:
    if annual_rate == 0:
        payment = principal / (years * payments_per_year)
        total_paid = principal
        interest_paid = 0
    else:
        rate = annual_rate / 100 / payments_per_year
        n = years * payments_per_year
        payment = principal * (rate * (1 + rate) ** n) / ((1 + rate) ** n - 1)
        total_paid = payment * n
        interest_paid = total_paid - principal

    return {
        "principal": principal,
        "annual_rate": annual_rate,
        "years": years,
        "payments_per_year": payments_per_year,
        "payment": payment,
        "total_paid": total_paid,
        "interest_paid": interest_paid,
    }


def calculate_discount(original_price: float, discount_percent: float) -> dict[str, float]:
    discount_amount = calculate_percentage(original_price, discount_percent)
    final_price = original_price - discount_amount

    return {
        "original_price": original_price,
        "discount_percent": discount_percent,
        "discount_amount": discount_amount,
        "final_price": final_price,
    }


def calculate_markup(cost: float, markup_percent: float) -> dict[str, float]:
    markup_amount = calculate_percentage(cost, markup_percent)
    selling_price = cost + markup_amount

    return {
        "cost": cost,
        "markup_percent": markup_percent,
        "markup_amount": markup_amount,
        "selling_price": selling_price,
    }


_shutdown_requested = False
_active_mathematical_computations = 0


mcp = FastMCP("MCP Mathematics")


@mcp.tool(
    title="Performance Metrics",
    tags={"monitoring", "performance", "metrics", "system"},
    meta={"category": "monitoring", "complexity": "low"},
    annotations=ToolAnnotations(idempotent=True, read_only=True),
)
async def performance_metrics() -> dict:
    """Get performance metrics"""
    with _computation_metrics_lock:
        stats_values = []
        for i in range(_get_computation_stats().size()):
            key = (
                list(_get_computation_stats().cache.keys())[i]
                if i < len(_get_computation_stats().cache)
                else None
            )
            if key:
                stat = _get_computation_stats().get(key)
                if stat:
                    stats_values.append(stat)

        total_computations = sum(stats["count"] for stats in stats_values)
        total_time = sum(stats["total_time"] for stats in stats_values)
        avg_time = total_time / total_computations if total_computations > 0 else 0

    with _rate_limiting_lock:
        active_clients = len(mathematical_computation_rate_limiter.requests)
        total_requests = sum(
            len(reqs) for reqs in mathematical_computation_rate_limiter.requests.values()
        )

    history_size = len(mathematical_calculation_history.history)
    cache_size = _get_expression_cache().size()
    ast_cache_size = _get_parsed_cache().size()
    session_stats = _get_session_manager().get_stats()

    return {
        "computations": {
            "total": total_computations,
            "average_time": round(avg_time, 3),
            "active": _active_mathematical_computations,
        },
        "rate_limiting": {"active_clients": active_clients, "total_requests": total_requests},
        "cache": {
            "expression_cache": cache_size,
            "ast_cache": ast_cache_size,
            "max_size": MAXIMUM_CACHE_SIZE,
        },
        "sessions": {
            "active": session_stats["active_sessions"],
            "max": session_stats["max_sessions"],
        },
        "history": {"entries": history_size, "max": CALCULATION_HISTORY_ENTRY_LIMIT},
        "configuration": {
            "max_expression_length": MAXIMUM_MATHEMATICAL_EXPRESSION_CHARACTER_LIMIT,
            "max_ast_depth": MAXIMUM_AST_NODE_DEPTH_LIMIT,
            "max_computation_time": MAXIMUM_COMPUTATION_DURATION_SECONDS,
            "computation_timeout": MATHEMATICAL_OPERATION_TIMEOUT_SECONDS,
            "memory_limit_mb": MAXIMUM_MEMORY_USAGE_MEGABYTES,
            "available_functions": len(ALL_FUNCTIONS),
        },
        "features": {
            "security_monitoring": SECURITY_AUDIT_LOGGING_ENABLED,
            "rate_limiting": ENABLE_RATE_LIMITING,
        },
    }


@mcp.tool(
    title="Security Status",
    tags={"security", "monitoring", "audit", "system"},
    meta={"category": "security", "complexity": "low"},
    annotations=ToolAnnotations(idempotent=True, read_only=True),
)
async def security_status() -> dict:
    """Get security status"""
    with _rate_limiting_lock:
        active_clients = len(mathematical_computation_rate_limiter.requests)

    return {
        "rate_limiting": {
            "enabled": ENABLE_RATE_LIMITING,
            "window_seconds": RATE_LIMIT_WINDOW,
            "max_requests": MAXIMUM_CLIENT_REQUESTS_PER_TIME_WINDOW,
            "active_clients": active_clients,
        },
        "threat_detection": {
            "forbidden_patterns_count": len(FORBIDDEN_PATTERNS),
            "input_hashing_enabled": ENABLE_INPUT_HASHING,
            "timeout_protection_seconds": MATHEMATICAL_OPERATION_TIMEOUT_SECONDS,
            "memory_protection_mb": MAXIMUM_MEMORY_USAGE_MEGABYTES,
        },
        "audit_configuration": {
            "audit_logging_enabled": SECURITY_AUDIT_LOGGING_ENABLED,
            "security_logger_active": True,
            "async_logging_enabled": True,
        },
        "resource_limits": {
            "max_factorial": FACTORIAL_COMPUTATION_UPPER_BOUND,
            "max_power_exponent": EXPONENTIATION_SAFETY_THRESHOLD,
            "max_result_length": MAXIMUM_COMPUTATION_RESULT_CHARACTER_LIMIT,
            "max_list_size": MAXIMUM_LIST_ELEMENT_COUNT_LIMIT,
        },
    }


@mcp.tool(
    title="Memory Statistics",
    tags={"monitoring", "memory", "performance", "system"},
    meta={"category": "monitoring", "complexity": "low"},
    annotations=ToolAnnotations(idempotent=True, read_only=True),
)
async def memory_statistics() -> dict:
    """Get memory statistics"""
    try:
        stats = get_memory_usage_stats()
        return {
            "process_memory": {
                "process_memory_mb": stats["process_memory_mb"],
                "virtual_memory_mb": stats["virtual_memory_mb"],
            },
            "cache_usage": {
                "expression_cache": {
                    "size": stats["expression_cache_size"],
                    "max": MAXIMUM_CACHE_SIZE,
                },
                "ast_cache": {"size": stats["ast_cache_size"], "max": MAXIMUM_CACHE_SIZE},
                "computation_stats": {
                    "size": stats["computation_stats_size"],
                    "max": MAXIMUM_COMPUTATION_STATISTICS,
                },
            },
            "session_management": {
                "active_sessions": stats["active_sessions"],
                "max_sessions": MAXIMUM_SESSIONS,
            },
            "other_components": {
                "rate_limiter_clients": stats["rate_limiter_clients"],
                "history_entries": {
                    "count": stats["history_entries"],
                    "max": CALCULATION_HISTORY_ENTRY_LIMIT,
                },
            },
        }
    except ImportError:
        return {"success": False, "error": "psutil package is required for memory monitoring"}
    except Exception as e:
        return {"success": False, "error": f"Error getting memory usage: {str(e)}"}


@mcp.tool(
    title="Calculate Expression",
    tags={"calculation", "basic", "math", "expression"},
    meta={"category": "calculation", "complexity": "medium"},
    annotations=ToolAnnotations(idempotent=True),
)
async def calculate_expression(expr: Annotated[str, "Mathematical expression to evaluate"]) -> dict:
    """Evaluate math expression"""
    global _active_mathematical_computations

    if _shutdown_requested:
        return {"success": False, "error": "Server is shutting down and cannot accept new requests"}

    _active_mathematical_computations += 1

    try:
        result = compute_expression(expr)
        return {
            "success": result.success,
            "expression": expr,
            "result": result.result if result.success else None,
            "error": result.error if not result.success else None,
        }
    except Exception as ex:
        return {"success": False, "error": str(ex)}
    finally:
        _active_mathematical_computations -= 1


@mcp.tool(
    title="Batch Calculate",
    tags={"calculation", "batch", "multiple", "expressions"},
    meta={"category": "calculation", "complexity": "medium"},
    annotations=ToolAnnotations(progress_tracking=True, long_running=True),
)
async def batch_calculate(
    expressions: Annotated[list[str], "List of mathematical expressions to evaluate"], c: Context
) -> dict:
    """Batch calculate expressions"""
    results = []
    total_expressions = len(expressions)

    for i, expr in enumerate(expressions):
        progress_percent = ((i + 1) / total_expressions) * 100
        await c.report_progress(progress=progress_percent, total=100)

        result = compute_expression(expr)
        results.append(
            {
                "expression": expr,
                "success": result.success,
                "result": result.result if result.success else None,
                "error": result.error["message"] if not result.success else None,
            }
        )

    return {"total_expressions": total_expressions, "results": results}


@mcp.tool(
    title="Statistical Analysis",
    tags={"statistics", "calculation", "analysis", "data"},
    meta={"category": "statistics", "complexity": "medium"},
    annotations=ToolAnnotations(progress_tracking=True, requires_confirmation=False),
)
async def calculate_statistics(
    data: Annotated[list[float], "List of numbers to analyze"],
    operation: Annotated[str, "Statistical operation (mean, median, mode, stdev, etc.)"],
    c: Context,
) -> dict:
    """Calculate statistics"""
    try:
        if operation not in STATISTICS_FUNCTIONS:
            elicit_result = await c.elicit(
                message=f"Unknown operation '{operation}'. Please select a statistical operation:",
                response_type=StatisticsOperationChoice,
            )

            if elicit_result.action == "accept":
                operation = elicit_result.data.statistical_operation_type
                if operation not in STATISTICS_FUNCTIONS:
                    return {
                        "success": False,
                        "error": f"Invalid operation selection '{operation}'",
                        "valid_options": sorted(STATISTICS_FUNCTIONS.keys()),
                    }
            else:
                return {"success": False, "error": "Operation cancelled by user"}

        await c.report_progress(progress=25, total=100)
        func = STATISTICS_FUNCTIONS[operation]
        await c.report_progress(progress=75, total=100)
        result = func(data)
        await c.report_progress(progress=100, total=100)

        return {"success": True, "operation": operation, "data_count": len(data), "result": result}
    except statistics.StatisticsError as e:
        return {"success": False, "error": "statistics_error", "message": str(e)}
    except Exception as e:
        return {"success": False, "error": "unexpected_error", "message": str(e)}


@mcp.tool(
    title="Matrix Operations",
    tags={"matrix", "linear-algebra", "advanced", "math"},
    meta={"category": "matrix", "complexity": "high"},
    annotations=ToolAnnotations(progress_tracking=True, destructive=False),
)
async def matrix_operation(
    matrices: Annotated[list[list[list[float]]], "List of matrices for operation"],
    operation: Annotated[str, "Matrix operation (multiply, determinant, inverse)"],
    c: Context,
) -> dict:
    """Matrix operations"""
    try:
        if operation == "multiply":
            if len(matrices) != 2:
                return {
                    "success": False,
                    "error": "Matrix multiplication requires exactly 2 matrices",
                    "required_matrices": 2,
                    "provided": len(matrices),
                }
            await c.report_progress(progress=25, total=100)
            result = matrix_multiply(matrices[0], matrices[1])
            await c.report_progress(progress=100, total=100)
            return {"success": True, "operation": "multiply", "result": result}

        elif operation == "determinant":
            if len(matrices) != 1:
                return {
                    "success": False,
                    "error": "Determinant requires exactly 1 matrix",
                    "required_matrices": 1,
                    "provided": len(matrices),
                }
            await c.report_progress(progress=50, total=100)
            result = matrix_determinant(matrices[0])
            await c.report_progress(progress=100, total=100)
            return {"success": True, "operation": "determinant", "result": result}

        elif operation == "inverse":
            if len(matrices) != 1:
                return {
                    "success": False,
                    "error": "Inverse requires exactly 1 matrix",
                    "required_matrices": 1,
                    "provided": len(matrices),
                }
            await c.report_progress(progress=40, total=100)
            result = matrix_inverse(matrices[0])
            await c.report_progress(progress=100, total=100)
            return {"success": True, "operation": "inverse", "result": result}

        else:
            elicit_result = await c.elicit(
                message=f"Unknown operation '{operation}'. Please select a matrix operation:",
                response_type=MatrixOperationChoice,
            )

            if elicit_result.action == "accept":
                operation = elicit_result.data.matrix_operation_type
                if operation == "multiply":
                    if len(matrices) != 2:
                        return {
                            "success": False,
                            "error": "Matrix multiplication requires exactly 2 matrices",
                            "required_matrices": 2,
                            "provided": len(matrices),
                        }
                    await c.report_progress(progress=25, total=100)
                    result_matrix = matrix_multiply(matrices[0], matrices[1])
                    await c.report_progress(progress=100, total=100)
                    return {"success": True, "operation": "multiply", "result": result_matrix}
                elif operation == "determinant":
                    if len(matrices) != 1:
                        return {
                            "success": False,
                            "error": "Determinant requires exactly 1 matrix",
                            "required_matrices": 1,
                            "provided": len(matrices),
                        }
                    await c.report_progress(progress=50, total=100)
                    result_det = matrix_determinant(matrices[0])
                    await c.report_progress(progress=100, total=100)
                    return {"success": True, "operation": "determinant", "result": result_det}
                elif operation == "inverse":
                    if len(matrices) != 1:
                        return {
                            "success": False,
                            "error": "Inverse requires exactly 1 matrix",
                            "required_matrices": 1,
                            "provided": len(matrices),
                        }
                    await c.report_progress(progress=40, total=100)
                    result_inv = matrix_inverse(matrices[0])
                    await c.report_progress(progress=100, total=100)
                    return {"success": True, "operation": "inverse", "result": result_inv}
                else:
                    return {
                        "success": False,
                        "error": "Invalid operation selection",
                        "operation": operation,
                        "valid_options": ["multiply", "determinant", "inverse"],
                    }
            else:
                return {"success": False, "error": "Operation cancelled by user"}

    except Exception as e:
        return {"success": False, "error": "unexpected_error", "message": str(e)}


@mcp.tool(
    title="Unit Conversion",
    tags={"conversion", "units", "measurement"},
    meta={"category": "conversion", "complexity": "low"},
    annotations=ToolAnnotations(idempotent=True),
)
async def convert_units(
    value: Annotated[float, "Numeric value to convert"],
    from_unit: Annotated[str, "Source unit"],
    to_unit: Annotated[str, "Target unit"],
    unit_type: Annotated[str, "Unit category (length, mass, time, temperature, etc.)"],
) -> dict:
    """Unit conversion"""
    try:
        from_unit_resolved = resolve_unit_alias(from_unit)
        to_unit_resolved = resolve_unit_alias(to_unit)
        result = convert_unit(value, from_unit_resolved, to_unit_resolved, unit_type)
        return {
            "success": True,
            "input_value": value,
            "input_unit": from_unit,
            "output_value": result,
            "output_unit": to_unit,
            "unit_type": unit_type,
            "resolved_input_unit": from_unit_resolved,
            "resolved_output_unit": to_unit_resolved,
        }
    except Exception as e:
        return {"success": False, "error": "conversion_failed", "message": str(e)}


@mcp.tool(
    title="Natural Language Conversion",
    tags={"conversion", "natural-language", "units", "nlp"},
    meta={"category": "conversion", "complexity": "medium"},
    annotations=ToolAnnotations(requires_confirmation=True),
)
async def convert_natural_language(
    query: Annotated[str, "Natural language conversion request"],
) -> dict:
    """Natural language conversion"""
    try:
        parsed = parse_natural_language_conversion(query)
        if not parsed:
            return {
                "success": False,
                "error": "parse_failed",
                "query": query,
                "supported_patterns": [
                    "convert X unit to unit",
                    "what is X unit in unit",
                    "X unit -> unit",
                    "X unit equals how many unit",
                    "from X unit to unit",
                ],
            }

        value, from_unit, to_unit, unit_type = parsed
        from_unit_resolved = resolve_unit_alias(from_unit)
        to_unit_resolved = resolve_unit_alias(to_unit)
        result = convert_unit(value, from_unit_resolved, to_unit_resolved, unit_type)

        return {
            "success": True,
            "conversion": {
                "original_query": query,
                "input_value": value,
                "input_unit": from_unit,
                "output_value": result,
                "output_unit": to_unit,
                "unit_type": unit_type,
                "resolved_input_unit": from_unit_resolved,
                "resolved_output_unit": to_unit_resolved,
            },
        }
    except Exception as e:
        return {"success": False, "error": "conversion_failed", "details": str(e), "query": query}


@mcp.tool(
    title="Number Theory",
    tags={"number-theory", "advanced", "math", "primes"},
    meta={"category": "number-theory", "complexity": "high"},
    annotations=ToolAnnotations(progress_tracking=True, long_running=True),
)
async def analyze_number_theory(
    number: Annotated[int, "Integer to analyze"],
    operation: Annotated[
        str, "Number theory operation (is_prime, prime_factors, divisors, totient)"
    ],
    c: Context,
) -> dict:
    """Number theory operations"""
    try:
        if operation == "is_prime":
            await c.report_progress(progress=50, total=100)
            result = is_prime(number)
            await c.report_progress(progress=100, total=100)
            return {
                "success": True,
                "operation": "is_prime",
                "number": number,
                "result": result,
                "is_prime": result,
            }

        elif operation == "prime_factors":
            await c.report_progress(progress=25, total=100)
            result = prime_factors(number)
            await c.report_progress(progress=100, total=100)
            return {
                "success": True,
                "operation": "prime_factors",
                "number": number,
                "factors": result,
            }

        elif operation == "divisors":
            await c.report_progress(progress=30, total=100)
            divisors = [i for i in range(1, number + 1) if number % i == 0]
            await c.report_progress(progress=100, total=100)
            return {
                "success": True,
                "operation": "divisors",
                "number": number,
                "divisors": divisors,
                "count": len(divisors),
            }

        elif operation == "totient":
            await c.report_progress(progress=35, total=100)
            result = sum(1 for i in range(1, number) if math.gcd(i, number) == 1)
            await c.report_progress(progress=100, total=100)
            return {"success": True, "operation": "totient", "number": number, "result": result}

        else:
            elicit_result = await c.elicit(
                message=f"Unknown operation '{operation}'. Please select a number theory operation:",
                response_type=NumberTheoryOperationChoice,
            )

            if elicit_result.action == "accept":
                operation = elicit_result.data.number_theory_operation_type
                if operation == "is_prime":
                    await c.report_progress(progress=50, total=100)
                    result = is_prime(number)
                    await c.report_progress(progress=100, total=100)
                    return {
                        "success": True,
                        "operation": "is_prime",
                        "number": number,
                        "result": result,
                        "is_prime": result,
                    }
                elif operation == "prime_factors":
                    await c.report_progress(progress=25, total=100)
                    result = prime_factors(number)
                    await c.report_progress(progress=100, total=100)
                    return {
                        "success": True,
                        "operation": "prime_factors",
                        "number": number,
                        "factors": result,
                    }
                elif operation == "divisors":
                    await c.report_progress(progress=30, total=100)
                    divisors = [i for i in range(1, number + 1) if number % i == 0]
                    await c.report_progress(progress=100, total=100)
                    return {
                        "success": True,
                        "operation": "divisors",
                        "number": number,
                        "divisors": divisors,
                        "count": len(divisors),
                    }
                elif operation == "totient":
                    await c.report_progress(progress=35, total=100)
                    result = sum(1 for i in range(1, number) if math.gcd(i, number) == 1)
                    await c.report_progress(progress=100, total=100)
                    return {
                        "success": True,
                        "operation": "totient",
                        "number": number,
                        "result": result,
                    }
                else:
                    return {
                        "success": False,
                        "error": "Invalid operation selection",
                        "operation": operation,
                        "valid_options": ["is_prime", "prime_factors", "divisors", "totient"],
                    }
            else:
                return {"success": False, "error": "Operation cancelled by user"}

    except Exception as e:
        return {"success": False, "error": "unexpected_error", "message": str(e)}


@mcp.tool(
    title="Create Session",
    tags={"session", "management", "variables", "state"},
    meta={"category": "session", "complexity": "low"},
    annotations=ToolAnnotations(destructive=False),
)
async def create_session(
    session_id: Annotated[str | None, "Optional session identifier"] = None,
    variables: Annotated[dict[str, float] | None, "Initial session variables"] = None,
) -> dict:
    """Create session"""
    try:
        if not session_id:
            session_id = f"session_{int(time.time() * 1000)}"

        _get_session_manager().create_session(session_id, variables)
        return {
            "success": True,
            "session_id": session_id,
            "initial_variables": variables or {},
            "variable_count": len(variables) if variables else 0,
        }
    except Exception as e:
        return {"success": False, "error": "session_creation_failed", "message": str(e)}


@mcp.tool(
    title="Session Calculation",
    tags={"calculation", "session", "variables", "state"},
    meta={"category": "session-calculation", "complexity": "medium"},
    annotations=ToolAnnotations(idempotent=False),
)
async def session_calculate(
    session_id: Annotated[str, "Session identifier"],
    expr: Annotated[str, "Mathematical expression to evaluate"],
    var_name: Annotated[str | None, "Variable name to store result"] = None,
) -> dict:
    """Session calculation"""
    global _active_mathematical_computations

    if _shutdown_requested:
        return {"success": False, "error": "Server is shutting down and cannot accept new requests"}

    _active_mathematical_computations += 1

    try:
        result = compute_expression(expr, session_id)

        if result.success and var_name:
            _get_session_manager().update_session(session_id, var_name, result.result)

        return {
            "success": result.success,
            "session_id": session_id,
            "expression": expr,
            "result": result.result if result.success else None,
            "error": result.error if not result.success else None,
            "variable_stored": var_name if (result.success and var_name) else None,
        }
    except Exception as e:
        return {"success": False, "error": "unexpected_error", "message": str(e)}
    finally:
        _active_mathematical_computations -= 1


@mcp.tool(
    title="List Session Variables",
    tags={"session", "variables", "management", "inspection"},
    meta={"category": "session", "complexity": "low"},
    annotations=ToolAnnotations(idempotent=True, read_only=True),
)
async def list_session_variables(session_id: Annotated[str, "Session identifier"]) -> dict:
    """List session variables"""
    variables = _get_session_manager().get_session(session_id)
    if variables is None:
        return {"success": False, "error": "Session not found", "session_id": session_id}

    return {
        "success": True,
        "session_id": session_id,
        "variables": variables,
        "count": len(variables),
    }


@mcp.tool(
    title="Delete Session",
    tags={"session", "management", "cleanup"},
    meta={"category": "session", "complexity": "low"},
    annotations=ToolAnnotations(destructive=True, requires_confirmation=False),
)
async def delete_session(session_id: Annotated[str, "Session identifier"]) -> dict:
    """Delete session"""
    deleted = _get_session_manager().delete_session(session_id)
    return {
        "success": deleted,
        "session_id": session_id,
        "message": (
            f"Session {session_id} deleted" if deleted else f"Session {session_id} not found"
        ),
    }


@mcp.tool(
    title="Calculation History",
    tags={"history", "audit", "calculation", "tracking"},
    meta={"category": "history", "complexity": "low"},
    annotations=ToolAnnotations(idempotent=True, read_only=True),
)
async def get_calculation_history(
    limit: Annotated[int, "Number of recent calculations to retrieve"] = 10,
) -> dict:
    """Get calculation history"""
    limit_requested = limit
    if limit > CALCULATION_HISTORY_ENTRY_LIMIT:
        limit = CALCULATION_HISTORY_ENTRY_LIMIT

    history = mathematical_calculation_history.get_recent(limit)
    if not history:
        return {
            "success": True,
            "limit_requested": limit_requested,
            "limit_used": limit,
            "entries_count": 0,
            "entries": [],
        }

    return {
        "success": True,
        "limit_requested": limit_requested,
        "limit_used": limit,
        "entries_count": len(history),
        "entries": [
            {
                "expression": entry["expression"],
                "result": entry["result"],
                "timestamp": entry["timestamp"],
            }
            for entry in history
        ],
    }


@mcp.tool(
    title="Clear History",
    tags={"history", "management", "cleanup"},
    meta={"category": "history", "complexity": "low"},
    annotations=ToolAnnotations(destructive=True, requires_confirmation=True),
)
async def clear_history() -> dict:
    """Clear history"""
    mathematical_calculation_history.clear()
    return {"success": True, "message": "Calculation history cleared successfully"}


@mcp.tool(
    title="Optimize Memory",
    tags={"optimization", "memory", "management", "cleanup"},
    meta={"category": "optimization", "complexity": "low"},
    annotations=ToolAnnotations(destructive=True, requires_confirmation=True),
)
async def optimize_memory() -> dict:
    """Optimize memory"""
    try:
        cleanup_stats = cleanup_expired_cache_entries()
        total_cleaned = sum(cleanup_stats.values())
        return {
            "success": True,
            "cleanup_stats": {
                "expression_cache_expired": cleanup_stats["expression_cache_expired"],
                "sessions_expired": cleanup_stats["sessions_expired"],
                "rate_limiter_expired": cleanup_stats["rate_limiter_expired"],
            },
            "total_cleaned": total_cleaned,
        }
    except Exception as e:
        return {"success": False, "error": "cleanup_failed", "message": str(e)}


@mcp.tool(
    title="List Functions",
    tags={"discovery", "help", "reference", "documentation"},
    meta={"category": "discovery", "complexity": "low"},
    annotations=ToolAnnotations(idempotent=True, read_only=True),
)
async def list_functions() -> dict:
    """List functions"""
    basic_funcs = ["sin", "cos", "tan", "sqrt", "exp", "log", "log10", "log2", "pow", "factorial"]
    basic_functions = sorted(f for f in MATH_FUNCTIONS if f in basic_funcs)

    statistics_functions = sorted(STATISTICS_FUNCTIONS.keys())
    complex_functions = sorted(COMPLEX_FUNCTIONS.keys())

    constants = {const: MATH_CONSTANTS[const] for const in sorted(MATH_CONSTANTS.keys())}

    operators = {
        "arithmetic": ["+", "-", "*", "/", "//", "%", "**", "×", "÷", "^"],
        "comparison": ["==", "!=", "<", "<=", ">", ">="],
    }

    unit_types = {
        unit_type: list(UNIT_CONVERSIONS[unit_type].keys()) for unit_type in UNIT_CONVERSIONS
    }

    return {
        "success": True,
        "basic_functions": basic_functions,
        "statistics_functions": statistics_functions,
        "complex_functions": complex_functions,
        "constants": constants,
        "operators": operators,
        "unit_types": unit_types,
        "total_functions": len(basic_functions)
        + len(statistics_functions)
        + len(complex_functions),
    }


@mcp.resource(
    "resource://history/recent",
    title="Recent Calculation History",
    description="Returns the 20 most recent mathematical calculations with their results and timestamps",
    mime_type="text/plain",
    tags={"history", "audit", "calculations", "recent"},
    meta={"category": "history", "max_entries": 20, "format": "text"},
    annotations={"readOnlyHint": True, "idempotentHint": True},
)
async def recent_calculation_history() -> str:
    history = mathematical_calculation_history.get_recent(20)
    if not history:
        return "No calculation history available"

    lines = ["Recent Calculations:"]
    for entry in history:
        lines.append(f"  {entry['expression']} = {entry['result']}")
    return "\\n".join(lines)


@mcp.resource(
    "resource://functions/all",
    title="Mathematical Functions Catalog",
    description="Comprehensive catalog of all available mathematical functions organized by category (trigonometric, hyperbolic, logarithmic, statistical, and other functions)",
    mime_type="text/plain",
    tags={"functions", "reference", "documentation", "catalog"},
    meta={
        "category": "reference",
        "includes": ["trigonometric", "hyperbolic", "logarithmic", "statistical", "other"],
    },
    annotations={"readOnlyHint": True, "idempotentHint": True},
)
async def mathematical_functions_catalog() -> str:
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

    lines.append("\\nStatistical:")
    for func in sorted(STATISTICS_FUNCTIONS.keys()):
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


@mcp.resource(
    "resource://constants/math",
    title="Mathematical Constants Catalog",
    description="Complete catalog of mathematical constants including pi, e, golden ratio, and other fundamental constants with their precise values",
    mime_type="text/plain",
    tags={"constants", "reference", "mathematics", "values"},
    meta={
        "category": "reference",
        "precision": "high",
        "includes_constants": list(MATH_CONSTANTS.keys())[:10],
    },
    annotations={"readOnlyHint": True, "idempotentHint": True},
)
async def mathematical_constants_catalog() -> str:
    lines = ["Mathematical Constants:"]
    for name, value in MATH_CONSTANTS.items():
        lines.append(f"  {name} = {value}")
    return "\\n".join(lines)


@mcp.prompt(
    name="scientific_calculation",
    title="Scientific Calculation Prompt Generator",
    description="Generate scientific calculation prompt with examples and precision settings",
    tags={"calculation", "scientific", "mathematics"},
    meta={
        "category": "calculation",
        "supports": ["general", "trigonometric", "logarithmic", "statistical"],
    },
)
async def sci_calc(
    calc_type: Annotated[
        str, "Calculation type (general, trigonometric, logarithmic, statistical)"
    ] = "general",
    precision: Annotated[int, "Decimal precision for results"] = 6,
    show_steps: Annotated[bool, "Include step-by-step solution"] = False,
) -> str:
    """Generate scientific calculation prompt with customizable parameters for different mathematical operations."""
    examples = {
        "general": "2+3, 10-4, 5*6",
        "trigonometric": "sin(pi/2), cos(0)",
        "logarithmic": "log(10), exp(1)",
        "statistical": "mean([1,2,3]), stdev([1,2,3])",
    }
    steps_text = " with step-by-step solution" if show_steps else ""
    return f"Calculate with {precision} decimal precision{steps_text}. Examples: {examples.get(calc_type, examples['general'])}"


@mcp.prompt(
    name="batch_calculation",
    title="Batch Calculation Prompt Generator",
    description="Generate batch calculation prompt with configurable operation types and complexity levels",
    tags={"calculation", "batch", "multiple"},
    meta={"category": "calculation", "complexity_levels": ["simple", "medium", "advanced"]},
)
async def batch_calc(
    batch_size: Annotated[int, "Number of calculations to process"] = 5,
    operation_types: Annotated[list[str], "Types of operations to include"] = None,
    complexity: Annotated[str, "Complexity level (simple, medium, advanced)"] = "medium",
) -> str:
    """Generate batch calculation prompt for processing multiple mathematical expressions at once."""
    if operation_types is None:
        operation_types = ["arithmetic", "trigonometric"]
    examples = {
        "simple": "2+2, 10-4, 5*6",
        "medium": "sin(pi/2), sqrt(16), log(10)",
        "advanced": "factorial(20)/factorial(15), mean([1,2,3])*stdev([1,2,3])",
    }
    return f"Process {batch_size} calculations including {', '.join(operation_types)} operations at {complexity} complexity. Examples: {examples.get(complexity, examples['medium'])}"


if __name__ == "__main__":
    mcp.run()
