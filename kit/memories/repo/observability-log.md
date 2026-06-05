# Observability Log

Auto-tier memory. Structured failure ledger for harness, model, and spec failures.
See `skills/context-memory/references/observability-log-template.md` for the entry schema.

## Trend Summary

> Updated by `harness-maintain` Improve Mode after each triage run.

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
- For promotion, route to `/context-memory` Post-Ship Sync.

## Entries

<!-- Append new entries below in OBS-001, OBS-002, ... order. -->

## Retired Entries

<!-- Entries promoted into instruction-tier memory. -->
