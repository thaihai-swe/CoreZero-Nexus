#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
KIT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
TMP_DIR="$(mktemp -d)"
KIT_VERSION="$(tr -d '[:space:]' < "$KIT_ROOT/VERSION")"
trap 'rm -rf "$TMP_DIR"' EXIT

DRY_RUN_TARGET="$TMP_DIR/dry-run"
FRESH_TARGET="$TMP_DIR/fresh"

echo "1. Dry-run installer"
DRY_RUN_LOG="$TMP_DIR/dry-run.log"
bash "$KIT_ROOT/scripts/install.sh" "$DRY_RUN_TARGET" --dry-run | tee "$DRY_RUN_LOG"

echo "2. Fresh install"
FRESH_LOG="$TMP_DIR/fresh.log"
bash "$KIT_ROOT/scripts/install.sh" "$FRESH_TARGET" | tee "$FRESH_LOG"

echo "3. Verify installed surface"
python3 "$FRESH_TARGET/scripts/check-surface-truth.py" --mode installed --root "$FRESH_TARGET"

echo "4. Verify version stamp"
grep -q "$KIT_VERSION" "$FRESH_TARGET/.corezero-version"

echo "5. Verify first-feature lifecycle guidance"
grep -q "Start the first feature with /spec-requirements" "$DRY_RUN_LOG"
grep -q "Use /context-session only after a feature slug and status.md already exist" "$DRY_RUN_LOG"
if grep -q "Open work with /context-session" "$DRY_RUN_LOG"; then
  echo "ERROR: installer still advertises /context-session before first-feature creation" >&2
  exit 1
fi
grep -q "Start the first feature with" "$FRESH_TARGET/docs/INSTALL.md"
grep -q "feature slug already exists" "$FRESH_TARGET/docs/README.md"
grep -q "before changing behavior" "$FRESH_TARGET/docs/ADOPTION_GUIDE.md"

echo "6. Verify reinstall preserves adopter-owned seeded files"
printf 'Customized adopter content\n' > "$FRESH_TARGET/docs/PRODUCT_SENSE.md"
bash "$KIT_ROOT/scripts/install.sh" "$FRESH_TARGET"
grep -q "Customized adopter content" "$FRESH_TARGET/docs/PRODUCT_SENSE.md"
