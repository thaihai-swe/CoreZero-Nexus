# Shipped Template Surface

This document maps the complete folder and file layout generated in your project after running the **CoreZero Nexus** installer.

---

## Shipped Directory Tree

When installed into an empty project directory, the folder structure looks like this:

```text
├── .github/
│   └── workflows/
│       └── harness-check.yml         # CI workflow enforcing verification/review status
├── artifacts/
│   └── features/                     # Per-feature process state (status, spec, plan, tasks)
├── docs/
│   ├── generated/
│   │   ├── codemap.md                # Generated structural map of your codebase
│   │   ├── dashboard.html            # [New] Visual interactive dashboard
│   │   └── references-index.md       # Generated cross-file reference index
│   ├── system-specs/                 # Cross-cutting system specs (output of /spec-requirements System Spec Mode)
│   │   └── README.md                 # Explains system specs purpose and workflow
│   ├── ADOPTION_GUIDE.md             # Greenfield and brownfield onboarding guide
│   ├── INSTALL.md                    # Installer behavior, upgrades, and rollback
│   ├── README.md                     # Start page and entrypoint for the adopter surface
│   ├── architecture.md               # System architecture baseline
│   ├── code-design.md                # Shipped normative coding-policy guidance
│   ├── GLOSSARY.md                   # Naming conventions and shared vocabulary
│   ├── GOVERNANCE.md                 # Review, approval, and ownership workflow rules
│   ├── PRODUCT_SENSE.md              # Vision, user context, and success metrics
│   ├── PROJECT_CONSTRAINTS.md        # Budgets, deployments, and security constraints
│   ├── QUALITY_POLICY.md             # Testing posture and quality gate rules
│   ├── RELIABILITY_POLICY.md         # Incident response, SLA, and observability rules
│   ├── TECH_DEBT_REGISTER.md         # Tech debt tracking template
│   └── TECH_STACK_REFERENCE.md       # LLM-friendly dependencies and tool reference
├── memories/
│   ├── domains/
│   │   ├── README.md                 # Domain-pack schema and trigger rules
│   │   └── example/
│   │       ├── anti-patterns.md
│   │       ├── boundary-rules.md
│   │       ├── glossary.md
│   │       └── patterns.md
│   └── repo/
│       ├── adr-log.md                # Index registry of Architecture Decision Records (ADRs)
│       ├── constitution.md           # Repository normative rules and agent guidelines
│       ├── domain-specs.md           # Ubiquitous language definitions for the project
│       ├── harness-config.md         # Commands, paths, and adaptive rigor settings
│       ├── INDEX.md                  # Always-loaded memory router and phase matrix
│       ├── learned-heuristics.md     # Evidence-backed developer/agent instincts
│       ├── observability-log.md      # Auto-tier YAML failure log + trend summary
│       ├── project-knowledge-base.md # Durable patterns, boundaries, and reusable knowledge
│       └── security-policy.md        # Trust boundaries, permissions, and sandbox policies
├── rules/
│   ├── python.md                     # Language-specific coding standards for Python
│   ├── security.md                   # Project security and sanitization standards
├── scripts/
│   ├── check-surface-truth.py        # Validates shipped paths and router constraints
│   ├── doctor.sh                     # Repair and drift-check entrypoint
│   ├── generate-dashboard.py         # Dashboard generator script
│   ├── install.sh                    # Idempotent manifest-driven installer script
│   ├── parse-observability.py        # Observability log parser script
├── skills/
│   ├── _shared/                      # Shared rigor profiles, status definitions, diagrams
│   ├── code-review/                  # Google-standard code review skill
│   ├── codebase-documenter/          # Onboarding README generation skill
│   ├── context-memory/               # Memory triage, post-ship sync, and router skill
│   ├── context-session/              # Session START, CHECKPOINT, and END lifecycle skill
│   ├── context-status/               # Multi-feature project-wide reporting skill
│   ├── harness-maintain/             # Harness assessment and self-improvement skill
│   ├── harness-verify/               # Mechanical verification and alignment gate skill
│   ├── spec-adr/                     # Architectural decision logs generation skill
│   ├── spec-implement/               # Surgical implementation task runner skill
│   ├── spec-plan/                    # Plan and task list generation skill
│   ├── spec-requirements/            # intake, grilling, and spec authoring skill
│   ├── spec-research/                # Brownfield mapping and diagnosis skill
│   ├── starter-init/                 # Harness initialization and prefilling skill
│   ├── technical-docs/               # API contract and event flow documentation skill
│   └── visualize/                    # SVG and Mermaid diagram generation skill
├── AGENTS.md                         # Agent router and operating constraints
└── HARNESS_CARD.md                   # Single-page harness configuration metadata
```

---

## File Categories & Installation Posture

Files copied during installation belong to one of three categories defined in `manifest.json`:

### 1. Kit-Managed Content (`overwrite`)
*Folders/Files:* `skills/**`, `rules/*.md`, `scripts/*.sh`, `scripts/*.py`, `scripts/evals/**`, `docs/{README,ADOPTION_GUIDE,INSTALL,code-design}.md`, `docs/system-specs/README.md`, `.github/workflows/harness-check.yml`
*Posture:* Overwritten on install. These are core kit tools and guides that update automatically when upgrading the CoreZero Nexus.

### 2. Seeding Content (`copyIfMissing`)
*Folders/Files:* `AGENTS.md`, `HARNESS_CARD.md`, `memories/repo/INDEX.md`, `memories/repo/constitution.md`, `memories/repo/security-policy.md`, `memories/repo/learned-heuristics.md`, `memories/repo/project-knowledge-base.md`, `memories/repo/harness-config.md`, `memories/repo/domain-specs.md`, `memories/repo/observability-log.md`, `memories/repo/adr-log.md`, `memories/domains/README.md`, `memories/domains/example/*`, `docs/architecture.md`, `docs/{PRODUCT_SENSE,PROJECT_CONSTRAINTS,GLOSSARY,GOVERNANCE,RELIABILITY_POLICY,QUALITY_POLICY,TECH_DEBT_REGISTER,TECH_STACK_REFERENCE}.md`, `docs/generated/*`
*Posture:* Copied only if they do not already exist in the target project. If they exist, they are preserved so you can customize them for your specific project.

### 3. User Content & Workspaces (`preserve`)
*Folders/Files:* `memories/repo/` content, `artifacts/` features state, `.corezero-version`
*Posture:* Never modified or deleted by the installer. These files contain your active feature branches, development artifacts, and custom configuration settings.

Files under `memories/repo/brownfield/` are not seeded by install. They are created later by
`/starter-init` (Phase A) when a repository needs the archaeology pass.

---

## Document Updates & Ownership Matrix

This section defines the ownership lifecycle of files under the `docs/` directory: whether they are static/read-only, updated automatically by skills, or collaboratively maintained.

| Path / File | Ownership Category | Update Trigger | Owner / Skill |
|---|---|---|---|
| `docs/README.md` | Static (Read-Only) | Upgrades only | Kit Installer |
| `docs/ADOPTION_GUIDE.md` | Static (Read-Only) | Upgrades only | Kit Installer |
| `docs/INSTALL.md` | Static (Read-Only) | Upgrades only | Kit Installer |
| `docs/code-design.md` | Static (Read-Only) | Upgrades only | Kit Installer |
| `docs/architecture.md` | Collaborative | Init + Knowledge Sweep | `/starter-init` / `/context-memory` |
| `docs/generated/codemap.md` | Tool-Generated | Repo structure change | `/harness-maintain` |
| `docs/generated/references-index.md` | Tool-Generated | Reference mapping update | `/harness-maintain` |
| `docs/generated/dashboard.html` | Tool-Generated | Status update | `/context-status` |

### Detailed Ownership Lifecycles

#### 1. Static Documents
These documents serve as standard guides and routers for the CoreZero Nexus. They are written by kit maintainers and **should never be edited manually or by local project skills**:
- `README.md`, `ADOPTION_GUIDE.md`, and `INSTALL.md`.

#### 2. Tool-Generated Indexes
These are codebase index files. They are **written and updated exclusively by automation skills** and should not be modified manually:
- `docs/generated/codemap.md` and `docs/generated/references-index.md` (Updated via the codebase indexers in `/harness-maintain`).
- `docs/generated/dashboard.html` (Updated via status runner in `/context-status`).

#### 3. Collaborative Architecture Map
- `docs/architecture.md` is initialized and pre-filled from code structure analysis during `/starter-init`. During feature delivery, if a verification passes and triggers a knowledge sync, the `/context-memory` Post-Ship Sync will offer diff proposals. Humans can refine, edit, or customize the file at any time.

---

## Adopter Documents Ownership Lifecycle (`docs/`)

Project-level policy documents copied to `docs/` have distinct pre-fill levels and maintainer rules. All of them support initial seeding by skills and subsequent human refinement.

### Tier 1 — Skill-Pre-Filled from Code Evidence (User refines later)
These files are **automatically analyzed and drafted by the `/starter-init` skill** at initialization time, and subsequently customized by developers:
- **`TECH_STACK_REFERENCE.md`** — Filled by scanning package/config files (`package.json`, `Cargo.toml`, etc.).
- **`QUALITY_POLICY.md`** — Filled by scanning test configurations, linter settings, and rules.
- **`PROJECT_CONSTRAINTS.md`** — Filled by scanning build pipelines, container pins, and CI environments.

### Tier 2 — Skill Asks Clarifying Questions (User-owned context)
These files require business or product decisions. The `/starter-init` skill **asks 2–4 focused questions** to pre-fill initial content, leaving the rest marked `[USER REVIEW NEEDED]` for manual developer editing:
- **`PRODUCT_SENSE.md`** (Audience, objectives, metrics)
- **`GLOSSARY.md`** (Domain glossary and terminology)
- **`GOVERNANCE.md`** (Approvers, review gates)
- **`RELIABILITY_POLICY.md`** (SLOs, acceptable downtime bounds)

### Tier 3 — Populated Later (User-maintained or verified)
These are not processed at initialization time, but are maintained during development:
- **`TECH_DEBT_REGISTER.md`** — Updated by the `/harness-verify` fallow pass during closeout, and `/harness-maintain` Improve Mode.
