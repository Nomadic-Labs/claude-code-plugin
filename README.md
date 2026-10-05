# Polystate — Claude Code Plugin

**Version 2.0+** — Live **MCP** connection to `https://polystate-mcp-server.shy-surf-2fdf.workers.dev/mcp` plus **offline JSON fallbacks** (no API key required for fallback).

> Immigration & tax intelligence: **171** jurisdictions for crypto-tax and scoring, **100+** visa-program rows, curated residency and **company formation** catalogs.

## MCP setup (live data)

1. Get a free Polystate **API key** (100 requests/month) at https://polystate.io/developers.
2. Install the plugin (or use `--plugin-dir`). When you enable it, Claude Code asks for the **Polystate API key** and stores it in your system's secure credential store. To set or change it later, run `/plugin`, select **polystate** and open its configuration.
3. Run `/reload-plugins`, then `/mcp` and confirm the **`polystate`** server is connected.

The key is sent only to the Polystate MCP server, as a Bearer token.

Without a key, skills still work using bundled `data/*.json` (older snapshot).

## Install

This repo is its own Claude Code marketplace. Add it, then install the plugin:

```bash
/plugin marketplace add Nomadic-Labs/claude-code-plugin
/plugin install polystate@polystate
```

For live MCP data, get a free API key (100 requests/month) at
https://polystate.io/developers and enter it when the plugin asks for the
**Polystate API key**. The key is optional: skills fall back to bundled data without it.

Then `/reload-plugins` and `/mcp` to confirm the **polystate** server is connected.

Test locally from a clone:

```bash
claude --plugin-dir ./claude-code-plugin
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

Refresh by copying newer JSON from `polystate-mcp-server/data/` on `main` and bumping the plugin version.

## MCP tools

The live server exposes 13 tools:

| Tool | What it does |
|------|--------------|
| `visa_check` | Visa requirement for one passport and one destination |
| `get_visa_requirements` | Requirements and documents for a visa, for one passport and one destination |
| `optimize_relocation` | Ranked jurisdictions for open-ended "where should I move" questions |
| `compare_jurisdictions` | Ranked multi-country comparison on a weighted scoring model |
| `tax_compare` | Tax comparison of two countries |
| `get_tax_rates` | Income, corporate, VAT, capital gains and crypto rates for a country |
| `get_crypto_tax_treatment` | Crypto tax treatment for a country |
| `get_tax_treaties` | Double-tax treaty partners of a country |
| `get_residency_programs` | Residency programs for a country |
| `get_company_formation` | Company and LLC formation options |
| `get_legal_changes` | Legal and regulatory changes, newest first |
| `check_eligibility` | Free check of a nationality against a Polystate service |
| `book_service` | Starts a paid Stripe checkout for a Polystate service |

`book_service` is the only tool that leads to a charge. It returns a checkout link; nothing is billed until the user pays in the browser.

## About Polystate

👉 **https://polystate.io** — Consultations, applications, services.

## License

MIT
