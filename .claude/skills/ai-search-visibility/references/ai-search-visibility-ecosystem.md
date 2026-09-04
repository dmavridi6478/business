# The AI Search Visibility Ecosystem

Source: infographic by Searchable.com, "The AI Search Visibility Ecosystem — How brands get found, trusted, and tracked." 20 sources that shape whether a brand gets surfaced, cited, or recommended by AI systems, grouped by type. Use this as the *map* of where visibility work actually needs to happen — pair with `seo-wheel-2026.md` for the *discipline* (AEO/GEO/etc.) and `15-day-ai-search-action-plan.md` for the *sequence*.

## The 20 sources, by category

| # | Source | Category | Role |
|---|---|---|---|
| 1 | ChatGPT | AI | Largest AI assistant; frequently cites trusted brands, communities, reviews, and original content |
| 2 | Gemini | AI | Uses Google's search index and Knowledge Graph plus web content to generate answers |
| 3 | AI Overviews | AI | Google's AI-generated search results that summarise and recommend sources directly |
| 4 | Claude | AI | Relies on authoritative content, documentation, and trusted sources for responses |
| 5 | Perplexity | AI | Citation-first search engine that openly references the sources behind answers |
| 6 | Copilot | AI | Combines Bing search and AI to answer informational and commercial queries |
| 7 | Trustpilot | Reviews | Strong reputation signal that influences brand trust and recommendation likelihood |
| 8 | YouTube | Content | Video content helps establish expertise, authority, and topical relevance |
| 9 | Reddit | Community | One of the most-cited sources in AI-generated recommendations and product comparisons |
| 10 | LinkedIn | Authority | Reinforces expertise, authorship, and professional credibility for people and brands |
| 11 | G2 | Reviews | Major software review platform frequently used for B2B product evaluation |
| 12 | Capterra | Reviews | Provides reviews, ratings, and comparisons that influence purchasing decisions |
| 13 | Crunchbase | Entity | Helps AI understand company information, funding, leadership, and market position |
| 14 | Google | Search | Traditional rankings still influence what AI systems discover and reference |
| 15 | Gartner | Search | High-authority analyst research that shapes enterprise trust and software selection |
| 16 | Wikidata | Entity | Provides structured entity data that helps AI understand brands and relationships |
| 17 | Wikipedia | Entity | A trusted entity source used to validate people, companies, and topics |
| 18 | Grok | AI | Leverages real-time conversations and social content from the X ecosystem |
| 19 | GBP (Google Business Profile) | Local | Critical for local visibility, reputation, and business information accuracy |
| 20 | Searchable | Tracking | Tracks visibility, citations, and prompts across leading AI search platforms |

## Connector availability for this account

Checked against this Claude account's installed connectors and the wider MCP registry (as of this write-up — re-verify before relying on this table, connector availability changes):

| Source | Status | Notes |
|---|---|---|
| **YouTube** | ✅ Covered — **NexLev** is installed and connected | YouTube niche/channel/video analytics; use it for source #8 work directly |
| **LinkedIn** | ✅ Covered — **Taplio MCP LinkedIn** is installed and connected | Own-account LinkedIn posting/analytics; use for source #10 work and pairs with `linkedin-virality-playbook` |
| **G2** | ⚠️ Available but not installed | A real "G2" connector exists in the registry (`browse_competitive_intelligence`, `list_product_reviews`, `show_product`, etc.) — tell the user they could connect it via claude.ai if G2 review/buyer-intent monitoring (source #11) becomes a recurring need |
| **Google Business Profile / local visibility** | ⚠️ Available but not installed | **Local Falcon** ("AI visibility and local search intelligence platform") is in the registry and covers source #19 directly, plus broader local AI-visibility scanning — worth connecting for any local-SEO-heavy engagement |
| **Google (organic rankings)** | 🟡 Partial — via **Semrush** and **Ahrefs** (both installed) | No dedicated Google Search Console connector found; Semrush/Ahrefs' SERP/ranking data is the closest available proxy for source #14 |
| **Crunchbase** | 🟡 Partial — via **Vibe Prospecting** (installed) | No Crunchbase connector itself; Vibe Prospecting's company/contact data covers similar entity-lookup ground for source #13. CB Insights and Harmonic exist in the registry as closer Crunchbase analogs if deeper company/funding data is needed, but aren't installed |
| **Wikipedia / Wikidata** | 🟢 No connector needed | Both are public, no-auth sources — reach them directly with the native `WebFetch` tool rather than via an MCP connector, for sources #16 and #17 |
| **Trustpilot** | ❌ No connector found | No MCP connector exists in the registry for source #7 |
| **Reddit** | ❌ No connector found | No MCP connector exists in the registry for source #9, despite it being one of the most AI-cited sources — a real gap |
| **Capterra** | ❌ No connector found | No dedicated connector for source #12; **G2** (above) is the closest available substitute if connected |
| **Gartner** | ❌ No connector found | No MCP connector exists for source #15 |
| **Searchable** | ❌ No connector found | The infographic's own product (source #20) has no MCP connector in the registry |
| **ChatGPT, Gemini, AI Overviews, Perplexity, Copilot, Grok** | N/A | These are the AI systems being optimized *for* (sources #1, #2, #3, #5, #6, #18) — not integration targets. Visibility here is earned through the other sources' content, not queried via a connector. (Claude, #4, is this assistant itself.) |

## Using this reference

- When a task needs live data from one of the ✅/⚠️ rows, use the connector directly (NexLev, Taplio) or tell the user it's available to connect (G2, Local Falcon) rather than trying to approximate it from training knowledge.
- For the ❌ rows, be explicit that no live connector exists — don't fabricate data or pretend to check Reddit/Trustpilot/Gartner in real time; either use `WebFetch` where a public page is reachable, or say the gap out loud.
- Reddit having no connector despite being one of the most AI-cited sources (per source #9's own description) is worth flagging to the user if Reddit visibility becomes a recurring focus — it's a real, not incidental, gap in this account's current tooling.
