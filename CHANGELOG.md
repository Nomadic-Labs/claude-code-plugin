# Changelog

All notable changes to the Polystate Claude Code plugin.

## [2.3.1] — 2026-11

### Changed
- The live-MCP part of every skill now matches the current server. The bundled
  data and the offline-fallback steps are unchanged.
  - Country inputs: an ISO-3166 code or an English country name. The skills no
    longer tell Claude to convert names to codes first.
  - `polystate-apply`: uses `list_services`, then `check_eligibility`, then
    `book_service`. It no longer says that booking has no MCP tool.
  - `visa-check`: follows up with `get_visa_requirements`.
  - `tax-compare` and `residency`: call `get_verified_facts` first for Paraguay,
    Honduras and Próspera.
  - `jurisdiction`: uses `optimize_relocation` for open-ended "where should I
    move" questions.
  - Each skill carries the server's presentation rules: quote the source's
    wording for a conditional rate, a null value is not zero, no guarantees.
- README skills table updated to match.

## [2.3.0] — 2026-11

### Changed
- MCP endpoint is now `https://mcp.polystate.io/mcp` (was the `workers.dev` host,
  which still serves the same Worker).
- Listing and README now say 16 MCP tools (13 is the ChatGPT surface) and list
  `list_services`, `check_licensed_agent` and `get_verified_facts`.
- Bundled data refreshed from `main`: `crypto-tax.json`, `visa-programs.json` and
  `residency-compare.json` from `polystate-brain/data/countries/`;
  `company-formation.json` and `jurisdiction-scoring.json` from
  `polystate-mcp-server/data/`.
  - `company-formation.json`: 95 entries (was 92), adding three Georgia entries
    ("Individual Entrepreneur (Small Business Status)", "Limited Liability Company
    (LLC)", "LLC with Virtual Zone Status"). Every entry now carries `compiled_by: "claude-llm-assisted"`, and 72
    entries are rated `medium` confidence instead of `high`.
  - `visa-programs.json`: every row now has an alpha-2 `countryCode`.
  - `residency-compare.json`, Uruguay digital nomad permit: no fixed income figure
    is published; the USD 1,500/month requirement is replaced by a sworn statement
    of economic means, with a Uruguay XXI source (`lastVerified` 2026-10-26).
  - `crypto-tax.json`, Honduras: crypto is not regulated or legal tender (central
    bank notice, 29 Jul 2022), replacing "exploring Bitcoin as legal tender".
  - `crypto-tax.json` and `jurisdiction-scoring.json`: 172 garbled characters
    repaired ("â¬600K" now "€600K", "Â£220k" now "£220k", dashes and accents); same fix
    as polystate-brain#93 and polystate-mcp-server#63.
  - `jurisdiction-scoring.json`: no content change.

## [2.2.3] — 2026-10

### Fixed
- `data/residency-compare.json`, Uruguay Mercosur: the record said Uruguayan residency
  is not cancelled by a fixed absence count. Permanent residence can be cancelled after
  more than three years abroad (Migration Law 18.250, Art. 47).

## [2.2.2] — 2026-10

### Fixed
- `data/residency-compare.json`, Uruguay Mercosur: the driving-licence line no longer
  lists Mexico under the 1968 Vienna Convention on Road Traffic (Mexico signed and
  never ratified) and no longer says the 1968 and 1949 conventions do not overlap.

## [2.2.1] — 2026-10

### Changed
- `data/residency-compare.json` refreshed from the canonical dataset. Four Latin
  America records carry the September 2026 update (Paraguay temporary and permanent
  residency, Uruguay Mercosur, Brazil investor), and every record now has an alpha-2
  `countryCode`.
- Paraguay permanent residency: a diploma alone is no longer accepted as proof of
  economic solvency (Resolution DNM 407/2026, applications filed from 6 July 2026).
  The previous file said it was.

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
