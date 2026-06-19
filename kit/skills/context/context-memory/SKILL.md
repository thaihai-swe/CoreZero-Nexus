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
- **Next Skill**: `/context-status` (if audit mode used)

## Workflow
1. **Mode Selection**: Determine if this is a regular update or audit (see Audit Mode below).
2. **Session Extracts**: Read `artifacts/features/<slug>/session-extracts.md`. For each entry marked `[CANDIDATE]`: promote confirmed durable lessons to `learned-heuristics.md` (using `references/learned-heuristics-template.md`) or the relevant domain pack's `patterns.md`; discard noise. Remove promoted entries from the candidates list.
3. **Config Drift Check**: Identify any new file paths, canonical commands, or module roots introduced during the session. Update `core-policies.md` `## Harness Config` and `project-knowledge-base.md` `## Repository Overview` to reflect them (consult `references/pkb-*-template.md` as needed). Mark unknowns `[UNKNOWN]` per CC-003 — do not guess.
4. **Domain Pack Update**: If the active feature touched a domain with an installed pack, check whether any new patterns or anti-patterns emerged. Update `memories/domain/<name>/patterns.md` or `anti-patterns.md` with evidence-backed entries only.
5. **Size Check**: For every file modified in Steps 2–4, count lines. If any file exceeds 600 lines, open a promotion proposal at `artifacts/features/<slug>/promotions.md` per `MASTER_INDEX.md` Section 2 Rule 5.

## Core Rules
- No fabrication: do not invent patterns or heuristics; only record what was observed.
- Incremental growth: add detail over time rather than creating new files for minor insights.
- Evidence-based: every entry should trace to a specific observation or session extract.

## Audit Mode

### Usage
Invoke with `/context-memory --audit` (or pass `audit` as the subcommand).

### Checks
1. **File size thresholds** — for every `memories/repo/*.md`, count lines and report:
   - >= 600 lines: early warning (start a promotion proposal)
   - >= 800 lines: threshold breached (open `artifacts/features/<slug>/promotions.md`)
   - >= 1200 lines: hard cap (block further appends until promotion lands)
2. **Domain pack trigger relevance** — for every pack under `memories/domain/`, read trigger keywords from `glossary.md` frontmatter and grep the codebase for occurrences. Flag triggers with zero matches as candidates for removal or rewording.
3. **Memory-to-code accuracy** — sample referenced paths, file names, and module roots from `project-knowledge-base.md`, `core-policies.md` `## Harness Config`, and `MASTER_INDEX.md` and confirm each still exists. Flag stale references.
4. **Domain pack usage** — read `harness-telemetry.md` (when populated) and `artifacts/features/*/session-extracts.md` for pack-load events; list packs not loaded in any recent session.
5. **Promotion watchlist sync** — compare files flagged in checks 1–4 against `MASTER_INDEX.md` `## Promotion Watchlist`. Surface drift in either direction.

### Output
Write a structured Markdown report to `artifacts/features/<slug>/memory-audit.md` (feature-scoped) or `docs/generated/memory-audit.md` (global). Sections:

- `## Summary` — counts by severity (info / warn / error)
- `## Size Findings` — table of file, line count, severity, suggested action
- `## Trigger Drift` — domain packs with stale or unmatched triggers
- `## Stale References` — paths and identifiers that no longer exist
- `## Unused Packs` — domain packs with zero recent loads
- `## Watchlist Sync` — proposed updates to `MASTER_INDEX.md` `## Promotion Watchlist`

### Core Rules — Audit Mode
- Mechanical only — count lines, grep keywords, stat paths. Do not interpret content.
- Evidence-required — every finding cites the file and the check that produced it.
- No edits — the audit produces a report only. Promotions and rewrites stay manual or route through a regular `/context-memory` invocation.
