#!/usr/bin/env bash
# gate-runner.sh
# Orchestrates mechanical validation (linters, typecheckers, syntax) and behavioral tests.
# Returns 0 only if all gates pass. Automatically pipes failures to telemetry-collector.sh if present.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TELEMETRY_SCRIPT="$SCRIPT_DIR/telemetry-collector.sh"

run_gate() {
    local cmd="$1"
    echo "=> Running: $cmd"
    
    # Run the command, capture stdout/stderr, and exit if it fails
    if ! OUTPUT=$(eval "$cmd" 2>&1); then
        echo "$OUTPUT"
        echo "=> Gate failed: $cmd"
        if [ -x "$TELEMETRY_SCRIPT" ]; then
            echo "$OUTPUT" | "$TELEMETRY_SCRIPT"
        fi
        exit 1
    fi
}

# Load project configuration if available
if [ -f "package.json" ]; then
    echo "=> Node.js configuration detected."
    
    if grep -q '"lint":' package.json; then
        run_gate "npm run lint"
    fi
    if grep -q '"typecheck":' package.json; then
        run_gate "npm run typecheck"
    fi
    if grep -q '"test":' package.json; then
        run_gate "npm test"
    fi
elif [ -f "pytest.ini" ] || [ -f "pyproject.toml" ]; then
    echo "=> Python configuration detected."
    if command -v flake8 >/dev/null 2>&1; then
        run_gate "flake8 ."
    fi
    if command -v mypy >/dev/null 2>&1; then
        run_gate "mypy ."
    fi
    if command -v pytest >/dev/null 2>&1; then
        run_gate "pytest"
    fi
else
    echo "=> No recognizable project configuration found. Skipping specific language gates."
    echo "=> Please configure gate-runner.sh for your language stack."
fi

echo "=> All gates passed successfully."
exit 0
