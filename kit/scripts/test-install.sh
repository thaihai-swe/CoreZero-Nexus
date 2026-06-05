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
bash "$KIT_ROOT/scripts/install.sh" "$DRY_RUN_TARGET" --dry-run

echo "2. Fresh install"
bash "$KIT_ROOT/scripts/install.sh" "$FRESH_TARGET"

echo "3. Verify installed surface"
python3 "$FRESH_TARGET/scripts/check-surface-truth.py" --mode installed --root "$FRESH_TARGET"

echo "4. Verify version stamp"
grep -q "$KIT_VERSION" "$FRESH_TARGET/.corezero-version"

echo "5. Verify reinstall preserves adopter-owned seeded files"
printf 'Customized adopter content\n' > "$FRESH_TARGET/docs/PRODUCT_SENSE.md"
bash "$KIT_ROOT/scripts/install.sh" "$FRESH_TARGET"
grep -q "Customized adopter content" "$FRESH_TARGET/docs/PRODUCT_SENSE.md"
