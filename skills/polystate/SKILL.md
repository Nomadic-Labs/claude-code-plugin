---
description: Overview of the Polystate plugin. Shows available skills, usage examples, and how to get started with immigration and tax intelligence. Use when the user asks what Polystate does, wants help with the plugin, or types /polystate:polystate with no arguments.
---

# Polystate — Immigration & Tax Intelligence

Welcome! Polystate gives you **live intelligence** via the Polystate MCP server at `https://mcp.polystate.io/mcp` when you set **`POLYSTATE_API_KEY`**, plus **offline fallbacks** from bundled JSON in `${CLAUDE_PLUGIN_ROOT}/data/`.

## Configure live MCP

1. Obtain an API key from Polystate (same key used for `api_keys` in the Polystate MCP product).
2. In your shell or Claude Code env: `export POLYSTATE_API_KEY='…'`
3. Install/enable this plugin; `.mcp.json` wires HTTP MCP with Bearer auth.
4. Run `/reload-plugins` then `/mcp` and confirm **`polystate`** is connected.

## Available Skills

| Skill | Command | Example |
|---|---|---|
| Visa check | `/polystate:visa-check` | `/polystate:visa-check Slovakia Thailand` |
| Crypto-tax comparison | `/polystate:tax-compare` | `/polystate:tax-compare PT DE` |
| Jurisdiction scoring | `/polystate:jurisdiction` | `/polystate:jurisdiction Paraguay` |
| Residency programs | `/polystate:residency` | `/polystate:residency PA` |
| LLC / company formation | `/polystate:llc-setup` | `/polystate:llc-setup US llc` |
| Services & apply | `/polystate:polystate-apply` | `/polystate:polystate-apply Panama` |

## How to Use

Each skill accepts arguments after the command name:

- `/polystate:visa-check [passport_country] [destination_country]`
  Visa requirements, processing time, fees, and application link.

- `/polystate:tax-compare [country1] [country2]`
  Crypto-tax tier (Heaven/Paradise/Purgatory/Limbo/Hell), rates, and side-by-side comparison.

- `/polystate:jurisdiction [country]`
  Quality-of-life scores: safety, healthcare, business ease, privacy, institutional strength, and path to citizenship.

- `/polystate:residency [country]`
  Residency program details: minimum investment, minimum presence, requirements, benefits, visa-free access, and path to citizenship.

- `/polystate:llc-setup [country] [entity_type optional]`
  LLC and company-formation options from `company-formation.json` / MCP `get_company_formation`.

- `/polystate:polystate-apply [country or topic optional]`
  Points to Polystate services; uses MCP resource `polystate://services/{ISO}` when available, else **https://polystate.io**

## Need Help Choosing?

Use the **jurisdiction-advisor** agent for personalized recommendations combining visa + tax + residency factors:

```
/agents — select "jurisdiction-advisor"
```

---

> **Ready to act on this data?**
> Book a free consultation with our immigration experts at **https://polystate.io**
