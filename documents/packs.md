# Harness Packs

This guide documents the four core packs that organize CoreZero Nexus commands and files for adopter repositories.

---

## 1. Project Starter

### What This Pack Solves
The `Project Starter` pack bootstraps a repository for AI-assisted development by setting up the entrypoint router, baseline memory configuration, system architecture guides, and project templates.

### When To Use It
- Installing CoreZero Nexus in a project for the first time.
- Re-initializing operating configurations after a major workflow change.
- Aligning template files with the actual project structure and code evidence.

### Public Command
* `/starter-init` — Boots the harness configuration.

### Key Files Touched
- `AGENTS.md` (router entrypoint)
- `HARNESS_CARD.md` (harness summary card)
- `memories/repo/*` (memory router and seed instruction files)
- `docs/architecture.md` (durable architecture baseline)
- `docs/*.md` project-policy docs seeded for the adopter to refine
- `docs/generated/*` (index & codemap artifacts)

---

## 2. Context Engineering

### What This Pack Solves
`Context Engineering` preserves session continuity across tool and context window resets, maintains durable repository knowledge, and manages orchestration views to prevent amnesia and redundancy.

### When To Use It
- Starting or resuming a task boundary.
- Documenting, amending, or promoting repository knowledge to memory.
- Reviewing status and progress across multiple active features.

### Public Commands
* `/context-session` — Begins, checkpoints, or ends a working session.
* `/context-memory` — Sweeps, triages, and promotes durable repository memory.
* `/context-status` — Provides project-wide views of active features.

### Key Files Touched
- `memories/repo/INDEX.md`
- `memories/repo/constitution.md`
- `memories/repo/security-policy.md`
- `memories/repo/learned-heuristics.md`
- `memories/repo/project-knowledge-base.md`
- `artifacts/features/<slug>/progress.md`
- `artifacts/features/<slug>/handoff.md`
- `artifacts/features/<slug>/session-extracts.md`
- `docs/architecture.md`
- `docs/generated/codemap.md`
- `docs/generated/references-index.md`


---

## 3. Spec-Driven Development

### What This Pack Solves
`Spec-Driven Development` (SDD) translates user requirements into structured analysis, Socratic grilling, locked specifications, design breakdowns, and micro-task implementations.

### When To Use It
- Investigating system behavior or mapping complex brownfield codebases.
- Drafting, grilling, and locking requirement scopes.
- Designing execution plans and executing micro-tasks.
- Recording technology tradeoffs and architectural decisions.

### Public Commands
* `/spec-research` — Crawls the codebase and maps behaviors.
* `/spec-requirements` — Defines specifications and locks acceptance criteria.
* `/spec-plan` — Sets plans, design files, and micro-task lists.
* `/spec-implement` — Executes task-by-task implementations with local proofs.
* `/spec-adr` — Records and indexes Architectural Decision Records (ADRs).

### Key Files Touched
- `artifacts/features/<slug>/analysis.md`
- `artifacts/features/<slug>/proposal.md`
- `artifacts/features/<slug>/spec.md`
- `artifacts/features/<slug>/requirements-review.md`
- `artifacts/features/<slug>/design.md`
- `artifacts/features/<slug>/plan.md`
- `artifacts/features/<slug>/tasks.md`
- `artifacts/features/<slug>/adr-*.md`
- `memories/repo/adr-log.md`
- [`docs/PRODUCT_SENSE.md`](../kit/docs/PRODUCT_SENSE.md)
- [`docs/GLOSSARY.md`](../kit/docs/GLOSSARY.md)
- [`docs/TECH_STACK_REFERENCE.md`](../kit/docs/TECH_STACK_REFERENCE.md)
- [`docs/PROJECT_CONSTRAINTS.md`](../kit/docs/PROJECT_CONSTRAINTS.md)

---

## 4. Harness Engineering

### What This Pack Solves
`Harness Engineering` enforces mechanical proofs, quality standards, alignment metrics, and security policies to make AI actions reliable and prevent structural regressions.

### When To Use It
- Verifying code correctness and requirement alignment before shipping.
- Running codebase health checks and evaluator checks.
- Repairing or upgrading the harness environment itself.

### Public Commands
* `/harness-verify` — Runs verification gates, alignment audits, and security reviews.
* `/harness-maintain` — Assesses, configures, or evaluates the harness systems.

### Key Files Touched
- `docs/code-design.md`
- [`docs/GOVERNANCE.md`](../kit/docs/GOVERNANCE.md)
- [`docs/QUALITY_POLICY.md`](../kit/docs/QUALITY_POLICY.md)
- [`docs/RELIABILITY_POLICY.md`](../kit/docs/RELIABILITY_POLICY.md)
- [`docs/TECH_DEBT_REGISTER.md`](../kit/docs/TECH_DEBT_REGISTER.md)
- `artifacts/features/<slug>/review.md`
- `artifacts/features/<slug>/testing-scenarios.md`
- `artifacts/features/<slug>/harness-assessment.md`
- `artifacts/features/<slug>/eval-report.md`
