# Master Index

> Repo-level routing index for maintaining CoreZero itself.
> The shipped package lives under `kit/`. Maintainer docs live under `documents/`.

## Context Indexes (load on demand)

| File | Contents | When to load |
|------|----------|--------------|
| `kit/memories/repo/INDEX.md` | Index of shipped package memories, rules, and domain-specific memories. | To locate kit constraints, heuristics, and routing rules. |
| `kit/docs/generated/codemap.md` | Placeholder map of installed package locations. | Before changing shipped package structure. |
| `kit/docs/generated/references-index.md` | Placeholder index of installed package references. | When tracing shipped doc and rules links. |
| `kit/docs/rules/` | Shipped Python and security rules. | When the active task touches language or security guidance. |
| `kit/manifest.json` | Installation manifest for the shipped package. | When auditing or changing what adopters receive. |
| kit/memories/repo/core-policies.md | Repo-wide normative rules, canonical commands, limits, and security policy. | Read at session start and before changing core policies or security rules. |
| documents/README.md | Maintainer docs entrypoint. | When changing maintainer-facing docs or repo architecture. |

## Structural Reference

```mermaid
graph TD
    AGENTS["AGENTS.md (Entrypoint)"] --> INDEX["INDEX.md (Master Index)"]
    INDEX --> MEM["kit/memories/repo/INDEX.md"]
    INDEX --> RULES["kit/docs/rules/README.md"]
    INDEX --> DOCS["kit/docs/generated/references-index.md"]
    INDEX --> MAP["kit/docs/generated/codemap.md"]
    INDEX --> MANIFEST["kit/manifest.json"]
    INDEX --> POLICIES["kit/memories/repo/core-policies.md"]
    INDEX --> MAINT["documents/README.md"]
```
