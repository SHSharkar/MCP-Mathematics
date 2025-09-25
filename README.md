# MCP Mathematics

A comprehensive Model Context Protocol (MCP) server that transforms AI assistants into powerful mathematical computation engines. MCP Mathematics delivers enterprise-grade capabilities including 52 advanced mathematical functions, 158 unit conversions across 15 categories, complete financial calculations, and secure AST-based evaluation—all through a production-ready, sandboxed environment.

## What Is MCP Mathematics?

MCP Mathematics is the most comprehensive mathematical computation server for AI assistants, purpose-built for the Model Context Protocol. This production-ready solution transforms any MCP-compatible AI into a sophisticated mathematical powerhouse, capable of handling everything from basic arithmetic to complex financial calculations, unit conversions across multiple domains, and advanced scientific computations.

**Key Innovation**: Through Python's Abstract Syntax Tree (AST) evaluation, MCP Mathematics provides unprecedented mathematical capabilities while maintaining enterprise-level security—eliminating code injection vulnerabilities without compromising functionality.

## Why Choose MCP Mathematics?

### Uncompromising Security

- **AST-Based Evaluation**: Every expression is parsed and validated through Python's AST, eliminating code injection vulnerabilities
- **Sandboxed Execution**: Calculations run in a controlled environment with strict operation whitelisting
- **Zero External Dependencies**: Minimal attack surface with no third-party libraries required for core functionality

### Comprehensive Mathematical Power

- **52 Built-In Functions**: From basic arithmetic to advanced scientific computations
- **158 Unit Conversions**: Extensive unit conversion support across 15 categories
- **Financial Calculations**: Complete suite of financial functions including interest, loans, and tax calculations
- **Unicode Operator Support**: Natural mathematical notation using symbols like ×, ÷, and ^
- **Full Math Library Coverage**: Complete access to Python's mathematical functions

### Production-Ready Architecture

- **Type-Safe Design**: Full type annotations throughout the codebase ensure reliability
- **Clean Production Code**: No debug statements, console logs, or unnecessary comments
- **Comprehensive Testing**: 130 unit tests provide thorough coverage of all functionality

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

📦 **Package Information**: [mcp-mathematics on PyPI](https://pypi.org/project/mcp-mathematics)

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
      "args": [
        "mcp-mathematics"
      ]
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
          "args": [
            "mcp-mathematics"
          ]
        }
      }
    }
  ]
}
```

## Available MCP Tools

MCP Mathematics exposes its comprehensive mathematical capabilities through seven specialized MCP tools, each designed for specific use cases and optimized for performance:

### Core Calculation Tools

#### 1. `calculate` - Single Expression Evaluation

The primary tool for evaluating mathematical expressions with support for all 52 built-in functions, unit conversions, and financial calculations. Handles everything from basic arithmetic to complex scientific computations.

**Use Cases:**

- Quick calculations: `"2 * pi * 10"` → `"62.83185307179586"`
- Scientific computing: `"sin(pi/2) + log10(1000)"` → `"4.0"`
- Financial analysis: `"compound_interest(5000, 6.5, 15)"` → Complete interest breakdown
- Unit conversions: `"convert_unit(100, 'km', 'mi')"` → Automatic unit detection and conversion

#### 2. `batch_calculate` - Parallel Processing Engine

Optimized for processing multiple expressions simultaneously, providing significant performance benefits for bulk calculations and data analysis workflows.

**Use Cases:**

- Data processing: Process arrays of financial calculations
- Scientific analysis: Batch trigonometric computations
- Bulk conversions: Convert multiple values simultaneously

```
Input: ["sin(pi/2)", "cos(0)", "sqrt(16)", "factorial(5)"]
Output: ["1.0", "1.0", "4.0", "120"]
```

### Specialized Calculation Tools

#### 3. `convert_unit` - Advanced Unit Conversion System

Intelligent unit conversion engine supporting 158 units across 15 categories with automatic type detection, alias support, and compound unit parsing.

**Advanced Features:**

- Smart detection: Automatically identifies unit categories
- Alias support: Accepts multiple spellings and abbreviations
- Compound units: Handles complex units like m/s², kg·m/s²
- History tracking: Maintains conversion audit trail

```
Input: value=100, from_unit="meters", to_unit="feet"
Output: "328.084" (with automatic precision handling)
```

#### 4. `financial_calculate` - Comprehensive Financial Engine

Complete financial calculation suite for professional applications, supporting interest calculations, loan analysis, tax computations, and business calculations.

**Financial Functions Available:**

- Interest: Simple, compound, continuous compounding
- Loans: Payment calculations, amortization schedules
- Business: Markup, discount, profit margin analysis
- Personal: Bill splitting, tip calculation, tax computation

```
Input: function="compound_interest", principal=1000, rate=5, time=10, frequency=12
Output: {"amount": 1647.01, "interest": 647.01, "effective_rate": 5.12}
```

### Management and Discovery Tools

#### 5. `get_calculation_history` - Calculation Audit Trail

Maintains a complete audit trail of all calculations with timestamps, enabling tracking, verification, and reproducibility of mathematical operations.

**Features:**

- Timestamped records: Every calculation includes execution time
- Configurable limits: Retrieve 1-100 recent calculations
- Expression tracking: Full input and output logging
- Error logging: Failed calculations with error details

#### 6. `clear_history` - History Management

Provides controlled cleanup of calculation history for privacy, performance, or storage management requirements.

#### 7. `list_functions` - Function and Capability Discovery

Comprehensive reference tool providing real-time access to all available mathematical functions, constants, unit conversions, and their parameters.

**Discovery Categories:**

- Mathematical functions: All 52 available functions with signatures
- Constants: Mathematical and physical constants with values
- Unit conversions: All 158 units organized by category
- Financial functions: Complete financial calculation catalog

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

MCP Mathematics provides a comprehensive mathematical computation environment with support for over 52 functions spanning basic arithmetic, advanced scientific computing, and specialized mathematical operations. The system is designed to handle everything from simple calculations to complex scientific and financial computations with precision and reliability.

### Basic Operations

Beyond standard arithmetic, MCP Mathematics supports intuitive mathematical operators including Unicode symbols for natural mathematical expression:

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
calculate("10 / 3")  # Result: 3.3333333333333335
calculate("2 ** 8")  # Result: 256
```

### Scientific Computing

```python
calculate("sin(pi/2)")  # Result: 1.0
calculate("log10(1000)")  # Result: 3.0
calculate("sqrt(16) + cos(0)")  # Result: 5.0
```

### Complex Mathematical Expressions

```python
calculate("(2 + 3) * sqrt(16) / sin(pi/2)")  # Result: 20.0
calculate("factorial(5) + gcd(12, 8)")  # Result: 124
```

### Natural Mathematical Notation

```python
calculate("5 × 3")  # Result: 15
calculate("20 ÷ 4")  # Result: 5.0
calculate("2 ^ 10")  # Result: 1024
```

## Comprehensive Unit Conversion System

MCP Mathematics features an advanced unit conversion engine supporting 158 precisely calibrated units across 15 essential categories. This system goes beyond simple conversions to provide intelligent unit detection, alias support, compound unit parsing, and comprehensive history tracking—making it ideal for scientific applications, engineering calculations, and everyday conversions.

The conversion system automatically handles precision management, supports multiple input formats, and maintains full compatibility with the mathematical expression engine for seamless integration in complex calculations.

### Supported Unit Categories

#### Length (15 units)

- Metric: `m`, `km`, `cm`, `mm`, `nm`, `micron`, `angstrom`
- Imperial: `mi`, `yd`, `ft`, `in`
- Astronomical: `ly` (light-years), `AU` (astronomical units), `pc` (parsecs)
- Nautical: `nmi` (nautical miles)

#### Mass (13 units)

- Metric: `kg`, `g`, `mg`, `ton` (metric), `t`
- Imperial: `lb`, `oz`, `ton_us` (short ton), `ton_uk` (long ton), `st` (stone)
- Special: `ct` (carats), `gr` (grains), `amu` (atomic mass units)

#### Time (15 units)

- Standard: `s`, `min`, `h`, `d`, `wk`, `mo`, `yr`
- Sub-second: `ms`, `us`, `ns`, `ps`
- Extended: `decade`, `century`, `millennium`, `fortnight`

#### Temperature (3 units)

- `K` (Kelvin), `C` (Celsius), `F` (Fahrenheit)

#### Area (12 units)

- Metric: `m2`, `km2`, `cm2`, `mm2`, `hectare`, `are`
- Imperial: `ft2`, `yd2`, `in2`, `mi2`, `acre`, `sqch` (square chains)

#### Volume (16 units)

- Metric: `L`, `mL`, `m3`, `cm3`
- US: `gal`, `qt`, `pt`, `fl_oz`, `cup`, `tbsp`, `tsp`
- UK: `gal_uk`, `qt_uk`, `pt_uk`
- Cubic: `ft3`, `in3`

#### Speed/Velocity (10 units)

- `m/s`, `km/h`, `mph`, `ft/s`, `knot`, `mach`, `cm/s`, `mi/min`, `in/s`, `c` (speed of light percentage)

#### Data/Digital Storage (16 units)

- Binary: `B`, `KB`, `MB`, `GB`, `TB`, `PB`, `EB`, `ZB`
- Bits: `bit`, `Kbit`, `Mbit`, `Gbit`, `Tbit`
- IEC: `KiB`, `MiB`, `GiB`

#### Pressure (10 units)

- `Pa`, `kPa`, `MPa`, `atm`, `bar`, `mbar`, `psi`, `torr`, `mmHg`, `inHg`

#### Energy (12 units)

- `J`, `kJ`, `MJ`, `cal`, `kcal`, `Wh`, `kWh`, `BTU`, `eV`, `ft_lb`, `erg`, `therm`

#### Power (10 units)

- `W`, `kW`, `MW`, `hp`, `PS`, `BTU/h`, `ft_lb/s`, `cal/s`, `erg/s`, `ton_refrigeration`

#### Force (8 units)

- `N`, `kN`, `lbf`, `kgf`, `dyne`, `pdl`, `ozf`, `tonf`

#### Angle (6 units)

- `deg`, `rad`, `grad`, `arcmin`, `arcsec`, `turn`

#### Frequency (6 units)

- `Hz`, `kHz`, `MHz`, `GHz`, `rpm`, `rad/s`

#### Fuel Economy (6 units)

- `mpg`, `mpg_uk`, `L/100km`, `km/L`, `mi/L`, `gal/100mi`

### Smart Features

#### Unit Aliases

MCP Mathematics supports common unit aliases for convenience:

```python
convert_unit(100, "kilometers", "miles")  # Works with full names
convert_unit(100, "km", "mi")  # Works with abbreviations
convert_unit(100, "metre", "yard")  # Supports alternate spellings
```

#### Auto-Detection

The system automatically detects unit types from context:

```python
convert_unit(100, "kg", "lb")  # Automatically knows it's mass conversion
```

#### Compound Units

Parse and handle complex compound units:

```python
parse_compound_unit("m/s²")  # Acceleration units
parse_compound_unit("kg·m/s²")  # Force units
```

#### Scientific Notation

Automatic formatting for very large or small values:

```python
format_scientific_notation(0.000001, precision=2)  # 1.00e-6
format_scientific_notation(1000000, precision=2)  # 1.00e+6
```

#### Conversion History

Track all conversions with timestamps:

```python
convert_with_history(100, "m", "ft", precision=2)  # Stores in history
conversion_history.get_recent(10)  # Retrieve last 10
```

### Unit Conversion Examples

```python
# Length conversions
convert_unit(100, "meters", "feet")  # 328.084
convert_unit(1, "mile", "kilometers")  # 1.60934

# Mass conversions
convert_unit(1, "kg", "pounds")  # 2.20462
convert_unit(100, "grams", "ounces")  # 3.52740

# Temperature conversions
convert_unit(0, "C", "F")  # 32
convert_unit(100, "F", "C")  # 37.7778

# Data storage conversions
convert_unit(1024, "MB", "GB")  # 1.024
convert_unit(1, "TB", "bytes")  # 1099511627776
```

## Professional Financial Calculation Suite

MCP Mathematics provides a complete financial analysis toolkit designed for professional applications, educational purposes, and personal finance management. The financial engine supports advanced calculations including compound interest modeling, loan analysis, tax computations, and business financial operations.

All financial functions maintain high precision for accurate monetary calculations and support various compounding frequencies, payment schedules, and tax scenarios commonly encountered in real-world financial applications.

### Core Financial Functions

#### Percentage Operations

```python
calculate_percentage(1000, 15)  # 150 (15% of 1000)
calculate_percentage_of(50, 200)  # 25 (50 is 25% of 200)
calculate_percentage_change(100, 150)  # 50 (50% increase)
```

#### Interest Calculations

```python
# Simple Interest
calculate_simple_interest(1000, 5, 10)
# Returns: {"interest": 500, "amount": 1500}

# Compound Interest
calculate_compound_interest(1000, 5, 10, 12)  # Monthly compounding
# Returns: {"amount": 1647.01, "interest": 647.01}
```

#### Loan Calculations

```python
# Calculate monthly payment
calculate_loan_payment(100000, 5, 30, 12)  # $100k, 5%, 30 years, monthly
# Returns: {"payment": 536.82, "total_paid": 193255.78, "interest_paid": 93255.78}
```

#### Tax Calculations

```python
# Calculate tax (inclusive or exclusive)
calculate_tax(100, 10, is_inclusive=False)  # 10% tax on $100
# Returns: {"amount": 100, "tax": 10, "total": 110}

calculate_tax(110, 10, is_inclusive=True)  # Price includes 10% tax
# Returns: {"amount": 100, "tax": 10, "total": 110}
```

#### Bill Operations

```python
# Split bill with tip
split_bill(100, 4, tip_percent=20)
# Returns: {"total": 120, "per_person": 30, "tip": 20}

# Calculate tip
calculate_tip(100, 18)  # 18% tip on $100
# Returns: 18
```

#### Discount and Markup

```python
# Calculate discount
calculate_discount(100, 20)  # 20% off $100
# Returns: {"original": 100, "discount": 20, "final": 80}

# Calculate markup
calculate_markup(100, 25)  # 25% markup on $100 cost
# Returns: {"cost": 100, "markup": 25, "price": 125}
```

## Enterprise Architecture & Security

MCP Mathematics is engineered as an enterprise-grade mathematical computation platform, combining robust security measures with production-ready architecture. The system is designed to handle mission-critical calculations while maintaining the highest standards of code quality and security.

### Multi-Layered Security Framework

#### Core Security Principles

- **Zero-Trust Architecture**: Every input is validated and every operation is verified
- **Defense in Depth**: Multiple security layers ensure comprehensive protection
- **Principle of Least Privilege**: Only essential operations are permitted
- **Fail-Safe Defaults**: Secure defaults prevent accidental vulnerabilities

#### Security Implementation

- **AST Evaluation Engine**: Every mathematical expression is parsed into an Abstract Syntax Tree before evaluation, eliminating code injection vulnerabilities while preserving full mathematical capability
- **Operation Whitelisting**: Only explicitly approved mathematical operations and functions can be executed, preventing unauthorized code execution
- **Input Sanitization**: Rigorous validation of all expressions and parameters before processing
- **Error Containment**: Comprehensive error handling ensures calculation failures don't compromise system security
- **Dependency Minimization**: Core functionality requires no external libraries, dramatically reducing attack surface

### Production-Grade Architecture

#### Code Quality Standards

- **Type Safety**: Complete type annotations using Python 3.10+ features ensure compile-time error detection
- **Clean Architecture**: Modular design with clear separation of concerns enables maintainability and scalability
- **Professional Codebase**: Production-ready code with no debug statements, console logs, or unnecessary comments
- **Comprehensive Testing**: 130 unit tests provide thorough coverage across all mathematical functions and edge cases
- **Automated Quality**: Code standards enforced through Black formatting and Ruff linting

#### Performance & Reliability

- **Optimized Computation**: Efficient algorithms and data structures for high-performance calculations
- **Memory Management**: Careful resource allocation prevents memory leaks in long-running processes
- **Error Recovery**: Graceful handling of mathematical edge cases and invalid inputs
- **Scalability**: Architecture designed to handle high-volume calculation workloads

## Development Guide

This comprehensive guide provides everything needed to contribute to MCP Mathematics, from setting up the development environment to building production-ready distributions. The project follows strict quality standards and automated workflows to ensure reliability and maintainability.

### Development Environment Setup

#### Prerequisites

```bash
# Ensure Python 3.10+ is installed
python --version # Should be 3.10 or higher

# Clone the repository
git clone https://github.com/SHSharkar/MCP-Mathematics.git
cd MCP-Mathematics

# Create virtual environment
python -m venv .venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"
```

### Quality Assurance Workflow

#### Running the Complete Test Suite

Execute the comprehensive test suite covering all 130 test cases:

```bash
# Run all tests with detailed output
python -m pytest tests/ -v

# Run tests with coverage reporting
python -m pytest tests/ --cov=src --cov-report=html

# Run specific test categories
python -m pytest tests/test_calculator.py -v      # Core functionality
python -m pytest tests/test_unit_conversion.py -v # Unit conversions
python -m pytest tests/test_financial.py -v       # Financial calculations
```

#### Code Quality and Standards

Maintain professional code standards with automated quality tools:

```bash
# Auto-format code with Black (100-character line limit)
black src/ tests/ --line-length 100

# Comprehensive linting with Ruff
ruff check src/ tests/ --fix

# Type checking with mypy
mypy src/

# Run complete pre-commit validation
pre-commit run --all-files
```

#### Performance and Security Validation

```bash
# Security analysis
bandit -r src/

# Performance profiling for mathematical operations
python -m cProfile -s cumtime scripts/benchmark.py

# Memory usage analysis
python -m memory_profiler scripts/memory_test.py
```

### Distribution and Deployment

#### Building Production Packages

Create optimized distribution packages for PyPI:

```bash
# Install build tools
pip install build twine

# Clean previous builds
rm -rf dist/ build/

# Build source and wheel distributions
python -m build

# Verify package integrity
twine check dist/*

# Test installation in clean environment
pip install dist/*.whl
```

#### Release Management

```bash
# Tag release version
git tag -a v1.0.0 -m "Release version 1.0.0"

# Push tags to trigger CI/CD
git push origin --tags

# Upload to PyPI (maintainers only)
twine upload dist/*
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
