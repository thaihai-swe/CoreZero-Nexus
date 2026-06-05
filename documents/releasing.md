# Releasing CoreZero Nexus

Maintainer runbook. Two release flows: **automatic** for routine merges to `main`, **manual** for milestone or breaking releases.

## First public release (v0.1.0) — from a feature branch

If you're reading this on a feature branch (e.g. `features/refactor-harness`) and want to ship the very first public release, follow this exact sequence. After v0.1.0 lands, future releases use the routine flows below.


### 2. Commit the feature branch

```bash
git status                                # eyeball what's staged
git add .
git commit -m "release: v0.1.0 — initial public release"
git push -u origin features/refactor-harness
```

The `release:` prefix matters — it tells `auto-bump.yml` to ignore this commit when it eventually lands on `main`.

### 3. Open a PR to main

On GitHub: `features/refactor-harness → main`. Title: `Release v0.1.0 — public installer, memory router, post-ship sync`. The CI consistency check runs on the PR.

### 4. Squash and merge

When merging, set the squash commit subject to:

```
release: v0.1.0 — initial public release
```

The `release:` prefix prevents `auto-bump.yml` from firing. You want to control v0.1.0 manually because the auto-bump workflow would compute the next version from the existing VERSION (already `0.1.0`) and produce `0.2.0` instead.

### 5. Tag and create the release branch

```bash
git checkout main
git pull
git tag v0.1.0
git push origin v0.1.0

# Create the release/0.1.x branch from the same commit
git push origin main:refs/heads/release/0.1.x
```

The tag push fires `release.yml` → consistency check → GitHub release page.

### 6. Watch and verify

- GitHub → Actions → Release should turn green
- Release page lives at `https://github.com/<user>/AI-agents-dev-kits/releases/tag/v0.1.0`
- Branch `release/0.1.x` exists on origin

### 7. Public install smoke test

```bash
curl -fsSL https://raw.githubusercontent.com/<user>/AI-agents-dev-kits/main/scripts/install.sh \
  | bash -s -- /tmp/post-release-test
cat /tmp/post-release-test/.corezero-version    # should print: 0.1.0
```

If this works, v0.1.0 is real and adopters can use it.

After v0.1.0, switch to the routine flows below — most future releases use the automatic path.

## Two paths to release

| Flow | Trigger | When to use |
|---|---|---|
| **Automatic** | Push commit with `major:` / `minor:` / `patch:` prefix to `main` | Routine work — most releases |
| **Manual** | `git tag v<x.y.z> && git push origin v<x.y.z>` | Coordinated releases, breaking changes, milestone tags, hotfixes you want to control exactly |

## Branch strategy

- **Feature branches** (`features/*`): develop new functionality. Open a PR to merge into `main`. The PR must use the `release:` or appropriate prefix for version bumps; merges are squash‑and‑merge to keep history clean.
- **Main branch** (`main`): holds the latest development state. All regular releases are created from `main` via the automatic flow.
- **Release branches** (`release/<major>.<minor>.x`): long‑lived parking lines for a minor series. Created automatically on a minor or major bump. Patches are fast‑forwarded on this branch.
- **Hotfix branches** (`hotfix/*` or direct work on `release/<major>.<minor>.x`): urgent fixes are applied to the appropriate release branch, then a new patch tag is created. After the hotfix, cherry‑pick or merge the change back to `main` if it should be included in future releases.

The CI workflows enforce that:
- Pull requests targeting `main` may only come from branches matching `features/*`.
- Pull requests targeting a `release/*` branch may only come from `hotfix/*` branches.
- Tags are created only by the `auto-bump.yml` (automatic) or manually via the `manual flow`.

Both paths converge on the same `release.yml` workflow that publishes the GitHub release. They just differ in who creates the tag and the release branch.

## What gets created on every release

Each release produces these artifacts:

1. **Tag** `v<x.y.z>` — immutable pointer to the released commit. Adopters pin to it.
2. **GitHub Release page** at `releases/tag/v<x.y.z>` — human-readable notes.
3. **Release branch** `release/<major>.<minor>.x` — long-lived parking line for the minor series. **Created on minor or major bumps only.** Patches fast-forward the existing branch — they do not get their own branch.

### Why patches don't get their own branch

This follows the standard Git Flow / GitHub Flow practice used by Linux, Node.js, Kubernetes, Postgres, and most production projects:

- **One branch per minor series.** `release/0.5.x` covers v0.5.0, v0.5.1, v0.5.2, …, v0.5.N.
- **Tags mark each release** within the series. The branch is the parking line; the tag is the milestone.
- **Hotfixes branch off the release branch**, not main. You cherry-pick or write the fix on `release/0.5.x`, then tag a new patch.
- **Branches are expensive long-term** — every release branch you create is a long-lived object you have to maintain, keep secure, and decide whether to support. Creating one per patch (`release/0.5.1`, `release/0.5.2`, …) explodes maintenance with no upside, since patches are exactly the changes you'd cherry-pick onto an existing branch.
- **Adopters pin to tags, not branches.** The tag is what guarantees immutability. The branch is for the maintainer.

So the rule is:

```
Major bump  →  new release branch (release/<major>.0.x) + tag
Minor bump  →  new release branch (release/<major>.<minor>.x) + tag
Patch bump  →  reuse the existing release branch, fast-forward, + tag
```

Concretely:

| Sequence | What lands on each branch |
|---|---|
| `v0.5.0` (minor) | Creates `release/0.5.x`, points at `v0.5.0` |
| `v0.5.1` (patch) | Fast-forwards `release/0.5.x` to `v0.5.1` |
| `v0.5.2` (patch) | Fast-forwards `release/0.5.x` to `v0.5.2` |
| `v0.6.0` (minor) | Creates `release/0.6.x` (parallel to `release/0.5.x`) |
| `v0.6.1` (patch) | Fast-forwards `release/0.6.x` to `v0.6.1` |

This is exactly what `auto-bump.yml` implements.

## Versioning

Strict semver. The bump level is decided by commit prefix (auto) or by you (manual).

| Bump | Use for | Examples |
|---|---|---|
| **Major (1.0.0 → 2.0.0)** | Adopter-visible breaking change | `INDEX.md` schema change, manifest categories renamed, skill removed or renamed, command-line flag dropped |
| **Minor (0.1.0 → 0.2.0)** | New public surface, backward-compatible | New skill, new memory file, new template, new CLI flag, new manifest entry |
| **Patch (0.1.0 → 0.1.1)** | Behavior-preserving fixes | Prompt edits, installer bug fix, doc correction, dead-link fix |

Decision rule when in doubt:

```
Did this change break adopter-visible behavior?
├── YES → Major
└── NO
    Did it add a new public surface?
    ├── YES → Minor
    └── NO
        Did it fix or improve existing behavior?
        ├── YES → Patch
        └── NO  → Don't release (chore/docs/refactor)
```

## Commit prefix → bump (automatic flow)

The `auto-bump.yml` workflow inspects the merge commit on `main` and picks the bump level. Prefix names the bump level directly:

| Commit prefix | Auto-bump | Use for |
|---|---|---|
| `major:` | **Major** | Breaking change to memory schema, manifest, or skill contract |
| `minor:` or `feature:` | **Minor** | New skill, new memory file, new template, new public surface |
| `patch:` | **Patch** | Bug fix, prompt edit, doc correction, dead-link fix |
| `feat!:` `fix!:` or `BREAKING CHANGE:` in body | **Major** (alias) | Conventional-Commits style breaking change |
| `feat:` | **Minor** (alias) | Conventional-Commits style new feature |
| `fix:` `perf:` `revert:` | **Patch** (alias) | Conventional-Commits style fix |
| `chore:` `docs:` `refactor:` `style:` `test:` `release:` | No release | Internal cleanup, doc edits, the bot's own commits |
| Anything else (no prefix, free-form) | No release | Skipped silently |

The literal `major:` / `minor:` / `patch:` prefixes are the recommended style — the prefix names the bump level so there's nothing to memorize. `feat:` / `fix:` aliases exist so Conventional-Commits-style commits also work.

Two override switches:

- `[skip release]` anywhere in the commit message — auto-bump exits cleanly, no tag, no release
- `release:` prefix — used by the auto-bump bot itself; ignored to prevent loops

When auto-bump fires it: bumps `VERSION`, runs the consistency check, commits `release: v<next>`, creates and pushes the tag. The tag push then triggers `release.yml`.

## Automatic flow (most releases)

You merge a PR with a Conventional-Commit prefix, and the rest is automatic.

### Standard sequence

1. Land your PR on `main` with the right prefix:
   ```
   minor: add corezero-predict skill
   ```
2. GitHub fires `auto-bump.yml`:
   - Reads commit prefix → `minor`
   - Reads `VERSION` (e.g. `0.1.0`)
   - Computes next: `0.2.0`
   - Bumps `VERSION` to `0.2.0`
   - Commits `release: v0.2.0 [skip ci]`
   - Tags `v0.2.0` and pushes both
3. Tag push fires `release.yml`:
   - Verifies tag matches `VERSION`
   - Runs consistency check again
   - Creates the GitHub release page
4. Release is live at `releases/tag/v0.2.0`.

### Skipping a release on a feature commit

When you want a `minor:` commit on `main` but don't want to ship yet (collecting multiple changes for one release):

```
minor: add corezero-predict skill [skip release]
```

## Automatic release of future versions

### Release 0.3.0 (minor bump)
1. Add a commit on `main` with a **minor** prefix, e.g.:
```bash
minor: add new skill X
```
2. Push the commit. `auto-bump.yml` will detect the `minor:` prefix, bump `VERSION` from `0.2.0` to `0.3.0`, commit `release: v0.3.0 [skip ci]`, tag `v0.3.0` and push both.
3. The tag push triggers `release.yml`, publishing the GitHub release at `releases/tag/v0.3.0`.

### Release 0.2.1 (patch bump)
1. Add a commit on `main` with a **patch** prefix, e.g.:
```bash
patch: fix installer script
```
2. Push the commit. `auto-bump.yml` will bump `VERSION` to `0.2.1`, create tag `v0.2.1` and fast‑forward the existing `release/0.2.x` branch.
3. The tag push again triggers `release.yml`.

**Tip:** The harness‑check workflow now warns and skips the review step if no `artifacts/features` are present, so you can release even from a clean repo.


The auto-bump workflow exits cleanly. When you're ready to ship, push a follow-up commit without `[skip release]` (or use the manual path).

### Auto-bump fails

The workflow logs will say which step failed. Common cases:

- **Consistency check failed:** the merge introduced drift. Fix on `main` with another commit. The next release-worthy commit picks up your fix.
- **Tag already exists:** somebody pushed the same tag manually. Use the manual path with the next version.

### Quick reference: prefixes you'll actually use

```
major: rename INDEX.md schema      # 0.5.0 → 1.0.0
minor: add corezero-predict skill     # 0.5.0 → 0.6.0
patch: fix install.sh on macOS     # 0.5.0 → 0.5.1
chore: rename internal var         # no release
docs: update QUICKSTART            # no release
```

## Manual flow (milestone / breaking / controlled releases)

Use this when you want to:

- Cut a milestone release (`v1.0.0`) deliberately
- Ship multiple merged changes as one bundled release
- Release a hotfix without waiting for a `fix:` commit
- Test the release machinery with a specific version

### Standard sequence (manual path)

1. **Land all changes on `main`.**
   ```bash
   git checkout main
   git pull
   ```

2. **Bump `VERSION` to the next semver value.** Pick by hand using the table above.
   ```bash
   echo "1.0.0" > VERSION
   ```

4. **Commit the bump with `release:` prefix** so auto-bump doesn't fire:
   ```bash
   git add VERSION
   git commit -m "release: v1.0.0"
   git push
   ```

5. **Tag, then handle the branch by bump type.**

   **Major or minor** — create the release branch:
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   git push origin main:refs/heads/release/1.0.x
   ```

   **Patch** — fast-forward the existing release branch:
   ```bash
   # On main, with the patch already committed:
   git tag v1.0.1
   git push origin v1.0.1
   git checkout release/1.0.x
   git merge --ff-only v1.0.1
   git push origin release/1.0.x
   git checkout main
   ```

   If you cannot fast-forward (release branch has commits main doesn't), you have a divergence — see the hotfix section below.

6. **Watch the release workflow** in GitHub → Actions → Release. When green, the release page is live at `releases/tag/v1.0.0`.

7. **Verify the public install works** (optional, from a clean target):
   ```bash
   curl -fsSL https://raw.githubusercontent.com/<user>/AI-agents-dev-kits/main/scripts/install.sh \
     | bash -s -- /tmp/post-release-test
   cat /tmp/post-release-test/.corezero-version
   ```

The `release:` commit prefix matters — without it, auto-bump would also fire on step 4's push and try to create another tag.

## Combining the two flows

The flows compose cleanly because they use different triggers (commit type vs. tag push). You can:

- Use auto for `feat:`/`fix:` (most weeks) and manual for breaking releases
- Use auto for everything until a milestone, then manually tag `v1.0.0` from whatever auto landed last
- Disable auto for a stretch by prefixing all merges with `[skip release]`, then manually tag

The manual path always wins. If you tag `v0.5.0` directly while `auto-bump` is mid-flight, the worst case is one workflow fails the "tag already exists" check and exits cleanly.

## If a release goes wrong

### Workflow failed before publishing

No release page was created. Fix on `main`, push a new commit, the next release-worthy commit picks up the fix.

For tag/VERSION mismatches on the manual path:
```bash
git push --delete origin v0.2.0
git tag -d v0.2.0
# fix VERSION, recommit, retag, repush
```

### The release shipped a bug

Cut a patch release. **Never rewrite a published tag** — adopters may have pinned to it.

Auto path: push a `patch: ...` commit, get a patch bump automatically.
Manual path: bump VERSION to the next patch, follow steps 4-6 above.

If the bug is severe (broken installer, corrupted manifest), call it out in the patch release notes so adopters know to upgrade.

## Hotfixing an older release

This is what release branches are for.

Scenario: `main` is at v0.6.0, but a critical bug is reported in v0.5.x. Adopters who pinned to v0.5.0 need a fix without inheriting v0.6.0's other changes.

```bash
# 1. Switch to the parked release branch
git checkout release/0.5.x
git pull

# 2. Cherry-pick the fix from main (or write it directly here)
git cherry-pick <commit-sha-on-main>

# 3. Bump VERSION on the branch
echo "0.5.1" > VERSION

# 4. Commit with release: prefix so auto-bump doesn't fire
#    (auto-bump only watches main anyway, but the prefix is a safety habit)
git add VERSION
git commit -m "release: v0.5.1 — hotfix <issue>"

# 5. Tag and push the branch + tag
git tag v0.5.1
git push origin release/0.5.x
git push origin v0.5.1
```

The tag push fires `release.yml` and publishes v0.5.1 — even though `main` is at v0.6.0.

The same fix should also land on `main` for v0.7.0 and beyond. Either cherry-pick the other direction or land it on a normal feature branch and merge to `main` with the right prefix.

## What the workflows do NOT do

- **No npm / homebrew / package registry publish.** Kit ships from GitHub raw URLs only.
- **No automatic VERSION bump on `chore:` / `docs:` / `refactor:`** — those don't get releases.
- **No installer end-to-end test.** Workflows run consistency check, not a full install. Smoke-test manually if the change touches `install.sh` or `manifest.json`.
- **No release on PR open.** Only the merge commit on `main` matters.

## Pre-release checklist (manual path)

Before tagging:

- [ ] All target changes merged to `main`
- [ ] `VERSION` bumped using the semver decision rule
- [ ] Skills, memory schema, or templates that changed are reflected in `manifest.json` if needed
- [ ] If skills changed materially, `HARNESS_CARD.md` subsystem table is up to date
- [ ] If `manifest.json` changed, smoke-tested fresh install in `/tmp/`
- [ ] Commit pushed to `main` with `release:` prefix

After publishing:

- [ ] GitHub Actions release run is green
- [ ] Release page exists at `releases/tag/v<x.y.z>`
- [ ] `curl ... install.sh | bash` works from a clean target

## Pre-merge checklist (automatic path)

Before merging a PR:

- [ ] Commit message uses the right prefix for the change you intend (see table)
- [ ] If multiple commits in the PR, the merge commit prefix is what auto-bump reads — squash to a single Conventional-Commit subject
- [ ] If you don't want this PR to ship, add `[skip release]` to the merge commit
