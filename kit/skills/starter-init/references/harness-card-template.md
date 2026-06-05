# Harness Card

`HARNESS_CARD.md` lives at the repo root. It's the single document that tells a new agent (or contributor) what the harness does, what it assumes, and where its limits are.

Generated from this template at `starter-init` time. Updated whenever a harness subsystem changes materially. Keep under 200 lines — anything longer goes in `documents/` or `memories/repo/`.

## Why a Harness Card

- **Onboarding** — one file communicates harness shape.
- **Visibility** — context-engineering and adaptive-rigor disciplines are otherwise invisible from the README.
- **Drift detection** — when reality diverges from the card, one of them is wrong.
- **Auditability** — third parties compare cards across repos without reading every memory file.

## Template

Copy the block below into `HARNESS_CARD.md`. Replace placeholders. **Required** sections must be filled; **optional** may be omitted.

```markdown
# Harness Card

> Standardized summary of this repository's agent harness. See `skills/starter-init/references/harness-card-template.md`.

- **Repo:** <name>
- **Harness version:** <kit version or commit>
- **Card last updated:** <YYYY-MM-DD>
- **Maintainer:** <name or team>

## Repository Profile (required)

- **Repository type:** Greenfield | Brownfield | Vibecoded
- **Default rigor profile:** Tiny | Standard | Complex
- **Primary stack:** <e.g., Python 3.10 + FastAPI; TypeScript + React; Go services>
- **Test runner:** <command>
- **Build command:** <command or N/A>

## Harness Subsystems (required)

Mark each `Active` (fully wired), `Partial` (wired with known gaps), or `Off` (intentionally unused).

| Subsystem | Status | Owner File |
|---|---|---|
| Instructions (router) | Active | `AGENTS.md` |
| State (per-feature) | Active | `artifacts/features/<slug>/` |
| Verification (mechanical gate) | Active | `harness-verify` + `harness-config.md` test command |
| Scope (one task at a time) | Active | `tasks.md` focused, independently-verifiable tasks |
| Lifecycle (init → spec/research → session → verify) | Active | `brownfield-init` (brownfield only), `starter-init`, `spec-requirements` / `spec-research`, `context-session`, `harness-verify` |
| Security (permission tiers) | Active \| Partial \| Off | `memories/repo/security-policy.md` + `skills/harness-maintain/hooks/git-guardrails.sh` |
| Context Engineering (tiered) | Active | `context-session/references/context-assembly.md` |

## Memory Tiers (required)

| Tier | Files | Status |
|---|---|---|
| Instruction | `memories/repo/{constitution,security-policy,learned-heuristics,project-knowledge-base,harness-config}.md`, `docs/architecture.md` | Active |
| Brownfield Risk | `memories/repo/brownfield/{README,brownfield-map,dependency-graph}.md` | Active \| Empty \| Off |
| Auto | `memories/repo/observability-log.md` | Active \| Empty \| Off |
| Extracted | `artifacts/features/<slug>/session-extracts.md` | Active \| Empty \| Off |

## Adaptive Rigor (required)

- **Default profile:** <Tiny \| Standard \| Complex>
- **Rationale:** <one sentence — why this is the default for this repo>
- **Promotion triggers:** <conditions that promote a feature to a higher profile>
- **Reference:** `skills/_shared/rigor-profiles.md`

## Verification Posture (required)

- **Mechanical gate:** <commands run, e.g., `pytest && ruff check .`>
- **Standard:** mechanical + alignment + security lens
- **Complex:** above + traceability + `testing-scenarios.md` (and `harness-maintain Eval Mode` if the work modifies the harness itself)
- **CI integration:** <workflow path or "none">

## Security Posture (required)

- **Sensitive paths:** <list, or link to `security-policy.md`>
- **Secrets handling:** <env vars, vault, or "none required">
- **Sandbox / permission model:** <link or summary>
- **Tool-layer enforcement:** <`git-guardrails.sh` wired in `.claude/settings.json` | "opt-out — recorded in `harness-config.md`">
- **Prompt-injection surfaces:** <known external-content surfaces>

## Context Engineering (required)

- **Tiered assembly:** Active per `context-session/references/context-assembly.md`
- **Brownfield routing:** If the repo is inherited, `INDEX.md` routes `memories/repo/brownfield/*`
- **JIT loading:** Yes — only the immediate task's files load into Tier 5
- **Compaction triggers:** <link to `harness-config.md` `## Session Defaults`>
- **Subagent-driven exploration:** <Yes / No>

## Known Limits (required)

List honestly what the harness does NOT cover. Examples:

- The harness does not gate production deploys.
- `visualize` is opt-in; not all features have diagrams.
- Brownfield map is current as of <date>; rerun if the layout shifts.
- Brownfield repos must run `/brownfield-init` before `/starter-init`.
- The auto-tier observability log is empty — no failures captured yet.

## Customizations (optional)

Each deviation from kit defaults + the reason.

## Cross-References (optional)

- Architecture: `docs/architecture.md`
- Constitution: `memories/repo/constitution.md`
- Security policy: `memories/repo/security-policy.md`
- Rigor profiles: `skills/_shared/rigor-profiles.md`
```

## Maintenance Rules

- **Update when** — a subsystem moves Active/Partial/Off, default profile changes, test command changes, sensitive paths added/removed.
- **Don't update when** — a single feature's spec changes, a session ends, a candidate is triaged. Those belong in feature artifacts/memory tiers.
- **Audit cadence** — review whenever `harness Assess Mode` runs.
- **Drift signal** — if the card claims Active but the file is missing/empty, fix the card or the harness.
