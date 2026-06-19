# Kit Architecture

## Overview

CoreZero is organized around one shipped package and one maintainer surface.

---

## Product Boundaries

### 1. Installable package: `kit/`

This is the only surface that adopters receive. The package contains:

- **Runtime Entrypoints**: Standardized around the canonical, agent-agnostic `AGENTS.md` entrypoint.
- **Harness Scripts**: Shipped under `kit/scripts/harness/` (specifically the mechanical `gate-runner.sh` validation gate and the `telemetry-collector.sh` failure log collector).
- **Shipped Docs & Templates**: Seeded project documentation and templates.
- **Seeded Generated Placeholders**: Directory structures for feature artifacts and temporary execution files.
- **Shipped Memories**: Durable repository-wide configuration memories in `kit/memories/` (e.g. `core-policies.md`, `INDEX.md`).
- **Shipped Skills**: Task-specific agent directives in `kit/skills/` (e.g. `starter-init`, `spec-requirements`, `spec-plan`, `spec-implement`, `harness-verify`, `context-memory`).
- **Shipped Rules**: Syntactic, language, and quality policy rules.
- **Install & Validation Helpers**: Deployment scripts (`install.sh`) to configure adopter workspaces.

`kit/manifest.json` is the source of truth for this surface.

### 2. Maintainer and site surfaces: `documents/` and `page-document/`

These files explain, document, and publish the kit, but they are not installed into adopter repositories.

---

## Key Rules

- Shipped behavior changes belong in `kit/`.
- Maintainer explanations belong in `documents/`.
- Public site shell and landing content belong in `page-document/`.
- When shipped behavior changes, update `kit/manifest.json`, the relevant `SKILL.md`, and the maintainer docs in the same change wave.

---

## Entrypoint Layer & Agent Agnosticism

The toolkit strictly enforces an **agent-agnostic standard**.

All IDE-specific rule configurations, such as `CLAUDE.md`, `.cursorrules`, or custom editor configuration profiles, have been completely deprecated and removed from the codebase.

Instead, the kit relies on `AGENTS.md` in the workspace root as the single, canonical, agent-agnostic entrypoint for all AI coding agents. Any agent interacting with the workspace must read `AGENTS.md` first to understand the routing to specific modular skills and repository policies. This guarantees that adopters can run any modern AI coding agent without coupling their workspace to a specific vendor or IDE.

---

## Installed Delivery Path

The shipped package supports this compact path:

```text
/starter-init
/spec-requirements
/spec-plan
/spec-implement
/harness-verify
```

Supporting lifecycle commands:

- `/context-session`
- `/context-memory`
- `/context-status`
- `/spec-adr`
- `/harness-maintain`
- `/code-review`
- `/technical-docs`
- `/codebase-documenter`
- `/visualize`

The first five commands above remain the default feature-delivery loop. The other shipped commands support governance, documentation, and visualization when the task needs them.

---

## Source-Only Marker

Use the `source-only` marker only when a skill stays in `kit/` but is intentionally excluded from `kit/manifest.json`. No current shipped skill uses that marker.

---

## Verification Boundaries

Repo-level verification for packaging changes must cover:

- manifest entries resolve
- shipped doc links resolve
- installer dry-run succeeds
- real install smoke test succeeds
- installed target matches the manifest-declared surface
- release version files stay in sync across `VERSION`, `kit/VERSION`, and `kit/manifest.json`
