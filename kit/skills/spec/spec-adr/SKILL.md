---
name: spec-adr
description: Record an Architectural Decision Record (ADR).
compatibility: Designed for AI coding agents.
---

# Kit ADR

## Overview
Record significant architectural decisions.

## I/O Hand-off Protocol
- **Reads**: Codebase context.
- **Writes**: `docs/project/architecture.md` (append ADR).
- **Next Skill**: Return to previous skill (e.g., `/spec-plan` or `/spec-implement`).

## Workflow
1. Identify the decision to be made.
2. Consider context, options, and consequences.
3. Append the decision to `docs/project/architecture.md`.

## Core Rules
- Keep ADRs concise but informative.
