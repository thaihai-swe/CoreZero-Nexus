# Domain Context Pack

Domain packs add project-specific semantic context to the memory router. Each pack captures
the ubiquitous language, proven patterns, anti-patterns, and boundary rules for a specific
business or technical domain (e.g., payments, web-api, data-pipeline, auth).

Domain packs live in `memories/domain/`. The memory router loads a pack when
the active task's keywords match the pack's declared triggers.

> [!NOTE]
> Domain packs represent context for a specific *bounded subdomain* within the app. They do not replace or duplicate project-wide documentation. Use `docs/project/glossary.md` for project-wide dictionary terms, `docs/project/architecture.md` for top-level component maps, and `docs/project/tech-stack-reference.md` for global dependencies.

## Directory Structure

```
memories/domain/
├── README.md           ← this file
├── glossary.md       ← ubiquitous language + trigger keywords (REQUIRED)
├── patterns.md       ← proven patterns for this domain
├── anti-patterns.md  ← failure modes and what not to do
├── boundaries.md     ← what this domain owns, what it defers to others
└── spec.md           ← optional: canonical domain spec (REQ/AC contract)
```

The optional `spec.md` is the single source of truth for the domain's
behavior. Features that change cross-cutting domain behavior file a `## Delta`
in their feature `spec.md` (ADDED / MODIFIED / REMOVED requirements), and
`/harness-verify` post-ship sync merges the delta into this canonical file.
See `skills/spec-requirements/references/delta-spec-operations.md` for the
merge rules. Skip `spec.md` for domains where there is no shared contract to
anchor.

## Creating a Domain Pack

1. Create directory: `memories/domain/`
2. Create all 4 required files using the schema below.
3. Optionally create `spec.md` if the domain has a cross-cutting REQ/AC contract.
4. Add trigger keywords to `glossary.md` frontmatter.
5. Add the domain to `memories/repo/INDEX.md` under `## By Domain Packs`.

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

### boundaries.md

What this domain owns, what it explicitly does NOT own, and how it integrates
with adjacent domains.

- **Owns:** What this domain is responsible for
- **Does not own:** What this domain defers to other domains
- **Integration contracts:** How this domain's outputs become other domains' inputs

### spec.md (optional)

Canonical REQ/AC contract for the domain — the durable list of behaviors that
all features in this domain must respect. Same shape as a feature `spec.md`
(REQ-### with priority and acceptance notes, AC-### with proof targets) but
without feature-specific scope sections.

Use it when:
- Multiple features touch the same set of REQs (auth, billing, data model).
- Cross-feature regressions are a real risk.
- Brownfield refactors need a stable map of "what already exists."

Skip it when:
- The domain has no shared contract — only ad-hoc utilities.
- The codebase is small enough that the source-of-truth can stay in code.

When present, feature specs that change this domain's behavior file a
`## Delta` (ADDED / MODIFIED / REMOVED). The merge happens in
`/harness-verify` post-ship sync. See
`skills/spec-requirements/references/delta-spec-operations.md` for rules.

## Lifecycle

- Domain packs are **adopter-owned** — the kit seeds the schema but does not prescribe content.
- Update packs during `/context-memory` Post-Ship Sync when new patterns emerge from features.
- Promote durable patterns from `artifacts/features/<slug>/session-extracts.md` into the domain pack.
- Remove outdated entries when the codebase no longer uses a pattern.
