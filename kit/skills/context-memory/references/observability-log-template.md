# Observability Log

Auto-tier memory. Structured failure ledger for harness, model, and spec failures observed during agent execution.

## Trend Summary

> Updated by `harness-maintain` Improve Mode after each triage run.

| Classification | Last 10 entries | Open | Promoted | Retired |
|---|---|---|---|---|
| harness | 0 | 0 | 0 | 0 |
| model | 0 | 0 | 0 | 0 |
| spec | 0 | 0 | 0 | 0 |

**Promotion queue** (entries where `promotion_candidate: true` and status is `open`):
- _none_

## The Harness Governance (GC) Loop

This file acts as the repository's failure ledger, enabling continuous self-repair via a 3-step loop:
1. **Log (Identify)**: When a feature verification fails, or an agent experiences severe friction, the failure is logged here as a structured YAML entry.
2. **Maintain (Repair)**: `/harness-maintain improve` is run to apply a proposed durable fix to a harness subsystem or rules.
3. **Promote (Refine)**: `/context-memory` Post-Ship Sync triages open entries. Lessons promoted to instruction-tier files (`constitution.md`, `security-policy.md`, `learned-heuristics.md`, `project-knowledge-base.md`); entry status updated to `promoted`.

## How To Use This File

- One entry per discrete failure or near-miss. Do not batch unrelated observations.
- Append entries in `OBS-NNN` order (OBS-001, OBS-002, …). Newest at the bottom.
- Every entry is a fenced `yaml` block — machine-parseable, human-readable.
- `harness-maintain` updates `## Trend Summary` after each Improve Mode run.
- Do not use this file for feature-local notes. Those belong in `artifacts/features/<slug>/`.

## Entry Schema

Required fields for every entry:

```yaml
- id: OBS-NNN
  date: YYYY-MM-DD
  classification: harness | model | spec
  severity: low | medium | high | critical
  skill: <skill-name-that-was-active>
  description: "One sentence: what went wrong."
  root_cause: "One sentence: why it happened."
  fix_applied: "What was changed to prevent recurrence. 'none yet' if open."
  recurrence_risk: low | medium | high
  promotion_candidate: true | false
  status: open | promoted | retired
```

**Classification guide:**
- `harness` — The environment allowed or encouraged the mistake (missing gate, bad template, weak rule)
- `model` — The environment was adequate but execution was poor (agent ignored a clear rule)
- `spec` — The artifact contract was underspecified or contradictory

**Severity guide:**
- `low` — Minor friction, no incorrect output
- `medium` — Incorrect output caught by verification gate
- `high` — Incorrect output reached a review artifact; required rework
- `critical` — Incorrect output reached production or caused data loss

## Entries

<!-- Append new entries below in OBS-001, OBS-002, ... order. -->

## Retired Entries

<!-- When an entry has been promoted into instruction memory and the lesson is durable,
     move it here with status: retired and a one-line note of the destination file. -->
