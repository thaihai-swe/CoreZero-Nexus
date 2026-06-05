# Domain Context Packs

Domain packs add project-specific semantic context to the memory router. Each pack captures
the ubiquitous language, proven patterns, anti-patterns, and boundary rules for a specific
business or technical domain (e.g., payments, web-api, data-pipeline, auth).

Domain packs live in `memories/domains/<name>/`. The memory router loads a pack when
the active task's keywords match the pack's declared triggers.

## Directory Structure

```
memories/domains/
├── README.md           ← this file
└── <domain-name>/
    ├── glossary.md       ← ubiquitous language + trigger keywords (REQUIRED)
    ├── patterns.md       ← proven patterns for this domain
    ├── anti-patterns.md  ← failure modes and what not to do
    └── boundary-rules.md ← what this domain owns, what it defers to others
```

## Creating a Domain Pack

1. Create directory: `memories/domains/<your-domain-name>/`
2. Create all 4 required files using the schema below.
3. Add trigger keywords to `glossary.md` frontmatter.
4. Add the domain to `memories/repo/INDEX.md` under `## By Domain Packs`.

See `memories/domains/example/` for a worked example.

## Trigger Keyword Rules

- Keywords are declared in `glossary.md` YAML frontmatter under `triggers:`.
- The memory router loads a pack when **3 or more** of its trigger keywords match
  the active task description (high-confidence load).
- With 1–2 matches (low confidence), only `glossary.md` is loaded (partial load).
- With 0 matches, the pack is skipped entirely.

## File Schema

### glossary.md

Frontmatter:
```yaml
domain: <name>
triggers: [keyword1, keyword2, keyword3, keyword4, keyword5]
```

Body: Ubiquitous language table — terms the agent must use consistently when working
in this domain. One row per term.

| Term | Definition | Example Usage |
|---|---|---|

### patterns.md

Proven implementation patterns for this domain. Each pattern entry:
- **Pattern name** (bold heading)
- When to use it
- Key implementation notes
- Citation (file or PR where this was established)

### anti-patterns.md

Known failure modes and what NOT to do. Each entry:
- **Anti-pattern name** (bold heading)
- Why it fails in this domain
- What to do instead
- Citation (incident, review, or post-mortem)

### boundary-rules.md

What this domain owns, what it explicitly does NOT own, and how it integrates
with adjacent domains.

- **Owns:** What this domain is responsible for
- **Does not own:** What this domain defers to other domains
- **Integration contracts:** How this domain's outputs become other domains' inputs

## Lifecycle

- Domain packs are **adopter-owned** — the kit seeds the schema but does not prescribe content.
- Update packs during `/context-memory` Post-Ship Sync when new patterns emerge from features.
- Promote durable patterns from `artifacts/features/<slug>/session-extracts.md` into the appropriate domain pack.
- Remove outdated entries when the codebase no longer uses a pattern.
