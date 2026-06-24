#!/usr/bin/env bash
# readiness-score.sh — thin wrapper around spec_validator.py --readiness

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR=""
SPEC_PATH=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --root) ROOT_DIR="$2"; shift 2 ;;
    --spec) SPEC_PATH="$2"; shift 2 ;;
    *) shift ;;
  esac
done

source "$SCRIPT_DIR/_lib/root.sh"
RESOLVED_ROOT=$(resolve_repo_root "${ROOT_DIR:-}") || {
  echo "ERROR: Could not resolve repository root." >&2; exit 1
}
RESOLVED_ROOT="$(cd "$RESOLVED_ROOT" && pwd)"

FEATURE_SLUG="${1:-}"
if [[ -n "$FEATURE_SLUG" ]]; then
  SPEC_PATH="$RESOLVED_ROOT/artifacts/features/$FEATURE_SLUG/spec.md"
fi

PYTHON_ENGINE="$SCRIPT_DIR/../core/spec_validator.py"

exec python3 "$PYTHON_ENGINE" --spec "$SPEC_PATH" --readiness
