# CoreZero Nexus

CoreZero Nexus is a pack-based framework for teams that want AI-assisted delivery without drift, context loss, or vague workflow glue.

It combines four capabilities in one install:

- `Project Starter` for bootstrapping AI-ready project structure and operating defaults
- `Context Engineering` for session continuity, memory routing, and durable context
- `Spec-Driven Development` for turning requests into researched, specified, planned, and implemented work
- `Harness Engineering` for verification, evaluation, constraints, and reliability

## Guided Start

Use this public workflow first:

1. Install the kit
2. Run `starter-init`
3. Open or resume work with `context-session`
4. Deliver through `spec-requirements`, `spec-plan`, and `spec-implement`
5. Close out with `harness-verify`

```bash
curl -fsSL https://raw.githubusercontent.com/thaihai-swe/AI-agents-dev-kits/main/scripts/install.sh \
  | bash -s -- /path/to/your/project
```

Then in your AI agent:

```text
/starter-init
/context-session
/spec-requirements
/spec-plan
/spec-implement
/harness-verify
```

## Choose Your Surface

- Adopting the kit into a project: [docs/README.md](kit/docs/README.md)
- Maintaining or evolving the kit itself: [documents/README.md](documents/README.md)

## What Ships Into Adopter Projects

The default installed surface is the adopter-facing package under `kit/docs/`, plus the runtime and workflow assets the kit needs:

- `kit/docs/README.md`, `kit/docs/ADOPTION_GUIDE.md`, `kit/docs/INSTALL.md`
- `kit/docs/templates/*`
- `kit/docs/generated/*`
- `kit/docs/architecture.md`
- `kit/skills/**`
- `kit/rules/*.md`
- `kit/AGENTS.md`, `kit/HARNESS_CARD.md`, and `kit/memories/repo/*`
- `kit/scripts/install.sh` and `kit/.github/workflows/harness-check.yml`

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

- Adopter docs: [docs/README.md](kit/docs/README.md)
- Installation details: [docs/INSTALL.md](kit/docs/INSTALL.md)
- Maintainer docs: [documents/README.md](documents/README.md)
- Workflow and command taxonomy: [documents/skills-guide.md](documents/skills-guide.md)
- End-to-end lifecycle walkthrough: [documents/end-to-end-tutorial.md](documents/end-to-end-tutorial.md)

python3 -m http.server 8080
