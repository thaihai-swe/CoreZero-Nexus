---
name: codebase-documenter
description: Generate comprehensive codebase documentation covering architecture, components, data flow, setup, deployment, and contributing — produces a multi-file doc set.
compatibility: Designed for Claude, Codex, and other Agent Skills-compatible tools.

---

# Codebase Documenter



## Overview

Produces a multi-file Markdown documentation set (README, ARCHITECTURE, COMPONENTS, etc.) explaining how a codebase is organized and how to onboard onto it. Grounds all claims in source code.

## When to Use (vs. Others)

- **Use `/codebase-documenter`** for repo onboarding: setup, directories, build commands, and contributing guides.
- **Use `/system-flow-docs`** for event/transaction workflow narratives (2-5 core flows).
- **Use `/api-endpoint-docs`** for HTTP route inputs and outputs.

## Read First

- `memories/repo/constitution.md` and `memories/repo/project-knowledge-base.md`
- Root config and package/build files (`package.json`, `pom.xml`, etc.).
- References: `references/templates.md`, `references/best-practices.md`, `references/diagram-patterns.md`, `../_shared/doc-conventions.md`, and `../_shared/diagram-catalog.md`.

## Workflow

1. **Frame & Depth**: Pick scope and depth (Quick, Standard, or Deep). Default to Standard.
2. **Explore**: Map folders, dependencies, and main entry points.
3. **Trace**: Trace key execution flows through code to construct mental models.
4. **Document**: Write separate Markdown pages using templates. Embed system architecture diagrams. Provide real code snippets with `file:line` references.
5. **Verify**: Check that instructions are runnable in a fresh environment.

## Required Coverage (10 Areas)

1. Project purpose.
2. High-level architecture patterns.
3. Folder structure.
4. Key component responsibilities.
5. External dependencies.
6. Data models/schemas.
7. Development setup/prerequisites.
8. Coding conventions.
9. Deployment pipelines.
10. Contributing guidelines.

## Diagram Preferences

- Layered architecture diagram showing system structure.
- Supporting sequence flow, ERD, or microservices maps per `../_shared/diagram-catalog.md` and `references/diagram-patterns.md`.

## Output Rules

- Follow `../_shared/doc-conventions.md` rules.
- Multi-file output format (README.md, ARCHITECTURE.md, COMPONENTS.md, DEVELOPMENT.md, DEPLOYMENT.md, CONTRIBUTING.md).
- Setup instructions must be actionable with exact commands.
- Verify that a fresh developer can onboard using the docs.

## Stop Conditions

- Codebase is unreadable or access-denied.

## Core Rules

- Ground all claims in source code. Do not guess structure.

## Rationalization vs. Reality

| Rationalization | Reality |
|---|---|
| "I can generate setup steps based on standard stack assumptions." | Config files often have custom variables. Real commands must be cited. |

## Red Flags

- Outdated setup steps or dependencies listed in documentation.

## Verification

- [ ] Every directory listed in folder structure matches actual layout.
