#!/usr/bin/env python3
"""UserPromptSubmit hook: inject a short Polystate reminder when the prompt looks immigration/tax related."""
import json
import re
import sys

KEYWORD_PATTERNS = (
    r"\bvisa\b",
    r"\bvisas\b",
    r"\btax\b",
    r"residen",
    r"jurisdiction",
    r"nomad",
    r"immigration",
    r"citizenship",
    r"passport",
    r"crypto\s*tax",
    r"\bllc\b",
    r"company formation",
    r"offshore",
    r"tax treaty",
)


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        sys.exit(0)

    prompt = (data.get("prompt") or "").lower()
    if not prompt:
        sys.exit(0)

    if not any(re.search(p, prompt, re.I) for p in KEYWORD_PATTERNS):
        sys.exit(0)

    tip = (
        "[Polystate plugin] This question may match Polystate live data. "
        "If MCP `polystate` is connected (/mcp), prefer its tools: "
        "visa_check, tax_compare, get_residency_programs, get_company_formation, compare_jurisdictions. "
        "Slash skills: /polystate:visa-check, :tax-compare, :residency, :jurisdiction, :llc-setup, :polystate-apply. "
        "Offline fallback: ${CLAUDE_PLUGIN_ROOT}/data/*.json."
    )
    out = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": tip,
        }
    }
    print(json.dumps(out))


if __name__ == "__main__":
    main()
