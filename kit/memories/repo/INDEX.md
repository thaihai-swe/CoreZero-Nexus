# Memory Router

> Always-loaded routing index for `memories/repo/`. Keep under 120 lines.
> Sessions read this first, then load only the groups that match the task.

## How To Use This Index

1. Files in the **Always** group load on every session start.
2. Files in the **By Intent** groups load only when their trigger keywords match the active task.
   - **Confidence-Scored Loading:** If the active task triggers ≤2 keywords from a group (low confidence), perform a **partial-load**: load ONLY the top-level index file or the summary header for that group instead of all files. Only load the full group for high-confidence matches (3+ keywords).
3. Files in the **By Debug** group load only when debugging, retro, or post-mortem work begins.
4. The **Phase × Lane Matrix** below tells you what to add (and what to stop reading) once the active rigor profile is known.
5. If a file outgrows its slot (>800 lines, 3+ distinct subtopics, or 5+ artifacts reference one slice), open a promotion proposal under `artifacts/features/<slug>/promotions.md`.

## Always (load every session)

- `constitution.md` — repo-wide normative rules (CC-* identifiers).
- `harness-config.md` — canonical commands, paths, rigor defaults.
- `security-policy.md` — permission tiers, trust boundaries, secret handling.

## By Intent — Knowledge

Trigger keywords: `architecture`, `pattern`, `convention`, `stack`, `module`, `api surface`, `domain`, `glossary`, `terminology`, `bootstrap`, `skill`, `template`, `adr`, `decision`, `decision record`.

- `project-knowledge-base.md` — durable patterns, watchouts, project continuity facts.
- `domain-specs.md` — ubiquitous language for the kit (skills, artifacts, memory tiers).
- `adr-log.md` — index of architecture decisions; load when the task touches prior decisions, requires a new ADR, or affects architectural tradeoffs. *(Skip if file does not exist yet — it is lazy-created by the first `/spec-adr` run.)*
- `docs/architecture.md` — durable system structure, boundaries, integration seams.
- `docs/generated/codemap.md` — generated map of code locations.
- `docs/generated/references-index.md` — generated index of cross-file references.

## By Intent — Learned

Trigger keywords: `heuristic`, `instinct`, `recurring`, `lesson`, `we always`, `we never`, `last time`.

- `learned-heuristics.md` — evidence-backed instincts that improve future execution.

## By Domain Packs

Domain packs live in `memories/domains/<name>/`. Each pack declares its trigger keywords
in `glossary.md` frontmatter.

- **High confidence (3+ keyword matches):** Load all 4 files from the matching pack:
  `glossary.md`, `patterns.md`, `anti-patterns.md`, `boundary-rules.md`.
- **Low confidence (1–2 keyword matches):** Partial load — load `glossary.md` only.
- **No match:** Skip all domain packs.
- **No packs installed:** Skip this section entirely.

Installed packs:

- _no domain packs installed_

## By Debug (load on debug, retro, or failure)

Trigger keywords: `debug`, `failure`, `regression`, `incident`, `retro`, `flaky`, `why did`, `root cause`.

- `observability-log.md` — auto-tier failure log written by `harness-maintain` and `harness-verify`.
- `artifacts/features/<slug>/session-extracts.md` — per-feature distillation, candidate-only until triaged.

## Phase × Lane Matrix

The Always group loads every session. This matrix says what to **add** at each phase based on the active rigor profile and what to **stop reading** when it's not relevant. `Must` = required reading; `Should` = read unless reason to skip; `Skip` = do not read.

| Source | Tiny — Spec | Tiny — Plan | Tiny — Implement | Tiny — Verify | Standard — Spec | Standard — Plan | Standard — Implement | Standard — Verify | Complex — Spec | Complex — Plan | Complex — Implement | Complex — Verify |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `constitution.md` | Must | Must | Must | Must | Must | Must | Must | Must | Must | Must | Must | Must |
| `harness-config.md` | Must | Must | Must | Must | Must | Must | Must | Must | Must | Must | Must | Must |
| `security-policy.md` | Should | Skip | Skip | Should | Must | Must | Should | Must | Must | Must | Must | Must |
| `project-knowledge-base.md` | Skip | Skip | Skip | Skip | Should | Must | Should | Should | Must | Must | Must | Must |
| `domain-specs.md` (when relevant) | Skip | Skip | Skip | Skip | Should | Should | Should | Should | Must | Must | Must | Must |
| `docs/architecture.md` | Skip | Skip | Skip | Skip | Should | Should | Skip | Should | Must | Must | Should | Must |
| `learned-heuristics.md` | Skip | Skip | Skip | Skip | Should | Should | Should | Should | Must | Must | Must | Must |
| `docs/generated/codemap.md` | Skip | Skip | Skip | Skip | Should | Should | Should | Skip | Must | Must | Must | Skip |
| `docs/generated/references-index.md` | Skip | Skip | Skip | Skip | Skip | Should | Should | Skip | Should | Must | Must | Skip |
| `observability-log.md` | Skip | Skip | Skip | Skip if clean | Skip | Skip | Skip | Should | Should | Should | Should | Must |
| Prior `session-extracts.md` | Skip | Skip | Skip | Skip | Skip | Should | Skip | Skip | Should | Should | Skip | Should |

Phase definitions:

- **Spec** — running `spec-requirements` (intake, grilling, proposal, requirements review).
- **Plan** — running `spec-plan` (design, plan, tasks, mechanical gate).
- **Implement** — running `spec-implement` (one task at a time, proof-driven).
- **Verify** — running `harness-verify` (mechanical gate, alignment, traceability, scenarios, post-ship sync).

When a task escalates lane mid-flight (Tiny → Standard, Standard → Complex), re-read the column at the new lane before continuing — files marked `Skip` at the old lane may now be `Must`.

## Promotion Watchlist

Files approaching promotion thresholds. Empty when no file is near a limit.

- _none_

## Maintenance

- This file is updated by `context-memory` when groups are added, files are promoted, or trigger keywords drift.
- `context-session` reads this on start. `harness-verify` reads this during the post-ship sync gate.
- Do not list feature artifacts here. Feature state belongs under `artifacts/features/<slug>/`.
