# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.1] — 2026-06-06

### Changed
- **EH-01 merged**: `/brownfield-init` archaeology pass absorbed into `/starter-init` as Phase A (brownfield repos only). Single `/starter-init` entry point replaces the previous two-skill sequence. `kit/skills/brownfield-init/` directory removed.

### Added
- **EO-01**: Structured Observability Log. Rewrote `observability-log.md` with a structured YAML entry schema and a `## Trend Summary` section for tracking failure trends. Updated `harness-maintain` Improve Mode to read, triage, and update the summary.
- **EO-02**: Automated Eval Harness. Added a structural evaluation suite under `kit/scripts/evals/` containing 3 automated checks (SKILL.md completeness, INDEX.md cross-reference integrity, and unresolved template placeholders) run via `run-evals.sh` and wired into the CI workflow.
- **EC-03**: Domain-Specific Context Packs. Added the domain packs layout under `memories/domains/` with a complete `example/` pack implementing glossary triggers, patterns, anti-patterns, and boundary rules. Extended the memory router `INDEX.md` and `index-template.md` with By Domain Packs trigger routing logic.
