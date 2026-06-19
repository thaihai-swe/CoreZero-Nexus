---
name: context-session
description: Manage session start, checkpoint, and end handoffs for an existing feature.
compatibility: Designed for AI coding agents.
---

# Context Session

## Overview
Used to resume, checkpoint, or close work for an existing feature slug. This skill is for session boundaries after `artifacts/features/<slug>/status.md` exists; new feature intake starts with `/spec-requirements` or `/spec-research`.

## Modes

| Mode | Use When | Primary Outputs |
|---|---|---|
| `START` | Resuming an existing feature session. | Readiness summary with loaded context, current phase, next task, blockers. |
| `CHECKPOINT` | Pausing after a completed skill, major edit wave, or meaningful progress. | Updated `progress.md`, claim/status notes, and next-step summary. |
| `END` | Closing a long session or preparing a handoff to a future session. | `handoff.md`, updated `progress.md`, and candidate `session-extracts.md` entries when durable lessons exist. |

`END` is required for long sessions because chat history is volatile. It is not the only mode.

## I/O Hand-off Protocol
- **Reads**: `AGENTS.md`, `MASTER_INDEX.md`, feature `status.md`, `progress.md`, optional `handoff.md`, optional `claim.md`, and routed memory files.
- **Writes**: feature `progress.md`, `handoff.md`, optional `session-extracts.md`, optional `claim.md` status updates, and telemetry pruning updates when required.

## Workflow
1. **Resolve Mode**: If the user did not specify `START`, `CHECKPOINT`, or `END`, infer the mode from the request and state it before proceeding.
2. **Load Routed Context**: Follow `references/session-start-flow.md` and `references/context-assembly.md` for `START` and any mode that needs fresh context.
3. **Respect Claims**: Follow `references/multi-agent-protocol.md` before taking or releasing ownership of a feature slug.
4. **Record Progress**: Use `references/progress-template.md` for checkpoint and end summaries.
5. **Create Handoff On End**: Use `references/session-handoff-template.md` and append candidate extracts using `references/session-extracts-template.md` when durable lessons exist.
6. **Prune Telemetry**: If ending a session or if `memories/repo/harness-telemetry.md` exceeds 500 lines, compress older closed tasks and log entries into a summarized historical record while keeping the active state verbose.
