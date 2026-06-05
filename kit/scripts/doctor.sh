#!/usr/bin/env bash

set -euo pipefail

TARGET_DIR="${1:-.}"
TARGET_DIR="$(cd "$TARGET_DIR" && pwd)"

if [[ -f "$TARGET_DIR/kit/manifest.json" ]]; then
  MODE="source-repo"
  CHECKER="$TARGET_DIR/kit/scripts/check-surface-truth.py"
elif [[ -f "$TARGET_DIR/scripts/check-surface-truth.py" ]]; then
  MODE="installed"
  CHECKER="$TARGET_DIR/scripts/check-surface-truth.py"
else
  echo "ERROR: could not find a CoreZero truth-check script in $TARGET_DIR" >&2
  exit 1
fi

echo "Running CoreZero doctor in $MODE mode..."
python3 "$CHECKER" --mode "$MODE" --root "$TARGET_DIR"
echo "Doctor check completed without structural or lifecycle errors."
