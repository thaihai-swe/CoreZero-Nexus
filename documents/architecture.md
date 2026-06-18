# Kit Architecture

## Overview

CoreZero Nexus is organized around one shipped package and one maintainer surface.

## Product Boundaries

### 1. Installable package: `kit/`

This is the only surface that adopters receive. The package contains:

- runtime entrypoints
- shipped docs
- seeded project docs
- seeded generated placeholders
- shipped memories
- shipped skills
- shipped rules
- install and validation helpers

`kit/manifest.json` is the source of truth for this surface.

### 2. Maintainer and site surfaces: `documents/` and `page-document/`

These files explain, document, and publish the kit, but they are not installed into adopter repositories.

## Key Rules

- Shipped behavior changes belong in `kit/`.
- Maintainer explanations belong in `documents/`.
- Public site shell and landing content belong in `page-document/`.
- When shipped behavior changes, update `kit/manifest.json`, the relevant `SKILL.md`, and the maintainer docs in the same change wave.

## Installed Delivery Path

The shipped package supports this compact path:

```text
/starter-init
/spec-research or /spec-requirements
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

## Source-Only Marker

Use the `source-only` marker only when a skill stays in `kit/` but is intentionally excluded from `kit/manifest.json`. No current shipped skill uses that marker.

## Verification Boundaries

Repo-level verification for packaging changes must cover:

- manifest entries resolve
- shipped doc links resolve
- installer dry-run succeeds
- real install smoke test succeeds
- installed target matches the manifest-declared surface
- release version files stay in sync across `VERSION`, `kit/VERSION`, and `kit/manifest.json`
