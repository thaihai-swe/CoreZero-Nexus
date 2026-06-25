# Shipped Template Surface

This document maps the complete folder and file layout shipped to adopters after running the **CoreZero Nexus** installer.

> **Note:** For a conceptual overview of what each folder does, see [kit-map.md](kit-map.md). For the high-level system architecture, see [architecture.md](architecture.md). For ownership rules during upgrades, see [skills-guide.md](skills-guide.md).

---

## Shipped Directory Tree

When installed into an empty project directory, the shipped folder structure looks like this (derived from `kit/manifest.json`):

```text
├── AGENTS.md                     # Agent router and operating constraints
├── MASTER_INDEX.md               # Master routing index for memory
├── .corezero-version             # Installed semver stamp
├── artifacts/
│   └── features/                 # Per-feature process state
├── docs/
│   ├── generated/
│   │   └── dashboard.html        # Visual interactive dashboard
│   ├── policies/
│   │   └── code-design.md        # Cross-cutting code design policies
│   ├── project/
│   │   ├── adr/                  # ADR registry (overwrite)
│   │   │   ├── index.md
│   │   │   └── 0001-example.md
│   │   ├── agent-capabilities.md # Adopter-owned seed
│   │   ├── architecture.md       # Adopter-owned seed
│   │   ├── code-map.md           # Adopter-owned seed
│   │   ├── glossary.md           # Adopter-owned seed
│   │   ├── harness-config.yaml   # Phase precondition config (overwrite; not memories/repo/harness-config.md)
│   │   ├── product-sense.md      # Adopter-owned seed
│   │   ├── project-constraints.md # Adopter-owned seed
│   │   ├── spec-schema.json      # JSON schema (overwrite)
│   │   └── tech-stack.md         # Adopter-owned seed
│   ├── rules/                    # Shipped rules and standards
│   │   ├── README.md             # How-to for adding rule files
│   │   ├── ponytail.md           # YAGNI ladder
│   │   ├── python.md             # Python conventions
│   │   └── security.md           # Security rules
│   └── index.html                # Documentation portal
├── memories/
│   ├── domain/                   # Domain context packs
│   │   ├── README.md             # Pack schema
│   │   └── example/              # Example pack
│   │       ├── anti-patterns.md
│   │       ├── boundaries.md
│   │       ├── glossary.md
│   │       └── patterns.md
│   └── repo/                     # Durable repository memory
│       ├── archive/              # Cold storage
│       │   └── deprecated-heuristics.md
│       ├── adr-log.md
│       ├── core-policies.md
│       ├── harness-config.md
│       ├── harness-telemetry.md
│       ├── learned-heuristics.md
│       └── project-knowledge-base.md
├── scripts/
│   ├── context-loader.py         # MVC context loader CLI
│   ├── generate-dashboard.py     # Dashboard generator
│   ├── render_template.py        # Template render CLI
│   ├── template_convert.py       # Template converter CLI
│   ├── core/                     # Python engine layer
│   │   ├── __init__.py
│   │   ├── context_engine.py     # Context loading engine
│   │   ├── harness.py            # Harness engine (gates, lifecycle)
│   │   ├── template_engine.py    # Template rendering engine
│   │   └── _lib/                 # Shared helpers
│   │       ├── __init__.py
│   │       ├── token_counter.py  # Token estimation
│   │       └── yaml_reader.py    # Pure-Python YAML reader
│   ├── harness/                  # Verification and telemetry scripts
│   │   ├── doctor.sh             # Kit self-diagnosis
│   │   ├── gate-runner.sh        # Mechanical gate runner
│   │   ├── gate-runner.local.example.sh  # Local gate override template
│   │   ├── phase-gate.sh         # Phase precondition validation
│   │   ├── telemetry-collector.sh  # Append failure record
│   │   ├── telemetry-count.sh    # Count open telemetry records
│   │   ├── telemetry-update.sh   # Update telemetry record fields
│   │   ├── telemetry-render.sh   # Regenerate harness-telemetry.md
│   │   ├── harness-lifecycle.sh  # Phase transition/state
│   │   ├── _lib/root.sh          # Repo root resolution helper
│   │   └── plugins/              # Harness plugin extensibility
│   └── install.sh                # Idempotent manifest-driven installer
└── skills/                       # 17 shipped skills (kit-managed)
    ├── _shared/                  # Shared resources
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
