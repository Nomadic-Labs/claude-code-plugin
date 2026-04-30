# Polystate — Claude Code Plugin

> Immigration & tax intelligence: **171 jurisdictions** for crypto-tax and scoring, **100+** visa-program entries, and **curated** residency-program data — ready in your terminal.

## Install

```bash
/plugin install github:Spider333/polystate-claude-plugin
```

Or test locally:

```bash
claude --plugin-dir ./polystate-claude-plugin
```

## Skills

All skills are namespaced under `/polystate:`.

### `/polystate:visa-check [passport] [destination]`

Visa requirements, fees, processing time, and official application link.

```
/polystate:visa-check Slovakia Thailand
/polystate:visa-check Germany Portugal
```

### `/polystate:tax-compare [country1] [country2]`

Crypto-tax tier (Heaven → Hell), capital gains, income tax, staking/mining treatment.

```
/polystate:tax-compare Paraguay
/polystate:tax-compare UAE Portugal
```

### `/polystate:jurisdiction [country]`

Quality-of-life scores: safety, healthcare, business ease, privacy, banking, citizenship path.

```
/polystate:jurisdiction Panama
/polystate:jurisdiction Paraguay vs Georgia
```

### `/polystate:residency [country]`

Residency programs: investment, presence, requirements, benefits, path to citizenship.

```
/polystate:residency Panama
/polystate:residency Paraguay
```

### `/polystate:polystate`

Overview and help.

## Jurisdiction Advisor Agent

For complex multi-factor questions (tax + residency + lifestyle), use the built-in agent:

```
/agents → select "jurisdiction-advisor"
```

Ask it things like:

- *"I'm a Slovak crypto investor wanting to minimize taxes with minimal travel. Top 3 options?"*
- *"Best low-presence residency for someone with a UK passport and $50K/year remote income?"*

## Data

- **Crypto-tax + jurisdiction scoring:** `countries` arrays cover **171** ISO jurisdictions (bundled dataset).
- **Visa programs:** **104** program rows in `visa-programs.json` (multiple programs per destination where applicable).
- **Residency programs:** **27** curated entries in `residency-compare.json`.
- Sources: Polystate MCP server data snapshots (visa, crypto-tax, residency compare, jurisdiction scoring).
- Embedded in the plugin (**no internet** required). Refresh by bumping the plugin version after copying newer JSON from `polystate-mcp-server/data/`.

## About Polystate

Polystate helps global citizens navigate immigration, residency, and tax optimization.

👉 **https://polystate.io** — Book a consultation or explore our services.

## License

MIT
