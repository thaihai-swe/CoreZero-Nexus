# Observability Log

Auto-tier memory. Append-only record of harness, model, and spec failures observed during agent execution. `harness-maintain Improve Mode` writes here when a failure surfaces a lesson worth outliving the current feature. `context-memory` triages entries for promotion into instruction-tier files (constitution, security-policy, learned-heuristics, project-knowledge-base) or for retirement once the underlying issue is fixed.

## How To Use This File

- One entry per discrete failure or near-miss. Do not batch unrelated observations.
- Classify every entry as **Harness**, **Model**, or **Spec** problem before writing the fix proposal.
- Keep entries terse. Link to the source artifact (review, session log, or commit) instead of re-narrating it.
- Mark each entry's status: `open`, `promoted`, or `retired`. `context-memory` updates this field during triage.
- Do not use this file for feature-local notes. Those belong in `artifacts/features/<slug>/`.

## Entry Template

```
### OBS-<NNN> — <one-line summary>

- Date: YYYY-MM-DD
- Source: <path/to/review.md, handoff.md, or commit hash>
- Class: Harness | Model | Spec
- Status: open | promoted | retired
- Promotion target: <constitution.md | security-policy.md | learned-heuristics.md | project-knowledge-base.md | none>

**What happened**
<2-4 sentences describing the failure mode. Cite evidence.>

**Why it matters**
<Why this would recur without a durable fix.>

**Proposed durable fix**
<Concrete change to a memory file, skill, gate, or rule. Not a session note.>

**Triage notes**
<context-memory's promotion decision and rationale, if processed.>
```

## Entries

<!-- Append new entries below in OBS-001, OBS-002, ... order. Newest at the bottom. -->

## Retired Entries

<!-- When an entry has been promoted into instruction memory and the lesson is durable, move it here with a one-line summary and the destination file. -->
