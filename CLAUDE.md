# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

CoreZero is a spec-anchored AI software delivery framework. It ships an installable package (the "kit") that bootstraps AI-assisted software development workflows into downstream repositories.

**Two explicit products:**
- `kit/` — The installable adopter package (shipped surface)
- `documents/` + `page-document/` — Maintainer and public documentation

## Commands

### Installation

```bash
bash scripts/install.sh /path/to/target
```

### Kit Development / Validation

```bash
# Run harness gate-runner (auto-detects Node.js or Python)
bash kit/scripts/harness/gate-runner.sh

# Override with project-specific gates
# Create: scripts/harness/gate-runner.local.sh
```

### Dashboard Generation

```bash
python kit/scripts/generate-dashboard.py --root .
python kit/scripts/generate-dashboard.py --dry-run  # Check without writing
```

## Architecture

### Routing Hierarchy

1. **`AGENTS.md`** (repo root) — Agent entrypoint; read every session
2. **`INDEX.md`** (repo root) — Repo-level routing index for maintaining CoreZero itself
3. **`kit/MASTER_INDEX.md`** — Kit's memory router; load on demand by task intent

### Key Directories

| Path | Purpose |
|------|---------|
| `kit/skills/` | Agent capability contracts (SKILL.md per slash command) |
| `kit/memories/repo/` | Repository-level memory (policies, heuristics, knowledge base) |
| `kit/memories/domain/` | Domain context packs (glossary, patterns, anti-patterns) |
| `kit/docs/` | Shipped documentation surface |
| `kit/scripts/` | Installation and harness scripts |
| `artifacts/features/<slug>/` | Per-feature artifacts (specs, plans, progress, handoffs) |
| `documents/` | Maintainer-only documentation (not installed) |

### Shipped Skills (Slash Commands)

**Lifecycle:** `/starter-init` → `/spec-research` → `/spec-requirements` → `/spec-plan` → `/spec-implement` → `/harness-verify`

**Context:** `/context-session`, `/context-memory`, `/context-status`, `/context-compact`

**Quality:** `/code-review`, `/harness-maintain`, `/spec-adr`

**Docs:** `/technical-docs`, `/codebase-documenter`, `/visualize`

### 7-Phase Delivery Loop

1. Bootstrap (`/starter-init`)
2. Session START (`/context-session START`)
3. Requirements (`/spec-requirements`)
4. Planning (`/spec-plan`)
5. Implementation (`/spec-implement`)
6. Verification (`/harness-verify`)
7. Memory Sync (`/context-memory`, `/context-session END`)

## Normative Rules (CC-* Series)

Key rules from `kit/memories/repo/core-policies.md`:

- **CC-001**: Skill contracts (SKILL.md) are the single source of truth
- **CC-002**: Completion requires fresh evidence, not plausible diffs
- **CC-003**: Unknown stays unknown — mark `[UNKNOWN]`, never guess
- **CC-005**: Prefer surgical updates — touch only what the task requires
- **CC-006**: Spec is the source of truth for feature behavior
- **CC-012**: Spec mutations are logged, not silent

## Verification

The harness gate-runner (`kit/scripts/harness/gate-runner.sh`) auto-detects project type:
- **Node.js**: Runs `npm run lint`, `npm run typecheck`, `npm test` (if scripts exist)
- **Python**: Runs `flake8`, `mypy`, `pytest` (if tools available)
- **Override**: Create `scripts/harness/gate-runner.local.sh` for custom gates

## Session Defaults

- Feature artifacts: `artifacts/features/<slug>/`
- Progress logs: `artifacts/features/<slug>/progress.md`
- Handoffs: `artifacts/features/<slug>/handoff.md`
- Feature slug format: kebab-case
- Branch naming: `features/<name>`
- Checkpoint after completing each skill or major edit wave
- Stop and ask after two failed corrections on the same issue

## Memory Loading

Use intent-based routing per `kit/MASTER_INDEX.md`:
- **Always**: `core-policies.md`
- **By Intent**: Load specific files based on task keywords (architecture, security, domain, etc.)
- **By Debug**: Load telemetry and extracts only during debugging

Do not dump full project context. Use `MASTER_INDEX.md` to locate specific sub-indexes on demand.
