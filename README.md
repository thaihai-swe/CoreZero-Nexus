# CoreZero Nexus

CoreZero Nexus is a starter kit for coding-agent workflows that need durable context, specification-driven delivery, and a mechanical verification harness.

It combines four packs in one install:

- `Project Starter` for bootstrap and baseline capture
- `Context Engineering` for session continuity and durable memory
- `Spec-Driven Development` for research, requirements, planning, and implementation
- `Harness Engineering` for verification, drift detection, and repair

## Guided Start

```bash
curl -fsSL https://raw.githubusercontent.com/thaihai-swe/CoreZero-Nexus/main/scripts/install.sh \
  | bash -s -- /path/to/your/project
```

Then in your AI agent:

```text
/starter-init
/spec-research     # brownfield or unknown behavior
/spec-requirements
/spec-plan
/spec-implement
/harness-verify
```

## Choose Your Surface

- Adopting the kit into a project: [kit/docs/README.md](kit/docs/README.md)
- Maintaining or evolving the kit itself: [documents/README.md](documents/README.md)

## What Ships Into Adopter Projects

The installed surface comes from `kit/` and includes:

- `kit/AGENTS.md` and `kit/HARNESS_CARD.md`
- `kit/docs/README.md`, `kit/docs/ADOPTION_GUIDE.md`, `kit/docs/INSTALL.md`, `kit/docs/code-design.md`, and `kit/docs/system-specs/README.md`
- seeded project docs under `kit/docs/*.md`
- generated-reference placeholders under `kit/docs/generated/*`
- `kit/memories/repo/*`
- `kit/skills/**`
- `kit/rules/*.md`
- `kit/scripts/install.sh`, `kit/scripts/doctor.sh`, and `kit/scripts/check-surface-truth.py`
- `kit/.github/workflows/harness-check.yml`

Maintainer documentation under `documents/` stays in this source repository and is not part of the default installed package.


## The Four Packs

| Pack | Purpose | Primary commands |
|---|---|---|
| **Project Starter** | Bootstrap a repo so any agent can orient fast | `/starter-init` |
| **Context Engineering** | Keep sessions resumable and lean across context windows | `/context-session`, `/context-memory`, `/context-status` |
| **Spec-Driven Development** | Turn requests into researched, specified, and implemented work | `/spec-research`, `/spec-requirements`, `/spec-plan`, `/spec-implement`, `/spec-adr` |
| **Harness Engineering** | Enforce proof, quality constraints, and continuous improvement | `/harness-verify`, `/harness-maintain` |

Full workflow, command taxonomy, and internal skill mapping: [documents/skills-guide.md](documents/skills-guide.md)

## Learn More

- Adopter docs: [kit/docs/README.md](kit/docs/README.md)
- Installation details: [kit/docs/INSTALL.md](kit/docs/INSTALL.md)
- Maintainer docs: [documents/README.md](documents/README.md)
- Workflow taxonomy: [documents/skills-guide.md](documents/skills-guide.md)
- Shipped surface map: [documents/TEMPLATE_SURFACE.md](documents/TEMPLATE_SURFACE.md)
