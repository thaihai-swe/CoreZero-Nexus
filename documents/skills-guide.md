# Workflow And Skills Guide

This guide describes the current shipped commands and the reserved `source-only` marker.

## Shipped Commands

| Command | Role | Status |
|---|---|---|
| `/starter-init` | bootstrap a repository and customize seeded memory files for the adopter project | shipped now |
| `/spec-research` | brownfield or unknown-behavior analysis | shipped now |
| `/spec-requirements` | define requirements and acceptance criteria | shipped now |
| `/spec-plan` | convert requirements into a safe execution plan | shipped now |
| `/spec-implement` | execute planned work task by task | shipped now |
| `/harness-verify` | verify proof, alignment, and closeout | shipped now |
| `/context-session` | manage feature-session continuity | shipped now |
| `/context-memory` | maintain durable repo memory; `--audit` subcommand checks file sizes, trigger relevance, stale references, and unused domain packs | shipped now |
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

## Memory Audit

Run `/context-memory --audit` to produce a structured report of memory system health. The audit checks:

- File sizes against the 600 / 800 / 1200 line thresholds in `core-policies.md`
- Domain pack trigger keyword relevance against the current codebase
- Stale references in memory files (paths or identifiers that no longer exist)
- Unused domain packs (no recent load events in telemetry or session extracts)
- Drift between findings and `memories/repo/INDEX.md` `## Promotion Watchlist`

Output is written to `artifacts/features/<slug>/memory-audit.md` (feature-scoped) or `docs/generated/memory-audit.md` (global). The audit produces a report only — promotions and rewrites stay manual or route through a regular `/context-memory` invocation.

## Source-Only Marker

Use `source-only` only when a skill exists in `kit/` but is intentionally excluded from the installer surface. There are no current `source-only` skills in the shipped package.

## Shipping Rule

If a command is not listed in the shipped table above, it must not be described as part of the installed package.
