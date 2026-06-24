# Changelog

All notable changes to the Polystate Claude Code plugin.

## [2.0.0] — 2026-06

### Added
- **Live MCP server connection** (`.mcp.json`, HTTP transport, Bearer auth) to the
  Polystate MCP — 10 tools: `visa_check`, `get_visa_requirements`, `tax_compare`,
  `get_tax_rates`, `get_crypto_tax_treatment`, `get_tax_treaties`,
  `get_residency_programs`, `get_company_formation`, `compare_jurisdictions`,
  `get_legal_changes`.
- Skills: `/polystate:visa-check`, `/polystate:tax-compare`, `/polystate:jurisdiction`,
  `/polystate:residency`, `/polystate:llc-setup`, `/polystate:polystate-apply`,
  `/polystate:polystate`.
- `jurisdiction-advisor` agent.
- `UserPromptSubmit` topic-hint hook (suggests Polystate tools on immigration/tax queries).
- Bundled offline JSON for 171 jurisdictions (crypto-tax, scoring, visa programs,
  residency, company formation) — skills work without an API key.

### Notes
- Get a free API key (100 requests/month) at https://polystate.io/developers.
- Endpoint: `https://polystate-mcp-server.shy-surf-2fdf.workers.dev/mcp`
  (a branded `mcp.polystate.io` is planned for a future release).

## [1.0.0]

- Initial release: 7 core skills with bundled offline data.
