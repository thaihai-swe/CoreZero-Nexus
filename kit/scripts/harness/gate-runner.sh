#!/usr/bin/env bash
# gate-runner.sh
# Orchestrates mechanical validation (linters, typecheckers, syntax) and behavioral tests.
# Returns 0 only if all gates pass. Automatically pipes failures to telemetry-collector.sh if present.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TELEMETRY_SCRIPT="$SCRIPT_DIR/telemetry-collector.sh"

TASK_ID=""
FEATURE_SLUG=""
ROOT_DIR=""

# Parse options
while [[ $# -gt 0 ]]; do
  case "$1" in
    --task)
      TASK_ID="$2"; shift 2 ;;
    --feature)
      FEATURE_SLUG="$2"; shift 2 ;;
    --root)
      ROOT_DIR="$2"; shift 2 ;;
    *)
      # Ignore other options or shift
      shift ;;
  esac
done

source "$SCRIPT_DIR/_lib/root.sh"
RESOLVED_ROOT=$(resolve_repo_root "${ROOT_DIR:-}") || {
  echo "ERROR: Could not resolve repository root." >&2
  exit 1
}

# Shift execution Cwd to RESOLVED_ROOT so all build/lint/test commands run in the target project root
cd "$RESOLVED_ROOT"

run_gate() {
    local cmd="$1"
    echo "=> Running: $cmd"
    
    # Run the command, capture stdout/stderr, and exit if it fails
    if ! OUTPUT=$(eval "$cmd" 2>&1); then
        echo "$OUTPUT"
        echo "=> Gate failed: $cmd"
        if [ -x "$TELEMETRY_SCRIPT" ]; then
            local args=()
            [[ -n "$TASK_ID" ]] && args+=(--task "$TASK_ID")
            [[ -n "$FEATURE_SLUG" ]] && args+=(--feature "$FEATURE_SLUG")
            echo "$OUTPUT" | "$TELEMETRY_SCRIPT" "${args[@]}"
        fi
        exit 1
    fi
}

# New override hook
if [ -f "./scripts/harness/gate-runner.local.sh" ]; then
  echo "=> Using project-local gate-runner override."
  bash "./scripts/harness/gate-runner.local.sh"; exit $?
fi

# Pre-flight check function (new):
preflight_check() {
  local cmd="$1"
  if ! command -v "$cmd" > /dev/null 2>&1; then
    echo "SETUP_FAILURE: Required tool '$cmd' not found. Run setup/install before harness."
    exit 2
  fi
}

# Load project configuration if available
if [ -f "package.json" ]; then
    echo "=> Node.js configuration detected."
    preflight_check npm
    
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
    preflight_check python3
    if command -v flake8 >/dev/null 2>&1; then
        run_gate "flake8 ."
    fi
    if command -v mypy >/dev/null 2>&1; then
        run_gate "mypy ."
    fi
    if command -v pytest >/dev/null 2>&1; then
        run_gate "pytest"
    else
        echo "SETUP_FAILURE: pytest not found in Python path."
        exit 2
    fi
else
    echo "ERROR: No recognizable project configuration found (no package.json, pytest.ini, or pyproject.toml)."
    echo "=> Copy the generic template and customize it:"
    echo "   cp scripts/harness/gate-runner.local.example.sh scripts/harness/gate-runner.local.sh"
    echo "=> Then edit gate-runner.local.sh with your build/lint/test commands."
    exit 1
fi

echo "=> All gates passed successfully."
exit 0
