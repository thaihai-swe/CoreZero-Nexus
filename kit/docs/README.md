# Project Docs

This folder is the installed documentation surface for downstream repositories using CoreZero Nexus.

## Start Here

1. Fill in the adopter-owned files under [project/](project/).
2. Review the coding constraints in [rules/](rules/).
3. Use the shipped core workflow:
   `/starter-init` -> `/spec-research` or `/spec-requirements` -> `/spec-plan` -> `/spec-implement` -> `/harness-verify`
4. Use the governance bundle when needed:
   `/context-status`, `/context-compact`, `/harness-maintain`, `/spec-adr`
5. Use the docs authoring bundle when the repo needs durable documentation outputs:
   `/technical-docs`, `/codebase-documenter`
6. Use `/visualize` when Mermaid or polished SVG diagrams materially improve clarity.

## Installed Surfaces

### First-read docs

- [policies/code-design.md](policies/code-design.md) — kit-managed design policy
- [rules/](rules/) — language-specific coding and security rules

### Adopter-owned project docs

- [project/architecture.md](project/architecture.md)
- [project/product-sense.md](project/product-sense.md)
- [project/glossary.md](project/glossary.md)
- [project/tech-stack-reference.md](project/tech-stack-reference.md)
- [project/project-constraints.md](project/project-constraints.md)

### Generated placeholders

- [generated/codemap.md](generated/codemap.md)
- [generated/dashboard.html](generated/dashboard.html)
- [generated/references-index.md](generated/references-index.md)

The `generated/` files are seeded placeholders until your project refreshes them.
Use `/harness-maintain` to rebuild `codemap` and `references-index`, and `/context-status` to regenerate the dashboard when your project adopts those governance surfaces.

## Output Ownership

- `/technical-docs` owns feature-scoped API and flow documentation outputs.
- `/codebase-documenter` owns repo onboarding and architecture doc sets.
- `/visualize` owns optional SVG and Mermaid diagram outputs.
