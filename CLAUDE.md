# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

MCP Mathematics is a production-ready Model Context Protocol (MCP) server providing comprehensive mathematical computation capabilities. Built with FastMCP v2.0+, it exposes 52 advanced mathematical functions, 158 unit conversions across 15 categories, financial calculations, and statistical operations through 21 specialized MCP tools.

**Key Architecture Principle**: AST-based expression evaluation ensures security by preventing code injection while maintaining full mathematical capability.

## Development Commands

### Testing

```bash
# Run all tests (130 test cases)
python -m pytest tests/ -v

# Run tests with coverage
python -m pytest tests/ --cov=src --cov-report=html

# Run specific test categories
python -m pytest tests/test_calculator.py -v # Core functionality
python -m pytest tests/performance/ -v       # Performance tests
python -m pytest tests/security/ -v          # Security validation
python -m pytest tests/precision/ -v         # Numerical precision
python -m pytest tests/validation/ -v        # Input validation
```

### Code Quality

```bash
# Auto-format code (100-character line limit)
black src/ tests/ --line-length 100

# Lint with Ruff
ruff check src/ tests/ --fix

# Type checking
mypy src/

# Security analysis
bandit -r src/

# Run all pre-commit checks
pre-commit run --all-files
```

### Running the Server

```bash
# Development mode (local testing)
python -m mcp_mathematics

# Using uv (recommended for production)
uvx mcp-mathematics

# Install in editable mode for development
pip install -e .
```

### Building and Distribution

```bash
# Clean previous builds
rm -rf dist/ build/

# Build source and wheel distributions
python -m build

# Verify package integrity
twine check dist/*

# Test installation in clean environment
pip install dist/*.whl
```

## Architecture Overview

### Core Components

**Single-File Architecture**: All functionality is consolidated in `src/mcp_mathematics/calculator.py` (~4500 lines) for maximum portability and minimal dependencies.

#### Security Layer (AST Evaluation Engine)

- **Input Validation**: Regex-based pattern matching blocks forbidden operations (`import`, `exec`, `eval`, `__*__`, etc.)
- **AST Parsing**: Python's Abstract Syntax Tree validates expression structure before evaluation
- **Node Depth Limiting**: Maximum AST depth of 10 prevents deeply nested attacks
- **Operation Whitelisting**: Only approved mathematical operations (arithmetic, functions, comparisons) are allowed
- **Resource Limits**: Expression length (1000 chars), computation timeout (15s), memory limits (512MB)

#### Cache System

- **LRUExpressionCache**: Bounded LRU cache with configurable max size (1000 entries)
- **TTLExpressionCache**: Time-based expiry (300s default) for computation results
- **Thread-Safe**: RLock-based synchronization for concurrent access
- **Memory Management**: Automatic cleanup via threading.Timer (no signal-based timeouts)

#### Session Management

- **SessionVariableManager**: Stateful calculation contexts with variable storage
- **Session Isolation**: Independent namespaces per session_id
- **TTL-Based Cleanup**: Automatic session expiry (3600s default, configurable)
- **Bounded Sessions**: Maximum 100 concurrent sessions with LRU eviction

#### Computation Tracking

- **ComputationMetrics**: Thread-safe performance monitoring
- **CalculationHistory**: Deque-based history with configurable limit (100 entries)
- **Rate Limiting**: Per-client request tracking (1M requests/60s window)

### FastMCP Integration

**Configuration**: `fastmcp.json` defines:

- **Source**: `src/mcp_mathematics/calculator.py` with entrypoint `mcp`
- **Environment**: `uv` with Python >=3.10, dependencies: `mcp>=1.4.1`, `fastmcp>=0.1.0`
- **Deployment**: stdio transport, INFO log level

**Tool Annotations**: All 21 tools use FastMCP's `ToolAnnotations` for behavioral metadata (safe, caches, writes, etc.)

### MCP Tools Structure

21 tools organized by domain with descriptive mathematical names:

**Core Calculation**:

1. `evaluate_mathematical_expression` - Single expression evaluation
2. `evaluate_multiple_mathematical_expressions` - Parallel batch processing
3. `convert_between_measurement_units` - 158 units across 15 categories
4. `convert_units_from_natural_language` - NLP-based unit conversion
5. `compute_statistical_operations` - Statistical analysis (mean, median, std dev, etc.)
6. `perform_matrix_mathematical_operations` - Linear algebra (multiply, determinant, inverse)
7. `perform_number_theory_analysis` - Prime testing, factorization, divisors

**Session Management**:
8\. `create_mathematical_calculation_session` - Initialize stateful context
9\. `evaluate_expression_in_session_context` - Session-aware calculations
10\. `list_mathematical_session_variables` - Variable inspection
11\. `delete_mathematical_calculation_session` - Session cleanup

**System Monitoring**:
12\. `performance_metrics` - Performance stats
13\. `security_status` - Security status
14\. `memory_statistics` - Memory analytics

**Management**:
15\. `get_calculation_history` - Audit trail (1-100 recent calculations)
16\. `clear_history` - History cleanup
17\. `optimize_memory` - Cache/session cleanup
18\. `list_functions` - Complete capability discovery

**Resources**: 3 MCP resources (`history://recent`, `functions://available`, `constants://math`)
**Prompts**: 2 MCP prompts (`scientific_calculation`, `batch_calculation`)

## Critical Implementation Details

### Mathematical Functions (52 total)

**Trigonometric**: sin, cos, tan, asin, acos, atan, atan2
**Hyperbolic**: sinh, cosh, tanh, asinh, acosh, atanh
**Logarithmic**: log, log10, log2, log1p, exp, exp2, expm1
**Power/Root**: sqrt, pow, cbrt, isqrt
**Rounding**: ceil, floor, trunc
**Special**: factorial, gamma, lgamma, erf, erfc
**Number Theory**: gcd, lcm, comb, perm
**Float Ops**: fabs, copysign, fmod, remainder, modf, frexp, ldexp, hypot
**Comparison**: isfinite, isinf, isnan, isclose
**Advanced**: nextafter, ulp
**Angle**: degrees, radians

**Constants**: pi, e, tau, inf, nan

### Unit Conversion System

**15 Categories, 158 Units**:

- Length (15): m, km, mi, ft, in, ly, AU, etc.
- Mass (13): kg, g, lb, oz, ton, ct, amu, etc.
- Time (15): s, min, h, d, yr, ms, ns, millennium, etc.
- Temperature (3): K, C, F
- Area (12): m2, km2, acre, hectare, ft2, etc.
- Volume (16): L, gal, qt, m3, cup, tbsp, etc.
- Speed (10): m/s, km/h, mph, knot, mach, c (light speed %)
- Data (16): B, KB, MB, GB, TB, bit, KiB, etc.
- Pressure (10): Pa, atm, bar, psi, torr, mmHg, etc.
- Energy (12): J, kJ, cal, kcal, Wh, BTU, eV, etc.
- Power (10): W, kW, hp, BTU/h, cal/s, etc.
- Force (8): N, kN, lbf, kgf, dyne, etc.
- Angle (6): deg, rad, grad, arcmin, arcsec, turn
- Frequency (6): Hz, kHz, MHz, GHz, rpm, rad/s
- Fuel Economy (6): mpg, L/100km, km/L, etc.

**Features**: Unit aliases, auto-detection, compound unit parsing, conversion history tracking

### Financial Functions

**Core**: calculate_percentage, calculate_percentage_of, calculate_percentage_change
**Interest**: calculate_simple_interest, calculate_compound_interest
**Loans**: calculate_loan_payment (with amortization)
**Tax**: calculate_tax (inclusive/exclusive)
**Bills**: split_bill, calculate_tip
**Pricing**: calculate_discount, calculate_markup

### Security Configuration

**Limits** (modifiable via constants):

- `MAXIMUM_MATHEMATICAL_EXPRESSION_CHARACTER_LIMIT = 1000`
- `MAXIMUM_AST_NODE_DEPTH_LIMIT = 10`
- `MATHEMATICAL_OPERATION_TIMEOUT_SECONDS = 15.0`
- `MAXIMUM_COMPUTATION_DURATION_SECONDS = 20.0`
- `FACTORIAL_COMPUTATION_UPPER_BOUND = 300`
- `EXPONENTIATION_SAFETY_THRESHOLD = 10000`
- `MAXIMUM_MEMORY_USAGE_MEGABYTES = 512`
- `MAXIMUM_LIST_ELEMENT_COUNT_LIMIT = 10000`

**Forbidden Patterns**: 10 regex patterns block imports, exec/eval, dunder methods, introspection functions

**Thread Safety**: 5 RLocks protect shared resources (cache, metrics, history, sessions, rate limiting)

## Code Quality Standards

**Production-Grade Requirements**:

- **No Debug Code**: Zero console.log, print statements, or debug comments in production code
- **Type Safety**: Complete type annotations using Python 3.10+ syntax
- **Clean Code**: Professional codebase with minimal inline comments (code is self-documenting)
- **100-Character Line Limit**: Enforced via Black formatter
- **Comprehensive Testing**: 130 tests across 5 categories (core, performance, security, precision, validation)

**Automated Quality Tools**:

- Black (formatting)
- Ruff (linting with E, W, F, I, B, C4, UP, ARG, SIM rules)
- mypy (type checking)
- bandit (security analysis)
- pre-commit hooks

## Common Development Workflows

### Adding a New Mathematical Function

1. Add function to `SAFE_MATHEMATICAL_FUNCTIONS` dict in `calculator.py`
2. Update `list_functions` documentation
3. Add comprehensive tests in `tests/test_calculator.py`
4. Verify security: ensure function can't bypass AST validation
5. Run full test suite + security analysis

### Adding a New Unit Conversion Category

1. Add conversion factors to `UNIT_CONVERSION_FACTORS` dict
2. Update unit aliases in `UNIT_ALIASES` dict
3. Add category to `list_functions` output
4. Add conversion tests with edge cases
5. Verify precision and rounding behavior

### Modifying Security Limits

1. Update constants at top of `calculator.py`
2. Test edge cases at new limits
3. Run security test suite: `pytest tests/security/ -v`
4. Document changes in CHANGELOG.md

### Adding a New MCP Tool

1. Define tool function with FastMCP `@mcp.tool()` decorator
2. Add `ToolAnnotations` with appropriate behavioral metadata
3. Implement input validation and error handling
4. Add comprehensive docstring with parameter descriptions
5. Write unit tests covering success/failure cases
6. Update README.md with tool documentation

## Testing Strategy

**Test Categories**:

- **Core Functionality** (`test_calculator.py`): All 52 functions, operators, edge cases, error handling
- **Performance** (`tests/performance/`): Timeout handling, batch processing, cache efficiency
- **Security** (`tests/security/`): AST validation, forbidden patterns, resource limits
- **Precision** (`tests/precision/`): Numerical accuracy, rounding, float comparison
- **Validation** (`tests/validation/`): Input sanitization, type checking, boundary conditions

**Coverage Target**: >90% code coverage across all modules

## Deployment Considerations

**Packaging**: Built with `hatchling`, distributed via PyPI as `mcp-mathematics`
**Entry Point**: `mcp-mathematics` command via `project.scripts`
**FastMCP Cloud**: Available at `https://mathematics.fastmcp.app/mcp` for cloud deployment

**MCP Client Configuration**:

- Claude Desktop: `claude_desktop_config.json` with `uvx` or `mcp-mathematics` command
- VS Code Continue: `mcpServers` config with `uvx` transport
- FastMCP Cloud: Multiple connection methods (Claude Code, Codex, Gemini, Cursor)

## Troubleshooting

**Memory Leaks**: If memory grows unbounded, check:

- Cache TTL cleanup timer initialization
- Session cleanup interval (SESSION_CLEANUP_INTERVAL)
- Call `optimize_memory` periodically

**Performance Degradation**: Monitor via `performance_metrics`:

- Cache hit rate (should be >70% for repetitive workloads)
- Average computation time (should be \<100ms for simple expressions)
- Memory usage (should stay below MAXIMUM_MEMORY_USAGE_MEGABYTES)

**Security Alerts**: Check `security_status`:

- Rate limit violations (adjust MAXIMUM_CLIENT_REQUESTS_PER_TIME_WINDOW)
- Forbidden pattern matches (review FORBIDDEN_PATTERNS)
- AST depth violations (review MAXIMUM_AST_NODE_DEPTH_LIMIT)

## Important Notes

- **Single Source of Truth**: All functionality in `calculator.py` - no separate modules
- **Zero External Dependencies**: Core math uses only Python stdlib (math, ast, operator)
- **Thread Safety**: All shared state protected by RLocks - safe for concurrent MCP requests
- **Timer-Based Timeouts**: Uses threading.Timer instead of signals for cross-platform compatibility
- **Unicode Operators**: Supports ×, ÷, ^ for natural mathematical notation
- **FastMCP v2.0+ Compliance**: 100% compliant with FastMCP v2.0+ behavioral annotation standards

## Task Master AI Instructions

**Import Task Master's development workflow commands and guidelines, treat as if import is in the main CLAUDE.md file.**
@./.taskmaster/CLAUDE.md
