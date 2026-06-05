# Rules

This directory contains per-language and per-domain rule files that give AI coding agents explicit, project-specific guidance beyond what is captured in `memories/repo/constitution.md` and `memories/repo/project-knowledge-base.md`.

## What Belongs Here

- **Per-language coding rules** — naming conventions, file layout expectations, preferred libraries, and style decisions specific to a language (e.g., `python.md`, `typescript.md`, `go.md`).
- **Per-domain rules** — coding standards specific to a domain area of the project (e.g., `api.md`, `database.md`, `frontend.md`).
- **Security rules** — concrete do/do-not patterns for handling secrets, auth, and external input in this project's stack (see `security.md`).

## What Does Not Belong Here

- Repo-wide normative mandates → `memories/repo/constitution.md`
- Descriptive architecture and stack patterns → `memories/repo/project-knowledge-base.md`
- Permission tiers and trust boundaries → `memories/repo/security-policy.md`
- Feature-specific implementation notes → `artifacts/features/<slug>/`

## How Agents Use These Files

Agents load rule files in this directory when the active task touches the matching language or domain. To make a rule file discoverable, add it to the `By-Intent` groups in `memories/repo/INDEX.md` with appropriate trigger keywords. For example:

```markdown
### Knowledge Group
Trigger keywords: python, typescript, go
Files: rules/python.md, rules/typescript.md
```

## Adding a Rule File

1. Create the file (e.g., `rules/typescript.md`).
2. Add it to the correct intent group in `memories/repo/INDEX.md`.
3. Keep rules concrete and operational — write "Use X in layer Y" rather than "Consider X".
4. Ground every rule in actual project patterns, not general best practices.

## Existing Files

| File | Scope |
|---|---|
| `python.md` | Python coding conventions and style rules |
| `security.md` | Cross-language security patterns and anti-patterns |
