# Harness Config

## Repository Identity

- Project name: AI Agents Development Kit (CoreZero Nexus)
- Repository type: Harness Engineering kit (template/starter kit)
- Primary code roots: `skills/`, `scripts/`, `memories/repo/`
- Default working branch: main
- Supported agent clients: Claude Code, Cursor, Codex, Gemini CLI

## Work Tracking

- Issue tracker mode: GitHub
- Issue/project location: https://github.com/thaihai-swe/CoreZero-Nexus/issues
- Default work item format: GitHub Issues
- Required labels or states: `breaking-change` for skill name or artifact schema changes
- Escalation / blocker handling: Stop and ask user

## Artifact Routing

- Feature artifact root: `artifacts/features/<slug>/`
- Docs root: `docs/`
- Architecture doc path: `docs/architecture.md`
- Security policy path: `memories/repo/security-policy.md`
- Learned heuristics path: `memories/repo/learned-heuristics.md`
- ADR location: `artifacts/features/<slug>/adr-*.md`
- Generated documentation location: `docs/generated/`
- Codemap path: `docs/generated/codemap.md`
- References index path: `docs/generated/references-index.md`

## Verification Commands

- Install / bootstrap command: `bash scripts/install.sh /path/to/target`
- Lint / format command: N/A (documentation-first repo)
- Typecheck command: N/A
- Build command: N/A

## Session Defaults

- Session bootstrap skill: `/starter-init`
- Progress log path: `artifacts/features/<slug>/progress.md`
- Handoff path: `artifacts/features/<slug>/handoff.md`
- When to checkpoint: After completing a skill or major edit wave
- Context compaction triggers: Raw grep output, large file listings, superseded design detail
- Stale-context eviction rules: Summarize raw tool output after extracting findings
- When to stop and escalate: After two failed corrections on the same issue

## Environment And Access

- Required local services: None
- Required env files or secrets handling: None
- Sandbox / permission watchouts: Do not modify target project files outside bootstrap
- Browser / UI verification target: N/A

## Conventions That Affect Automation

- Feature slug format: kebab-case
- Branch naming format: features/<name>
- Commit / PR expectations: Subject under 72 chars, body explains why
- Required reviewers or owners: None (solo maintainer)

## Adaptive Rigor

- Default profile: Standard
  (Choose from: Tiny | Standard | Complex. See `skills/_shared/rigor-profiles.md`.)
- Promotion triggers:
  - Changes to skills, harness templates, or `memories/repo/` schemas -> Complex (apply System Spec Mode + `harness-maintain Eval Mode`)
  - Bootstrap script or consistency check changes -> at least Complex
  - Documentation-only updates that do not change skill behavior -> Tiny
- When in doubt: pick the higher profile. Over-ceremony costs time; under-ceremony costs correctness.

## Memory Promotion Thresholds

Used by `context-memory` post-ship sync to flag files that should be split into a group. Promotion is proposed, not automatic — the user approves any restructure.

- File length: warn at 800 lines, hard threshold at 1200 lines
- Distinct subtopics: 3 or more H2 sections covering separable concerns
- Artifact references: 5 or more `artifacts/features/<slug>/` files cite the same slice of one memory file
- Action when threshold hit: add the file to `## Promotion Watchlist` in `memories/repo/INDEX.md` and write a one-paragraph proposal to `artifacts/features/<slug>/promotions.md`
