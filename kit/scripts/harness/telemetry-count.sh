#!/usr/bin/env bash
# telemetry-count.sh
# Count telemetry OBS-* entries for a given task or feature.
# Used by harness-verify to enforce the <2 vs >=2 failure escalation rule.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/_lib/root.sh"

ROOT_DIR=""
TASK_ID=""
FEATURE_SLUG=""

usage() {
  echo "Usage: $0 --task <TASK-NNN> [--root <path>] [--feature <slug>]"
  exit 1
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --root)
      ROOT_DIR="$2"; shift 2 ;;
    --task)
      TASK_ID="$2"; shift 2 ;;
    --feature)
      FEATURE_SLUG="$2"; shift 2 ;;
    *)
      usage ;;
  esac
done

[[ -z "$TASK_ID" ]] && usage

ROOT_DIR=$(resolve_repo_root "${ROOT_DIR:-}") || {
  echo "ERROR: Could not resolve repository root." >&2
  exit 1
}

TELEMETRY_FILE="$ROOT_DIR/memories/repo/harness-telemetry.md"
[[ -f "$TELEMETRY_FILE" ]] || { echo "0"; exit 0; }

COUNT=0
CURRENT_TASK=""
CURRENT_FEATURE=""
CURRENT_STATUS=""

while IFS= read -r line; do
  # Trim trailing CR if any (Windows compat)
  line="${line%$'\r'}"
  
  if [[ "$line" =~ ^[[:space:]]*-?[[:space:]]*id: ]]; then
    # We hit a new entry, evaluate the previous one
    if [[ "$CURRENT_TASK" == "$TASK_ID" && "$CURRENT_STATUS" == "open" ]]; then
      if [[ -z "$FEATURE_SLUG" || "$CURRENT_FEATURE" == "$FEATURE_SLUG" ]]; then
        COUNT=$((COUNT + 1))
      fi
    fi
    CURRENT_TASK=""
    CURRENT_FEATURE=""
    CURRENT_STATUS=""
  elif [[ "$line" =~ ^[[:space:]]*task:[[:space:]]*\"?([^\"]*)\"?$ ]]; then
    CURRENT_TASK="${BASH_REMATCH[1]}"
  elif [[ "$line" =~ ^[[:space:]]*feature:[[:space:]]*\"?([^\"]*)\"?$ ]]; then
    CURRENT_FEATURE="${BASH_REMATCH[1]}"
  elif [[ "$line" =~ ^[[:space:]]*status:[[:space:]]*\"?([^\"]*)\"?$ ]]; then
    CURRENT_STATUS="${BASH_REMATCH[1]}"
  fi
done < "$TELEMETRY_FILE"

# Evaluate the last entry at EOF
if [[ "$CURRENT_TASK" == "$TASK_ID" && "$CURRENT_STATUS" == "open" ]]; then
  if [[ -z "$FEATURE_SLUG" || "$CURRENT_FEATURE" == "$FEATURE_SLUG" ]]; then
    COUNT=$((COUNT + 1))
  fi
fi

echo "$COUNT"
