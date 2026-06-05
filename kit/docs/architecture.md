# Architecture

Living architecture doc for the CoreZero Nexus repository.

## System Snapshot

- Repository type: Documentation-first kit repository
- Primary runtime(s): Markdown, Bash, optional Python 3 for validation and visualization helpers
- Main entrypoints: `README.md`, `AGENTS.md`, `scripts/install.sh`, `skills/*/SKILL.md`
- Deployment shape: Source repository that installs a packaged workflow surface into downstream projects
- Confidence: High

## Top-Level Components

| Component | Responsibility | Key Paths | Depends On | Notes |
| --- | --- | --- | --- | --- |
| Public package surface | What adopters receive by default | `docs/`, `skills/`, `rules/`, `scripts/install.sh`, `.github/workflows/harness-check.yml` | `manifest.json` | Must stay aligned with installer behavior |
| Maintainer documentation | Kit-internal product and architecture guidance | `documents/` | Public workflow, reference artifacts | Source-only; not part of the default installed package |
| Durable repo memory | Long-lived repo knowledge and policy | `memories/repo/` | Skill contracts, maintainer upkeep | Guides future kit maintenance sessions |
| Skill contracts | Canonical workflow logic and references | `skills/*/SKILL.md`, `skills/*/references/` | Memory files, templates, public docs | Behavioral source of truth |
| Packaging and validation | Installation, upgrade behavior, and consistency checks | `manifest.json`, `scripts/install.sh`, `.github/workflows/harness-check.yml`, `scripts/check-doc-consistency.py` | Public docs, generated references | High-risk area for drift |

## Runtime Boundaries

- Boundary: Adopter package vs maintainer docs
  Owner: `manifest.json` and `scripts/install.sh`
  Why it exists: Adopters need a lean install surface; maintainers need deeper source-repo docs
  Crossing rule: `documents/` stays in the source repository unless an explicit packaging decision changes that
  Evidence: `manifest.json` install lists and `docs/INSTALL.md`

- Boundary: Skill behavior vs explanation surfaces
  Owner: `skills/` and docs under `docs/` and `documents/`
  Why it exists: Workflow behavior must be implemented once and explained consistently elsewhere
  Crossing rule: When a public command or artifact contract changes, update the matching docs and checks in the same wave
  Evidence: `skills/*/SKILL.md`, `docs/README.md`, `documents/skills-guide.md`

- Boundary: Generated references vs maintained source docs
  Owner: `docs/generated/`
  Why it exists: Generated summaries are useful landing pages but can drift if not refreshed
  Crossing rule: Generated references must only claim repo facts that are present and supported
  Evidence: `docs/generated/codemap.md`, `docs/generated/references-index.md`

## Data And Control Flow

- Flow: Adopter install
  Starts at: `scripts/install.sh`
  Passes through: `manifest.json`, template maps, copy/overwrite/preserve rules
  Ends at: downstream repo with `docs/`, `skills/`, `rules/`, memory files, and install workflow
  Why it matters: Packaging drift directly changes what adopters can understand and run

- Flow: Public workflow maintenance
  Starts at: command or artifact change in `skills/*/SKILL.md`
  Passes through: `docs/`, `documents/`, generated references, consistency checks
  Ends at: aligned product documentation and CI enforcement
  Why it matters: Most user confusion comes from drift across these surfaces, not missing capability

## External Integrations

| Integration | Purpose | Protocol | Auth Method | Failure/Latency Watchout |
| --- | --- | --- | --- | --- |
| GitHub raw content | Curl-pipe install path | HTTPS | Public repo access | Network failure blocks remote install |
| GitHub Actions | CI validation and release flows | GitHub workflow runtime | `GITHUB_TOKEN` in Actions | Workflow drift can ship stale package surfaces |

## Runtime Environment

- Production: N/A for the kit itself; this repository is shipped as source content
- Staging: N/A
- Local dev: Repository editing plus shell and Python-based checks
- CI/CD: GitHub Actions workflows under `.github/workflows/`

## Architectural Decisions

- Decision: Keep public adopter docs and maintainer docs as separate surfaces
  Status: Accepted
  Why: Adopters need a smaller install surface and simpler navigation than maintainers
  Evidence: `docs/README.md`, `documents/README.md`, `manifest.json`
  Related artifact: `docs/INSTALL.md`

- Decision: Use skill contracts as the canonical workflow source of truth
  Status: Accepted
  Why: Behavioral drift is lower when implementation contracts exist in one place and docs mirror them
  Evidence: `skills/*/SKILL.md`, `documents/skills-guide.md`
  Related artifact: `docs/generated/codemap.md`

## Safe Change Guidance

### High-Risk Areas

- Area: `manifest.json` and `scripts/install.sh`
  Watch for: shipped-surface drift, missing seeded files, broken upgrade behavior
  Validation needed: installer dry-run plus doc consistency check

- Area: public command taxonomy
  Watch for: stale legacy command prefixes, bare `spec` command references, or retired command names in docs and templates
  Validation needed: repo-wide string checks plus quickstart/readme review

### Safe Areas

- Area: Maintainer narrative docs in `documents/`
  Why isolated: They do not change runtime behavior as long as they stay aligned with the public workflow

### Cross-Cutting Concerns

- Concern: Documentation drift
  Affects: `docs/`, `documents/`, `skills/`, generated references, CI checks

- Concern: Packaging clarity
  Affects: `manifest.json`, `scripts/install.sh`, `docs/INSTALL.md`, `README.md`
