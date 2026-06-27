## Purpose

Entrypoint agent instruction router for this repository — the CoreZero kit source. Read first every session.

## What this repo is

**Source repo for the CoreZero kit** — a spec-anchored AI software delivery framework shipped via `install.sh` into downstream repos.

Three surfaces:
- `kit/` — the shipped package (what adopters install)
- `documents/` — maintainer docs (NOT installed into adopter repos)
- `page-document/` — public website assets

The shipped adopter router is at `kit/AGENTS.md`. The shipped master index is at `kit/MASTER_INDEX.md`. This `AGENTS.md` is for maintaining the kit itself.

## Priority Rules

These override all other guidance. Key non-obvious ones:

- **No flattery, no filler.** Start with the answer, action, or blocker. No ceremonial openers.
- **Correct false premises** immediately if the user is wrong.
- **Never fabricate.** Read files or say `[UNKNOWN]`. Never guess paths, hashes, test results, or API behavior.
- **Fail loud.** Do not mark work done if verification was skipped or failed.
- **Touch only the request.** No drive-by refactors, formatting churn, or unrelated cleanup.
- **Preserve behavior** unless explicitly asked to change it.
- **Read `kit/core-zero/policies/code-design.md`** before architecture or refactoring work — its rules carry equal weight.

## Kit architecture (non-obvious)

- **Two AGENTS.md files exist.** Root `AGENTS.md` (this file) is for source-repo maintainers. `kit/AGENTS.md` ships into downstream repos.
- **INDEX.md does not exist.** The root AGENTS.md historically referenced it. Use `kit/MASTER_INDEX.md` instead for context routing.
- **No build system, no package.json, no test runner for the kit itself.** The kit is a collection of bash scripts, markdown skill files, and Python helpers. Verification is via `doctor.sh`.
- **17 shipped slash commands (skills)** live in `kit/skills/<name>/SKILL.md`. Each is a behavioral spec for one command.
- **`core-zero/rules/*.md`** — per-language coding rules shipped as overwrite-only instruction files.
- **`scripts/harness/`** — all mechanical gates and validation scripts.

## Commands (exact, non-obvious)

| What | Command |
|---|---|
| Kit self-diagnosis | `bash kit/scripts/harness/doctor.sh` |
| Install kit (dry-run) | `bash kit/scripts/install.sh /tmp/test --dry-run` |
| Install kit (real) | `bash kit/scripts/install.sh /path/to/target` |
| Mechanical gate | `bash kit/scripts/harness/gate-runner.sh` |
| Phase precondition gate | `bash kit/scripts/harness/phase-gate.sh <slug> <phase>` |
| Telemetry | `bash kit/scripts/harness/telemetry-collector.sh --task <ID> --feature <slug>` |
| Telemetry count | `bash kit/scripts/harness/telemetry-count.sh --task <ID>` |
| Context partial load | `python3 kit/scripts/context-loader.py <file> --mode summary` |
| Generate dashboard | `python3 kit/scripts/generate-dashboard.py` |

## Verification (what to run before claiming work done)

Priority order:
1. `bash kit/scripts/harness/doctor.sh` — 8 checks (manifest, sections, paths, thresholds, IDs, ADR status, telemetry schema). Exit 0 required.
2. `bash kit/scripts/install.sh /tmp/corezero-test --dry-run` — verifies manifest resolves, no missing source files.
3. Grep audits:
   - `grep -rn "kit/" kit/skills/ kit/MASTER_INDEX.md` → zero hits (shipped paths must be flat)
   - `grep -rnE "\bTiny\b|\bStandard\b" kit/skills/` → only in the canonical mapping table
4. For new scripts: `chmod +x` and add to `kit/manifest.json` under the appropriate `overwrite` or `copyIfMissing` array.

## Versioning and release

- Single version source: `kit/manifest.json` → `version` field. No separate `VERSION` files.
- CI auto-bumps on merge to `main` based on commit prefix: `feat:` → minor, `fix:` → patch, `major:` or `BREAKING CHANGE:` → major. `chore:` / `docs:` / `refactor:` → no release.
- Tag format: `v<semver>`. Release workflow verifies the tag matches manifest.json before creating a release.
- Version in manifest.json on disk is the **next** release version (before tag), not the current live release.

## Operating loop (short)

1. Understand the goal in repo-specific terms.
2. Inspect before building (read relevant code/core-zero/artifacts/patterns first).
3. Plan the smallest safe change. Load `kit/core-zero/rules/ponytail.md` before architecture or implementation work.
4. Implement surgically. Match existing style. No dead code cleanup unless asked.
5. Verify with `doctor.sh` + install dry-run + grep audits.
6. Report: what changed, what verified, what gaps remain, next step.

## Context management

- Read `kit/MASTER_INDEX.md` at session start to find which memory files to load.
- Use subagents for broad exploration (searching patterns across the codebase, reading large files, parallel edits).
- Always review subagent output yourself. You own the result quality.
- If stuck after two failed corrections on the same issue, stop and ask whether to reset approach.
