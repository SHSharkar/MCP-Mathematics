# Changelog

All notable changes to mcp-mathematics will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.3.0] - 2025-10-18

### Changed
- **Internal refactoring**: Renamed 6 Python function names for improved conciseness and token efficiency
  - Tools: `get_performance_metrics` → `performance_metrics`, `get_security_status` → `security_status`, `get_memory_statistics` → `memory_statistics`
  - Resources: `get_recent_mathematical_computation_history` → `recent_calculation_history`, `get_available_mathematical_functions_catalog` → `mathematical_functions_catalog`, `get_comprehensive_mathematical_constants_catalog` → `mathematical_constants_catalog`
  - **Note**: Zero breaking changes - MCP clients use decorator `title` parameter, not Python function names
  - Completed deferred Task 6 from FastMCP v2.0+ compliance implementation
  - Total token savings: ~65 characters across renamed functions

## [2.2.1] - 2025-09-26

### Added
- GitHub Actions workflow for automated PyPI publishing with Trusted Publisher support
- Comprehensive project URLs in pyproject.toml for PyPI verification (Homepage, Source, Repository, Issues, Documentation)

### Fixed
- Version alignment between pyproject.toml and uv.lock
- Documentation corrections and updates

### Changed
- Updated Python version to 3.13 in GitHub Actions workflow

## [2.2.0] - 2025-09-26

### Added
- **FastMCP configuration file** (`fastmcp.json`) for improved tool discovery and integration
- **Operation selection via elicitation** - Interactive prompts for better UX when multiple operations match
- **Natural language unit conversion** - Support for conversational unit conversion requests
- **Comprehensive docstrings** for all conversion functions improving API documentation
- **Cloud configuration documentation** in README for deployment instructions

### Changed
- **BREAKING**: Renamed mathematical tools for improved clarity and consistency with MCP standards
  - Tools now follow clearer naming conventions for better discoverability
- **Refactored calculation infrastructure** - Improved internal architecture for better performance and maintainability
- **Updated error messages** - More descriptive and helpful error messages throughout the system
- **Enhanced README documentation** with:
  - Cloud deployment instructions
  - Better formatting and readability
  - Clearer installation steps
  - Updated tool naming examples

### Improved
- **Expanded MCP Mathematics tool suite** with better categorization
- **Unit conversion accuracy** - Fixed precision issues in various conversions
- **Error handling** - More robust error handling with clearer user feedback
- **Documentation quality** - Better inline documentation and usage examples

### Technical
- Updated `uv.lock` dependency file
- Refactored `calculator.py` module for better code organization
- Improved tool naming conventions following MCP best practices

## [2.0.8] - 2025-09-26

### Added
- Enhanced prompts following MCP standards
- Comprehensive docstrings for all mathematical functions

### Fixed
- GitHub CI by adding fastmcp to dependencies

### Changed
- Tool renaming for better clarity

## [2.0.7] - 2025-09-26

### Fixed
- Memory management refactoring for better performance

## [2.0.6] - 2025-09-26

### Fixed
- Memory management improvements

## [2.0.5] - 2025-09-26

### Fixed
- FastMCP v2 compatibility - Removed asyncio conflicts and simplified entry points
- FastMCP Cloud compatibility - Better handling of existing event loops

## [2.0.4] - 2025-09-26

### Changed
- Updated pyproject.toml with FastMCP v2 integration
- Optimized PyPI keywords for better discoverability
- Enhanced README documentation for improved user experience
- Refined documentation for clarity and accuracy

### Fixed
- Publishing script validation for configuration integrity
- Ruff target-version configuration (changed from package version to Python version)