---
name: brownfield-init
description: Archaeology pass for existing repositories — maps tech debt, risky paths, implicit contracts, and module dependencies before feature work begins. Produces durable memory artifacts that inform all future sessions.
compatibility: Designed for Claude, Codex, and other Agent Skills-compatible tools working in harness-engineered repositories that use memories/repo/ and artifacts/features/<slug>/.
---

# Brownfield Init

## Overview

Pre-feature archaeology skill for repositories with existing code, history, CI, or tests. Run once after `install.sh` and before `/starter-init` on brownfield repos. Produces `memories/repo/brownfield/` artifacts that the memory router loads for all subsequent sessions, auto-promotes risky features to Complex profile, and seeds `learned-heuristics.md` with repo-specific watchouts.

Do not confuse this skill with `starter-init`'s Brownfield Mode. `starter-init` Brownfield Mode handles entrypoint conflicts and test inventory during bootstrap. This skill is a deeper, pre-bootstrap archaeology pass for non-trivial existing codebases.

## Read First

- `AGENTS.md` and `HARNESS_CARD.md` (if present — may not exist yet before `starter-init`)
- `memories/repo/harness-config.md` (if present)
- `memories/repo/security-policy.md` (if present)

## When to Use

- The target repository has existing code, tests, CI pipelines, or meaningful git history.
- The team is adopting the kit into an established codebase (brownfield or legacy).
- Run ONCE, before `/starter-init`. Subsequent sessions load the produced artifacts from `memories/repo/brownfield/` automatically via the memory router.

Do not run on empty or near-empty repositories — use `/starter-init` directly for greenfield repos.

## Workflow

1. **Scope Declaration**: State the repo path and confirm the target is non-trivial (has code/history). If the repo is greenfield (no meaningful git history, no existing code), stop and route to `/starter-init` instead.

2. **Subagent Sweep (Read-Only)**: Delegate a broad read-only exploration to subagents. Each subagent produces a summary report; raw output stays isolated. Subagents explore:
   - Source tree structure (top-level directories, file counts by type)
   - Test coverage indicators (test directories, CI config, coverage reports)
   - Security-sensitive paths (auth, payments, secrets loading, external API calls)
   - Entry points and public interfaces (routes, exported modules, CLI entrypoints)
   - High-fan-in modules (files imported by many others — high blast radius)

3. **Brownfield Map**: Produce `memories/repo/brownfield/brownfield-map.md` using the template at `references/brownfield-map-template.md`. Classify each identified area by severity: `low` | `medium` | `high` | `critical`. Record: area name, severity, description, risky paths, implicit contracts, recommended action.

4. **Dependency Graph**: Produce `memories/repo/brownfield/dependency-graph.md` using the template at `references/dependency-graph-template.md`. Map module-to-module dependencies. Flag modules with fan-in ≥ 5 as `risk-flag: true`.

5. **HARNESS_CARD.md Annotation**: If `HARNESS_CARD.md` exists, update the `## Known Limits` section with brownfield-specific caveats found during the sweep (e.g., "Auth middleware has no test coverage", "Payment handler has 8 dependents — blast radius is high").

6. **Heuristics Seeding**: Append 3–5 repo-specific watchouts to `memories/repo/learned-heuristics.md` (create the file if absent). Each watchout must be: evidence-backed (cite a file or pattern found), actionable, and specific to this codebase. Format: standard heuristic entry with source citation.

7. **Profile Auto-Promotion Rule**: Record in `memories/repo/brownfield/brownfield-map.md` under `## Profile Rules`: any feature that touches a path rated `high` or `critical` in the brownfield map MUST be promoted to `Complex` profile in its `status.md`. This rule is enforced by the developer running `/spec-requirements` — they check the map before setting the profile.

8. **Handoff**: Report what was produced, what gaps remain (e.g., areas that couldn't be mapped due to missing tooling), and recommended rigor profile for the first feature based on the severity distribution in the brownfield map.

## Stop Conditions

- Repository is greenfield (no existing code or meaningful history) — route to `/starter-init` instead.
- The subagent sweep finds active production credentials or secrets in tracked files — halt, surface the finding, and require user remediation before any feature work begins.
- The repository has no readable source files (empty, binary-only, or access-denied) — cannot produce meaningful map; stop and report.

## Core Rules

- **Read-Only Sweep**: The subagent exploration phase MUST be read-only. No file modifications during the sweep.
- **Subagent Summaries Only**: Raw subagent output (file listings, grep output) never floods the main context. Only summary reports merge back.
- **Evidence-Backed Heuristics**: Every entry added to `learned-heuristics.md` must cite a specific file, pattern, or commit as its evidence. No invented watchouts.
- **Memory Layer Placement**: All brownfield artifacts go into `memories/repo/brownfield/` — they are memory artifacts, not feature artifacts. They persist across all future sessions.
- **One-Shot Skill**: This skill runs once per repository. Re-running overwrites the prior brownfield map; require explicit user confirmation before a re-run on an existing map.
- **Profile Rules Are Advisory Until Enforced**: The profile auto-promotion rule is recorded in the map for future session reference — it does not retroactively change existing feature artifacts.

## Rationalization vs. Reality

| Rationalization | Reality |
|---|---|
| "I can just run starter-init and fill in brownfield details later." | Brownfield repos have implicit contracts and risky paths that must be documented before any feature lands. Discovering them mid-feature is expensive. |
| "The subagent sweep takes too long — I'll skip it." | Skipping the sweep means the brownfield map is guesswork. A partial map is worse than no map (false confidence). |
| "I'll add heuristics from memory, not from the code." | Heuristics without code evidence are invented rules. They will be wrong and will mislead future agents. |
| "I can run this after starter-init." | Running after starter-init risks filling memory files with wrong baselines. Run brownfield-init first, starter-init second. |

## Red Flags

- Brownfield map produced without a real subagent sweep (fabricated from assumptions).
- Heuristics added to `learned-heuristics.md` without file citations.
- `HARNESS_CARD.md` Known Limits section not updated after the sweep.
- Severity ratings of `low` across the entire map for a large, legacy codebase (under-rating risk).
- Skill run on a greenfield repo (produces a meaningless empty map).

## Verification

- [ ] `memories/repo/brownfield/brownfield-map.md` exists and has at least one rated area.
- [ ] `memories/repo/brownfield/dependency-graph.md` exists and lists module dependencies.
- [ ] `memories/repo/learned-heuristics.md` has 3–5 new entries with file citations.
- [ ] `HARNESS_CARD.md` Known Limits section updated (or a note that it was skipped because the file doesn't exist yet).
- [ ] Handoff states the recommended rigor profile for the first feature.
- [ ] No raw grep output or file listings in the main context — only summaries.

## Output Rules

- Can create: `memories/repo/brownfield/brownfield-map.md`, `memories/repo/brownfield/dependency-graph.md`.
- Can update: `memories/repo/learned-heuristics.md`, `HARNESS_CARD.md` (Known Limits section only).
- Cannot modify: `memories/repo/constitution.md`, `memories/repo/security-policy.md`, `memories/repo/harness-config.md` (route to `/context-memory` or `/starter-init`).
- Cannot create: `spec.md`, `plan.md`, `tasks.md`, `status.md`, feature artifacts.

## References

- [references/brownfield-map-template.md](references/brownfield-map-template.md)
- [references/dependency-graph-template.md](references/dependency-graph-template.md)
- [../starter-init/references/brownfield-mode.md](../starter-init/references/brownfield-mode.md)
- [../spec-research/SKILL.md](../spec-research/SKILL.md)
- [../_shared/rigor-profiles.md](../_shared/rigor-profiles.md)
- [../../memories/repo/INDEX.md](../../memories/repo/INDEX.md)
