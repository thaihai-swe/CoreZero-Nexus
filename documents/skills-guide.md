# Workflow And Skills Guide

This guide describes the current shipped commands and the reserved `source-only` marker.

---

## Shipped Commands

| Command | Role | Status |
|---|---|---|
| `/starter-init` | Bootstrap a repository and customize seeded memory files for the adopter project | Shipped now |
| `/spec-research` | Brownfield or unknown-behavior analysis | Shipped now |
| `/spec-requirements` | Define requirements and acceptance criteria | Shipped now |
| `/spec-plan` | Convert requirements into a safe execution plan | Shipped now |
| `/spec-implement` | Execute planned work task by task | Shipped now |
| `/harness-verify` | Verify proof, alignment, and closeout | Shipped now |
| `/context-session` | Manage feature-session continuity | Shipped now |
| `/context-memory` | Maintain durable repo memory | Shipped now |
| `/context-compact` | Compress and garbage-collect oversized memory files to preserve token context | Shipped now |
| `/context-status` | Report multi-feature status and regenerate dashboard | Shipped now |
| `/harness-maintain` | Assess and improve the harness itself | Shipped now |
| `/spec-adr` | Capture durable architecture decisions | Shipped now |
| `/code-review` | Review implementation quality | Shipped now |
| `/technical-docs` | Generate grounded API and flow documentation | Shipped now |
| `/codebase-documenter` | Generate repo onboarding and architecture doc sets | Shipped now |
| `/visualize` | Generate SVG and Mermaid technical diagrams | Shipped now |
| `/ponytail` | Enforces simplicity-first coding — YAGNI, laziest effective solution, trims over-engineering. Intensity: lite / full (default) / ultra. | Shipped now |

---

## Default Delivery Flow

```text
/starter-init
/spec-research or /spec-requirements
/spec-plan
/spec-implement
/harness-verify
```

Governance, docs authoring, and visualization commands are shipped helpers. They are installed by default, but they are not required on every single feature path.

---

## Memory Audit

Run `/context-memory --audit` to produce a structured report of memory system health. The audit checks:

- File sizes against the soft warning threshold (800 lines) and hard limit (1200 lines) configured in `core-policies.md`
- Domain pack trigger keyword relevance against the current codebase
- Stale references in memory files (paths or identifiers that no longer exist)
- Unused domain packs (no recent load events in telemetry or session extracts)
- Drift between findings and `memories/repo/INDEX.md` `## Promotion Watchlist`

Output is written to `artifacts/features/<slug>/memory-audit.md` (feature-scoped) or `docs/generated/memory-audit.md` (global). The audit produces a report only — promotions and rewrites stay manual or route through a regular `/context-memory` or `/context-compact` invocation.

---

## Source-Only Marker

Use `source-only` only when a skill exists in `kit/` but is intentionally excluded from the installer surface. There are no current `source-only` skills in the shipped package.

---

## Shipping Rule

If a command is not listed in the shipped table above, it must not be described as part of the installed package.
