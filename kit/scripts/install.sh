#!/usr/bin/env bash
#
# CoreZero Nexus installer
#
# Usage:
#   scripts/install.sh <target_dir> [--version <x.y.z>] [--dry-run]
#
# Behavior:
#   - Reads manifest.json at the kit root.
#   - Backs up existing kit-managed files to <target>/.corezero-backup-<timestamp>/.
#   - Overwrites kit content (skills, scripts, rules, doc references).
#   - Copies user-content files (memory, templates, architecture) only if missing.
#   - Preserves user state (memories/repo content, artifacts/, local settings).
#   - Writes <target>/.corezero-version with the installed version.
#   - Idempotent. Re-running upgrades the kit and preserves your content.
#
# Curl-pipe support:
#   When piped from curl, the script clones this repo to a temp dir, runs the
#   installer, and cleans up.

set -euo pipefail

REPO_URL="${HARNESS_KIT_REPO_URL:-https://github.com/thaihai-swe/CoreZero-Nexus.git}"

err() { printf 'ERROR: %s   ' "$*" >&2; exit 1; }
log() { printf '%s   ' "$*"; }

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || err "required command not found: $1"
}

read_manifest_array() {
  local manifest="$1"
  local path="$2"
  python3 - "$manifest" "$path" <<'PY'
import json, sys
m = json.load(open(sys.argv[1]))
cur = m
for k in sys.argv[2].split('.'):
    cur = cur[k]
if not isinstance(cur, list):
    raise SystemExit("expected list at " + sys.argv[2])
for item in cur:
    print(item)
PY
}

read_manifest_string() {
  local manifest="$1"
  local path="$2"
  python3 - "$manifest" "$path" <<'PY'
import json, sys
m = json.load(open(sys.argv[1]))
cur = m
for k in sys.argv[2].split('.'):
    cur = cur[k]
print(cur)
PY
}

read_template_for() {
  local manifest="$1"
  local target_rel="$2"
  python3 - "$manifest" "$target_rel" <<'PY'
import json, sys
m = json.load(open(sys.argv[1]))
print(m.get("templateMap", {}).get(sys.argv[2], ""))
PY
}

if sed --version >/dev/null 2>&1; then
  SED_INPLACE=(sed -i)
else
  SED_INPLACE=(sed -i '')
fi

expand_glob() {
  local pattern="$1"
  pushd "$SOURCE_DIR" >/dev/null
  if [[ "$pattern" == *"**"* ]]; then
    local base="${pattern%%/\*\**}"
    [[ -d "$base" ]] && find "$base" -type f
  elif [[ "$pattern" == *"*"* ]]; then
    shopt -s nullglob
    local matches=( $pattern )
    shopt -u nullglob
    local m
    for m in "${matches[@]}"; do
      [[ -f "$m" ]] && echo "$m"
    done
  else
    [[ -f "$pattern" ]] && echo "$pattern"
  fi
  popd >/dev/null
}

copy_into_target() {
  local rel="$1"
  local src="$SOURCE_DIR/$rel"
  local dst="$TARGET_DIR/$rel"
  [[ -f "$src" ]] || err "manifest references missing source: $rel"
  if [[ "$DRY_RUN" == "true" ]]; then
    log "  [dry-run] would copy: $rel"
    return
  fi
  mkdir -p "$(dirname "$dst")"
  cp "$src" "$dst"
}

backup_file() {
  local rel="$1"
  local dst="$TARGET_DIR/$rel"
  [[ -f "$dst" ]] || return 0
  if [[ "$DRY_RUN" == "true" ]]; then
    log "  [dry-run] would back up: $rel"
    return
  fi
  local backup_path="$BACKUP_DIR/$rel"
  mkdir -p "$(dirname "$backup_path")"
  cp "$dst" "$backup_path"
}

resolve_source_dir() {
  if [[ "${BASH_SOURCE[0]:-}" != "" && -f "${BASH_SOURCE[0]}" ]]; then
    local script_dir
    script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    local maybe_root
    maybe_root="$(cd "$script_dir/.." && pwd)"
    if [[ -f "$maybe_root/manifest.json" ]]; then
      SOURCE_DIR="$maybe_root"
      SOURCE_TEMP=""
      return
    fi
  fi
  require_cmd git
  SOURCE_TEMP="$(mktemp -d)"
  log "Cloning kit to temp: $SOURCE_TEMP"
  if [[ -n "${PIN_VERSION:-}" ]]; then
    git clone --depth 1 --branch "v$PIN_VERSION" "$REPO_URL" "$SOURCE_TEMP" >/dev/null 2>&1 \
      || err "could not clone $REPO_URL at tag v$PIN_VERSION"
  else
    git clone --depth 1 "$REPO_URL" "$SOURCE_TEMP" >/dev/null 2>&1 \
      || err "could not clone $REPO_URL"
  fi
  SOURCE_DIR="$SOURCE_TEMP"
}

cleanup_source_temp() {
  if [[ -n "${SOURCE_TEMP:-}" && -d "$SOURCE_TEMP" ]]; then
    rm -rf "$SOURCE_TEMP"
  fi
}

TARGET_DIR=""
PIN_VERSION=""
DRY_RUN="false"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --version)
      PIN_VERSION="${2:-}"; shift 2
      [[ -n "$PIN_VERSION" ]] || err "--version requires a value"
      ;;
    --dry-run)
      DRY_RUN="true"; shift
      ;;
    -h|--help)
      log "Usage: install.sh <target_dir> [--version <x.y.z>] [--dry-run]"
      exit 0
      ;;
    *)
      [[ -z "$TARGET_DIR" ]] || err "unexpected argument: $1"
      TARGET_DIR="$1"; shift
      ;;
  esac
done

[[ -n "$TARGET_DIR" ]] || err "Usage: install.sh <target_dir> [--version <x.y.z>] [--dry-run]"

require_cmd python3
require_cmd cp
require_cmd find

trap cleanup_source_temp EXIT

resolve_source_dir
MANIFEST="$SOURCE_DIR/manifest.json"
[[ -f "$MANIFEST" ]] || err "manifest.json not found at $MANIFEST"

KIT_VERSION="$(read_manifest_string "$MANIFEST" version)"

if [[ -n "$PIN_VERSION" && "$PIN_VERSION" != "$KIT_VERSION" ]]; then
  err "kit clone is version $KIT_VERSION but --version $PIN_VERSION was requested"
fi

mkdir -p "$TARGET_DIR"
TARGET_DIR="$(cd "$TARGET_DIR" && pwd)"

EXISTING_VERSION=""
if [[ -f "$TARGET_DIR/.corezero-version" ]]; then
  EXISTING_VERSION="$(tr -d '[:space:]' < "$TARGET_DIR/.corezero-version")"
fi

TIMESTAMP="$(date +%Y%m%d-%H%M%S)"
BACKUP_DIR="$TARGET_DIR/.corezero-backup-$TIMESTAMP"

log "CoreZero Nexus installer"
log "  Source:   $SOURCE_DIR"
log "  Target:   $TARGET_DIR"
log "  Version:  $KIT_VERSION${EXISTING_VERSION:+ (replacing $EXISTING_VERSION)}"
log "  Dry run:  $DRY_RUN"
log "  Package:  adopter docs in docs/; maintainer docs stay in the source repo"
log ""

while IFS= read -r dir; do
  [[ -n "$dir" ]] || continue
  if [[ "$DRY_RUN" == "true" ]]; then
    log "  [dry-run] would mkdir: $dir"
  else
    mkdir -p "$TARGET_DIR/$dir"
  fi
done < <(read_manifest_array "$MANIFEST" directories)

log "Installing kit content (overwrite)..."
overwrite_count=0
backup_count=0

while IFS= read -r pattern; do
  [[ -n "$pattern" ]] || continue
  while IFS= read -r rel; do
    [[ -n "$rel" ]] || continue
    if [[ -f "$TARGET_DIR/$rel" ]]; then
      backup_file "$rel"
      backup_count=$((backup_count + 1))
    fi
    copy_into_target "$rel"
    overwrite_count=$((overwrite_count + 1))
  done < <(expand_glob "$pattern")
done < <(read_manifest_array "$MANIFEST" files.overwrite)

log "Seeding user content (copyIfMissing)..."
seeded_count=0
skipped_count=0

while IFS= read -r rel; do
  [[ -n "$rel" ]] || continue
  if [[ -f "$TARGET_DIR/$rel" ]]; then
    skipped_count=$((skipped_count + 1))
    continue
  fi
  template_rel="$(read_template_for "$MANIFEST" "$rel")"
  if [[ -n "$template_rel" ]]; then
    [[ -f "$SOURCE_DIR/$template_rel" ]] || err "templateMap points at missing file: $template_rel"
    if [[ "$DRY_RUN" == "true" ]]; then
      log "  [dry-run] would seed from template: $rel <- $template_rel"
    else
      mkdir -p "$(dirname "$TARGET_DIR/$rel")"
      cp "$SOURCE_DIR/$template_rel" "$TARGET_DIR/$rel"
    fi
  else
    [[ -f "$SOURCE_DIR/$rel" ]] || err "copyIfMissing references missing source: $rel"
    copy_into_target "$rel"
  fi
  seeded_count=$((seeded_count + 1))
done < <(read_manifest_array "$MANIFEST" files.copyIfMissing)

detect_stack_and_prefill_config() {
  local config_file="$TARGET_DIR/memories/repo/harness-config.md"
  [[ -f "$config_file" ]] || return
  if ! grep -qE '^- Test:[[:space:]]*$|^- Test command:[[:space:]]*$' "$config_file"; then
    return 0
  fi

  local install_cmd="" test_cmd="" lint_cmd="" typecheck_cmd="" build_cmd="" stack=""

  if [[ -f "$TARGET_DIR/package.json" ]]; then
    stack="Node.js"
    install_cmd="npm install"; test_cmd="npm test"
    lint_cmd="npm run lint"; typecheck_cmd="npm run typecheck"; build_cmd="npm run build"
  elif [[ -f "$TARGET_DIR/pyproject.toml" || -f "$TARGET_DIR/requirements.txt" ]]; then
    stack="Python"
    install_cmd="pip install -e ."; test_cmd="pytest"
    lint_cmd="ruff check ."; typecheck_cmd="mypy ."; build_cmd="python -m build"
  elif [[ -f "$TARGET_DIR/go.mod" ]]; then
    stack="Go"
    install_cmd="go mod download"; test_cmd="go test ./..."
    lint_cmd="golangci-lint run ./..."; typecheck_cmd="go vet ./..."; build_cmd="go build ./..."
  elif [[ -f "$TARGET_DIR/Cargo.toml" ]]; then
    stack="Rust"
    install_cmd="cargo fetch"; test_cmd="cargo test"
    lint_cmd="cargo clippy -- -D warnings"; typecheck_cmd="cargo check"; build_cmd="cargo build --release"
  fi

  [[ -z "$stack" ]] && return

  if [[ "$DRY_RUN" == "true" ]]; then
    log "  [dry-run] would prefill harness-config.md for $stack"
    return
  fi

  "${SED_INPLACE[@]}" \
    -e "s|^- Install / bootstrap:[[:space:]]*$|- Install / bootstrap: ${install_cmd}|" \
    -e "s|^- Install / bootstrap command:[[:space:]]*$|- Install / bootstrap command: ${install_cmd}|" \
    -e "s|^- Test:[[:space:]]*$|- Test: ${test_cmd}|" \
    -e "s|^- Test command:[[:space:]]*$|- Test command: ${test_cmd}|" \
    -e "s|^- Lint / format:[[:space:]]*$|- Lint / format: ${lint_cmd}|" \
    -e "s|^- Lint / format command:[[:space:]]*$|- Lint / format command: ${lint_cmd}|" \
    -e "s|^- Typecheck:[[:space:]]*$|- Typecheck: ${typecheck_cmd}|" \
    -e "s|^- Typecheck command:[[:space:]]*$|- Typecheck command: ${typecheck_cmd}|" \
    -e "s|^- Build:[[:space:]]*$|- Build: ${build_cmd}|" \
    -e "s|^- Build command:[[:space:]]*$|- Build command: ${build_cmd}|" \
    "$config_file"

  log "  Auto-detected stack: $stack — prefilled harness-config.md"
}

detect_stack_and_prefill_config

if [[ "$DRY_RUN" != "true" ]]; then
  [[ -f "$TARGET_DIR/scripts/install.sh" ]] && chmod +x "$TARGET_DIR/scripts/install.sh"
  printf '%s   ' "$KIT_VERSION" > "$TARGET_DIR/.corezero-version"
fi

errors=0
validate_path() {
  local path="$1" label="$2"
  if [[ -e "$TARGET_DIR/$path" ]]; then
    log "  [OK]   $label"
  else
    log "  [FAIL] $label — missing: $path"
    errors=$((errors + 1))
  fi
}

if [[ "$DRY_RUN" != "true" ]]; then
  log ""
  log "Post-install validation"
  validate_path "skills" "Skills directory"
  validate_path "memories/repo" "Memory layer"
  validate_path "memories/repo/INDEX.md" "Memory router"
  validate_path "memories/repo/constitution.md" "Constitution"
  validate_path "memories/repo/harness-config.md" "Harness config"
  validate_path "memories/repo/security-policy.md" "Security policy"
  validate_path "HARNESS_CARD.md" "Harness card"
  validate_path "AGENTS.md" "Runtime entrypoint"
  validate_path "scripts/install.sh" "Installer (self-shipped)"
  validate_path ".corezero-version" "Version stamp"
fi

log ""
log "Summary"
log "  Files installed: $overwrite_count"
log "  Files seeded:    $seeded_count"
log "  Files skipped:   $skipped_count (already present)"
log "  Files backed up: $backup_count -> $BACKUP_DIR"
log "  Installed docs: docs/ (adopter-facing)"
log "  Not installed by default: documents/ (maintainer-only)"

if [[ $errors -gt 0 ]]; then
  log ""
  err "validation failed with $errors error(s)"
fi

log ""
log "Next steps:"
log "  1. Read docs/ADOPTION_GUIDE.md for the guided pack-based start"
log "  2. Run /starter-init in your AI agent"
log "  3. Open work with /context-session"
log "  4. Deliver through /spec-requirements, /spec-plan, /spec-implement"
log "  5. Close out with /harness-verify"
log "  6. Use documents/ only in the source repository when maintaining the kit itself"
log ""
log "Upgrade later: re-run this command. Memory and artifacts are preserved."
