# Shipped Template Surface

This document maps the complete folder and file layout shipped to adopters after running the **CoreZero Nexus** installer.

> **Note:** For a conceptual overview of what each folder does, see [kit-map.md](kit-map.md). For the high-level system architecture, see [architecture.md](architecture.md). For ownership rules during upgrades, see [skills-guide.md](skills-guide.md).

---

## Shipped Directory Tree

When installed into an empty project directory, the shipped folder structure looks like this (derived from `kit/manifest.json`):

```text
├── AGENTS.md                     # Agent router and operating constraints
├── MASTER_INDEX.md               # Master routing index for memory
├── artifacts/
│   └── features/                 # Per-feature process state
├── docs/
│   ├── generated/
│   │   └── dashboard.html        # Visual interactive dashboard
│   ├── policies/
│   │   └── code-design.md        # Cross-cutting code design and architectural policies
│   ├── project/                  # Adopter-owned project docs
│   │   ├── architecture.md
│   │   ├── code-map.md
│   │   ├── glossary.md
│   │   ├── product-sense.md
│   │   ├── project-constraints.md
│   │   └── tech-stack.md
│   ├── rules/                    # Shipped rules and standards
│   │   ├── ponytail.md
│   │   ├── python.md
│   │   └── security.md
│   └── index.html                # Documentation portal
├── memories/
│   ├── domain/                   # Adopter-owned domain context packs
│   │   ├── anti-patterns.md
│   │   ├── boundaries.md
│   │   ├── glossary.md
│   │   ├── patterns.md

│   └── repo/                     # Durable repository memory
│       ├── adr-log.md
│       ├── core-policies.md
│       ├── harness-telemetry.md
│       ├── learned-heuristics.md
│       └── project-knowledge-base.md
├── scripts/
│   ├── context-loader.py         # Memory constraint enforcement
│   ├── generate-dashboard.py     # Dashboard generator
│   ├── harness/                  # Verification and telemetry scripts
│   └── install.sh                # Idempotent manifest-driven installer
└── skills/                       # Shipped skills (kit-managed)
    ├── _shared/
    ├── code-review/
    ├── codebase-documenter/
    ├── context-compact/
    ├── context-memory/
    ├── context-session/
    ├── context-status/
    ├── harness-maintain/
    ├── harness-verify/
    ├── ponytail/
    ├── spec-adr/
    ├── spec-implement/
    ├── spec-plan/
    ├── spec-requirements/
    ├── spec-research/
    ├── starter-init/
    ├── technical-docs/
    └── visualize/
```

## Source Of Truth

The exact files copied, overwritten, or preserved are defined in `kit/manifest.json`. That JSON file is the only canonical source of truth for the installer.
