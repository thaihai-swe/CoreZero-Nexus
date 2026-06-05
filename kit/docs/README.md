# Project Docs

This folder is the installed documentation surface for downstream projects using CoreZero Nexus.

## Start Here

1. Install the kit
2. Read [INSTALL.md](INSTALL.md)
3. For brownfield/legacy repositories, run `/brownfield-init` first to map existing code debt
4. Run `/starter-init`
5. Start the first feature with `/spec-requirements` or `/spec-research`
6. Use `/context-session` only after the feature slug already exists
7. Deliver through `/spec-plan`, `/spec-implement`
8. Close out with `/harness-verify`

## Core Docs

- [ADOPTION_GUIDE.md](ADOPTION_GUIDE.md) — greenfield and brownfield adoption flow
- [INSTALL.md](INSTALL.md) — installer behavior, upgrade behavior, and installed surface
- [code-design.md](code-design.md) — normative coding-policy guidance

## Starter Inputs

- [PRODUCT_SENSE.md](PRODUCT_SENSE.md)
- [GLOSSARY.md](GLOSSARY.md)
- [TECH_STACK_REFERENCE.md](TECH_STACK_REFERENCE.md)
- [PROJECT_CONSTRAINTS.md](PROJECT_CONSTRAINTS.md)

## Continuity And Context

- [architecture.md](architecture.md)
- [generated/codemap.md](generated/codemap.md)
- [generated/dashboard.html](generated/dashboard.html)
- [generated/references-index.md](generated/references-index.md)
- `memories/repo/*`

## Quality And Repair

- [GOVERNANCE.md](GOVERNANCE.md)
- [QUALITY_POLICY.md](QUALITY_POLICY.md)
- [RELIABILITY_POLICY.md](RELIABILITY_POLICY.md)
- [TECH_DEBT_REGISTER.md](TECH_DEBT_REGISTER.md)
- `bash scripts/doctor.sh` — repair and drift check

## Generated Files

`docs/generated/codemap.md` and `docs/generated/references-index.md` are generated-reference surfaces. Refresh them with `/harness-maintain` when the repository structure changes materially.
