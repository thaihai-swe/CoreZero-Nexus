# Master Index

> Always-loaded master routing index. Keep under 100 lines.
> Read this at session start to locate domain-specific and category-specific index files. Do not load all files at session start. Load them only when the task requires them.

## Context Indexes (load on demand)

| File | Contents | When to load |
|------|----------|--------------|
| `memories/repo/INDEX.md` | Index of all repository memories, rules, and domain-specific memories, including trigger keywords and phase loading matrices. | To locate specific rules, heuristics, constraints, or architecture files matching the active task. |
| `docs/generated/codemap.md` | Generated map of code locations, file structures, counts, roots, and component domains. | Before any implementation task: new file, new route, new component. |
| `docs/generated/references-index.md` | Generated index of cross-file references and dependencies. | When tracing dependencies or references across files. |
| `rules/*.md` | Per-language and per-domain coding rules (e.g., Python style, security rules). | When the active task touches a specific language or security-sensitive domain. |
| `manifest.json` | Installation manifest listing kit-managed (overwrite) and adopter-owned (copyIfMissing/preserve) files. | When auditing or modifying the kit file structure or installation behavior. |
| `HARNESS_CARD.md` | Harness summary, subsystem status, active rigor profile, and known limits. | Skim before starting any non-trivial work to determine the verification rules and budgets. |
