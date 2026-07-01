# Client Integrations


## Integration Pattern

### 1. Router-First

Every client reads `AGENTS.md` as the entry point. It's a thin router (< 50 lines) that points to:
- Skills for workflow
- Memory files for context
- Harness config for commands

### 2. Skill Loading

Skills are loaded just-in-time when invoked. The agent reads the relevant `SKILL.md` and its `references/` directory. This keeps the context window lean.

### 3. Memory as Shared State

All clients share the same memory layer (`memories/repo/`). This means:
- Constitution rules apply regardless of which client is used
- Security policy is enforced uniformly
- Knowledge base is available to all agents
- Harness config provides consistent commands

## Multi-Client Projects

When multiple clients work on the same project:
- All share the same `memories/repo/` (single source of truth)
- All share the same `artifacts/features/` (durable state)
- Handoffs work across clients (handoff.md is client-agnostic)
- The harness config captures commands that work for all clients

## Code Intelligence Providers (optional)

CoreZero skills use **capability intents** instead of hard-coded tool names. When a skill needs to understand an execution flow, it asks for **[1] Explore / query concept**; before editing a symbol, it asks for **[3] Impact — upstream callers**. This allows the kit to work with any code intelligence MCP provider.

The mapping from capability intents to concrete tool calls lives in `core-zero/project/code-intelligence.md`. Set `active_provider` there to your chosen provider (or `none` to skip entirely — the kit works fully without it).

### GitNexus (primary example)

[GitNexus](https://github.com/abhigyanpatwari/GitNexus) indexes any codebase into a knowledge graph and exposes it via MCP. It supports all 11 capability intents natively.

#### Setup

```bash
npm install -g gitnexus
cd /path/to/your/repo && gitnexus analyze && gitnexus setup
```

#### OpenCode MCP config

Add to `~/.config/opencode/config.json`:

```json
{
  "mcp": {
    "gitnexus": {
      "type": "local",
      "command": ["gitnexus", "mcp"]
    }
  }
}
```

#### Activation

In `core-zero/project/code-intelligence.md`, set:

```yaml
active_provider: gitnexus
providers:
  gitnexus:
    enabled: true
```

### codebase-memory-mcp (alternative)

[codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) is a lightweight alternative covering 8 of 11 capability intents. Setup: download the binary, configure in your MCP client, then index the repo. See `core-zero/project/code-intelligence.md` for the full capability mapping table.

### Skills that benefit

| Skill | Capability intents used | Benefit |
|-------|------------------------|---------|
| `spec-research` | [1] Explore / query, [2] Symbol context | Architecture exploration and finding execution flows |
| `spec-plan` | [3] Impact — upstream callers | Blast radius analysis before designing changes |
| `spec-implement` | [2] Symbol context | Dependency awareness during implementation |
| `harness-verify` | [6] Detect changed symbols | Verify no unexpected side effects |
| `code-review` | [2] Symbol context, [6] Detect changes | Call chain audit + diff-to-symbol mapping |

The kit works identically without any code intelligence provider — it is additive, not required. When a provider is installed, `AGENTS.md` activates its `Never Do` rules (e.g. never edit without impact analysis first).

## Golden Config Pattern

For each client, the ideal setup:
1. Client reads its entrypoint file automatically
2. Entrypoint routes to `AGENTS.md` for operating rules
3. Agent loads skills JIT when invoked
4. Memory provides durable context without re-discovery
5. Artifacts provide feature state without chat history dependency
