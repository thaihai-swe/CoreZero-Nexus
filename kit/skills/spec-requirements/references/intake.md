# Intake (Opening Wave)

The intake gate is the first step in `spec-requirements`. It runs **before** any grilling, codebase reading, or spec authoring. Its job is to classify the work in two dimensions — *what kind of work this is* and *what risk it carries* — and produce a one-line lane decision recorded in `status.md`.

The principle: **classification first, ceremony second.** A misclassified piece of work either drowns in ceremony it didn't need or skips checks it required. The intake step makes that classification explicit and durable.

## Output

Append (or update) the `## 🧪 Intake` section in `artifacts/features/<slug>/status.md`:

```markdown
## 🧪 Intake

- **Input type:** <new_spec | spec_slice | change_request | new_initiative | maintenance | harness_improvement>
- **Risk flags:** <comma-separated list, or `none`>
- **Lane:** <Tiny | Standard | Complex>
- **One-line restatement:** <what this work actually is, in your own words>
- **Affected docs/specs:** <paths or `n/a`>
- **Reasoning:** <one sentence — why this lane>
```

The lane decision feeds the `## 🧭 Delivery Profile` section. If the lane differs from the existing profile, **promote** to the higher level — never silently demote.

## Input Types

Pick the one that fits best. If two seem to fit, pick the one with the heavier downstream artifacts.

| Type | Use when | Typical artifact |
|---|---|---|
| `new_spec` | Turning a user-provided project spec into harness-ready docs from scratch. | Product docs, candidate features, decisions. |
| `spec_slice` | Implementing a selected behavior from an already-accepted spec. | Feature spec under `artifacts/features/<slug>/`. |
| `change_request` | Changing, fixing, or refining an already-accepted behavior. | Feature spec or direct patch. |
| `new_initiative` | Adding a larger product area that needs multiple feature specs. | Initiative notes plus per-feature specs. |
| `maintenance` | Changing technical, operational, or dependency behavior (no product surface change). | Feature spec, validation report, or decision. |
| `harness_improvement` | Improving how humans and agents collaborate (skills, templates, memory, scripts). | Direct kit edit or harness backlog item. |

## Risk Flag Checklist

Mark every flag that applies. Multiple flags are common.

| Flag | Applies when the work touches |
|---|---|
| `auth` | login, logout, sessions, JWT, password, refresh token |
| `authorization` | roles, permissions, tenant or company scope |
| `data_model` | schema, migrations, uniqueness, deletion, retention |
| `provider` | external APIs, payment processors, identity providers |
| `migration` | data backfill, persistent state changes, schema rollouts |
| `cross_boundary` | more than one major architectural boundary |
| `public_api` | endpoints, SDK signatures, or contracts other features depend on |
| `security` | secrets, key handling, audit logs, anything in `security-policy.md` |
| `harness-maintain` | this kit's skills, templates, memory schemas, or scripts |
| `none` | none of the above — record explicitly to show you checked |

## Lane Decision Rules

Apply in order. The first matching rule wins.

1. If any of `auth`, `authorization`, `data_model`, `migration`, `public_api`, `security`, or `harness-maintain` is set → **Complex**.
2. If `cross_boundary` is set, OR input type is `new_initiative` or `harness_improvement` → at least **Standard** (promote to **Complex** if any rule above also applies on closer inspection).
3. If input type is `maintenance` and the change is one file with no behavior change → **Tiny**.
4. If input type is `change_request` and the surface is narrow with no risk flags → **Tiny**.
5. Otherwise → **Standard**.

When two rules push different ways, **always pick the higher lane**. Over-ceremony costs time; under-ceremony costs correctness.

## Stop Conditions

Stop and ask the user before proceeding when:

- The user prompt does not clearly fit any input type.
- Risk flags are set but the user has not confirmed this work should touch them.
- The lane decision would force System Spec Mode but the request is scoped to a single feature.

## Anti-Patterns

- **"It's obviously Tiny" without checking flags.** If `auth`, `data_model`, `security`, or `harness-maintain` is touched, it is not Tiny no matter how small the diff looks.
- **Recording `none` for risk flags without inspecting.** Read at least the affected files first.
- **Skipping intake on `change_request` because "we already have a spec."** A change request still needs a fresh lane decision — the original lane might be wrong now.
- **Picking a lane based on time estimate.** Lanes encode risk, not effort. A 30-minute auth change is still Complex.
