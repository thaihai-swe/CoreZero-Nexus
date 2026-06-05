# Project Docs

> **Who is this for?**
> — **Installing the kit into your project?** → You are in the right place. Start with [ADOPTION_GUIDE.md](ADOPTION_GUIDE.md).
> — **Maintaining the kit source repository?** → Go to [`documents/`](../documents/README.md) instead.
> — **Already installed and resuming work?** → Run `/context-session`, then `/context-status` if multiple features are active.

This folder is the adopter-facing surface that ships into downstream projects when they install CoreZero Nexus.

## Start Here

Choose the path that matches what you need right now:

1. Set up a new repo
   Read [ADOPTION_GUIDE.md](ADOPTION_GUIDE.md) and follow the greenfield flow.
2. Adopt into an existing repo
   Read [ADOPTION_GUIDE.md](ADOPTION_GUIDE.md) and follow the brownfield flow, including `spec-research`.
3. Resume work in an installed repo
   Run `/context-session`, then use `/context-status` if multiple features are active.
4. Implement a feature
   Use `/spec-requirements`, `/spec-plan`, `/spec-implement`, then `/harness-verify`.
5. Verify and close out work
   Use `/harness-verify`, then promote reusable knowledge with `/context-memory` if needed.

## Recommended First Path

1. Install the kit
2. Run `/starter-init`
3. Open or resume work with `/context-session`
4. Deliver through `/spec-requirements`, `/spec-plan`, and `/spec-implement`
5. Close out with `/harness-verify`

## Core Docs

- [ADOPTION_GUIDE.md](ADOPTION_GUIDE.md) — detailed greenfield and brownfield adoption flows
- [INSTALL.md](https://github.com/thaihai-swe/CoreZero-Nexus/blob/main/documents/INSTALL.md) — installer behavior, upgrade behavior, and shipped surface (source repo; not installed by default)
- [code-design.md](code-design.md) — shipped normative coding-policy guidance

## Key Surfaces

### Starter Inputs

| File | Purpose |
|---|---|
| [PRODUCT_SENSE.md](PRODUCT_SENSE.md) | Product vision, users, domain context, and success metrics |
| [GLOSSARY.md](GLOSSARY.md) | Shared vocabulary and naming conventions |
| [TECH_STACK_REFERENCE.md](TECH_STACK_REFERENCE.md) | LLM-friendly dependency and tool reference |
| [PROJECT_CONSTRAINTS.md](PROJECT_CONSTRAINTS.md) | Non-negotiable budgets, deployment, and security constraints |

### Continuity And Context

| File | Purpose |
|---|---|
| [architecture.md](architecture.md) | Durable architecture map for the adopter repo |
| [codemap.md](generated/codemap.md) | Generated file and subsystem map |
| [references-index.md](generated/references-index.md) | Generated cross-reference index |

### Quality And Governance

| File | Purpose |
|---|---|
| [code-design.md](code-design.md) | Normative coding-policy guidance |
| [GOVERNANCE.md](GOVERNANCE.md) | Approval, ownership, and review workflow rules |
| [QUALITY_POLICY.md](QUALITY_POLICY.md) | Quality gates, testing posture, and review standards |
| [RELIABILITY_POLICY.md](RELIABILITY_POLICY.md) | Reliability, observability, and incident expectations |
| [TECH_DEBT_REGISTER.md](TECH_DEBT_REGISTER.md) | Technical debt tracking and follow-through |



## Generated Files

`docs/generated/codemap.md` and `docs/generated/references-index.md` are produced by the `/harness-maintain` skill (templates live in `skills/harness-maintain/references/`). Re-run `/harness-maintain` whenever the repository structure changes significantly or a new subsystem is added. Do not hand-edit these files — regenerate them instead.

## Commands

Full public command reference: [documents/skills-guide.md](../documents/skills-guide.md)

## Harness Maintenance

To assess or repair the harness itself (not feature work), run `/harness-maintain`. The `assess` mode scores all 6 harness subsystems on a 1-5 scale and identifies the weakest areas. The `improve` mode generates a repair proposal for failing subsystems. Run this periodically or whenever the harness feels unreliable.
