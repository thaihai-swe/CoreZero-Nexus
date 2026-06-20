# Workflow, Skills, and Onboarding Guide

The CoreZero developer kit is an engineering harness built to provide strict, spec-anchored, and test-validated AI coding agent workflows. It prevents common AI agent failure modes—such as context window amnesia, code bloat ("AI slop"), spec drift, and silent regressions—by structuring the workspace and enforcing strict progression gates.

This guide describes the current shipped commands, the expected workflow, how to onboard onto a new repository, and the reserved `source-only` marker.

---

## Onboarding: First 30 Minutes

Use this guide after installing the kit into an adopter repository.

1. Read `kit-map.md` to understand the command layers and ownership model.
2. Read `AGENTS.md` and `INDEX.md` at the repo root.
3. Fill in the adopter-owned project docs under `docs/project/` with known facts. Use `[UNKNOWN]` where the answer is not known yet.
4. Run `/starter-init` to bootstrap the repo-specific harness state.
5. Start the first feature with `/spec-requirements` when the goal is clear, or `/spec-research` when existing behavior needs investigation first.

---

## Shipped Commands

| Command | Role | Status |
|---|---|---|
| `/starter-init` | Bootstrap a repository and customize seeded memory files for the adopter project | Shipped now |
| `/spec-research` | Brownfield or unknown-behavior analysis | Shipped now |
| `/spec-requirements` | Define requirements and acceptance criteria | Shipped now |
| `/spec-plan` | Convert requirements into a safe execution plan | Shipped now |
| `/spec-implement` | Execute planned work task by task | Shipped now |
| `/harness-verify` | Verify proof, alignment, and closeout | Shipped now |
| `/context-session` | Manage feature-session continuity | Shipped now |
| `/context-memory` | Maintain durable repo memory | Shipped now |
| `/context-compact` | Compact a named oversized memory file (>600 lines). Preserves all normative identifiers (CC-\*, LH-\*, INV-\*) with a mandatory pre/post safety protocol | Shipped now |
| `/context-status` | Report multi-feature status and regenerate dashboard | Shipped now |
| `/harness-maintain` | Assess and improve the harness itself | Shipped now |
| `/spec-adr` | Capture durable architecture decisions | Shipped now |
| `/code-review` | Review implementation quality | Shipped now |
| `/technical-docs` | Generate grounded API and flow documentation | Shipped now |
| `/codebase-documenter` | Generate repo onboarding and architecture doc sets | Shipped now |
| `/visualize` | Generate SVG and Mermaid technical diagrams | Shipped now |
| `/ponytail` | Enforces simplicity-first coding — YAGNI, laziest effective solution, trims over-engineering. Intensity: lite / full (default) / ultra. | Shipped now |

---

## Default Delivery Flow

The core delivery path is:

`/starter-init` -> `/spec-research` or `/spec-requirements` -> `/spec-plan` -> `/spec-implement` -> `/code-review` -> `/harness-verify`

This path does not include every skill. It includes the minimum sequence for shipping a feature with a spec, plan, implementation proof, and verification pass.

Governance, docs authoring, and visualization commands are shipped helpers. They are installed by default, but they are not required on every single feature path.

### End-to-End Workflow Lifecycle

A complete feature delivery lifecycle follows a rigorous chronological sequence of commands and phases:

```text
       1. Bootstrap           2. Session START        3. Requirements Intake
     ┌──────────────┐        ┌────────────────┐       ┌────────────────────┐
     │ /starter-init│ ──────>│/context-session│ ─────>│ /spec-requirements │
     └──────────────┘        └────────────────┘       └────────────────────┘
                                                                 │
                                                                 ▼
       6. Closeout            5. Implementation       4. Design & Planning
     ┌──────────────┐        ┌────────────────┐       ┌────────────────────┐
     │/harness-verify│<──────│ /spec-implement│<───── │     /spec-plan     │
     └──────────────┘        └────────────────┘       └────────────────────┘
            │
            ▼
       7. Memory Sync
     ┌────────────────┐
     │ /context-memory│ ──────> [Updated constitution, PKB & Heuristics]
     └────────────────┘
```

#### Phase 1: Repository Bootstrapping ([`/starter-init`](../kit/skills/starter-init/SKILL.md))
- Initializes the environment, parses dependencies, and registers targets.
- **Gitignore Injection:** Excludes ephemeral generated artifacts and telemetry (`docs/generated/*`, `memories/repo/harness-telemetry.md`) from version control.
- **Greenfield Mode:** Prefills standard templates and triggers.
- **Brownfield Mode (Phase A - Archaeology):** Runs a deep static sweep to identify code debt, dependency graphs, and records risk area notes into `memories/repo/project-knowledge-base.md`.

#### Phase 2: Session Initialization ([`/context-session START`](../kit/skills/context-session/SKILL.md))
- Initiates the feature sandbox under a specific slug (e.g. `feature-abc`).
- Sets up `status.md` and reads `handoff.md` from the previous session to ensure continuous execution.

#### Phase 3: Specification Intake ([`/spec-requirements`](../kit/skills/spec-requirements/SKILL.md))
- Conducts a Socratic evaluation phase, asking the developer clarifying questions to avoid assumptions.
- Authors the canonical `spec.md` requiring strict deterministic Acceptance Criteria formatted as markdown checklists (`- [ ]`) or Gherkin (`Given/When/Then`) mapped to binary verification commands.

#### Phase 4: Planning ([`/spec-plan`](../kit/skills/spec-plan/SKILL.md))
- Drafts Architectural Decision Records (ADRs) via `/spec-adr` if system architecture is modified.
- Generates `plan.md` (listing target files, code modification specifications, and verification commands).
- Populates `tasks.md` (a checklist of granular coding tasks paired with evidence-proving commands).

#### Phase 5: Implementation ([`/spec-implement`](../kit/skills/spec-implement/SKILL.md))
- Agent executes modifications in targeted files.
- Coding standards in `docs/rules/` (syntax, language-specific lints, and security standards) must be strictly adhered to.
- For every task item, the agent runs the localized mechanical verification gate via `kit/scripts/harness/gate-runner.sh`.
- **Telemetry Collection:** If the gate fails, errors are piped to `kit/scripts/harness/telemetry-collector.sh` to update `harness-telemetry.md`.
- **Minimum Viable Context & Eviction:** The agent operates under strict Minimum Viable Context (MVC) guidelines, JIT-loading only targeted files, and evicts raw execution output from the active context window immediately after summarization.

#### Phase 6: Verification & Review ([`/harness-verify`](../kit/skills/harness-verify/SKILL.md))
- **Mechanical Gate:** Runs the workspace-wide check suite via `kit/scripts/harness/gate-runner.sh` (linting, build verification, and test suites) to ensure zero broken baselines.
- **Circuit Breaker:** Tracks failure counts to prevent infinite loops; if an implementation fails verification >= 2 times, it routes back to `/spec-plan` to rethink the approach.
- **Alignment Audit:** Maps every single `AC-*` from `spec.md` to task proofs to verify full requirements implementation.
- **Code Review:** Checks code against safety guidelines and Google-standard coding policies.
- Promotes feature status to `Done` in `status.md`.

#### Phase 7: Memory Promotion ([`/context-memory`](../kit/skills/context-memory/SKILL.md))
- Closes out the session via `/context-session END` which distills lesson candidates into `session-extracts.md`.
- Post-ship sync evaluates candidate lessons and promotes them to the durable instruction tier (`project-knowledge-base.md`, `learned-heuristics.md`, or domain packs under `memories/domain/`).

---

## Session Flow

Use `/context-session` only after a feature slug and `artifacts/features/<slug>/status.md` already exist.

| Situation | Command |
|---|---|
| Resume an existing feature | `/context-session START` |
| Pause after meaningful progress | `/context-session CHECKPOINT` |
| Close a long session or prepare handoff | `/context-session END` |

`END` is emphasized because it creates durable handoff context before chat history disappears. It is not the only mode.

---

## Useful Follow-Up Commands

- `/context-status` shows active features, blockers, and recommended next commands.
- `/context-memory` promotes evidence-backed lessons after work is verified or a long session ends.
- `/harness-maintain` repairs stale indexes, generated references, or harness drift.
- `/technical-docs` and `/codebase-documenter` create durable documentation.
- `/visualize` creates diagrams when they materially improve clarity.

---

## Ownership During Upgrades

The installer treats files according to `manifest.json`:

- `overwrite` files are kit-managed and updated on each install.
- `copyIfMissing` files are adopter-owned seeds and are not overwritten after first install.
- `preserve` directories hold adopter state and must survive upgrades.

---

## Troubleshooting

- If a generated file looks stale, regenerate it with the owning skill instead of editing it by hand.
- If a feature has no `status.md`, start with `/spec-requirements` or `/spec-research`, not `/context-session`.
- If a session gets long or confusing, run `/context-session CHECKPOINT`; if context is saturated, run `/context-session END`.
- If installer validation fails, treat it as a kit packaging defect and repair the shipped source before distributing the kit.

---

## Memory Audit

Run `/context-memory --audit` to produce a structured report of memory system health. The audit checks:

- File sizes against the soft warning threshold (800 lines) and hard limit (1200 lines) configured in `core-policies.md`
- Domain pack trigger keyword relevance against the current codebase
- Stale references in memory files (paths or identifiers that no longer exist)
- Unused domain packs (no recent load events in telemetry or session extracts)
- Drift between findings and `memories/repo/INDEX.md` `## Promotion Watchlist`

Output is written to `artifacts/features/<slug>/memory-audit.md` (feature-scoped) or `docs/generated/memory-audit.md` (global). The audit produces a report only — promotions and rewrites stay manual or route through a regular `/context-memory` or `/context-compact` invocation.

---

## Source-Only Marker

Use `source-only` only when a skill exists in `kit/` but is intentionally excluded from the installer surface. There are no current `source-only` skills in the shipped package.

---

## Shipping Rule

If a command is not listed in the shipped table above, it must not be described as part of the installed package.
