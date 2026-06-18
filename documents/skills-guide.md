# Workflow And Skills Guide

This guide describes the current shipped commands and the reserved `source-only` marker.

## Shipped Commands

| Command | Role | Status |
|---|---|---|
| `/starter-init` | bootstrap a repository | shipped now |
| `/spec-research` | brownfield or unknown-behavior analysis | shipped now |
| `/spec-requirements` | define requirements and acceptance criteria | shipped now |
| `/spec-plan` | convert requirements into a safe execution plan | shipped now |
| `/spec-implement` | execute planned work task by task | shipped now |
| `/harness-verify` | verify proof, alignment, and closeout | shipped now |
| `/context-session` | manage feature-session continuity | shipped now |
| `/context-memory` | maintain durable repo memory | shipped now |
| `/context-status` | report multi-feature status and regenerate dashboard | shipped now |
| `/harness-maintain` | assess and improve the harness itself | shipped now |
| `/spec-adr` | capture durable architecture decisions | shipped now |
| `/code-review` | review implementation quality | shipped now |
| `/technical-docs` | generate grounded API and flow documentation | shipped now |
| `/codebase-documenter` | generate repo onboarding and architecture doc sets | shipped now |
| `/visualize` | generate SVG and Mermaid technical diagrams | shipped now |

## Default Delivery Flow

```text
/starter-init
/spec-research or /spec-requirements
/spec-plan
/spec-implement
/harness-verify
```

Governance, docs authoring, and visualization commands are shipped helpers. They are installed by default, but they are not required on every single feature path.

## Source-Only Marker

Use `source-only` only when a skill exists in `kit/` but is intentionally excluded from the installer surface. There are no current `source-only` skills in the shipped package.

## Shipping Rule

If a command is not listed in the shipped table above, it must not be described as part of the installed package.
