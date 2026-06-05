#!/usr/bin/env bash
#
# Root entrypoint for CoreZero Nexus installation.
# Redirects to kit/scripts/install.sh locally, or clones the repository
# when run via curl-pipe.
#
set -euo pipefail

REPO_URL="${HARNESS_KIT_REPO_URL:-https://github.com/thaihai-swe/AI-agents-dev-kits.git}"

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || { echo "ERROR: required command not found: $1" >&2; exit 1; }
}

# Check if we are running from a local clone where kit/scripts/install.sh exists
SCRIPT_DIR=""
if [[ "${BASH_SOURCE[0]:-}" != "" && -f "${BASH_SOURCE[0]}" ]]; then
  SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
fi

if [[ -n "$SCRIPT_DIR" && -f "$SCRIPT_DIR/../kit/scripts/install.sh" ]]; then
  # Local execution
  exec "$SCRIPT_DIR/../kit/scripts/install.sh" "$@"
fi

# Curl-piped execution or fallback cloning path
require_cmd git
require_cmd mktemp

SOURCE_TEMP="$(mktemp -d)"
trap 'rm -rf "$SOURCE_TEMP"' EXIT

# Detect if --version was requested to clone the specific tag
PIN_VERSION=""
ARGS=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --version)
      if [[ $# -gt 1 ]]; then
        PIN_VERSION="$2"
        ARGS+=("$1" "$2")
        shift 2
      else
        echo "ERROR: --version requires an argument" >&2
        exit 1
      fi
      ;;
    *)
      ARGS+=("$1")
      shift
      ;;
  esac
done

echo "Cloning CoreZero Nexus to temp directory..."
if [[ -n "$PIN_VERSION" ]]; then
  git clone --depth 1 --branch "v$PIN_VERSION" "$REPO_URL" "$SOURCE_TEMP" >/dev/null 2>&1 \
    || { echo "ERROR: could not clone $REPO_URL at tag v$PIN_VERSION" >&2; exit 1; }
else
  git clone --depth 1 "$REPO_URL" "$SOURCE_TEMP" >/dev/null 2>&1 \
    || { echo "ERROR: could not clone $REPO_URL" >&2; exit 1; }
fi

# Execute the actual installer from the cloned kit directory
bash "$SOURCE_TEMP/kit/scripts/install.sh" "${ARGS[@]}"
