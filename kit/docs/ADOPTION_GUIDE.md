# Adoption Guide

Use this guide to adopt the shipped CoreZero Nexus surface into a downstream project.

Read [INSTALL.md](INSTALL.md) first for installer mechanics. Use this guide for the operating flow after install.

## Greenfield Adoption

1. Install the kit
2. Run `/starter-init`
3. Run `/context-session`
4. Deliver the first feature with:

```text
/spec-requirements
/spec-plan
/spec-implement
/harness-verify
```

## Brownfield Adoption

1. Install the kit
2. Run `/starter-init`
3. Run `/spec-research` before changing behavior
4. Capture durable findings with `/context-memory`
5. Open the active session with `/context-session`
6. Deliver the smallest safe slice through the spec -> plan -> implement -> verify flow

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
- If the harness surface looks incomplete or drifted, run `bash scripts/doctor.sh`.
- If durable memory is stale, run `/context-memory`.
- If the installer behavior looks wrong, re-run `bash scripts/install.sh /path/to/your/project --dry-run`.
