# Adoption Guide

Use this guide to adopt the shipped CoreZero Nexus surface into a downstream project.

Read [INSTALL.md](INSTALL.md) first for installer mechanics. Use this guide for the operating flow after install.

## Greenfield Adoption

1. Install the kit
2. Run `/starter-init`
3. Start the first feature with:

```text
/spec-requirements
/spec-plan
/spec-implement
/harness-verify
```

4. Use `/context-session` only after the feature slug already exists and you need `START`, `CHECKPOINT`, or `END` session lifecycle management.

## Brownfield Adoption

1. Install the kit
2. Run `/starter-init`
3. Run `/spec-research` before changing behavior
4. Produce a brownfield readiness map in `artifacts/features/<slug>/analysis.md` covering preserved behavior inventory, subsystem boundaries, reuse patterns, risk register, baseline proof surface, and migration constraints
5. Capture durable findings with `/context-memory` when the map surfaces reusable repo knowledge
6. Run `/spec-requirements` to lock the first safe slice against the brownfield constraints
7. Deliver through `/spec-plan` -> `/spec-implement` -> `/harness-verify`
8. Use `/context-session` only after the feature slug already exists and the work needs session resume, checkpoint, or handoff management

## Starter Surface

Review these files after install:

- [PRODUCT_SENSE.md](PRODUCT_SENSE.md)
- [GLOSSARY.md](GLOSSARY.md)
- [TECH_STACK_REFERENCE.md](TECH_STACK_REFERENCE.md)
- [PROJECT_CONSTRAINTS.md](PROJECT_CONSTRAINTS.md)
- [architecture.md](architecture.md)
- [code-design.md](code-design.md)

## Troubleshooting

- If `/starter-init` stops midway, re-run it. Seeded files are copied only when missing.
- If the harness surface looks incomplete, drifted, or the lifecycle guidance contradicts the skills, run `bash scripts/doctor.sh`.
- If durable memory is stale, run `/context-memory`.
- If the installer behavior looks wrong, re-run `bash scripts/install.sh /path/to/your/project --dry-run`.
