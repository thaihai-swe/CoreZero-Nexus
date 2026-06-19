---
name: starter-init
description: Initialize the kit structure in a new repository.
compatibility: Designed for AI coding agents.
---

# Starter Init

## Overview
Bootstraps the `docs/` and `memories/` directories with standard templates, then guides the adopter through customizing the seeded memory files for their project.

## I/O Hand-off Protocol
- **Reads**: target repo structure, `memories/repo/*.md` seeded by the installer.
- **Writes**: Generates `docs/` and `memories/` folders, baseline markdown files, `.gitignore` entries, and customized memory files.
- **Next Skill**: `/spec-research` (brownfield) or `/spec-requirements` (greenfield).

## Workflow

### Phase 1 — Bootstrap Structure
1. Ensure `docs/project`, `docs/generated`, `memories/repo`, and `memories/domain` exist. (Use `references/init-checklist.md` to guide the bootstrap process.)
2. Confirm the installer seeded `memories/repo/harness-telemetry.md`. Create any that are missing.
3. **Gitignore**: Detect or create `.gitignore` at the repository root. For each of the following entries — `docs/generated/*`, `memories/repo/harness-telemetry.md`, `scripts/harness/gate-runner.local.sh` — check whether an identical line already exists in `.gitignore`. Append **only** entries that are absent. Do not duplicate existing entries.

### Phase 2 — Baseline Detection
4. Detect greenfield vs. brownfield:
   - Greenfield: empty repo or only the kit's own files. Skip baseline test discovery.
   - Brownfield: existing source tree. Search for the canonical baseline test or compile command (`pytest`, `npm test`, `cargo test`, `go test`, `make test`). Record the result and any discovered high-risk or migration-prone areas in `memories/repo/project-knowledge-base.md` `## Repository Overview`.
   - If no baseline exists in a brownfield repo, ask the adopter to declare the best available proof surface and record their answer.

### Phase 3 — Memory Customization (mandatory)

The installer seeds `memories/repo/*.md` with the kit's *own* content. Those files describe the kit, not the adopter's project. This phase rewrites them to fit the target project. Run each step interactively — ask the adopter the listed prompts and write their answers into the corresponding file.

5. **Customize `core-policies.md`**:
   - Prompt: "What is this project's name and primary code roots? What is the default working branch? Which agent clients are supported?"
   - Update the `# Harness Config` `## Repository Identity` block.
   - Prompt: "What are the canonical install, lint, typecheck, build, and test commands?"
   - Update the `## Verification Commands` block. Mark commands as `N/A` only when the project genuinely has none.
   - Leave the `## Normative Rules` (CC-001 through CC-010) untouched unless the adopter wants to amend a rule. Amendments must follow `## Amendment Rules` in that file.

6. **Customize `core-policies.md` `## Security Policy`**:
   - Prompt: "What paths in this repo are security-sensitive? What external services or secrets does the project depend on? Which actions require explicit confirmation?"
   - Update `## Trust Boundaries`, `## Permission Tiers`, and `## Sandbox And Access Rules` with project-specific paths and rules.
   - Keep `## Prompt-Injection Defense` rules verbatim — they are kit-wide.

7. **Customize `project-knowledge-base.md`**:
   - Prompt: "What are this project's main components, integration boundaries, and bootstrap watchouts?"
   - Replace the kit-specific `## Repository Overview` and `## Key Architectural Boundaries` sections with the adopter's content.
   - Leave references to other memory files (e.g., `core-policies.md`, `architecture.md`) intact; they remain valid.

8. **Customize `learned-heuristics.md`**:
   - Drop the kit's LH-001 through LH-008 entries unless the adopter wants to keep any.
   - Tell the adopter that this file fills naturally as `/context-memory` runs after features. Leave it minimal at start.

9. **Domain pack selection**:
   - Read `memories/domain/glossary.md` frontmatter triggers.
   - Prompt: "Does this project have one or more bounded subdomains (auth, payments, data pipeline, etc.) that deserve a domain pack? If yes, list them."
   - For each domain the adopter names: copy the seeded `memories/domain/` scaffold into a per-domain subdirectory (`memories/domain/<name>/`) — only if multiple packs are needed; otherwise customize the existing files in place. Update `MASTER_INDEX.md` `## By Domain Packs` with the new pack name and trigger keywords.
   - If the adopter declines all packs, leave the existing scaffold.

### Phase 4 — Confirm and Hand Off
10. Run `/context-memory --audit` to confirm the seeded files no longer reference kit-internal paths and that domain pack triggers are populated.
11. Inform the adopter the kit is ready and route them to `/spec-research` (brownfield) or `/spec-requirements` (greenfield).

## Core Rules
- **Mandatory customization**: Skipping Phase 3 leaves the adopter with kit-content masquerading as project memory. The bootstrap is not complete until Phase 3 is done or explicitly deferred with a written `[DEFERRED]` marker in each affected file.
- **Ask, don't guess**: Every memory rewrite comes from an adopter answer, not from agent inference. Mark `[UNKNOWN]` per CC-003 when the adopter cannot answer yet.
- **Surgical edits**: Update only the sections this skill names. Preserve formatting, IDs (CC-*, LH-*), and cross-file references.
- **No code changes**: This skill only writes documentation, configuration, and memory files. It must not modify project source code.
