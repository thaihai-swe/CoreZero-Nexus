#!/usr/bin/env bash
# telemetry-count.sh
# Count telemetry OBS-* entries for a given task or feature.
# Used by harness-verify to enforce the <2 vs >=2 failure escalation rule.

set -euo pipefail

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

if [[ -z "$ROOT_DIR" ]]; then
  CURRENT_DIR="$PWD"
  while [[ "$CURRENT_DIR" != "/" && -n "$CURRENT_DIR" ]]; do
    if [[ -f "$CURRENT_DIR/AGENTS.md" && -d "$CURRENT_DIR/memories/repo" ]]; then
      ROOT_DIR="$CURRENT_DIR"
      break
    fi
    CURRENT_DIR="$(dirname "$CURRENT_DIR")"
  done
fi

TELEMETRY_FILE="$ROOT_DIR/memories/repo/harness-telemetry.md"
[[ -f "$TELEMETRY_FILE" ]] || { echo "0"; exit 0; }

COUNT=0
MATCHING=""

# Parse YAML blocks looking for task: <TASK_ID>
while IFS= read -r line; do
  if [[ "$line" =~ ^"  task: \"${TASK_ID}\""$ ]]; then
    MATCHING="yes"
  fi
  if [[ "$line" =~ ^"  status: open"$ && -n "$MATCHING" ]]; then
    if [[ -n "$FEATURE_SLUG" ]]; then
      # Also check feature field — read backwards a few lines
      # Simplification: count all open entries for this task
      :
    fi
    COUNT=$((COUNT + 1))
    MATCHING=""
  fi
  # Reset if we hit the next YAML block or entry
  if [[ "$line" =~ ^"- id:" ]]; then
    MATCHING=""
  fi
done < <(grep -A 10 "task: \"$TASK_ID\"" "$TELEMETRY_FILE" 2>/dev/null || true)

echo "$COUNT"
