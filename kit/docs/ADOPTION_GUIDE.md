# Adoption Guide

This guide explains how a downstream project adopts the shipped template surface and starts using the public CoreZero Nexus workflow.

Use [INSTALL.md](../../documents/INSTALL.md) in the source repository for installer mechanics. Use this guide for the actual adoption flow.

## What The Installer Adds

The default install surface includes:

- `docs/*` as adopter-owned templates
- `docs/architecture.md`
- `docs/generated/*`
- `memories/repo/*`
- root bootstrap files such as `AGENTS.md` and `HARNESS_CARD.md`
- `skills/**`, `rules/*.md`, `scripts/install.sh`, and `.github/workflows/harness-check.yml`

Maintainer docs in `documents/` stay in the source repository and are not installed by default.

## Greenfield Adoption

Use this when the target repo is new or near-empty.

### Step 1: Install

```bash
curl -fsSL https://raw.githubusercontent.com/thaihai-swe/AI-agents-dev-kits/main/scripts/install.sh \
  | bash -s -- /path/to/your/project
```

### Step 2: Run Project Starter

```text
/starter-init
```

This establishes the runtime router, durable memory baselines, architecture entrypoint, and the installed template surface.

### Step 3: Open a Session and Load Context

```text
/context-session
```

This opens the working session and loads the memory router. Every feature delivery should start with a session open and end with a session end + handoff. Sessions track phase, progress, and provide resumable state across context resets — see [documents/context-engineering.md](../documents/context-engineering.md) for the full model.

### Step 4: Deliver The First Feature

```text
/spec-requirements
/spec-plan
/spec-implement
/harness-verify
```

## Brownfield Adoption

Use this when the target repo already has real code, tests, or history.

### Step 1: Install

```bash
curl -fsSL https://raw.githubusercontent.com/thaihai-swe/AI-agents-dev-kits/main/scripts/install.sh \
  | bash -s -- /path/to/your/project
```

### Step 2: Bootstrap

```text
/starter-init
```

In brownfield repos, this establishes the baseline without pretending the project is clean or empty.

### Step 3: Investigate Before Changing

```text
/spec-research
```

This should map current behavior, fragile seams, and preserved behavior before feature work starts.

### Step 3: Capture Durable Context

```text
/context-memory
/context-session
```

This folds reusable findings into the durable context surfaces before implementation starts.

### Step 4: Deliver The Smallest Safe Feature

```text
/spec-requirements
/spec-plan
/spec-implement
/harness-verify
```

## Command Reference

Full public command list: [documents/skills-guide.md](../documents/skills-guide.md)

## Starter Surface

The most important files to review after install are:

- [PRODUCT_SENSE.md](PRODUCT_SENSE.md)
- [GLOSSARY.md](GLOSSARY.md)
- [TECH_STACK_REFERENCE.md](TECH_STACK_REFERENCE.md)
- [PROJECT_CONSTRAINTS.md](PROJECT_CONSTRAINTS.md)
- [architecture.md](architecture.md)
- [code-design.md](code-design.md)

## Practical Adoption Advice

- Start with `/starter-init` before manually curating every file.
- Use `/spec-research` first in brownfield systems instead of guessing how the existing code behaves.
- Keep `docs/code-design.md` visible to adopters because it is part of the shipped policy surface, not an internal kit note.
- Treat `docs/` as the downstream project’s source of truth once installed.
- For a complete lifecycle walkthrough of the kit in action, see [documents/end-to-end-tutorial.md](../documents/end-to-end-tutorial.md).

## Troubleshooting

### `/starter-init` failed midway or produced incomplete output
Re-run `/starter-init`. The install is idempotent — it will not overwrite files it already created correctly. Review `HARNESS_CARD.md` after the run to confirm all subsystems show a baseline score.

### Repository is in a broken or inconsistent harness state
Run `/harness-maintain assess` to get a scored subsystem report. This identifies exactly which of the 6 harness subsystems are deficient. Then run `/harness-maintain improve` to generate a repair proposal for the failing subsystems.

### Memory files are out of date or contain placeholders
Run `/context-memory` to triage and refresh. For a full post-feature sweep, run it after `/harness-verify` passes.

### Installer dry-run shows unexpected files in overwrite list
Run the installer with `--dry-run` to preview all operations before committing:

```bash
bash scripts/install.sh /path/to/your/project --dry-run
```

### Upgrading from a previous version
Re-run the installer. Kit-managed files in the `overwrite` category will be backed up to `.corezero-backup-<timestamp>/` before replacement. User-owned files (`memories/repo/`, `artifacts/`) are never overwritten.
