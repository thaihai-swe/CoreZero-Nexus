# Memory Router

> Always-loaded routing index for `memories/repo/`. Keep under 80 lines.
> Sessions read this first, then load only the groups that match the task.

## How To Use This Index

1. Files in the **Always** group load on every session start.
2. Files in the **By Intent** groups load only when their trigger keywords match the active task.
3. Files in the **By Debug** group load only when debugging, retro, or post-mortem work begins.
4. If a file outgrows its slot (>800 lines, 3+ distinct subtopics, or 5+ artifacts reference one slice), open a promotion proposal under `artifacts/features/<slug>/promotions.md`.

## Always (load every session)

- `constitution.md` — repo-wide normative rules (CC-* identifiers).
- `harness-config.md` — canonical commands, paths, rigor defaults.
- `security-policy.md` — permission tiers, trust boundaries, secret handling.

## By Intent — Knowledge

Trigger keywords: `architecture`, `pattern`, `convention`, `stack`, `module`, `api surface`, `domain`, `glossary`, `terminology`, `bootstrap`, `skill`, `template`, `adr`, `decision`, `decision record`.

- `project-knowledge-base.md` — durable patterns, watchouts, project continuity facts.
- `domain-specs.md` — ubiquitous language, domain rules, bounded-context terms.
- `adr-log.md` — index of architecture decisions; load when the task touches prior decisions, requires a new ADR, or affects architectural tradeoffs.
- `docs/architecture.md` — durable system structure, boundaries, integration seams.
- `docs/generated/codemap.md` — generated map of code locations.
- `docs/generated/references-index.md` — generated index of cross-file references.

## By Intent — Learned

Trigger keywords: `heuristic`, `instinct`, `recurring`, `lesson`, `we always`, `we never`, `last time`.

- `learned-heuristics.md` — evidence-backed instincts that improve future execution.

## By Debug (load on debug, retro, or failure)

Trigger keywords: `debug`, `failure`, `regression`, `incident`, `retro`, `flaky`, `why did`, `root cause`.

- `observability-log.md` — auto-tier failure log written by `harness-maintain` and `harness-verify`.
- `artifacts/features/<slug>/session-extracts.md` — per-feature distillation, candidate-only until triaged.

## Promotion Watchlist

Files approaching promotion thresholds. Empty when no file is near a limit.

- _none_

## Maintenance

- This file is updated by `context-memory` when groups are added, files are promoted, or trigger keywords drift.
- `context-session` reads this on start. `harness-verify` reads this during the post-ship sync gate.
- Do not list feature artifacts here. Feature state belongs under `artifacts/features/<slug>/`.
