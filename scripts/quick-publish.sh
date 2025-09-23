#!/bin/bash

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

case "$1" in
    "patch"|"minor"|"major")
        echo "🚀 Publishing $1 release..."
        python "$SCRIPT_DIR/publish.py" "$1" "${@:2}"
        ;;
    "dry")
        echo "🔍 Dry run for patch release..."
        python "$SCRIPT_DIR/publish.py" patch --dry-run "${@:2}"
        ;;
    "test")
        echo "🧪 Publishing to TestPyPI..."
        python "$SCRIPT_DIR/publish.py" patch --repository testpypi "${@:2}"
        ;;
    *)
        echo "Usage: $0 {patch|minor|major|dry|test} [options]"
        echo ""
        echo "Quick publishing commands:"
        echo "  patch   - Publish patch release (1.0.0 → 1.0.1)"
        echo "  minor   - Publish minor release (1.0.0 → 1.1.0)"
        echo "  major   - Publish major release (1.0.0 → 2.0.0)"
        echo "  dry     - Dry run for patch release"
        echo "  test    - Publish to TestPyPI"
        echo ""
        echo "Examples:"
        echo "  $0 patch"
        echo "  $0 minor --message 'Add new features'"
        echo "  $0 dry"
        echo "  $0 test"
        exit 1
        ;;
esac