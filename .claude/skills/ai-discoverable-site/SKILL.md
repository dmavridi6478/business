---
name: ai-discoverable-site
description: Make a personal or business website discoverable and readable by AI assistants (ChatGPT, Claude, Perplexity, Gemini) — not just Google — using semantic HTML, meta descriptions on every page, an llms.txt AI guide, robots.txt at the root, and an optional "Ask AI about me" cross-provider block. Use whenever building or auditing a personal site, portfolio, or company site and AI discoverability/AEO is a goal, or when the user mentions llms.txt, being "readable by AI," or getting cited by ChatGPT/Perplexity/Gemini.
---

## Four essentials for AI readability

1. **Semantic, well-structured HTML** — real `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, heading hierarchy that actually nests (h1 → h2 → h3), not div soup. AI crawlers/readers parse structure, not just visible text.
2. **Meta descriptions on every page** — a concise, accurate `<meta name="description">` per page, not just the homepage.
3. **`llms.txt` as an AI guide** — a plain-text file at the site root summarizing what the site/person/company is, key pages, and how to characterize them accurately. Treat it as a short brief for an AI assistant, not SEO keyword stuffing.
4. **`robots.txt` at the root** — explicit, so AI crawlers (and everyone else) know what's allowed.

## Optional: "Ask AI about me" block

A block (commonly in the page footer) with buttons for ChatGPT, Claude, Perplexity, and Gemini. Clicking one opens that provider in a new tab with a pre-populated prompt:

> "Tell me about [name] based on [domain]. Summarize who they are, what they do, and how to get in touch."

**Implementation notes:**

- Each provider's support for pre-filling a prompt via URL query parameters differs and changes over time — verify current behavior for each provider before shipping this, rather than assuming a pattern from an older screenshot still works. Where a provider doesn't support URL pre-fill, fall back to opening the provider's homepage and copying the prompt to the clipboard with a "prompt copied — paste it in" toast.
- Populate `[name]` and `[domain]` from the site's actual identity/positioning (see `product-marketing-context` below), not a placeholder.
- This block only pays off once the four essentials above are actually in place — an AI-prompt button on a page with no semantic structure, no meta description, and no llms.txt just sends the visitor to an AI that still has nothing solid to say.

## Related skills in this repo

- **product-marketing-context**: Source of the "who they are, what they do" summary that populates both `llms.txt` and the pre-filled "Ask AI about me" prompt.
- **frontend-design** / **web-artifacts-builder**: Implementation of the actual page structure and the AI-prompt block.
- **design-dev-resources**: Real provider logos (via SVGL) for the ChatGPT/Claude/Perplexity/Gemini buttons instead of hand-drawn icons.
- **content-strategy**: Decides what the site's pages/content actually are, which this skill then makes AI-legible.

## Notes

Source: a "Claude Code builds" screenshot carousel (@theromanknox) demonstrating this on a personal portfolio/profile site, deployed via a Hostinger MCP integration. The deployment mechanics are environment-specific (this repo doesn't assume Hostinger or any specific host) — the four essentials and the "Ask AI about me" pattern are the portable, reusable part.
