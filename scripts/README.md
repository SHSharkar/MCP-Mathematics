# Semver Publishing Script

Automated semantic versioning and PyPI publishing script for MCP Mathematics.

## Features

- ✅ **Semantic Versioning**: Automatically increment major, minor, or patch versions
- ✅ **PyPI Publishing**: Automated package building and publishing
- ✅ **Git Integration**: Automatic commits and tagging
- ✅ **Environment Integration**: Uses `.env` file for PyPI credentials
- ✅ **Comprehensive Testing**: Runs test suite before publishing
- ✅ **Error Handling**: Robust error handling and rollback guidance
- ✅ **Dry Run Mode**: Preview changes without making them

## Prerequisites

Required tools must be installed:
```bash
pip install build twine
```

PyPI credentials should be configured in `.env` file:
```bash
TWINE_USERNAME=__token__
TWINE_PASSWORD=pypi-your-token-here
```

## Usage

### Basic Usage

```bash
# Patch release (1.0.0 → 1.0.1)
python scripts/publish.py patch

# Minor release (1.0.1 → 1.1.0)
python scripts/publish.py minor

# Major release (1.1.0 → 2.0.0)
python scripts/publish.py major
```

### Advanced Options

```bash
# Dry run to preview changes
python scripts/publish.py patch --dry-run

# Skip tests (not recommended)
python scripts/publish.py patch --skip-tests

# Custom commit message
python scripts/publish.py minor --message "Add new mathematical functions"

# Publish to test PyPI
python scripts/publish.py patch --repository testpypi
```

## Workflow Steps

The script performs these steps in order:

1. **Git Status Check**: Ensures working directory is clean
2. **Version Detection**: Reads current version from `pyproject.toml`
3. **Version Increment**: Calculates new version based on semver rules
4. **Test Execution**: Runs full test suite (unless skipped)
5. **Version Update**: Updates `pyproject.toml` with new version
6. **Clean Build**: Removes old build artifacts
7. **Package Build**: Creates wheel and source distribution
8. **Package Validation**: Validates package with twine
9. **PyPI Publishing**: Uploads package to PyPI
10. **Git Operations**: Commits changes and creates version tag

## Semantic Versioning Rules

- **PATCH** (`x.y.Z`): Bug fixes, backward compatible
- **MINOR** (`x.Y.0`): New features, backward compatible
- **MAJOR** (`X.0.0`): Breaking changes, not backward compatible

## Error Handling

If publishing fails:
1. Check the error message for specific issues
2. Manually revert version changes if needed:
   ```bash
   git checkout pyproject.toml
   ```
3. Fix the underlying issue
4. Re-run the script

## Examples

### Publishing a Bug Fix
```bash
# Current: 1.0.0 → New: 1.0.1
python scripts/publish.py patch
```

### Adding New Features
```bash
# Current: 1.0.1 → New: 1.1.0
python scripts/publish.py minor
```

### Breaking Changes
```bash
# Current: 1.1.0 → New: 2.0.0
python scripts/publish.py major
```

### Testing Before Release
```bash
# Preview changes
python scripts/publish.py minor --dry-run

# Test on TestPyPI first
python scripts/publish.py minor --repository testpypi
```

## Post-Publishing

After successful publishing, push to Git:
```bash
git push origin main
git push origin v1.0.1  # Replace with actual version
```

## Troubleshooting

### Common Issues

**"Git working directory is not clean"**
- Commit or stash your changes before publishing
- Or use `--dry-run` to test without committing

**"Tests failed"**
- Fix failing tests before publishing
- Or use `--skip-tests` (not recommended)

**"Package validation failed"**
- Check package structure and metadata
- Ensure all required files are included

**"PyPI upload failed"**
- Verify credentials in `.env` file
- Check if version already exists on PyPI
- Ensure package name is available

### Manual Recovery

If the script fails mid-process:
```bash
# Revert version changes
git checkout pyproject.toml

# Clean build artifacts
rm -rf build/ dist/

# Check git status
git status
```

## Development Notes

The script automatically:
- Updates version in `pyproject.toml`
- Creates git commit with standardized message
- Tags the commit with version (e.g., `v1.0.1`)
- Publishes to PyPI using credentials from `.env`

For custom workflows, modify the `SemverPublisher` class methods as needed.