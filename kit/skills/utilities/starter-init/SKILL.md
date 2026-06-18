---
name: starter-init
description: Initialize the kit structure in a new repository.
compatibility: Designed for AI coding agents.
---

# Starter Init

## Overview
Bootstraps the `docs/` and `memories/` directories with standard templates.

## I/O Hand-off Protocol
- **Writes**: Generates `docs/` and `memories/` folders and baseline markdown files.

## Workflow
1. Ensure `docs/project`, `docs/generated`, and `memories/repo` exist.
2. Populate `docs/project/requirements.md`, `memories/repo/harness-telemetry.md`, `docs/generated/plan.md`, `docs/generated/tasks.md` with default structure.
3. Inform the user the kit is ready.
