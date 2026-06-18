# Codemap

> Seeded placeholder. Refresh with `/harness-maintain` after the installed surface changes materially.

## Installed Surface Map

| Path | Responsibility | Notes |
| :--- | :--- | :--- |
| `AGENTS.md` | Runtime entry router | Installed at the adopter repo root |
| `INDEX.md` | Root routing index | Points to deeper kit surfaces |
| `HARNESS_CARD.md` | Runtime status and limits card | Read before non-trivial work |
| `docs/` | Adopter-facing documentation | Includes `guides/`, `project/`, `policies/`, and `generated/` |
| `memories/repo/` | Durable repository memory | `INDEX.md` routes memory loading |
| `memories/domain/` | Adopter-owned domain pack templates | Replace example content with project-specific content |
| `skills/` | Shipped command contracts | Core workflow, governance, docs authoring, and specialist visualization |
| `rules/` | Shipped coding and safety rules | Includes Python and security guidance |
| `scripts/` | Install and validation helpers | Includes `install.sh` |

## First Entry Points

- `docs/README.md` — start here after install
- `docs/guides/onboarding.md` — required first-run guide
- `scripts/install.sh` — installer and upgrade entrypoint
