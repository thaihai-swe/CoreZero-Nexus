## Brownfield Mode

Activate when the repository has existing code, tests, CI, or history. Do not assume a clean baseline.

**Additional steps in Brownfield Mode:**

1. **Existing entrypoint check**: If `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, or `.github/copilot-instructions.md` already exists, read it before creating or overwriting. Preserve any rules that are still valid; flag conflicts explicitly.
2. **Broken test inventory**: Run the test suite. Do NOT fix broken tests silently. Document every failing test in `memories/repo/harness-config.md` under a `## Known Broken Tests` section. A brownfield baseline is the current state, not an idealized clean state.
3. **Security-sensitive path flagging**: Before proceeding, scan for auth middleware, payment handlers, secret loading, and external API integrations. List them in `memories/repo/security-policy.md` as high-attention paths requiring explicit confirmation before modification.
4. **Brownfield map recommendation**: If the codebase is non-trivial (more than ~10 files or multiple subsystems), recommend running `spec-research` with `../../spec-research/references/brownfield-mapping-template.md` before any feature work begins.
5. **Preserved behavior baseline**: Identify at least 3 behaviors that must not change regardless of what feature work follows. Record them in `memories/repo/project-knowledge-base.md` under `## Preserved Behavior Baseline`.

**Brownfield Mode stop conditions:**
- The repository has no tests and no build script — document this explicitly and require user acknowledgment before proceeding.
- Existing `AGENTS.md` or `CLAUDE.md` contains rules that directly conflict with the harness kit — surface the conflict and ask the user to resolve it before continuing.
