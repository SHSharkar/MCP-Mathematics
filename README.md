# MCP Mathematics

A comprehensive Model Context Protocol (MCP) server that turns any AI assistant into a powerful mathematical computation engine. MCP Mathematics gives you professional-grade features including 52 advanced mathematical functions, 158 unit conversions across 15 categories, complete financial calculations, and secure AST-based evaluation—all in a production-ready, secure environment.

## What Is MCP Mathematics?

MCP Mathematics is the most complete mathematical computation server for AI assistants, built specifically for the Model Context Protocol. This production-ready solution turns any MCP-compatible AI into a powerful mathematical tool that handles everything from simple arithmetic to complex financial calculations, unit conversions across many different fields, and advanced scientific computations.

**Key Innovation**: Using Python's Abstract Syntax Tree (AST) evaluation, MCP Mathematics gives you exceptional mathematical capabilities while staying completely secure—stopping code injection vulnerabilities without losing any features.

## Why Choose MCP Mathematics?

### Uncompromising Security

- **AST-Based Evaluation**: Every calculation is checked and verified through Python's AST, which stops code injection attacks
- **Sandboxed Execution**: All calculations run in a secure, controlled environment that only allows safe operations
- **Zero External Dependencies**: Lower security risk since the core features don't need any external libraries

### Complete Mathematical Power

- **52 Built-In Functions**: From simple math to complex scientific calculations
- **158 Unit Conversions**: Wide-ranging unit conversion support covering 15 different categories
- **Financial Calculations**: Full set of financial tools including interest, loan, and tax calculations
- **Unicode Operator Support**: Easy mathematical symbols like ×, ÷, and ^ that feel natural to use
- **Full Math Library Coverage**: Complete access to all of Python's mathematical functions

### Production-Ready Architecture

- **Type-Safe Design**: Complete type checking throughout the code makes sure everything works reliably
- **Clean Production Code**: Professional code with no debugging leftovers or extra comments
- **Complete Testing**: 130 tests make sure all features work properly
- **Thread-Safe Operations**: 100% reliable concurrent execution with Timer-based timeout system
- **Advanced Memory Management**: Bounded LRU/TTL caches stop memory leaks in production environments
- **Enterprise Error Handling**: Proper exception chaining and graceful resource cleanup

## Getting Started

### Prerequisites

Before you install MCP Mathematics, make sure you have:

- Python 3.10 or later on your system
- An MCP-compatible AI assistant (Claude Desktop, VS Code with Continue, or similar)

### Installation Options

Choose the installation method that works best for you:

#### Option 1: Quick Install with uv (Recommended)

This is the fastest way to get started:

```bash
# Install the uv package manager if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install and run MCP Mathematics
uvx mcp-mathematics
```

#### Option 2: Traditional pip Installation

If you prefer using pip:

```bash
pip install mcp-mathematics
```

📦 **Package Information**: [mcp-mathematics on PyPI](https://pypi.org/project/mcp-mathematics)

#### Option 3: Development Installation

If you want to help out or need the latest development version:

```bash
git clone https://github.com/SHSharkar/MCP-Mathematics.git
cd MCP-Mathematics
pip install -e .
```

## Configuration Guide

### Configuring Claude Desktop

To use MCP Mathematics with Claude Desktop, you'll need to update your configuration file.

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

If you're using VS Code with the Continue extension:

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

### FastMCP Cloud Configuration

MCP Mathematics is available as a cloud-hosted service through FastMCP for instant access without local installation. Choose from multiple connection methods:

#### Connect to Claude Code

Access your tools from the command line with quick setup:

```bash
claude mcp add --scope local --transport http mathematics https://mathematics.fastmcp.app/mcp
```

#### Connect to Claude Desktop

Use your tools directly in Claude's desktop app with one-click installation:

**Download Link:** [https://mathematics.fastmcp.app/manifest.dxt?v=aa76634e-bffb-4be5-b1fd-c680cd7f7142](https://mathematics.fastmcp.app/manifest.dxt?v=aa76634e-bffb-4be5-b1fd-c680cd7f7142)

*Downloads .dxt file. Open the file to connect automatically.*

#### Connect to Codex CLI

Access your tools in a Codex CLI session:

```bash
codex mcp add -- mathematics npx -y mcp-remote@latest https://mathematics.fastmcp.app/mcp
```

#### Configure Codex

Durably store your MCP via Codex's configuration file by adding this to `.codex/config.toml`:

```toml
[mcp_servers.mathematics]
command = "npx"
args = ["-y", "mcp-remote@latest", "https://mathematics.fastmcp.app/mcp"]
```

#### Connect to Gemini CLI

Access your tools from the command line with quick setup:

```bash
gemini mcp add mathematics https://mathematics.fastmcp.app/mcp --transport http
```

#### Connect to Cursor

AI-powered code editor with built-in tool support. Click to connect instantly:

**Connection Link:** [cursor://anysphere.cursor-deeplink/mcp/install?name=mathematics&config=eyJ1cmwiOiJodHRwczovL21hdGhlbWF0aWNzLmZhc3RtY3AuYXBwL21jcCJ9](cursor://anysphere.cursor-deeplink/mcp/install?name=mathematics&config=eyJ1cmwiOiJodHRwczovL21hdGhlbWF0aWNzLmZhc3RtY3AuYXBwL21jcCJ9)

**FastMCP Cloud Benefits:**

- No local installation required
- Always up-to-date with latest features
- Enhanced performance with cloud infrastructure
- Instant access across multiple platforms
- Production-ready deployment

## Available MCP Tools

MCP Mathematics gives you access to all its mathematical features through 21 specialized tools with descriptive, mathematical domain names for maximum clarity and memorability. Each tool is designed for specific tasks and built for excellent performance:

### Core Calculation Tools

#### 1. `evaluate_mathematical_expression` - Single Expression Evaluation

The main tool for working with mathematical expressions. It supports all 52 built-in functions, unit conversions, and financial calculations. It handles everything from simple arithmetic to complex scientific computations.

**Use Cases:**

- Quick calculations: `"2 * pi * 10"` → `"62.83185307179586"`
- Scientific computing: `"sin(pi/2) + log10(1000)"` → `"4.0"`
- Financial analysis: `"compound_interest(5000, 6.5, 15)"` → Complete interest breakdown
- Unit conversions: `"convert_between_measurement_units(100, 'km', 'mi', 'length')"` → Automatic unit detection and conversion

#### 2. `evaluate_multiple_mathematical_expressions` - Parallel Processing Engine

Built to handle many expressions at the same time, giving you much better performance when doing lots of calculations or data analysis work.

**Use Cases:**

- Data processing: Process arrays of financial calculations
- Scientific analysis: Batch trigonometric computations
- Bulk conversions: Convert multiple values simultaneously

```
Input: ["sin(pi/2)", "cos(0)", "sqrt(16)", "factorial(5)"]
Output: ["1.0", "1.0", "4.0", "120"]
```

### Specialized Calculation Tools

#### 3. `convert_between_measurement_units` - Advanced Unit Conversion System

Smart unit conversion system that works with 158 units across 15 categories. It automatically figures out unit types, supports different spellings, and handles complex compound units.

**Advanced Features:**

- Smart detection: Automatically figures out unit categories
- Alias support: Accepts multiple spellings and abbreviations
- Compound units: Handles complex units like m/s², kg·m/s²
- History tracking: Keeps a conversion audit trail

```
Input: value=100, from_unit="meters", to_unit="feet"
Output: "328.084" (with automatic precision handling)
```

#### 4. `convert_units_from_natural_language` - Natural Language Unit Conversion

Converts units using natural language queries, making unit conversions more intuitive and accessible. This tool parses natural language requests and automatically determines the appropriate conversion.

**Supported Natural Language Patterns:**

- "convert 100 meters to feet"
- "what is 32 Celsius in Fahrenheit"
- "50 mph -> km/h"
- "5 kilograms equals how many pounds"
- "from 100 USD to EUR"

```
Input: "convert 100 kilometers to miles"
Output: {
  "success": true,
  "conversion": {
    "original_query": "convert 100 kilometers to miles",
    "input_value": 100,
    "input_unit": "kilometers",
    "output_value": 62.137119,
    "output_unit": "miles",
    "unit_type": "length"
  }
}
```

#### 5. `compute_statistical_operations` - Statistical Analysis Engine

Performs comprehensive statistical calculations on datasets, providing essential statistical measures for data analysis and scientific computing.

**Available Statistical Operations:**

- Descriptive statistics: mean, median, mode, range
- Variability measures: variance, standard deviation
- Distribution analysis: skewness, kurtosis
- Data quality: quartiles, percentiles

```
Input: data=[1, 2, 3, 4, 5], operation="mean"
Output: "Result: 3.0"
```

#### 6. `perform_matrix_mathematical_operations` - Matrix Mathematics Engine

Advanced matrix operations for linear algebra, engineering calculations, and scientific computing with support for multiple matrix operations.

**Supported Matrix Operations:**

- Basic operations: multiply, transpose
- Advanced operations: determinant, inverse
- Matrix analysis: rank, eigenvalues (where applicable)
- Error handling for invalid operations

```
Input: matrices=[[[1,2],[3,4]], [[5,6],[7,8]]], operation="multiply"
Output: Matrix multiplication result with proper formatting
```

#### 7. `perform_number_theory_analysis` - Number Theory Analysis

Advanced number theory operations for mathematical research, cryptography, and computational mathematics.

**Available Number Theory Operations:**

- Prime testing: Check if numbers are prime
- Prime factorization: Find all prime factors
- Divisor analysis: Calculate all divisors
- Euler's totient: Compute φ(n) function

```
Input: n=97, operation="is_prime"
Output: "Result: 97 is prime"
```

### Session Management Tools

#### 8. `create_mathematical_calculation_session` - Session Initialization

Creates a new calculation session with optional initial variables, enabling stateful mathematical computations across multiple operations.

**Session Features:**

- Variable storage: Save and reuse calculation results
- State persistence: Maintain context across operations
- Isolated environments: Multiple independent sessions
- Custom initialization: Set initial variables

```
Input: session_id="analysis_1", variables={"x": 10, "pi": 3.14159}
Output: "Session created: analysis_1"
```

#### 9. `evaluate_expression_in_session_context` - Stateful Calculations

Performs calculations within a specific session context, with access to stored variables and the ability to save results for later use.

```
Input: session_id="analysis_1", expression="x * 2 + pi", save_as="result"
Output: "Result: 23.14159" (and saves as 'result' variable)
```

#### 10. `list_mathematical_session_variables` - Variable Management

Lists all variables currently stored in a calculation session, showing their names and values for easy reference.

```
Input: session_id="analysis_1"
Output: {"x": 10, "pi": 3.14159, "result": 23.14159}
```

#### 11. `delete_mathematical_calculation_session` - Session Cleanup

Safely removes a calculation session and all associated variables, freeing up memory and ensuring clean state management.

### System Monitoring Tools

#### 12. `get_mathematical_computation_performance_metrics` - Performance Monitoring

Provides comprehensive system performance metrics including computation statistics, memory usage, and operational uptime for monitoring system health.

**Metrics Included:**

- Computation statistics: Total calculations performed
- Performance data: Average response times
- Memory usage: Current memory consumption
- System uptime: Server operational time

#### 13. `get_mathematical_security_audit_report` - Security Information

Returns current security status including rate limiting information and session data for security monitoring and compliance.

#### 14. `get_mathematical_memory_usage_statistics` - Memory Analytics

Detailed memory usage statistics for cache and session management, helping with performance optimization and resource planning.

### Management and Discovery Tools

#### 15. `get_mathematical_computation_history` - Calculation Audit Trail

Keeps a complete record of all calculations with timestamps, so you can track, check, and repeat any mathematical work.

**Features:**

- Timestamped records: Every calculation includes when it was run
- Configurable limits: Get 1-100 recent calculations
- Expression tracking: Full input and output logging
- Error logging: Failed calculations with error details

#### 16. `clear_mathematical_computation_history` - History Management

Lets you safely clear your calculation history when you need to for privacy, performance, or storage reasons.

#### 17. `optimize_mathematical_computation_memory` - Memory Optimization

Cleans up expired cache entries and optimizes memory usage, helping maintain optimal performance in long-running sessions.

**Optimization Features:**

- Cache cleanup: Removes expired cache entries
- Memory defragmentation: Optimizes memory allocation
- Resource reclamation: Frees unused resources
- Performance improvement: Maintains system responsiveness

#### 18. `list_all_available_mathematical_functions_and_constants` - Complete Capability Discovery

Complete reference tool that gives you instant access to all available mathematical functions, constants, unit conversions, and their settings.

**Discovery Categories:**

- Mathematical functions: All 52 available functions with signatures
- Constants: Mathematical and physical constants with values
- Unit conversions: All 158 units organized by category
- System capabilities: Available operations and limits

**Note**: This tool consolidates the functionality of listing functions, constants, and recent history access in a single comprehensive interface.

## MCP Resources

Access these resources directly through the MCP protocol with their corresponding implementation functions:

- **`history://recent`** - View recent calculation history (implemented by `recent_calculation_history`)
- **`functions://available`** - Browse available mathematical functions (implemented by `mathematical_functions_catalog`)
- **`constants://math`** - Access mathematical constants with their values (implemented by `mathematical_constants_catalog`)

## MCP Prompts

Pre-configured prompts for common calculation patterns:

- **`scientific_calculation`** - Structured template for scientific computations
- **`batch_calculation`** - Optimized template for batch processing

## Mathematical Capabilities

MCP Mathematics gives you a complete mathematical computation environment with support for over 52 functions spanning basic arithmetic, advanced scientific computing, and specialized mathematical operations. The system handles everything from simple calculations to complex scientific and financial computations with precision and reliability.

### Basic Operations

Beyond standard arithmetic, MCP Mathematics supports easy-to-use mathematical operators including Unicode symbols for natural mathematical expression:

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
evaluate_mathematical_expression("2 + 3 * 4")  # Result: 14
evaluate_mathematical_expression("10 / 3")  # Result: 3.3333333333333335
evaluate_mathematical_expression("2 ** 8")  # Result: 256
```

### Scientific Computing

```python
evaluate_mathematical_expression("sin(pi/2)")  # Result: 1.0
evaluate_mathematical_expression("log10(1000)")  # Result: 3.0
evaluate_mathematical_expression("sqrt(16) + cos(0)")  # Result: 5.0
```

### Complex Mathematical Expressions

```python
evaluate_mathematical_expression("(2 + 3) * sqrt(16) / sin(pi/2)")  # Result: 20.0
evaluate_mathematical_expression("factorial(5) + gcd(12, 8)")  # Result: 124
```

### Natural Mathematical Notation

```python
evaluate_mathematical_expression("5 × 3")  # Result: 15
evaluate_mathematical_expression("20 ÷ 4")  # Result: 5.0
evaluate_mathematical_expression("2 ^ 10")  # Result: 1024
```

## Complete Unit Conversion System

MCP Mathematics includes a smart unit conversion system that works with 158 carefully calibrated units across 15 essential categories. This system does more than simple conversions—it provides smart unit detection, supports different spellings, handles complex compound units, and tracks your conversion history. This makes it perfect for scientific work, engineering calculations, and everyday conversions.

The conversion system automatically manages precision, accepts many different input formats, and works seamlessly with the mathematical expression engine for smooth integration in complex calculations.

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
convert_between_measurement_units(
    100, "kilometers", "miles", "length"
)  # Works with full names
convert_between_measurement_units(100, "km", "mi", "length")  # Works with abbreviations
convert_between_measurement_units(
    100, "metre", "yard", "length"
)  # Supports alternate spellings
```

#### Auto-Detection

The system automatically figures out unit types from context:

```python
convert_between_measurement_units(
    100, "kg", "lb", "mass"
)  # Automatically detects mass conversion
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
convert_between_measurement_units(100, "meters", "feet", "length")  # 328.084
convert_between_measurement_units(1, "mile", "kilometers", "length")  # 1.60934

# Mass conversions
convert_between_measurement_units(1, "kg", "pounds", "mass")  # 2.20462
convert_between_measurement_units(100, "grams", "ounces", "mass")  # 3.52740

# Temperature conversions
convert_between_measurement_units(0, "C", "F", "temperature")  # 32
convert_between_measurement_units(100, "F", "C", "temperature")  # 37.7778

# Data storage conversions
convert_between_measurement_units(1024, "MB", "GB", "data")  # 1.024
convert_between_measurement_units(1, "TB", "bytes", "data")  # 1099511627776
```

## Professional Financial Calculation Suite

MCP Mathematics includes a complete set of financial tools designed for professional use, education, and personal money management. The financial system supports advanced calculations including compound interest modeling, loan analysis, tax calculations, and business financial work.

All financial functions use high precision to make sure you get accurate money calculations and support different compounding frequencies, payment schedules, and tax situations you'll find in real-world financial work.

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

MCP Mathematics is built as an enterprise-grade mathematical computation platform that combines strong security measures with production-ready architecture. The system is designed to handle mission-critical calculations while maintaining the highest standards of code quality and security.

### Multi-Layered Security Framework

#### Core Security Principles

- **Zero-Trust Architecture**: Every input is checked and every operation is verified
- **Defense in Depth**: Multiple security layers give you complete protection
- **Principle of Least Privilege**: Only essential operations are allowed
- **Fail-Safe Defaults**: Safe defaults stop accidental security issues

#### Security Implementation

- **AST Evaluation Engine**: Every mathematical expression is processed through an Abstract Syntax Tree before evaluation, which stops code injection attacks while keeping full mathematical capability
- **Operation Whitelisting**: Only specifically approved mathematical operations and functions can run, which stops unauthorized code execution
- **Input Sanitization**: Thorough checking of all expressions and parameters before processing
- **Error Containment**: Complete error handling makes sure calculation failures don't affect system security
- **Dependency Minimization**: Core features need no external libraries, which greatly reduces security risks

### Production-Grade Architecture

#### Code Quality Standards

- **Type Safety**: Complete type annotations using Python 3.10+ features make sure you catch errors at compile-time
- **Clean Architecture**: Modular design with clear separation of concerns makes maintenance and scaling easier
- **Professional Codebase**: Production-ready code with no debug statements, console logs, or unnecessary comments
- **Complete Testing**: 130 unit tests give you thorough coverage across all mathematical functions and edge cases
- **Automated Quality**: Code standards enforced through Black formatting and Ruff linting

#### Performance & Reliability

- **Optimized Computation**: Efficient algorithms and data structures for high-performance calculations
- **Advanced Memory Management**: Bounded LRU and TTL cache systems with automatic cleanup stop memory leaks in long-running processes
- **Thread-Safe Concurrency**: 100% reliable concurrent execution using Timer-based timeouts instead of signal-based approaches
- **Session Management**: Graceful resource cleanup and session handling for enterprise environments
- **Error Recovery**: Proper exception chaining with better traceability for debugging and monitoring
- **Scalability**: Architecture designed to handle high-volume calculation workloads with concurrent processing

## Development Guide

This complete guide gives you everything you need to contribute to MCP Mathematics, from setting up your development environment to building production-ready distributions. The project follows strict quality standards and automated workflows to make sure everything works reliably and stays maintainable.

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

Run the comprehensive test suite covering all 130 test cases:

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

Keep professional code standards with automated quality tools:

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

MCP Mathematics gives you clear, helpful error messages to help you figure out what went wrong:

- **Syntax Errors**: Clear identification of malformed expressions
- **Division by Zero**: Smooth handling of mathematical impossibilities
- **Invalid Functions**: Helpful messages when unknown functions are called
- **Type Errors**: Detailed information about incompatible operations
- **Empty Expressions**: Helpful feedback when input is missing

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

We welcome contributions that maintain our high standards for code quality. When you contribute:

- Write clean, comment-free production code
- Include complete type annotations
- Add complete test coverage for new features
- Keep a clean, logical git history

## Acknowledgments

MCP Mathematics is built on the Model Context Protocol (MCP) specification developed by Anthropic, extending it with production-ready mathematical capabilities designed for professional use.
