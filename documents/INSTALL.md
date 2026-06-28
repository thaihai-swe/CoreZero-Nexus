# Install And Upgrade Flow

This runbook covers the supported install and upgrade path for the shipped package.

## Public Install Command

```bash
curl -fsSL https://raw.githubusercontent.com/thaihai-swe/CoreZero/main/scripts/install.sh \
  | bash -s -- /path/to/your/project
```

## Local Install Command

```bash
bash scripts/install.sh /path/to/your/project
bash scripts/install.sh /path/to/your/project --dry-run
```

## Installer Contract

- Root `scripts/install.sh` is the public entrypoint.
- `kit/scripts/install.sh` is the package installer implementation.
- `kit/manifest.json` decides what ships.
- `overwrite` content updates on every install.
- `copyIfMissing` content seeds only when absent.
- `preserve` content is never rewritten.

## Required First-Run Flow

After install:

1. Read `kit-map.md` to understand the command layers
2. Read `skills-guide.md` for the shipped command roster
3. (Optional but recommended) Install and index GitNexus for code-aware context:
   ```bash
   npm install -g gitnexus
   cd /path/to/project && gitnexus analyze && gitnexus setup
   ```
   GitNexus exposes a knowledge graph (deps, call chains, clusters) via MCP. The kit auto-detects it — `AGENTS.md` prefers `gitnexus context` / `gitnexus impact` before reading source files. See [agent-capabilities.md](https://github.com/abhigyanpatwari/GitNexus) for details.
4. Run `/starter-init`
5. Continue with `/spec-research` or `/spec-requirements`
6. Use `/context-status`, `/harness-maintain`, and `/spec-adr` when governance or multi-feature coordination work needs them
7. Use `/technical-docs` and `/codebase-documenter` when the repo needs durable documentation outputs
8. Use `/visualize` when a polished SVG or Mermaid diagram materially improves clarity

## Validation For Packaging Changes

Run the installer locally before shipping package changes:

```bash
bash scripts/install.sh /tmp/corezero-check --dry-run
```

If the change touches install behavior or shipped paths, also do one real install smoke test into a temporary directory.

For releases, also verify the command list, Pages landing copy, and version sync in `documents/releasing.md`.
