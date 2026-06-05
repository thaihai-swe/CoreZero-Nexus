# Harness Card

> Standardized summary of this repository's agent harness. See `skills/starter-init/references/harness-card-template.md` for the template.

- **Repo:** AI Agents Development Kit (CoreZero Nexus) / CoreZero Nexus
- **Harness version:** 0.2.0 (2026-06-04)
- **Card last updated:** 2026-06-04
- **Maintainer:** swe (solo)

## Repository Profile

- **Repository type:** Greenfield (this repo *is* the kit; adopting projects can be Greenfield, Brownfield, or Vibecoded)
- **Default rigor profile:** Standard
- **Primary stack:** Markdown + Bash (documentation-first repo). Optional Python 3.10+ for `visualize`.
- **Build command:** N/A (no compiled artifacts)

## Harness Subsystems

| Subsystem | Status | Owner File |
|---|---|---|
| Instructions (router) | Active | `AGENTS.md` (thin router under 50 lines that points to memory and skills) |
| State (per-feature) | Active | `artifacts/features/<slug>/` (status, progress, handoff) |
| Verification (mechanical gate) | Active | `harness-verify`  |
| Scope (one task at a time) | Active | `spec-plan` focused, independently-verifiable tasks |
| Lifecycle (init → session → verify) | Active | `starter-init`, `context-session`, `harness-verify` |
| Security (permission tiers) | Active | `memories/repo/security-policy.md` |
| Context Engineering (tiered) | Active | `skills/context-session/references/context-assembly.md` |
| Memory Router (intent-based load) | Active | `memories/repo/INDEX.md` |
| Knowledge Sync (post-ship sweep) | Active | `skills/context-memory/SKILL.md` Part 8, gated by `harness-verify` |

## Memory Tiers

| Tier | Files | Status |
|---|---|---|
| Instruction | `memories/repo/{constitution,security-policy,learned-heuristics,project-knowledge-base,harness-config,domain-specs}.md`, `docs/architecture.md` | Active |
| Auto | `memories/repo/observability-log.md` | Empty (no failures captured yet — file is bootstrapped from template) |
| Extracted | `artifacts/features/<slug>/session-extracts.md` | Empty (no features completed under the new flow yet) |

## Memory Router

- **Index file:** `memories/repo/INDEX.md`
- **Always group:** `constitution.md`, `harness-config.md`, `security-policy.md`
- **By-intent groups:** Knowledge (PKB, domain-specs, architecture), Learned (heuristics)
- **By-debug group:** `observability-log.md`, prior `session-extracts.md`
- **Promotion thresholds:** see `memories/repo/harness-config.md` `## Memory Promotion Thresholds`

## Adaptive Rigor

- **Default profile:** Standard
- **Rationale:** Most kit work is documentation and skill edits — not Tiny, but rarely Complex either. Standard fits the typical change.
- **Promotion triggers:**
  - Skill/template/schema changes → Complex (apply System Spec Mode + `harness-maintain Eval Mode`)
  - Bootstrap or consistency-check changes → at least Complex
  - Documentation-only updates that don't change skill behavior → Tiny
- **Reference:** `skills/_shared/rigor-profiles.md`

## Verification Posture

- **Required for `Standard`:** mechanical + alignment + security lens
- **Required for `Complex`:** all of `Standard` plus traceability, `testing-scenarios.md`, and `harness-maintain Eval Mode` when the work modifies the harness itself
- **CI integration:** `.github/workflows/harness-check.yml`

## Security Posture

- **Sensitive paths:** `scripts/install.sh` (writes into target projects), `memories/repo/security-policy.md` (the policy itself)
- **Secrets handling:** None required — repo has no runtime secrets
- **Sandbox / permission model:** See `memories/repo/security-policy.md`
- **Prompt-injection surfaces:** External content fetched via `spec-research` web tools

## Context Engineering

- **Tiered assembly:** Active per `skills/context-session/references/context-assembly.md` (Router + INDEX → Always memory → By-intent groups → Architecture → Feature artifacts → Raw code → Transient logs)
- **Intent routing:** Active — sessions read `memories/repo/INDEX.md` first and load only the by-intent groups whose triggers match the active task
- **JIT loading:** Yes — raw code loaded only for the immediate task
- **Compaction triggers:** See `memories/repo/harness-config.md` `## Session Defaults`
- **Subagent-driven exploration:** Yes for broad codebase mapping; main context receives summaries only

## Known Limits

- The auto-tier observability log is empty until real failures get captured. Expect entries once features run end-to-end under the new flow.
- The extracted-tier session-extracts files only exist per-feature; expect them to populate as features run `context-session END`.
- `visualize` requires Python venv + Mermaid CLI — non-trivial setup. Opt-in.
- Adversarial spec review is recommended for cross-cutting work in the `Complex` profile but not yet a separate skill.
- Maintainer docs live in `documents/`, but the default installer does not ship them into downstream projects.

## Customizations

- This repo *is* the kit, so the harness is bootstrapped by hand rather than by `install.sh`. Adopting repos always run the script.
- `visualize` is documented but rarely used in this repo's own work.

## Cross-References

- Architecture: `docs/architecture.md`
- Constitution: `memories/repo/constitution.md`
- Security policy: `memories/repo/security-policy.md`
- Repair utility: `scripts/doctor.sh`
- Rigor profiles: `skills/_shared/rigor-profiles.md`
- Memory tiers: `skills/context-memory/SKILL.md` `## Memory Tiers`
- Harness card template: `skills/starter-init/references/harness-card-template.md`
