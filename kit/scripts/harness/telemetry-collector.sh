#!/usr/bin/env bash
# telemetry-collector.sh
# Collects errors from the execution environment and logs them into harness-telemetry.md.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/_lib/root.sh"

ROOT_DIR=""
ERROR_MSG=""
TASK_ID=""
FEATURE_SLUG=""
CLASSIFICATION=""
SKILL_NAME=""
ROOT_CAUSE=""

# Parse options
while [[ $# -gt 0 ]]; do
  case "$1" in
    --root)
      if [[ $# -gt 1 ]]; then
        ROOT_DIR="$2"
        shift 2
      else
        echo "ERROR: --root requires an argument" >&2
        exit 1
      fi
      ;;
    --task)
      if [[ $# -gt 1 ]]; then
        TASK_ID="$2"
        shift 2
      else
        echo "ERROR: --task requires an argument" >&2
        exit 1
      fi
      ;;
    --feature)
      if [[ $# -gt 1 ]]; then
        FEATURE_SLUG="$2"
        shift 2
      else
        echo "ERROR: --feature requires an argument" >&2
        exit 1
      fi
      ;;
    --classification)
      if [[ $# -gt 1 ]]; then
        CLASSIFICATION="$2"
        shift 2
      else
        echo "ERROR: --classification requires an argument" >&2
        exit 1
      fi
      ;;
    --skill)
      if [[ $# -gt 1 ]]; then
        SKILL_NAME="$2"
        shift 2
      else
        echo "ERROR: --skill requires an argument" >&2
        exit 1
      fi
      ;;
    --root-cause)
      if [[ $# -gt 1 ]]; then
        ROOT_CAUSE="$2"
        shift 2
      else
        echo "ERROR: --root-cause requires an argument" >&2
        exit 1
      fi
      ;;
    *)
      if [[ -z "$ERROR_MSG" ]]; then
        ERROR_MSG="$1"
      else
        ERROR_MSG="$ERROR_MSG $1"
      fi
      shift
      ;;
  esac
done

if [ ! -t 0 ] && read -t 0 -r; then
  STDIN_MSG=$(cat)
  if [[ -n "$ERROR_MSG" ]]; then
    ERROR_MSG="${ERROR_MSG}
${STDIN_MSG}"
  else
    ERROR_MSG="$STDIN_MSG"
  fi
fi

if [[ -z "$ERROR_MSG" ]]; then
  echo "Usage: $0 [--root <path>] [--task <TASK-NNN>] [--feature <slug>] [--classification <class>] [--skill <skill>] [--root-cause <cause>] \"Error message or log snippet\""
  echo "       or pipe output to $0"
  exit 1
fi

# Resolve root directory
RESOLVED_ROOT=$(resolve_repo_root "${ROOT_DIR:-${HARNESS_REPO_ROOT:-}}") || {
  echo "ERROR: Could not resolve repository root. Walked up to / but did not find AGENTS.md and memories/repo/." >&2
  exit 1
}

TELEMETRY_FILE="$RESOLVED_ROOT/memories/repo/harness-telemetry.md"

# Ensure target directory exists
mkdir -p "$(dirname "$TELEMETRY_FILE")"

TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

# Create the file if it doesn't exist
if [ ! -f "$TELEMETRY_FILE" ]; then
    echo "# Harness Telemetry" > "$TELEMETRY_FILE"
    echo "Logs of mechanical and behavioral gate failures for diagnostic analysis." >> "$TELEMETRY_FILE"
    echo "" >> "$TELEMETRY_FILE"
fi

# Append the new log entry
NEXT_ID=$(grep -c "id: OBS-" "$TELEMETRY_FILE" 2>/dev/null || echo 0)
NEXT_ID=$(printf "OBS-%03d" $((NEXT_ID + 1)))
CLEAN_DESC=$(python3 -c 'import sys, json; print(json.dumps(sys.stdin.read().splitlines()[0][:120]))' <<< "$ERROR_MSG")

cat >> "$TELEMETRY_FILE" << EOF

\`\`\`yaml
- id: ${NEXT_ID}
  date: $(date +"%Y-%m-%d")
  classification: "${CLASSIFICATION:-[UNKNOWN: harness | model | spec]}"
  severity: medium
  skill: "${SKILL_NAME:-[UNKNOWN: <active-skill>]}"
  task: "${TASK_ID:-[UNKNOWN]}"
  feature: "${FEATURE_SLUG:-[UNKNOWN]}"
  description: ${CLEAN_DESC}
  root_cause: "${ROOT_CAUSE:-[UNKNOWN]}"
  fix_applied: "none yet"
  recurrence_risk: medium
  promotion_candidate: false
  status: open
\`\`\`
EOF

echo "=> Telemetry logged to $TELEMETRY_FILE"
