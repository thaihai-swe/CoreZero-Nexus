# Harness Config

Repo-specific operational setup agents need before feature work.

**Use for:** planning/doc locations, canonical verification commands, issue tracker, labels/states, default entrypoints/paths/environments.

**Don't use for:** feature-local decisions, architectural rationale (`docs/architecture.md`), repo-wide rules (`constitution.md`), descriptive patterns (`project-knowledge-base.md`).

## Repository Identity

- Project name:
- Repository type:
- Primary code roots:
- Default working branch:
- Supported agent clients:

## Work Tracking

- Issue tracker mode:        GitHub | Linear | Local files | None
- Issue/project location:
- Default work item format:
- Required labels or states:
- Escalation / blocker handling:

## Artifact Routing

- Feature artifact root:
- Docs root:
- Architecture doc path:
- Security policy path:
- Learned heuristics path:
- ADR location:
- Generated documentation location:
- Codemap path:
- References index path:

## Verification Commands

- Install / bootstrap:
- Test:
- Lint / format:
- Typecheck:
- Build:
- CI entrypoint:

## Session Defaults

- Session bootstrap skill:
- Progress log path:
- Handoff path:
- When to checkpoint:
- Context compaction triggers:
- Stale-context eviction rules:
- When to stop and escalate:

## Environment And Access

- Required local services:
- Required env files / secrets handling:
- Sandbox / permission watchouts:
- Browser / UI verification target:

## Conventions That Affect Automation

- Feature slug format:
- Branch naming:
- Commit / PR expectations:
- Required reviewers / owners:

## Adaptive Rigor

- **Default profile:** Standard
  (Tiny | Standard | Complex. See `skills/_shared/rigor-profiles.md`.)
- **Automated Profile Computation:** enabled
- **Promotion triggers:**
  - Touching paths flagged in `security-policy.md` → Complex
  - Cross-cutting policy or harness changes (e.g., modifying `skills/`, `memories/repo/`, `AGENTS.md`) → Complex (apply System Spec Mode + `harness-maintain Eval Mode`)
  - Crossing architectural boundaries defined in `docs/architecture.md` → Complex
  - Brownfield risk Medium/High in spec → at least Complex
- **Demotion criteria:** Only demote to Tiny if the work is a single-file, low-risk fix, with no boundary/harness/security intersections.
- **When in doubt:** pick the higher profile. Over-ceremony costs time; under-ceremony costs correctness.

## Memory Promotion Thresholds

Used by `context-memory` post-ship sync to flag files for split-into-group. Promotion is **proposed**, not automatic — user approves.

- File length: warn at 800 lines, hard threshold 1200 lines
- Distinct subtopics: 3+ H2 sections covering separable concerns
- Artifact references: 5+ feature artifacts cite the same slice
- Action when threshold hit: add to `## Promotion Watchlist` in `INDEX.md` + write proposal to `artifacts/features/<slug>/promotions.md`

## Open Setup Questions

- Question:
  Why unresolved:
  Best next source:
