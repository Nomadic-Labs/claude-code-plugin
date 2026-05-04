# Polystate — Claude Code Plugin

**Version 2.0+** — Live **MCP** connection to `https://mcp.polystate.io/mcp` plus **offline JSON fallbacks** (no API key required for fallback).

> Immigration & tax intelligence: **171** jurisdictions for crypto-tax and scoring, **100+** visa-program rows, curated residency and **company formation** catalogs.

## MCP setup (live data)

1. Obtain a Polystate **API key** (same key as for the MCP product / `api_keys` in Supabase).
2. Export it before starting Claude Code:

```bash
export POLYSTATE_API_KEY='your-key-here'
```

3. Install the plugin (or use `--plugin-dir`). The plugin ships **`.mcp.json`**: HTTP transport + `Authorization: Bearer ${POLYSTATE_API_KEY}`.
4. Run `/reload-plugins`, then `/mcp` and confirm the **`polystate`** server is connected.

Without a key, skills still work using bundled `data/*.json` (older snapshot).

## Install

```bash
/plugin install github:Spider333/polystate-claude-plugin
```

Test locally:

```bash
export POLYSTATE_API_KEY='…'   # optional for live MCP
claude --plugin-dir ./polystate-claude-plugin
```

## Skills

All skills are namespaced under `/polystate:`.

| Skill | Command | Notes |
|-------|---------|--------|
| Overview | `/polystate:polystate` | Setup, list commands |
| Visa | `/polystate:visa-check [passport] [dest]` | MCP: `visa_check` (ISO) |
| Tax | `/polystate:tax-compare [c1] [c2?]` | MCP: `tax_compare` (2 ISOs) or `get_crypto_tax_treatment` (1) |
| Jurisdiction | `/polystate:jurisdiction [country]` | MCP: `compare_jurisdictions`, `get_crypto_tax_treatment`, … |
| Residency | `/polystate:residency [country]` | MCP: `get_residency_programs` |
| LLC / formation | `/polystate:llc-setup [country] [type?]` | MCP: `get_company_formation` |
| Services / apply | `/polystate:polystate-apply [country?]` | MCP resource `polystate://services/{ISO}` when available; else **https://polystate.io** |

Examples:

```
/polystate:visa-check SK TH
/polystate:tax-compare PT DE
/polystate:llc-setup US llc
/polystate:polystate-apply PA
```

## Topic hint hook

When the plugin is enabled, **`hooks/UserPromptSubmit`** runs `hooks/polystate-topic-hint.py` on each prompt. If the text looks immigration/tax related, it injects a short reminder to use Polystate MCP or slash skills.

## Jurisdiction Advisor agent

```
/agents → select "jurisdiction-advisor"
```

Uses MCP tools when connected, otherwise reads `${CLAUDE_PLUGIN_ROOT}/data/`.

## Data (offline bundle)

| File | Role |
|------|------|
| `data/crypto-tax.json` | 171 jurisdictions |
| `data/jurisdiction-scoring.json` | Scoring / QoL |
| `data/visa-programs.json` | 104 program rows |
| `data/residency-compare.json` | 27 curated entries |
| `data/company-formation.json` | Company / LLC catalog |

Refresh by copying newer JSON from `polystate-mcp-server/data/` on branch **`chore/mcp-phase-2-v2`** (or current main) and bumping the plugin version.

## MCP server branch

The canonical MCP feature branch used for this phase is **`origin/chore/mcp-phase-2-v2`** on [`polystate-mcp-server`](https://github.com/Nomadic-Labs/polystate-mcp-server) (tools include `get_company_formation`, country services resource, auth via Bearer).

## About Polystate

👉 **https://polystate.io** — Consultations, applications, services.

## License

MIT
