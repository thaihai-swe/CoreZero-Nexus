# CoreZero Nexus Learned Heuristics

## Purpose

This file captures repeated, evidence-backed heuristics that improve maintenance of the kit.

## Heuristics

### LH-001: Docs drift fastest at the workflow surface
- Trigger:
  - a skill contract or command surface changes
- Working heuristic:
  - update `docs/README.md`, `docs/guides/onboarding.md`, and `documents/skills-guide.md` in the same wave
- Evidence:
  - repeated drift found in lifecycle docs, command references, and install guidance
- Confidence: High
- Last reviewed: 2026-05-27
- Promote to stronger rule? No

### LH-002: Bootstrap and docs must be verified together
- Trigger:
  - repo memory or canonical artifact set changes
- Working heuristic:
  - update `scripts/install.sh`, seeded templates, and consistency checks in one change
- Evidence:
  - prior bootstrap/docs drift around `core-policies.md` and removed commands
- Confidence: High
- Last reviewed: 2026-05-27
- Promote to stronger rule? No

### LH-003: Generated references are worth seeding early
- Trigger:
  - the repo grows enough that repeated codebase rediscovery is happening
- Working heuristic:
  - maintain `docs/generated/codemap.md` and `docs/generated/references-index.md` as compact landing surfaces
- Evidence:
  - repeated review and documentation passes required broad repo sweeps
- Confidence: Medium
- Last reviewed: 2026-05-27
- Promote to stronger rule? No
