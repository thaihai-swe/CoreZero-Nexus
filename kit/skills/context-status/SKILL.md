---
name: context-status
description: Orchestrate and report on the status of all active features. This meta-skill acts as a project manager, providing a high-level view of progress, blockers, and next steps across the repository.
compatibility: Designed for Claude, Codex, and other Agent Skills-compatible tools working in spec-driven repositories that use artifacts/features/.

---

# Kit Status



## Overview

Use this skill to get a bird's-eye view of the repository's active work.
This is a helper/orchestration skill, not part of the default single-feature delivery path.

It handles:
1. **Repository Health:** Scanning all `artifacts/features/` for `status.md` files.
2. **Progress Reporting:** Summarizing the current phase of every active feature.
3. **Delivery Profile Reporting:** Calling out whether the feature is moving as Tiny, Standard, or Complex work when status records it.
4. **Blocker Identification:** Highlighting any active blockers or open questions.
5. **Next-Step Guidance:** Recommending the exact public command to move each feature forward.

## Read First

- `artifacts/features/**/status.md`
- `references/status-report-template.md`
- `memories/repo/harness-config.md` (to resolve the canonical `artifacts/features/` path)

## When to Use

- Start a new session to see where things left off.
- Get a summary of all active work for a status update.
- Identify which features are blocked and why.
- Use it when multiple active features make `/context-session` too narrow.

## Workflow

1. **Discovery:** Find all directories in `artifacts/features/`.
2. **Parsing:** Read the `status.md` (and `handoff.md` if relevant) in each directory.
3. **Synthesis**: Create a summary table showing:
   - Feature Slug
   - Current Phase
   - Delivery Profile
   - Last Updated
   - Blockers (Yes/No)
   **Stale detection**: If a feature's `status.md` has a `Last Updated` field older than 7 days and no session checkpoint exists in `progress.md` within that period, flag the feature as `[STALE — no activity]` in the summary table. Do not suppress stale features from the report.
4. **Detailing:** For each feature, provide a 1-line summary of the "Next Step" using the public slash-command format (e.g., `/spec-plan`, `/harness-verify`), reading the current phase from its `status.md` to determine the correct command.
5. **Guidance:** If a feature is missing a `status.md`, recommend running `/spec-requirements` (or the appropriate initialization skill) to fix the process drift.
6. **Dashboard Generation**: Before running `python3 scripts/generate-dashboard.py`, verify the script exists at `scripts/generate-dashboard.py` and Python 3 is available. If the script is missing: produce the text-only summary report (Steps 1–5) and add a warning: "[dashboard generation skipped — scripts/generate-dashboard.py not found]". Do not fail the entire skill for a missing dashboard script. If the script exists, execute it to compile the visual interactive status report at `docs/generated/dashboard.html`.

## Stop Conditions

- No feature directories found in `artifacts/features/` → stop. Report: "No active features found. Run `/spec-requirements` to start a feature."
- `artifacts/features/` directory is inaccessible or unreadable → stop. Report the access error; do not produce a partial scan.
- A `status.md` file exists but is malformed (missing `## Current Phase` section) → skip that feature in the summary table and flag it: "[MALFORMED status.md — run /spec-requirements to repair]".

## Core Rules

- **Process First:** Call out features that are drifting from the SDD workflow.
- **Actionable:** Every feature summary must include a recommended next command.
- **Adaptive Visibility:** Report the delivery profile when the feature artifacts declare one.
- **Concise:** Keep the high-level report brief; only go into detail when blockers are present.

## Rationalization vs. Reality

| Rationalization | Reality |
|---|---|
| "Updating status is just busywork." | Status is the 'pulse' of the project. It ensures everyone (human or AI) knows exactly where we are. |
| "I'll update it at the end of the day." | Stale status leads to duplicated work and misaligned expectations. |
| "The user can see what I'm doing from the logs." | Logs are too granular. `status.md` provides the high-level narrative progress. |

## Red Flags

- Feature directories exist without a `status.md`.
- Features are marked `Done` but missing verification evidence.
- The "Next Step" command is missing or logically incorrect for the current phase.

## Verification

Before finalizing the report, verify:
- All active feature folders were scanned.
- The "Next Step" commands are syntactically correct (e.g., `/spec-plan`).
- Blockers are clearly highlighted.
- Visual dashboard was generated at `docs/generated/dashboard.html`.

## Output Rules

- Produce a summary report in the chat using `references/status-report-template.md` format.
- Include: summary table, phase/profile definitions, blockers (if any), next-step guidance.
- Update the visual dashboard file: `docs/generated/dashboard.html`.
- Do not modify other files.
