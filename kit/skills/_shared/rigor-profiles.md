# Rigor Profiles

A repo-wide and per-feature delivery profile that scales the kit's ceremony to the work's risk and scope. Set the default in `memories/repo/harness-config.md`. Override per feature in `artifacts/features/<slug>/status.md`.

## Why Profiles Exist

The kit can be run at full ceremony (Socratic grilling waves, ADR + diagram + design + plan + manual scenarios) or at minimum ceremony (a tight spec and a focused implementation). Without a declared profile, agents default to maximum ceremony — which is correct for risky changes and wasteful for trivial ones.

There are three profiles, ordered by ceremony: **Tiny**, **Standard**, and **Complex**. Complex is the top tier and absorbs what was previously a separate "Ultra" tier — its rules call out the cross-cutting / harness-change cases that need extra rigor.

A profile is a *contract* between the user and the agent: "for this work, run at this depth." Every downstream skill reads the profile and scales its workflow accordingly.

## The Three Profiles

### Tiny

For low-risk, reversible, narrow-surface work. One file, no behavior change, or a small bug fix with an obvious cause.

| Skill | Behavior |
|---|---|
| `spec-requirements` | 1-2 grilling questions max. Compact `proposal.md` only. `spec.md` allowed but minimal. Skip `requirements-review.md`. |
| `spec-research` | Skipped unless explicitly requested. |
| `visualize` | Skipped. |
| `spec-adr` | Skipped. |
| `spec-plan` | Lean `plan.md`, no `design.md`. `tasks.md` may be inline in plan if 3 or fewer tasks. |
| `spec-implement` | Standard. |
| `harness-verify` | Mechanical gate + spec alignment only. Security lens optional. Skip `testing-scenarios.md` unless behavior is user-visible. |
| `context-session` | Extraction step still runs but candidates can be brief or "no extractable lessons". |

**Use when:** typo fix, single-file refactor, doc update, dependency bump, comment cleanup. **Do not use when:** auth, payments, data migrations, or shared interfaces are touched.

### Standard

The default. For clear feature work with a known surface and routine risk.

| Skill | Behavior |
|---|---|
| `spec-requirements` | 3-5 grilling questions. Full `proposal.md`, `spec.md`, and `requirements-review.md`. |
| `spec-research` | Run if codebase context is unfamiliar. |
| `visualize` | Optional. Run when boundaries cross more than one component. |
| `spec-adr` | Run only when a non-obvious technical choice is locked. |
| `spec-plan` | Full `plan.md` and `tasks.md`. `design.md` only when ambiguity remains. |
| `spec-implement` | Standard. |
| `harness-verify` | Mechanical gate + alignment + security lens. `testing-scenarios.md` for user-facing changes. |
| `context-session` | Standard extraction. |

**Use when:** most feature work. New endpoint, new component, contained refactor, bug fix with non-trivial root cause.

### Complex

The top tier. Use for high-ambiguity, cross-boundary, brownfield-risky work, or repo-defining work — cross-cutting policy, system specs, harness changes, or high-blast-radius infrastructure.

| Skill | Behavior |
|---|---|
| `spec-requirements` | 5+ grilling questions; all gray-area decisions locked in `spec.md`. Full readiness review. **System Spec Mode** when the work is cross-cutting (multiple features constrained by it, or harness changes). Adversarial review pass before lock when the work changes public API, persistent data, or harness subsystems. |
| `spec-research` | Required. Subagent-driven exploration; parallel subagents for cross-cutting work. |
| `visualize` | Required when system structure is affected. Architecture diagrams must be regenerated for harness or system-spec work. |
| `spec-adr` | Required for each locked technical choice. |
| `spec-plan` | Full `design.md` + `plan.md` + `tasks.md`. Stress-test design with subagent. Adversarial plan review and phased rollout when the work is cross-cutting. Smaller-than-usual task slices with continuous proof for harness or migration work. |
| `spec-implement` | Standard; smaller slices for cross-cutting or migration work. |
| `harness-verify` | All modes: mechanical gate, alignment, traceability, security lens, optional fallow pass. `testing-scenarios.md` always. **`harness-maintain Eval Mode`** pass when the work modifies the harness itself. |
| `context-session` | Standard extraction; recommend mid-session checkpoint. Frequent checkpoints and detailed extraction for cross-cutting work. |

**Use when:** auth, payments, data migration, cross-feature contracts, any work touching paths flagged in `security-policy.md`, cross-cutting policy, harness subsystem changes, public API or schema migrations, or anything that becomes a constraint for future feature specs.

## Profile Selection Rules

1. **Default to `Standard`** when in doubt.
2. **Promote to `Complex`** when any of these are true:
   - The feature touches a path listed in `security-policy.md` as security-sensitive
   - The feature crosses more than one major architectural boundary
   - The brownfield risk rating in the spec is `Medium` or `High`
   - The acceptance criteria require contracts that other features depend on
   - The work is cross-cutting (multiple features will be constrained by it)
   - The work modifies the harness itself
   - The work changes a public API or migrates persistent data
3. **Demote to `Tiny`** only when all of these hold:
   - One file or a single-purpose change
   - No behavior change OR an obvious bug fix
   - No security-sensitive path is touched
   - No interface or contract is affected

When uncertain between two profiles, pick the higher one. Over-ceremony costs time; under-ceremony costs correctness.

### Automated Profile Selection Routine

At the start of the feature lifecycle (during `/spec-requirements`, `/spec-research`, or `/context-session` resume), the agent **MUST** automatically compute the profile by:
1. Listing the target files to be modified (either from the issue/proposal, or from a `git diff` if resuming work).
2. Checking intersections against:
   - Security-sensitive paths declared in `security-policy.md`
   - System boundary paths in `docs/architecture.md`
   - The agentic harness files (`skills/`, `memories/repo/`, `AGENTS.md`, `HARNESS_CARD.md`)
3. If an intersection is detected, write/promote the profile to `Complex` in `status.md` under `## 🧭 Delivery Profile`, detailing the matching rule. If no targets match but the task is a single-file minor fix with no boundary impacts, demote to `Tiny`. Otherwise, default to `Standard`.

## Where Profiles Live

- **Repo default**: `memories/repo/harness-config.md` -> `## Adaptive Rigor` -> `Default profile:`
- **Per-feature override**: `artifacts/features/<slug>/status.md` -> `## 🧭 Delivery Profile`
- **Skills consume**: each skill's "Read First" already loads `harness-config.md` and `status.md`. The profile read happens at the start of every skill's workflow.

## Anti-Patterns

- **"This is just Tiny" without checking the rules.** Tiny is narrowly scoped on purpose. If you're tempted to call risky work Tiny to skip ceremony, the right move is to do the work in smaller actually-Tiny pieces.
- **Treating `Standard` as a synonym for "default ceremony."** Standard means most feature work. If the feature is genuinely risky, promote it.
- **Locking the profile and never revisiting.** If implementation reveals the work is harder than the spec implied, promote the profile and re-run the affected phase. The artifacts are cheap; the bug isn't.
- **Setting the repo default to `Tiny`.** The repo default should match the typical work in this repo. For most repos that is `Standard`. `Tiny` as a default invites silent under-verification.
- **Treating Complex as one-size-fits-all.** Complex covers everything from a contained-but-risky feature to a repo-wide harness change. Read the Complex row carefully and apply only the rows that match the work — System Spec Mode and `harness-maintain Eval Mode` are reserved for cross-cutting / harness work, not every Complex feature.
