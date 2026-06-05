---
name: context-session
description: Manage the session lifecycle (start, checkpoint, end) to maintain context continuity, assemble context deliberately, budget context windows, and generate durable handoffs.
compatibility: Designed for Claude, Codex, and other Agent Skills-compatible tools working in spec-driven repositories that use memories/repo/ and artifacts/features/<slug>/.

---

# Kit Session



## Overview

Governs active feature session continuity after a feature slug already exists. It ensures clean resume, progress logging, context pruning, and clear delegation/handoff to the next session window.

## Read First

- `memories/repo/INDEX.md` (memory router)
- `memories/repo/constitution.md` and `memories/repo/harness-config.md`
- `artifacts/features/<slug>/status.md`
- Resuming files: `handoff.md` and `progress.md` (if they exist)
- References: `references/context-assembly.md`, `references/session-start-flow.md`, `references/session-handoff-template.md`, and `references/context-condensation.md`.

## When to Use

- **Start**: Begin a new conversation window and resume feature work.
- **Checkpoint**: Save progress mid-session and prune context.
- **End**: Conclude the session, document state, and write handoff notes.
- Use it only after `/spec-requirements` or `/spec-research` has created the feature slug and `status.md`.

## Workflow

### Session Start
1. **Slug Check**: If multiple features exist, run `/context-status` first to select the active slug.
2. **Claim Check**: Before loading context, check `artifacts/features/<slug>/claim.md`. If an active (non-expired) claim exists from another agent, stop and report `BLOCKED`. If no claim exists or the claim is stale, create/update `claim.md` to establish ownership. See [references/multi-agent-protocol.md](references/multi-agent-protocol.md).
3. **Context Load**: Load minimum required context per `references/context-assembly.md` and `references/session-start-flow.md`. When reading `INDEX.md`, strictly obey the **Confidence-Scored Loading** rule: if ≤2 keywords match a group, perform a **partial-load** (load only the index/header file for that group). Only load the full group for high-confidence matches (3+ keywords).
4. **Resumption**: Identify current phase, next task/artifact, and blockers.
5. **Report & Log**: Update `progress.md` with resumption details and name the exact next core command.

### Session Checkpoint
1. Review completed tasks. Append a snapshot to `progress.md`.
2. Check context budget. If crowded, run condensation/eviction per `references/context-condensation.md`. Prune raw logs and broad searches.

### Session End
1. Summarize completion state, proof status, and blockers.
2. **Delegation**: Document Conversation ID, role, and branch URIs for active subagents.
3. **Log & Extract**: Append end entry to `progress.md`. (Optional: Distill reusable lessons into `artifacts/features/<slug>/session-extracts.md`).
4. **Handoff**: Write `handoff.md` using `references/session-handoff-template.md`, ending with the next core command.
5. **Release Claim**: Update `claim.md` status to `Released` with release notes. This is mandatory — do not skip.

## Stop Conditions

- `starter-init` has not been run (no `AGENTS.md` or `harness-config.md` present).
- No feature slug is selected or `artifacts/features/<slug>/status.md` does not exist yet. In plain terms: status.md does not exist yet for this feature. Route to `/spec-requirements` when requirements can be defined directly, or `/spec-research` when brownfield behavior or root cause is unknown.

## Preconditions

- **Required files**: `AGENTS.md`, `memories/repo/harness-config.md`, `memories/repo/constitution.md`.
- **Required feature state**: Existing `artifacts/features/<slug>/status.md` created by `/spec-requirements` or `/spec-research`.
- **Phase sets**: Manages lifecycle across existing feature phases.

## Core Rules

- **No Amnesia**: The progress log is the system of record. Update it mid-session and on end.
- **Session Honesty**: Never hide a broken build or failing test in handoffs.
- **Tiered Assembly**: Read `INDEX.md` first, load only by-intent groups relevant to the active task.
- **Evict Stale Context**: Prune old logs/files once analyzed. Keep context window lean.

## Rationalization vs. Reality

| Rationalization | Reality |
|---|---|
| "I'll read chat history to resume." | Chat history gets truncated. `progress.md` is the system of record. |
| "I don't need checkpoints." | Long sessions lose coherence. Checkpoint frequently. |
| "Load design.md and plan.md in full." | Load only sections relevant to the immediate task. |
| "Handoff means feature is done." | Handoff means session is resumable. Verification owns done verdict. |

## Red Flags

- Starting session without reading `constitution.md`, `harness-config.md`, or `handoff.md`.
- Context condensation is ignored, carrying raw logs into implementation.
- Handoff implies completion without referencing tests or gate evidence.

## Verification

- [ ] Current phase, next task, and next core command explicitly named.
- [ ] Loaded context tiers match the active task.
- [ ] Progress log and handoff logs generated.

## Output Rules

- Can create/update: `progress.md`, `status.md`, `handoff.md`, `claim.md`, and `session-extracts.md` (only if reusable lessons exist).
- Cannot modify instruction memory files directly (candidates go to `session-extracts.md`).

## References

- [references/context-assembly.md](references/context-assembly.md)
- [references/session-start-flow.md](references/session-start-flow.md)
- [references/session-handoff-template.md](references/session-handoff-template.md)
- [references/progress-template.md](references/progress-template.md)
- [references/context-condensation.md](references/context-condensation.md)
- [references/multi-agent-protocol.md](references/multi-agent-protocol.md)
