# Memory Router

> Always-loaded routing index for `memories/repo/`. Keep under 120 lines.
> Sessions read this first, then load only the groups that match the task.

## How To Use This Index

1. Files in the **Always** group load on every session start.
2. Files in the **By Intent** groups load only when their trigger keywords or semantic concepts match the active task.
   - **Semantic Routing:** Evaluate if the active task's core requirements relate conceptually to system structure, heuristics, or debugging context, even if exact literal keywords are absent.
   - **Confidence-Scored Loading:** If the active task triggers ≤2 keywords or conceptual markers (low confidence), perform a **partial-load**: load ONLY the top-level index file or the summary header for that group instead of all files. Only load the full group for high-confidence matches (3+ keywords or clear semantic relevance).
3. Files in the **By Debug** group load only when debugging, retro, or post-mortem work begins.
4. The **Phase × Lane Matrix** below tells you what to add (and what to stop reading) once the active rigor profile is known.
5. If a file outgrows its slot (>800 lines, 3+ distinct subtopics, or 5+ artifacts reference one slice), open a promotion proposal under `artifacts/features/<slug>/promotions.md`.

## Always (load every session)

- `core-policies.md` — repo-wide normative rules (CC-* identifiers), canonical commands, paths, and rigor defaults.
- `security-policy.md` — permission tiers, trust boundaries, secret handling.

## By Intent — Knowledge

Trigger keywords: `architecture`, `pattern`, `convention`, `stack`, `module`, `api surface`, `domain`, `glossary`, `terminology`, `bootstrap`, `skill`, `template`, `adr`, `decision`, `decision record`, `product`, `users`, `metric`, `dependency`, `tooling`, `constraint`, `compliance`, `budget`, `deploy`.

- `project-knowledge-base.md` — durable patterns, watchouts, project continuity facts.
- `adr-log.md` — index of architecture decisions; load when the task touches prior decisions or architectural tradeoffs. *(Skip if the file does not exist yet.)*
- `docs/project/architecture.md` — durable system structure, boundaries, integration seams.
- `docs/project/product-sense.md` — product vision, target users, success metrics. Load on product/scoping work.
- `docs/project/glossary.md` — shared vocabulary and naming conventions. Load when naming or terminology matters.
- `docs/project/tech-stack-reference.md` — dependencies, APIs, tools, conventions. Load before adding deps or touching integrations.
- `docs/project/project-constraints.md` — budgets, compliance, deploy, security constraints. Load when constraints bound the change.
- `docs/generated/codemap.md` — generated map of code locations.
- `docs/generated/references-index.md` — generated index of cross-file references.

## By Intent — Rules

Trigger keywords: `python`, `security`, `secret`, `auth`, `input validation`, `injection`, plus the language or domain name of any rule file added here.

- `rules/python.md` — Python conventions and style; load on Python work.
- `rules/security.md` — cross-language security do/don't patterns; load on security-sensitive work (secrets, auth, external input).
- `docs/policies/code-design.md` — normative cross-cutting coding policy (overengineering pitfalls, spec/behavior drift); load when changing or adding software design. Its `MUST`/`MUST NOT` rules carry priority-rule weight.

This group grows by one row per shipped `rules/*.md` file added.

## By Intent — Learned

Trigger keywords: `heuristic`, `instinct`, `recurring`, `lesson`, `we always`, `we never`, `last time`.

- `learned-heuristics.md` — evidence-backed instincts that improve future execution.

## By Domain Packs

Domain packs live in `memories/domain/`. Trigger keywords are declared in `glossary.md` frontmatter.

- **High confidence (3+ keyword matches):** Load all files from the domain pack:
  `glossary.md`, `patterns.md`, `anti-patterns.md`, `boundaries.md`.
- **Low confidence (1–2 keyword matches):** Partial load — load `glossary.md` only.
- **No match:** Skip domain packs.
- **No packs installed:** Skip this section entirely.

Installed packs:

- **example** (`memories/domain/`) — triggers: `example`, `sample`, `demo`, `template`, `walkthrough`. Worked-example pack shipped as a schema demo; replace with a real domain pack.

## By Debug (load on debug, retro, or failure)

Trigger keywords: `debug`, `failure`, `regression`, `incident`, `retro`, `flaky`, `why did`, `root cause`.

- `harness-telemetry.md` — auto-tier failure log written by `/harness-verify` and triaged by `/harness-maintain`.
- `artifacts/features/<slug>/session-extracts.md` — per-feature distillation, candidate-only until triaged.

## Phase × Lane Matrix

The Always group loads every session. This matrix says what to **add** at each phase based on the active rigor profile and what to **stop reading** when it's not relevant. `Must` = required reading; `Should` = read unless reason to skip; `Skip` = do not read.

| Source | Tiny — Spec | Tiny — Plan | Tiny — Implement | Tiny — Verify | Standard — Spec | Standard — Plan | Standard — Implement | Standard — Verify | Complex — Spec | Complex — Plan | Complex — Implement | Complex — Verify |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `core-policies.md` | Must | Must | Must | Must | Must | Must | Must | Must | Must | Must | Must | Must |
| `security-policy.md` | Should | Skip | Skip | Should | Must | Must | Should | Must | Must | Must | Must | Must |
| `project-knowledge-base.md` | Skip | Skip | Skip | Skip | Should | Must | Should | Should | Must | Must | Must | Must |
| `docs/project/architecture.md` | Skip | Skip | Skip | Skip | Should | Should | Skip | Should | Must | Must | Should | Must |
| `docs/project/product-sense.md` | Skip | Skip | Skip | Skip | Should | Skip | Skip | Skip | Should | Should | Skip | Skip |
| `docs/project/glossary.md` | Skip | Skip | Skip | Skip | Should | Should | Skip | Skip | Should | Should | Should | Skip |
| `docs/project/tech-stack-reference.md` | Skip | Skip | Skip | Skip | Skip | Should | Should | Skip | Should | Must | Must | Skip |
| `docs/project/project-constraints.md` | Skip | Skip | Skip | Skip | Should | Should | Skip | Should | Must | Must | Should | Should |
| `learned-heuristics.md` | Skip | Skip | Skip | Skip | Should | Should | Should | Should | Must | Must | Must | Must |
| `docs/generated/codemap.md` | Skip | Skip | Skip | Skip | Should | Should | Should | Skip | Must | Must | Must | Skip |
| `docs/generated/references-index.md` | Skip | Skip | Skip | Skip | Skip | Should | Should | Skip | Should | Must | Must | Skip |
| `rules/*.md` (on language/domain match) | Skip | Skip | Should | Should | Skip | Should | Must | Should | Skip | Should | Must | Must |
| `docs/policies/code-design.md` (on software-design change) | Skip | Skip | Should | Skip | Skip | Should | Should | Skip | Should | Must | Must | Should |
| `harness-telemetry.md` | Skip | Skip | Skip | Skip if clean | Skip | Skip | Skip | Should | Should | Should | Should | Must |
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
