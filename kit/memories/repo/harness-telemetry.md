# Harness Telemetry (State & Logs)

## Index

- **Current State** — owned by context-status; phase, active task, profile
- **Observability Log** — auto-tier failure ledger owned by harness-verify and harness-maintain
- **Trend Summary** — counts by classification (harness/model/spec), promotion queue
- **Entry Schema** — OBS-NNN format with required YAML fields
- **Entries** — append-only log of discrete failures
- **Retired Entries** — failures promoted into instruction-tier memory

## Current State

Owned by `/context-status`. Updated when feature status changes.

- **Phase**: None
- **Active Task**: None
- **Profile**: Standard


# Observability Log

Auto-tier memory. Structured failure ledger for harness, model, and spec failures.
Owned by `harness-verify` (writes entries via `telemetry-collector.sh`) and `harness-maintain` (triages and promotes).

## Trend Summary

> Updated by the shipped governance bundle. `harness-maintain` Improve Mode updates this summary after each triage run.

| Classification | Last 10 entries | Open | Promoted | Retired |
|---|---|---|---|---|
| harness | 0 | 0 | 0 | 0 |
| model | 0 | 0 | 0 | 0 |
| spec | 0 | 0 | 0 | 0 |

**Promotion queue** (entries where `promotion_candidate: true` and status is `open`):
- _none_

## How To Use This File

- One entry per discrete failure or near-miss. Do not batch unrelated observations.
- Append entries in `OBS-NNN` order. Newest at the bottom.
- Every entry is a fenced `yaml` block.
- `harness-maintain` Improve Mode updates `## Trend Summary` after each triage run.
- `harness-verify` (writes entries via `telemetry-collector.sh`) and `harness-maintain` (triages via Improve Mode) are the governance owners of the `# Observability Log` and its entries.
- `/context-status` owns the `## Current State` section only.
- For promotion, route to `/context-memory` Post-Ship Sync.

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

<!-- Entries promoted into instruction-tier memory. -->
