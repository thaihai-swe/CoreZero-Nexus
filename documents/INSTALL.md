# Install CoreZero Nexus

CoreZero Nexus installs one adopter-facing package surface for downstream teams.

## Requirements

- `bash`
- `python3`
- `git` when using the curl-piped path
- standard POSIX tools such as `cp`, `find`, and `sed`

## Quick Install

```bash
curl -fsSL https://raw.githubusercontent.com/thaihai-swe/AI-agents-dev-kits/main/scripts/install.sh \
  | bash -s -- /path/to/your-project
```

## Pinned Version

```bash
curl -fsSL https://raw.githubusercontent.com/thaihai-swe/AI-agents-dev-kits/v0.2.0/scripts/install.sh \
  | bash -s -- /path/to/your-project --version 0.2.0
```

## Auditable Install

```bash
git clone --depth 1 https://github.com/thaihai-swe/AI-agents-dev-kits.git
bash AI-agents-dev-kits/scripts/install.sh /path/to/your-project
```

## What Gets Installed

The installer applies three categories:

- `overwrite` for kit-managed docs, scripts, rules, skills, and shipped checks
- `copyIfMissing` for bootstrap files, memories, templates, architecture, and generated references
- `preserve` for downstream state such as `memories/repo/` content, `artifacts/`, and local settings

The adopted project receives:

- adopter-facing docs under `docs/`
- project templates under `docs/templates/`
- generated references under `docs/generated/`
- runtime and memory scaffolding in the repo root and `memories/repo/`
- public skills, rules, installer, and the harness consistency workflow

For a detailed breakdown of file mappings and ownership rules, see [TEMPLATE_SURFACE.md](../../documents/TEMPLATE_SURFACE.md#file-categories--installation-posture) in the CoreZero Nexus source repository.

Maintainer docs under `documents/` remain in this source repository only. They are not part of the default installed surface.

## Upgrade Behavior

Re-running the installer:

1. reads `.corezero-version`
2. backs up kit-managed files
3. refreshes shipped surfaces
4. leaves adopter-owned state in place
5. writes the new version stamp

## Next Steps

After install, follow [ADOPTION_GUIDE.md](ADOPTION_GUIDE.md) for the full adoption flow.

## Rollback

The installer backs up all overwritten files to `.corezero-backup-<timestamp>/` before replacing them. To revert:

```bash
# Restore specific files from the most recent backup
cp .corezero-backup-<timestamp>/path/to/file path/to/file

# Or remove the entire installed surface manually
rm -rf skills/ rules/ scripts/ docs/ .github/workflows/harness-check.yml AGENTS.md HARNESS_CARD.md .corezero-version
```

User-owned files (`memories/repo/`, `artifacts/`) are never overwritten by the installer and do not need restoring.
