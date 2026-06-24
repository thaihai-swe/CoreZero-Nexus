#!/usr/bin/env bash
# phase-gate.sh <feature-slug> <target-phase>
# Mechanical precondition gate for spec-phase handoffs.
# Exits 0 if all checks pass; exits 1 with specific failure otherwise.

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
TARGET_PHASE="$2"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/_lib/root.sh"
RESOLVED_ROOT=$(resolve_repo_root "${ROOT_DIR:-}") || {
  echo "ERROR: Could not resolve repository root." >&2
  exit 1
}

FEATURE_DIR="$RESOLVED_ROOT/artifacts/features/$FEATURE_SLUG"

if [ -z "$FEATURE_SLUG" ] || [ -z "$TARGET_PHASE" ]; then
  echo "usage: phase-gate.sh [--root <path>] <feature-slug> <target-phase>"
  exit 1
fi

if [ ! -d "$FEATURE_DIR" ]; then
  echo "FAIL: feature directory $FEATURE_DIR does not exist"
  exit 1
fi

STATUS_FILE="$FEATURE_DIR/status.md"
if [ ! -f "$STATUS_FILE" ]; then
  echo "FAIL: $STATUS_FILE does not exist"
  exit 1
fi

# Check prior artifact exists based on target phase
case "$TARGET_PHASE" in
  "Spec Approved")
    if [ ! -f "$FEATURE_DIR/spec.md" ]; then
      echo "FAIL: spec.md not found — required before Spec Approved"
      exit 1
    fi
    ;;
  "Plan Approved")
    if [ ! -f "$FEATURE_DIR/plan.md" ]; then
      echo "FAIL: plan.md not found — required before Plan Approved"
      exit 1
    fi
    if [ ! -f "$FEATURE_DIR/tasks.md" ]; then
      echo "FAIL: tasks.md not found — required before Plan Approved"
      exit 1
    fi
    ;;
  "Implementing")
    if [ ! -f "$FEATURE_DIR/plan.md" ]; then
      echo "FAIL: plan.md not found — required before Implementing"
      exit 1
    fi
    if [ ! -f "$FEATURE_DIR/tasks.md" ]; then
      echo "FAIL: tasks.md not found — required before Implementing"
      exit 1
    fi
    # Check no stale plan
    if grep -q '\[STALE' "$FEATURE_DIR/plan.md" 2>/dev/null; then
      echo "FAIL: plan.md has STALE marker — spec was amended after plan approval"
      exit 1
    fi
    # Every AC in spec.md must appear in tasks.md
    if [ -f "$FEATURE_DIR/spec.md" ]; then
      while IFS= read -r ac_id; do
        if ! grep -qwE "\b${ac_id}\b" "$FEATURE_DIR/tasks.md" 2>/dev/null; then
          echo "FAIL: $ac_id in spec.md has no corresponding entry in tasks.md"
          exit 1
        fi
      done < <(grep -oE '\bAC-[0-9]+' "$FEATURE_DIR/spec.md" | sort -u)
    fi
    ;;
  "Verifying")
    if [ ! -f "$FEATURE_DIR/tasks.md" ]; then
      echo "FAIL: tasks.md not found — required before Verifying"
      exit 1
    fi
    # Every task must have validation evidence
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
        echo "FAIL: $task_id in tasks.md has no validation evidence"
        exit 1
      fi
    done < <(grep -oE '\bTASK-[0-9]+' "$FEATURE_DIR/tasks.md" | sort -u)
    ;;
  *)
    echo "PASS: no specific preconditions for target phase $TARGET_PHASE"
    exit 0
    ;;
esac

echo "PASS: all preconditions met for $TARGET_PHASE"
exit 0
