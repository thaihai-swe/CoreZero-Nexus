---
id: skill-context-status
name: context-status
description: "Orchestrate and report on the status of all active features. This meta-skill acts as a project manager, providing a high-level view of progress, blockers, and next steps across the repository."
tags: ['context', 'status', 'report']
triggers: ['status', 'report', 'overview', 'progress']
next_skill: 'harness-maintain'

---
# Context Status

## Overview
Aggregates status across all active feature branches, updates the repo-wide status dashboard, and synchronizes the active task phase.

## I/O Hand-off Protocol
- Reads: `core-zero/memories/repo/harness-telemetry.md`, `artifacts/features/*/status.md`, `artifacts/features/*/tasks.md`.
- Writes: `core-zero/memories/repo/harness-telemetry.md` `# Current State` section, command line status dashboard.

## Dashboard Formatting Guidance

### Phase Definitions
- Init — Repository bootstrapped, harness initialized
- Researching — Investigating existing behavior or brownfield state
- Spec'ing — Defining requirements and acceptance criteria
- Planning — Designing solution and breaking into tasks
- Implementing — Executing tasks, building code
- Verifying — Running mechanical gate, alignment audit, security check
- Done — Feature complete, verified, ready for merge

### Profile Definitions
- Simple — Small, reversible, low-risk (1–2 hours)
- Moderate — Clear feature or bug-fix (4–8 hours)
- Complex — Ambiguity, cross-boundary, risky (1–2 days)

### Blocker Format
When a feature has blockers, expand the summary table with a "Blockers" section:
```
### Blockers

Feature: `<slug>`
- Blocker: [Description]
- Reason: [Why it's blocked]
- Unblocks: [What happens when resolved]
- Owner: [Who can unblock]
- ETA: [When expected to resolve]
```

### Next-Step Guidance
For each feature, recommend the exact next command:
| Phase | Next Step |
|---|---|
| Init | `/starter-init` |
| Researching | `/spec-research` or `/spec-requirements` |
| Spec'ing | `/spec-requirements` or `/spec-plan` |
| Planning | `/spec-plan` or `/spec-implement` |
| Implementing | `/spec-implement` (specific task ID) or `/harness-verify` |
| Verifying | `/harness-verify` or (Complete) |
| Done | (Archive or start new feature) |

### Example Report
```
# Project Status Report
Generated: 2026-05-29
Scope: All active features in artifacts/features/
Total Features: 3

## Summary

| Feature Slug | Phase | Profile | Last Updated | Blockers | Next Step |
|---|---|---|---|---|---|
| `user-auth` | Done | Moderate | 2026-05-28 | None | (Complete) |
| `oauth-integration` | Implementing | Complex | 2026-05-29 | None | `/spec-implement` Task 6 |
| `password-reset` | Spec'ing | Simple | 2026-05-27 | Waiting on product | `/spec-requirements` (grilling waves) |

## Blockers

Feature: `password-reset`
- Blocker: Product team hasn't decided on email provider (SendGrid vs AWS SES)
- Reason: Affects spec acceptance criteria for email delivery SLA
- Unblocks: Can finalize spec and move to planning
- Owner: Product Manager
- ETA: 2026-05-30

## Recommendations

1. Unblock `password-reset` — Follow up with product on email provider decision
2. Continue `oauth-integration` — On track, no blockers
3. Archive `user-auth` — Complete and verified, ready for merge
```

### Output Rules
- Keep the summary table to one line per feature
- Expand blockers only when they exist
- Always include the exact next public command
- Report is read-only (do not modify feature artifacts)
- Regenerate on each session to reflect current state

## Workflow
1. Load Current State: Read `core-zero/memories/repo/harness-telemetry.md` to load the current global phase and failure counters.
2. Scan Features: Scan all feature subdirectories under `artifacts/features/` and read their respective `status.md` and `tasks.md` files. Identify:
   - Feature slug name.
   - Active phase (`## Current Phase`).
   - Complexity (`## Complexity`).
   - Current active task (`## Active Task`).
   - Blockers or open clarification flags (`## Blockers`).
   - Task completion percentage (from `tasks.md`).
   *Note: If `status.md` does not strictly follow the sections in `skills/_shared/status-template.md`, the dashboard parser will fail. Flag any malformed status files.*
3. Compile Dashboard: Format a text-based status dashboard using `references/status-report-template.md` containing:
   - A list of all active features, their current phase, and active task.
   - Any currently active blocker flags.
   - Current failure logs summary.
4. Update Current State: If the active feature slug or current task phase has changed, write the updated `# Current State` values to `core-zero/memories/repo/harness-telemetry.md`.
5. Regenerate HTML Dashboard: You MUST run `python3 scripts/generate-dashboard.py` to sync status to `core-zero/generated/dashboard.html`.
6. Feature Completion Cleanup (GC): If `status.md` shows `## Current Phase: Done`:
   - Check if `artifacts/features/<slug>/session-extracts.md` has been triaged (look for `<!-- triaged: true -->`).
   - If NOT triaged: emit a warning in your final response — "session-extracts.md for <slug> has not been triaged. Run /context-memory before cleanup." Do NOT delete files.
   - If triaged (or missing): delete `.corezero/sessions/<slug>/progress.md` and `.corezero/sessions/<slug>/handoff.md`. If `.corezero/sessions/<slug>/` is empty, remove the directory.
   - Do NOT delete durable artifacts (`spec.md`, `plan.md`, `status.md`, etc.).
   - Log the cleanup: `bash scripts/harness/telemetry-collector.sh --task system --feature <slug>` with classification "maintenance" and description "Feature completion GC: removed ephemeral artifacts."

## Core Rules
- No Stale Statuses: Always run context-status to sync telemetry state when a feature transitions to a new phase or completes a task.
- Accurate Aggregation: Do not guess feature statuses. If `status.md` is missing for a feature directory, mark its phase as `[UNKNOWN]`.

## Read First

Read this skill thoroughly before invoking it.

## When to Use

Use this skill for its designated purpose within the delivery flow.
