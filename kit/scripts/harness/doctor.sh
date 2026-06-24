#!/usr/bin/env bash
# doctor.sh — CoreZero kit self-diagnosis
# Checks internal consistency of the installed kit surface.
# Exits 0 if all checks pass, 1 with specific failures otherwise.
# Intended to run after install.sh and on-demand by harness-maintain.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/_lib/root.sh"

KIT_ROOT=$(resolve_repo_root) || {
  echo "FAIL: Could not resolve kit root (no AGENTS.md + memories/repo/)"
  exit 1
}

errors=0
warn()  { echo "  WARN: $*"; }
fail()  { echo "  FAIL: $*"; errors=$((errors + 1)); }
pass()  { echo "  PASS: $*"; }

echo "CoreZero doctor — $KIT_ROOT"
echo ""

# --- Check 1: manifest.json files exist ---
echo "--- Check 1: Manifest files exist ---"
if ! command -v python3 >/dev/null 2>&1; then
  fail "python3 is not installed or not in PATH"
  exit 1
fi
MANIFEST="$KIT_ROOT/manifest.json"
[[ -f "$MANIFEST" ]] || { fail "manifest.json not found"; exit 1; }

check_manifest_entries() {
  local field="$1"
  python3 - "$MANIFEST" "$field" <<'PY'
import json, sys, os, glob
m = json.load(open(sys.argv[1]))
cur = m
for k in sys.argv[2].split('.'):
    if isinstance(cur, list):
        break
    cur = cur.get(k, []) if isinstance(cur, dict) else cur
if isinstance(cur, list):
    for item in cur:
        if '*' in item or '**' in item:
            matches = glob.glob(os.path.join(os.path.dirname(sys.argv[1]), item), recursive=True)
            for m2 in matches:
                print(os.path.relpath(m2, os.path.dirname(sys.argv[1])))
        else:
            print(item)
PY
}

while IFS= read -r rel; do
  [[ -n "$rel" ]] || continue
  [[ -f "$KIT_ROOT/$rel" ]] || [[ -d "$KIT_ROOT/$rel" ]] || fail "manifest references missing file: $rel"
done < <(check_manifest_entries "files.overwrite")

while IFS= read -r rel; do
  [[ -n "$rel" ]] || continue
  [[ -f "$KIT_ROOT/$rel" ]] || [[ -d "$KIT_ROOT/$rel" ]] || fail "manifest (copyIfMissing) references missing file: $rel"
done < <(check_manifest_entries "files.copyIfMissing")

# --- Check 2: Sections referenced by SKILL.md exist ---
echo "--- Check 2: Referenced sections exist ---"

# ## Security Policy in core-policies.md
if grep -q "^## Security Policy" "$KIT_ROOT/memories/repo/core-policies.md" 2>/dev/null; then
  pass "core-policies.md has ## Security Policy"
else
  fail "core-policies.md missing ## Security Policy"
fi

# ## Promotion Watchlist in MASTER_INDEX.md
if grep -q "^## 5. Promotion Watchlist" "$KIT_ROOT/MASTER_INDEX.md" 2>/dev/null; then
  pass "MASTER_INDEX.md has ## Promotion Watchlist"
else
  fail "MASTER_INDEX.md missing ## Promotion Watchlist"
fi

# ## Memory Tiers in context-memory/SKILL.md
if grep -q "## Memory Tiers" "$KIT_ROOT/skills/context-memory/SKILL.md" 2>/dev/null; then
  pass "context-memory/SKILL.md has ## Memory Tiers"
else
  warn "context-memory/SKILL.md missing ## Memory Tiers (will be added in Pass 3)"
fi

# --- Check 3: No kit/-prefixed paths in installed SKILL.md files ---
echo "--- Check 3: No kit/-prefixed paths in skills ---"
KIT_PREFIX_HITS=$(grep -rn '"kit/' "$KIT_ROOT/skills/" 2>/dev/null || true)
if [[ -z "$KIT_PREFIX_HITS" ]]; then
  pass "No kit/-prefixed paths in skills/"
else
  fail "Found kit/-prefixed paths in skills/ (should be stripped for flat install):"
  echo "$KIT_PREFIX_HITS"
fi

# --- Check 4: MASTER_INDEX.md routes point to existing files ---
echo "--- Check 4: MASTER_INDEX.md routes exist ---"
# Check specific files referenced in MASTER_INDEX.md
for f in \
  "memories/repo/core-policies.md" \
  "memories/repo/project-knowledge-base.md" \
  "memories/repo/adr-log.md" \
  "memories/repo/learned-heuristics.md" \
  "memories/repo/harness-telemetry.md" \
  "docs/rules/security.md" \
  "docs/rules/ponytail.md" \
  "docs/policies/code-design.md" \
  "docs/index.html" \
  "skills/README.md" \
  "scripts/install.sh" \
  "scripts/harness/gate-runner.sh" \
  "scripts/harness/telemetry-collector.sh"; do
  [[ -f "$KIT_ROOT/$f" ]] || fail "MASTER_INDEX.md route missing: $f"
done


# --- Check 5: Threshold consistency (600/800/1200) ---
echo "--- Check 5: Threshold consistency ---"
check_threshold() {
  local file="$1" val="$2"
  if grep -q "$val" "$KIT_ROOT/$file" 2>/dev/null; then
    return 0
  fi
  return 1
}
# Just check core-policies.md has the canonical thresholds
if grep -q "Memory Promotion Thresholds" "$KIT_ROOT/memories/repo/core-policies.md" && grep -qE "800.1199" "$KIT_ROOT/memories/repo/core-policies.md"; then
  pass "core-policies.md has canonical thresholds table"
else
  fail "core-policies.md missing canonical thresholds"
fi

# --- Check 6: Task ID grammar is TASK-NNN ---
echo "--- Check 6: Task ID grammar (no T-01/T-NN in SKILL.md) ---"
T01_HITS=$(grep -rnE "\bT-[0-9]+\b|\bT-NN\b" "$KIT_ROOT/skills/" --include="SKILL.md" 2>/dev/null || true)
if [[ -z "$T01_HITS" ]]; then
  pass "No T-01/T-NN in SKILL.md files"
else
  fail "Found non-standard task IDs in SKILL.md files:"
  echo "$T01_HITS"
fi

# --- Check 7: ADR status vocabulary is unified ---
echo "--- Check 7: ADR status consistency ---"
if grep -q "Rejected" "$KIT_ROOT/memories/repo/adr-log.md" 2>/dev/null; then
  fail "adr-log.md still has 'Rejected' status (should be Deprecated/Superseded)"
else
  pass "adr-log.md status vocabulary clean"
fi

# --- Check 8: harness-telemetry.md schema has task/feature fields ---
echo "--- Check 8: Telemetry schema ---"
if grep -q "^  task:" "$KIT_ROOT/scripts/harness/telemetry-collector.sh" 2>/dev/null; then
  pass "telemetry-collector.sh emits task: field"
else
  fail "telemetry-collector.sh missing task: field"
fi
if [[ -f "$KIT_ROOT/scripts/harness/telemetry-count.sh" ]]; then
  pass "telemetry-count.sh exists"
else
  fail "telemetry-count.sh missing"
fi

# --- Check 9: Version consistency (Source repo only) ---
echo "--- Check 9: Version consistency ---"
if [[ -f "$KIT_ROOT/../VERSION" ]]; then
  SRC_VER=$(cat "$KIT_ROOT/../VERSION" 2>/dev/null | tr -d ' \n\r')
  KIT_VER=$(cat "$KIT_ROOT/VERSION" 2>/dev/null | tr -d ' \n\r')
  MANIFEST_VER=$(python3 -c "import json; print(json.load(open('$KIT_ROOT/manifest.json'))['version'])" 2>/dev/null | tr -d ' \n\r')
  
  if [[ "$SRC_VER" == "$KIT_VER" && "$KIT_VER" == "$MANIFEST_VER" ]]; then
    pass "Version surfaces match: $KIT_VER"
  else
    fail "Version mismatch: root VERSION='$SRC_VER', kit/VERSION='$KIT_VER', manifest.json version='$MANIFEST_VER'"
  fi
else
  pass "Not in source repository, skipping root VERSION consistency check"
fi

# --- Check 10: Executable bits assertion ---
echo "--- Check 10: Executable bits for harness scripts ---"
for f in "$KIT_ROOT"/scripts/harness/*.sh; do
  if [[ -f "$f" ]]; then
    if [[ -x "$f" ]]; then
      pass "$(basename "$f") is executable"
    else
      fail "$(basename "$f") is NOT executable"
    fi
  fi
done

# --- Summary ---
echo ""
if [[ $errors -eq 0 ]]; then
  echo "All checks passed."
  exit 0
else
  echo "$errors check(s) failed."
  exit 1
fi
