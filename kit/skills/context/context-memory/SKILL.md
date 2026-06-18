---
name: context-memory
description: Update repository memories and learned heuristics.
compatibility: Designed for AI coding agents.
---

# Context Memory

## Overview
Updates persistent AI memories (e.g., rules, architecture) so future agents don't repeat mistakes.

## I/O Hand-off Protocol
- **Reads**: Current context, `memories/repo/`.
- **Writes**: Files in `memories/repo/`.

## Workflow
1. Identify new heuristics, gotchas, or architectural patterns learned during the session.
2. Update the appropriate file in `memories/repo/` (e.g., `learned-heuristics.md`, `project-knowledge-base.md`).
