# Harness Card

This card summarizes the active session limits, rigor settings, and telemetry constraints.

## Active Rigor Profile & Telemetry

- **Default profile:** Standard (Refer to `skills/_shared/rigor-profiles.md` for profile details)
- **Session Token Capacity:** 200,000 tokens
- **Amnesia Warning Threshold:** 80% saturation (160,000 tokens)
- **Current Session Status:** Healthy

## Known Limits

- The auto-tier observability log is empty until real failures get captured. Expect entries once features run end-to-end under the new flow.
- The extracted-tier session-extracts files only exist per-feature; expect them to populate as features run `context-session END`.
- `visualize` ships in the package, but Mermaid-to-SVG rendering still depends on optional `mmdc`. Structural Mermaid validation works without it.
- Adversarial spec review is recommended for cross-cutting work in the `Complex` profile but not yet a separate skill.
- Maintainer docs live in `documents/`, but the default installer does not ship them into downstream projects.

## Customizations

- This repo *is* the kit, so the harness is bootstrapped by hand rather than by `install.sh`. Adopting repos always run the script.
- `visualize` is shipped as a specialist helper, not a mandatory step in the default delivery loop.

## Reference Documents

- Master Index: `INDEX.md`
- Harness Configuration: `memories/repo/core-policies.md`
- Security Policy: `memories/repo/security-policy.md`
- Rigor Profiles: `skills/_shared/rigor-profiles.md`
