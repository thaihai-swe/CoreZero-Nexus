---
name: harness-maintain
description: Maintain harness configuration and update system indexes.
compatibility: Designed for AI coding agents.
---

# Harness Maintain

## Overview
Regenerate project maps, audit installation integrity, or evaluate harness logic updates.

## I/O Hand-off Protocol
- **Reads**: Entire codebase, `kit/manifest.json`, `kit/memories/repo/core-policies.md`.
- **Writes**: `docs/project/codemap.md`, `docs/generated/dashboard.html`.

## Modes

| Mode | Trigger | Focus |
|---|---|---|
| **Codemap** | default | Regenerates codemaps and triggers dashboard refresh. |
| **Audit** | `--audit` | Compares manifest JSON with the actual kit folder tree to catch drift. |
| **Eval** | `--eval` | Runs validation checking that core policies (CC-*) and scripts are intact. |

## Workflow

### Codemap Mode (Default)
1. Walk the repository directory structure to compile a structured file map of core files.
2. Overwrite `docs/project/codemap.md` with the updated hierarchy.
3. Call `python3 scripts/generate-dashboard.py` to regenerate the HTML dashboard at `docs/generated/dashboard.html`.

### Audit Mode (`--audit`)
1. Read `manifest.json` and extract the expected files list.
2. Crawl the local directory tree under `kit/`. Compare the discovered files with the `overwrite` and `copyIfMissing` files listed in the manifest.
3. Report any untracked, missing, or misclassified files as a validation audit failure.
4. Verify all reference links inside `skills/**/*.md` point to existing files.

### Eval Mode (`--eval`)
1. Required before shipping updates to the verification harness or core policy files.
2. Verify all `CC-*` identifiers defined in `memories/repo/core-policies.md` are present and mapped.
3. Run `gate-runner.sh` and capture output to verify stack detection exits code `1` on unknown stacks.
4. Verify `telemetry-collector.sh` correctly appends YAML-formatted telemetry log entries.

## Core Rules
- **No Manual Codemaps**: Never edit `docs/project/codemap.md` by hand; always regenerate it programmatically.
- **Audit Before Ship**: Every package release requires running Audit mode to ensure manifest consistency.
