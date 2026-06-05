# Install

CoreZero Nexus installs one adopter-facing workflow surface into your project.

## Requirements

- `bash`
- `python3`
- `git` when using the curl-piped path
- standard shell tools such as `cp`, `find`, and `sed`

## Quick Install

```bash
curl -fsSL https://raw.githubusercontent.com/thaihai-swe/CoreZero-Nexus/main/scripts/install.sh \
  | bash -s -- /path/to/your-project
```

## Auditable Install

```bash
git clone --depth 1 https://github.com/thaihai-swe/CoreZero-Nexus.git
bash CoreZero-Nexus/scripts/install.sh /path/to/your-project
```

## Installed Surface

The installer writes four kinds of content:

- Kit-managed content refreshed on upgrade: `skills/`, `rules/`, `scripts/`, selected docs, and `.github/workflows/harness-check.yml`
- Seeded content copied only when missing: `AGENTS.md`, `HARNESS_CARD.md`, `memories/repo/*`, `docs/architecture.md`, and the project-policy docs under `docs/`
- Generated references seeded from templates: `docs/generated/codemap.md`, `docs/generated/references-index.md`
- Preserved adopter state: `artifacts/`, `memories/repo/`, and `.corezero-version`

For the exact file map, see `manifest.json` in the source repository and `documents/TEMPLATE_SURFACE.md`.

## Verification

After install:

1. Read `docs/ADOPTION_GUIDE.md`
2. Run `/starter-init`
3. Run `/context-session`
4. Run `bash scripts/doctor.sh` if the surface looks incomplete or drifted

## Upgrade Behavior

Re-running the installer:

1. reads `.corezero-version`
2. backs up kit-managed files
3. refreshes the installed surface
4. preserves adopter-owned files
5. writes the new version stamp

## Rollback

The installer backs up overwritten files to `.corezero-backup-<timestamp>/`.
Restore specific files from that backup if you need to revert a kit-managed change.
