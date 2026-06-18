# Releasing CoreZero Nexus

Maintainer runbook for release, version sync, and GitHub Pages expectations.

## Release Contract

- `VERSION`, `kit/VERSION`, and `kit/manifest.json` `version` must always match.
- `kit/manifest.json` is the shipped-surface contract.
- `scripts/install.sh` is the public installer entrypoint.
- Pages publishes a curated public copy of `kit/docs/`, `documents/`, and `page-document/`; it does not publish the whole repo.

## Release Checklist

Run this checklist before cutting or approving a release:

- `bash scripts/install.sh /tmp/corezero-check --dry-run`
- `bash scripts/install.sh /tmp/corezero-check`
- confirm the installed target contains the shipped skills listed in `documents/skills-guide.md`
- confirm root `README.md`, `kit/docs/README.md`, `documents/README.md`, and `page-document/index.html` agree on the shipped command surface
- confirm `VERSION`, `kit/VERSION`, and `kit/manifest.json` `version` match
- confirm Pages still publishes adopter docs under `adopters/` and maintainer docs under `maintainers/`

If any item fails, do not tag a release.

## Automatic Release Flow

Routine releases are driven by commit prefix on `main`:

- `major:` for adopter-visible breaking changes
- `minor:` or `feature:` for new public surface
- `patch:` for behavior-preserving fixes

`auto-bump.yml` updates all three version surfaces, creates the release commit, pushes the tag, and maintains the `release/<major>.<minor>.x` branch.

## Manual Release Flow

Use the manual path when you want to control the exact release point:

1. Update `VERSION`, `kit/VERSION`, and `kit/manifest.json` to the target version.
2. Run the release checklist above.
3. Commit the version change.
4. Tag `v<x.y.z>` on that commit.
5. Push the branch and the tag.
6. Confirm `release.yml` publishes the GitHub release.

## Pages Expectations

`pages.yml` should continue to publish:

- `kit/docs/*` into `adopters/`
- curated maintainer docs into `maintainers/`
- the static landing shell from `page-document/`

If the public landing page or doc taxonomy changes, update the copied paths and links in the same change.
