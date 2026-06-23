# Domain Packs

Each domain subdirectory under `memories/domain/` is a self-contained domain pack with 4 required files:

| File | When to load | Purpose |
|---|---|---|
| `glossary.md` | 1+ trigger keywords match | Ubiquitous language — terms, definitions, examples |
| `patterns.md` | Planning or implementing in this domain | Proven implementation patterns |
| `anti-patterns.md` | Code review, verification, debugging | Known failure modes to avoid |
| `boundaries.md` | Cross-domain calls, schema migrations, integration | What the domain owns, its contracts, and invariants |

## Directory schema

```
memories/domain/
  <name>/
    glossary.md     — frontmatter with `domain:` and `triggers:` arrays
    patterns.md     — reusable implementation patterns
    anti-patterns.md — failure modes to prevent
    boundaries.md   — ownership, contracts, invariants
```

Trigger keywords in `glossary.md` frontmatter are used by `/context-session` and `MASTER_INDEX.md` to decide when to load each pack.

## Shipped example

See `memories/domain/example/` for a worked schema demo. Replace it with a real domain pack.
