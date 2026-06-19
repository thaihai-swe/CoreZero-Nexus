# Codemap

> Seeded placeholder. Refresh with `/harness-maintain` after the installed surface changes materially.

## Installed Surface Map

| Path | Responsibility | Notes |
| :--- | :--- | :--- |
| `AGENTS.md` | Runtime entry router | Installed at the adopter repo root |
| `MASTER_INDEX.md` | Root routing index | Points to deeper kit surfaces |
| `docs/` | Adopter-facing documentation | Includes `project/`, `policies/`, and `generated/` |
| `memories/repo/` | Durable repository memory | `MASTER_INDEX.md` routes memory loading |
| `memories/domain/` | Adopter-owned domain pack templates | Replace example content with project-specific content |
| `skills/` | Shipped command contracts | Core workflow, governance, docs authoring, and specialist visualization |
| `docs/rules/` | Shipped coding and safety rules | Includes Python and security guidance |
| `scripts/` | Install and validation helpers | Includes `install.sh` |

## First Entry Points

- `MASTER_INDEX.md` — start here after install
- `scripts/install.sh` — installer and upgrade entrypoint
