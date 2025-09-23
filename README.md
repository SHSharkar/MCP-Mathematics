# MCP Mathematics

A powerful Model Context Protocol (MCP) server that brings production-ready mathematical calculations to AI assistants like Claude, featuring secure AST-based evaluation and comprehensive mathematical functions.

## What Is MCP Mathematics?

MCP Mathematics transforms your AI assistant into a powerful mathematical computation engine. Built specifically for the Model Context Protocol, this production-ready server enables AI agents to perform complex calculations through a secure, sandboxed environment. By leveraging Python's Abstract Syntax Tree (AST) evaluation, it delivers robust mathematical capabilities while maintaining the highest security standards—no direct code execution, no security risks.

## Why Choose MCP Mathematics?

### Uncompromising Security
- **AST-Based Evaluation**: Every expression is parsed and validated through Python's AST, eliminating code injection vulnerabilities
- **Sandboxed Execution**: Calculations run in a controlled environment with strict operation whitelisting
- **Zero External Dependencies**: Minimal attack surface with no third-party libraries required for core functionality

### Comprehensive Mathematical Power
- **52 Built-In Functions**: From basic arithmetic to advanced scientific computations
- **Unicode Operator Support**: Natural mathematical notation using symbols like ×, ÷, and ^
- **Full Math Library Coverage**: Complete access to Python's mathematical functions

### Production-Ready Architecture
- **Type-Safe Design**: Full type annotations throughout the codebase ensure reliability
- **Clean Production Code**: No debug statements, console logs, or unnecessary comments
- **Comprehensive Testing**: 61 unit tests provide thorough coverage of all functionality

## Getting Started

### Prerequisites

Before installing MCP Mathematics, ensure you have:
- Python 3.10 or later installed on your system
- An MCP-compatible AI assistant (Claude Desktop, VS Code with Continue, or similar)

### Installation Options

Choose the installation method that works best for your setup:

#### Option 1: Quick Install with uv (Recommended)

The fastest way to get started:

```bash
# Install the uv package manager if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install and run MCP Mathematics
uvx mcp-mathematics
```

#### Option 2: Traditional pip Installation

For those preferring pip:

```bash
pip install mcp-mathematics
```

#### Option 3: Development Installation

For contributors or those wanting the latest development version:

```bash
git clone https://github.com/SHSharkar/MCP-Mathematics.git
cd MCP-Mathematics
pip install -e .
```

## Configuration Guide

### Configuring Claude Desktop

To enable MCP Mathematics in Claude Desktop, you'll need to modify your configuration file.

**Configuration file locations:**
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

#### If you installed with uv:
```json
{
  "mcpServers": {
    "mcp-mathematics": {
      "command": "uvx",
      "args": ["mcp-mathematics"]
    }
  }
}
```

#### If you installed with pip:
```json
{
  "mcpServers": {
    "mcp-mathematics": {
      "command": "mcp-mathematics"
    }
  }
}
```

### Configuring VS Code with Continue

For VS Code users with the Continue extension:

```json
{
  "models": [
    {
      "model": "claude-3-5-sonnet",
      "provider": "anthropic",
      "mcpServers": {
        "mcp-mathematics": {
          "command": "uvx",
          "args": ["mcp-mathematics"]
        }
      }
    }
  ]
}
```

## Available MCP Tools

MCP Mathematics provides five powerful tools for mathematical operations:

### 1. `calculate` - Single Expression Evaluation
Evaluate any mathematical expression with full function support.
```
Input: "2 * pi * 10"
Output: "62.83185307179586"
```

### 2. `batch_calculate` - Parallel Processing
Process multiple expressions efficiently in a single operation.
```
Input: ["sin(pi/2)", "cos(0)", "sqrt(16)"]
Output: ["1.0", "1.0", "4.0"]
```

### 3. `get_calculation_history` - Audit Trail
Retrieve recent calculations with timestamps for tracking and verification.
```
Returns the last 10 calculations by default
```

### 4. `clear_history` - History Management
Clear all stored calculation history when needed.

### 5. `list_functions` - Function Discovery
Get a comprehensive list of all available mathematical functions and constants.

## MCP Resources

Access these resources directly through the MCP protocol:

- **`history://recent`** - View recent calculation history
- **`functions://available`** - Browse available mathematical functions
- **`constants://math`** - Access mathematical constants with their values

## MCP Prompts

Pre-configured prompts for common calculation patterns:

- **`scientific_calculation`** - Structured template for scientific computations
- **`batch_calculation`** - Optimized template for batch processing

## Mathematical Capabilities

### Basic Operations

MCP Mathematics supports standard mathematical operators with natural alternatives:

- Addition: `+`
- Subtraction: `-`
- Multiplication: `*` or `×`
- Division: `/` or `÷`
- Floor Division: `//`
- Modulo: `%`
- Exponentiation: `**` or `^`

### Complete Function Library

#### Trigonometric Functions
Essential trigonometric operations in radians:
- `sin(x)`, `cos(x)`, `tan(x)` - Standard trigonometric functions
- `asin(x)`, `acos(x)`, `atan(x)` - Inverse trigonometric functions
- `atan2(y, x)` - Two-argument arctangent for proper quadrant

#### Hyperbolic Functions
Complete hyperbolic function set:
- `sinh(x)`, `cosh(x)`, `tanh(x)` - Hyperbolic functions
- `asinh(x)`, `acosh(x)`, `atanh(x)` - Inverse hyperbolic functions

#### Logarithmic and Exponential Functions
Comprehensive logarithmic operations:
- `log(x)` - Natural logarithm
- `log10(x)` - Common logarithm (base 10)
- `log2(x)` - Binary logarithm
- `log1p(x)` - Natural logarithm of (1 + x) for precision
- `exp(x)` - Exponential function (e^x)
- `exp2(x)` - Base-2 exponential
- `expm1(x)` - Exponential minus 1 (e^x - 1)
- `sqrt(x)` - Square root
- `pow(x, y)` - Power function

#### Rounding and Precision
Control over numerical precision:
- `ceil(x)` - Round up to nearest integer
- `floor(x)` - Round down to nearest integer
- `trunc(x)` - Remove decimal portion

#### Special Mathematical Functions
Advanced mathematical operations:
- `factorial(x)` - Factorial computation
- `gamma(x)` - Gamma function
- `lgamma(x)` - Natural logarithm of gamma function
- `erf(x)` - Error function
- `erfc(x)` - Complementary error function

#### Number Theory
Integer and combinatorial mathematics:
- `gcd(x, y)` - Greatest common divisor
- `lcm(x, y)` - Least common multiple (Python 3.9+)
- `isqrt(x)` - Integer square root
- `comb(n, k)` - Binomial coefficient (combinations)
- `perm(n, k)` - Permutations

#### Floating-Point Operations
Precise control over floating-point arithmetic:
- `fabs(x)` - Floating-point absolute value
- `copysign(x, y)` - Magnitude of x with sign of y
- `fmod(x, y)` - Floating-point remainder
- `remainder(x, y)` - IEEE remainder operation
- `modf(x)` - Separate integer and fractional parts
- `frexp(x)` - Decompose into mantissa and exponent
- `ldexp(x, i)` - Compute x × 2^i efficiently
- `hypot(x, y)` - Euclidean distance calculation
- `cbrt(x)` - Cube root (Python 3.11+)

#### Numerical Comparison
Functions for numerical analysis:
- `isfinite(x)` - Check for finite values
- `isinf(x)` - Check for infinity
- `isnan(x)` - Check for Not-a-Number
- `isclose(a, b)` - Approximate equality testing

#### Advanced Numerical Functions
Specialized operations for scientific computing:
- `nextafter(x, y)` - Next representable floating-point value
- `ulp(x)` - Unit of least precision

#### Angle Conversion
Seamless conversion between angle units:
- `degrees(x)` - Convert radians to degrees
- `radians(x)` - Convert degrees to radians

### Mathematical Constants

Access fundamental mathematical constants:
- `pi` - π ≈ 3.141592653589793
- `e` - Euler's number ≈ 2.718281828459045
- `tau` - τ = 2π ≈ 6.283185307179586
- `inf` - Positive infinity
- `nan` - Not a Number

## Real-World Examples

### Basic Arithmetic
```python
calculate("2 + 3 * 4")  # Result: 14
calculate("10 / 3")     # Result: 3.3333333333333335
calculate("2 ** 8")     # Result: 256
```

### Scientific Computing
```python
calculate("sin(pi/2)")           # Result: 1.0
calculate("log10(1000)")         # Result: 3.0
calculate("sqrt(16) + cos(0)")   # Result: 5.0
```

### Complex Mathematical Expressions
```python
calculate("(2 + 3) * sqrt(16) / sin(pi/2)")  # Result: 20.0
calculate("factorial(5) + gcd(12, 8)")       # Result: 124
```

### Natural Mathematical Notation
```python
calculate("5 × 3")    # Result: 15
calculate("20 ÷ 4")   # Result: 5.0
calculate("2 ^ 10")   # Result: 1024
```

## Architecture and Security

### Security-First Design

MCP Mathematics prioritizes security without compromising functionality:

- **AST Evaluation Only**: Every expression is parsed into an Abstract Syntax Tree before evaluation, preventing any form of code injection
- **Strict Whitelisting**: Only explicitly approved operations and functions can be executed
- **Input Validation**: All expressions undergo rigorous validation before processing
- **Error Isolation**: Comprehensive error handling ensures failures don't compromise the system
- **Minimal Dependencies**: Core functionality requires no external libraries, reducing potential vulnerabilities

### Production-Grade Code Quality

Built to production standards:

- **Type Safety**: Complete type annotations using Python 3.10+ features
- **Clean Architecture**: Modular design with clear separation of concerns
- **Professional Codebase**: No debug statements or unnecessary comments in production
- **Comprehensive Testing**: 61 unit tests ensure reliability across all functions
- **Code Standards**: Enforced through automated linting and formatting

## Development Guide

### Running the Test Suite

Ensure all functionality works as expected:

```bash
python -m unittest discover -s tests
```

### Code Quality Tools

Maintain code standards with automated tools:

```bash
# Format code with Black
black src/ tests/

# Lint with Ruff
ruff check src/ tests/

# Run all pre-commit hooks
pre-commit run --all-files
```

### Building for Distribution

Create distribution packages:

```bash
pip install build
python -m build
```

## Error Handling

MCP Mathematics provides clear, actionable error messages to help diagnose issues:

- **Syntax Errors**: Clear identification of malformed expressions
- **Division by Zero**: Graceful handling of mathematical impossibilities
- **Invalid Functions**: Helpful messages when unknown functions are called
- **Type Errors**: Detailed information about incompatible operations
- **Empty Expressions**: Informative feedback for missing input

## System Requirements

- Python 3.10 or higher
- MCP SDK 1.4.1 or later

## License

MCP Mathematics is released under the MIT License. Copyright © 2025 Md. Sazzad Hossain Sharkar

## Author

**Md. Sazzad Hossain Sharkar**
GitHub: [@SHSharkar](https://github.com/SHSharkar)
Email: md@szd.sh

## Contributing

We welcome contributions that maintain our high standards for code quality. When contributing:

- Write clean, comment-free production code
- Include comprehensive type annotations
- Add thorough test coverage for new features
- Maintain a clean, logical git history

## Acknowledgments

MCP Mathematics builds upon the Model Context Protocol (MCP) specification developed by Anthropic, extending it with production-ready mathematical capabilities designed for professional deployments.