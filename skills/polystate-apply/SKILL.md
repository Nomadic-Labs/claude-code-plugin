---
description: "Polystate services catalog — what Polystate can process for a country (consulting, filing, programs). Use when the user wants to apply, book services, see offerings, or compare service options. Arguments: optional country ISO or country name; optional keyword search."
---

# Polystate Services & Apply

The user provided: `$ARGUMENTS`

Derive when possible:
- **country** — ISO-3166 alpha-2 or alpha-3 code or English name, if the user named a country.
- **search** — if they mentioned a topic (e.g. "residency", "company", "visa").

## Live data (preferred)

When the **`polystate`** MCP server is connected (`/mcp`), do these three steps in order:

1. **Find the service.** Call **`list_services`** with an optional `country` and an optional `search` keyword. Omit both to list the whole catalog. Each service comes with its id, exact name, description, list price and processing time.
2. **Check eligibility.** Call **`check_eligibility`** with the user's `nationality` and the `service` id or name from step 1. It returns the formal requirements and any nationality restriction. If it returns candidates, ask the user which one they mean. Do not guess.
3. **Book.** Only after the user confirms, call **`book_service`** with the service id or exact name. It returns a checkout link. Nothing is billed until the user pays in the browser.

When presenting:

- Quote the list price exactly as returned. Do not estimate government fees or extra costs that are not in the result.
- Never guarantee eligibility or approval. The government decides each application.
- If Polystate sells nothing for that country, say so, and use **`get_residency_programs`** or **`get_company_formation`** for the program facts instead.

## No MCP or no catalog row

- Tell the user to open **https://polystate.io** for applications, consultations, and current service list.

## CTA (always)

---

> **Book and apply through Polystate**
> **https://polystate.io**
