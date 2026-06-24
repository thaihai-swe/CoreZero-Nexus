#!/usr/bin/env bash
# traceability-audit.sh <feature-slug>
# Mechanical traceability audit: verifies every AC/REQ in spec.md maps to a task
# in tasks.md, and every task has validation evidence.
# Exits 0 if all traceable; exits 1 with specific failures otherwise.

set -euo pipefail

ROOT_DIR=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --root)
      ROOT_DIR="$2"; shift 2 ;;
    *)
      break ;;
  esac
done

FEATURE_SLUG="$1"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/_lib/root.sh"
RESOLVED_ROOT=$(resolve_repo_root "${ROOT_DIR:-}") || {
  echo "ERROR: Could not resolve repository root." >&2
  exit 1
}

FEATURE_DIR="$RESOLVED_ROOT/artifacts/features/$FEATURE_SLUG"

if [ -z "$FEATURE_SLUG" ]; then
  echo "usage: traceability-audit.sh [--root <path>] <feature-slug>"
  exit 1
fi

if [ ! -d "$FEATURE_DIR" ]; then
  echo "FAIL: feature directory $FEATURE_DIR does not exist"
  exit 1
fi

HAD_ERRORS=0

# 1. Check AC-NNN and REQ-NNN in spec.md map to tasks.md
if [ -f "$FEATURE_DIR/spec.md" ]; then
  while IFS= read -r ac_id; do
    if ! grep -qwE "\b${ac_id}\b" "$FEATURE_DIR/tasks.md" 2>/dev/null; then
      echo "UNMAPPED: $ac_id in spec.md has no corresponding entry in tasks.md"
      HAD_ERRORS=1
    fi
  done < <(grep -oE '\bAC-[0-9]+' "$FEATURE_DIR/spec.md" | sort -u)

  while IFS= read -r req_id; do
    if ! grep -qwE "\b${req_id}\b" "$FEATURE_DIR/tasks.md" 2>/dev/null; then
      echo "UNMAPPED: $req_id in spec.md has no corresponding entry in tasks.md"
      HAD_ERRORS=1
    fi
  done < <(grep -oE '\bREQ-[0-9]+' "$FEATURE_DIR/spec.md" | sort -u)
else
  echo "SKIP: no spec.md found — skipping AC/REQ traceability check"
fi

# 2. Check every task in tasks.md has validation evidence
if [ -f "$FEATURE_DIR/tasks.md" ]; then
  while IFS= read -r task_id; do
    evidence_block=$(awk -v task="**$task_id**" '
      $0 ~ task { printing = 1; print; next }
      printing {
        if ($0 ~ /\*\*TASK-/ || $0 ~ /^---$/ || $0 ~ /^#/) {
          printing = 0
        } else {
          print
        }
      }
    ' "$FEATURE_DIR/tasks.md" 2>/dev/null)
    if ! echo "$evidence_block" | grep -qE 'Proof:|Evidence:|Status:.*Done'; then
      echo "NO EVIDENCE: $task_id in tasks.md has no validation evidence"
      HAD_ERRORS=1
    fi
  done < <(grep -oE '\bTASK-[0-9]+' "$FEATURE_DIR/tasks.md" | sort -u)
else
  echo "SKIP: no tasks.md found — skipping task evidence check"
fi

if [ "$HAD_ERRORS" -eq 1 ]; then
  exit 1
fi

echo "PASS: full traceability — all ACs/REQs mapped and all tasks have evidence"
exit 0
