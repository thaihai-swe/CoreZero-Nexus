---
name: context-status
description: Orchestrate and report on the status of all active features. This meta-skill acts as a project manager, providing a high-level view of progress, blockers, and next steps across the repository.

---

# Context Status

## Overview
Aggregates status across all active feature branches, updates the repo-wide status dashboard, and synchronizes the active task phase.

## I/O Hand-off Protocol
- **Reads**: `memories/repo/harness-telemetry.md`, `artifacts/features/*/status.md`.
- **Writes**: `memories/repo/harness-telemetry.md` `# Current State` section, command line status dashboard.

## Workflow
1. **Load Current State**: Read `memories/repo/harness-telemetry.md` to load the current global phase and failure counters.
2. **Scan Features**: Scan all feature subdirectories under `artifacts/features/` and read their respective `status.md` files. Identify:
   - Feature slug name.
   - Active phase (Spec'ing, Planning, Implementing, Verifying, Done).
   - Current active task ID.
   - Blockers or open clarification flags.
3. **Compile Dashboard**: Format a text-based status dashboard using `references/status-report-template.md` containing:
   - A list of all active features, their current phase, and active task.
   - Any currently active blocker flags.
   - Current failure logs summary.
4. **Update Current State**: If the active feature slug or current task phase has changed, write the updated `# Current State` values to `memories/repo/harness-telemetry.md`.
5. **Regenerate HTML Dashboard**: You MUST run `python3 scripts/generate-dashboard.py` to sync status to `docs/generated/dashboard.html`.

## Core Rules
- **No Stale Statuses**: Always run context-status to sync telemetry state when a feature transitions to a new phase or completes a task.
- **Accurate Aggregation**: Do not guess feature statuses. If `status.md` is missing for a feature directory, mark its phase as `[UNKNOWN]`.
