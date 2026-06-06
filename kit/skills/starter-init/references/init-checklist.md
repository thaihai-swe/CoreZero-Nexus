# Initialization Checklist

Use this checklist to ensure the repository is fully prepared for harnessed agentic development.

### Brownfield Phase A (if applicable — skip for greenfield repos)

- [ ] Repo confirmed non-trivial (has existing code, tests, CI, or meaningful history).
- [ ] Subagent read-only sweep completed. No raw grep output in main context — summaries only.
- [ ] `memories/repo/brownfield/brownfield-map.md` exists and has at least one rated area.
- [ ] `memories/repo/brownfield/dependency-graph.md` exists and lists module dependencies.
- [ ] `memories/repo/learned-heuristics.md` has 3–5 new entries with file citations.
- [ ] `HARNESS_CARD.md` Known Limits section updated with brownfield-specific caveats.
- [ ] Profile auto-promotion rule recorded in `brownfield-map.md` under `## Profile Rules`.

### Phase B — Bootstrap (all repos)

- [ ] `install.sh` has already seeded the harness surface. If a seeded file is missing, run `bash scripts/doctor.sh` or re-run the installer before init continues.
- [ ] `AGENTS.md` exists at the project root and is router-style (< 50 lines, links to deeper docs).
- [ ] `HARNESS_CARD.md` exists at the project root.
- [ ] `memories/repo/harness-config.md` exists and captures repository workflow defaults.
- [ ] `memories/repo/constitution.md` exists and contains normative repo-wide rules.
- [ ] `memories/repo/security-policy.md` exists and captures permission tiers, trust boundaries, and secret handling.
- [ ] `memories/repo/learned-heuristics.md` exists and captures descriptive repeated heuristics only.
- [ ] `memories/repo/project-knowledge-base.md` exists and contains descriptive stack details, patterns, and conventions.
- [ ] Seeded project-policy docs under `docs/*.md` exist before pre-fill begins.
- [ ] `docs/architecture.md` exists when the repository has meaningful subsystem boundaries, runtime layers, or external integrations.
- [ ] `docs/generated/codemap.md` exists when the repo is large enough to benefit from a generated structural map.
- [ ] `docs/generated/references-index.md` exists when generated or external references should be tracked durably.
- [ ] Test runner command identified and documented in `harness-config.md`.
- [ ] Lint/format commands identified and documented in `harness-config.md`.
- [ ] Type checker command identified and documented in `harness-config.md` (if applicable).
- [ ] CI pipeline identified and documented in `harness-config.md` (if applicable).
- [ ] Build command identified and documented in `harness-config.md`.
- [ ] Context compaction triggers and stale-context rules are documented in `harness-config.md`.
- [ ] Security and sandbox expectations are documented in `harness-config.md`.
- [ ] Directory structure boundaries documented in the knowledge base.
- [ ] Issue tracker mode, artifact routing, and slug conventions documented in `harness-config.md`.
- [ ] Baseline verification: The repository passes all existing tests and lint checks in its current state.
