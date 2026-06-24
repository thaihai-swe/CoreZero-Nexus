# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Standardized `--root` flag across all harness scripts (`gate-runner.sh`, `phase-gate.sh`, `traceability-audit.sh`, `telemetry-count.sh`, `telemetry-collector.sh`).
- Shared root directory resolution library at `scripts/harness/_lib/root.sh`.
- Check 9 (version surface matching) and Check 10 (executable bit assertions) in `doctor.sh`.
- PR validation CI workflow under `.github/workflows/ci.yml`.
- Seeded example ADR `docs/project/adr/0001-example.md` to guide adopters.
- Added `/ponytail` command description to index surfaces.

### Changed
- Expanded `technical-docs/SKILL.md` body details to align with peer skills.
- Expanded `spec-adr/SKILL.md` workflow section to cover log/registry updates.
- Refactored `telemetry-count.sh` YAML parser to support macOS Bash 3.2 regex matching and `--feature` flag filtering.
- Renamed legacy complexity profiles `Tiny` and `Standard` to `Simple` and `Moderate` across all templates, policies, and files.
- Fixed `gate-runner.sh` and `traceability-audit.sh` to prevent false positive substring matches.
- Fixed sed tasks parser to avoid end-of-file validation evidence leak.
- Propagated errors and added python3 pre-flight check in `doctor.sh`.
- Removed unreachable dead code for local repo detection in `install.sh`.
- Fixed `install.sh` dry-run mode to prevent false increments of `backup_count`.

### Fixed
- Fixed XSS vulnerability in `generate-dashboard.py` features script injection.
- Fixed next-steps numbering jumps in `install.sh`.
