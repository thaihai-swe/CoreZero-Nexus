# Install CoreZero Nexus

CoreZero Nexus installs one adopter-facing package surface for downstream teams.

## Requirements

- `bash`
- `python3`
- `git` when using the curl-piped path
- standard POSIX tools such as `cp`, `find`, and `sed`

## Quick Install

```bash
curl -fsSL https://raw.githubusercontent.com/thaihai-swe/CoreZero-Nexus/main/scripts/install.sh \
  | bash -s -- /path/to/your-project
```

## Pinned Version

```bash
curl -fsSL https://raw.githubusercontent.com/thaihai-swe/CoreZero-Nexus/v0.1.2/scripts/install.sh \
  | bash -s -- /path/to/your-project --version 0.1.2
```

## Auditable Install

```bash
git clone --depth 1 https://github.com/thaihai-swe/CoreZero-Nexus.git
bash CoreZero-Nexus/scripts/install.sh /path/to/your-project
```

## What Gets Installed

The installer applies three categories:

- `overwrite` for kit-managed docs, scripts, rules, skills, and shipped checks
- `copyIfMissing` for bootstrap files, memories, adopter-owned docs, architecture, and generated references
- `preserve` for downstream state such as `memories/repo/` content, `artifacts/`, and local settings

The adopted project receives:

- adopter-facing docs under `docs/`
- adopter-owned project-policy docs under `docs/*.md`
- generated references under `docs/generated/`
- runtime and memory scaffolding in the repo root and `memories/repo/`
- public skills, rules, installer, and the harness consistency workflow

For a detailed breakdown of file mappings and ownership rules, see [TEMPLATE_SURFACE.md](TEMPLATE_SURFACE.md#file-categories--installation-posture).

Maintainer docs under `documents/` remain in this source repository only. They are not part of the default installed surface.

## Upgrade Behavior

Re-running the installer:

1. reads `.corezero-version`
2. backs up kit-managed files
3. refreshes shipped surfaces
4. leaves adopter-owned state in place
5. writes the new version stamp

## Next Steps

After install, follow [ADOPTION_GUIDE.md](../kit/docs/ADOPTION_GUIDE.md) for the full adoption flow.

## Rollback

The installer backs up all overwritten files to `.corezero-backup-<timestamp>/` before replacing them. To revert:

```bash
# Restore specific files from the most recent backup
cp .corezero-backup-<timestamp>/path/to/file path/to/file

# Or remove the entire installed surface manually
rm -rf skills/ rules/ scripts/ docs/ .github/workflows/harness-check.yml AGENTS.md HARNESS_CARD.md .corezero-version
```

User-owned files (`memories/repo/`, `artifacts/`) are never overwritten by the installer and do not need restoring.
