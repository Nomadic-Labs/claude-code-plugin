# Changelog

All notable changes to the Polystate Claude Code plugin.

## [2.2.0] — 2026-10

### Changed
- The API key is now a plugin setting (`userConfig.api_key`, stored in the system's
  secure credential store) and no longer read from the `POLYSTATE_API_KEY`
  environment variable. **Existing users must enter their key once in the plugin's
  configuration.**
- `data/crypto-tax.json` and `data/jurisdiction-scoring.json` are written one country
  per line. Same content, under the directory's 256 KiB per-file limit.
- Added `privacyPolicyUrl`.

## [2.1.0] — 2026-10

### Changed
- Listing and docs now cover all 13 MCP tools. Three shipped on the server after
  2.0.0: `optimize_relocation` (ranked jurisdictions for open-ended
  "where should I move" questions), `check_eligibility` (free check of a nationality against a Polystate
  service) and `book_service` (starts a paid Stripe checkout for a service; the
  user completes payment in the browser).
- README: removed references to the retired `chore/mcp-phase-2-v2` server branch.

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
