# Tool Reference: Firecrawl + DataForSEO

*Authored directly for this repo — the parent skill's Phase 2 section pointed here, but no source content shipped with the install. This fills that gap.*

Consolidated list of the MCP tools this skill uses, grouped by phase, with example call shapes. If a given MCP server isn't connected in this environment, say so explicitly rather than fabricating the data these tools would return — see `attachment-intake`'s broader "don't force-fit/guess" discipline, applied here to missing tool access instead of missing file context.

## Firecrawl (Phase 1: site scraping)

| Tool | Purpose | Example call |
|---|---|---|
| `firecrawl_map` | Discover a site's URL structure before deciding what to scrape | `firecrawl_map({ url: "https://competitor.com" })` → returns a list of discovered URLs to triage into homepage/pricing/features/about/etc. |
| `firecrawl_scrape` | Pull clean markdown/content from one specific page | `firecrawl_scrape({ url: "https://competitor.com/pricing" })` → returns page content as markdown, saved to `scrapes/pricing.md` |
| `firecrawl_search` | Find pages not linked from the main site map (e.g. a G2 review page, a Product Hunt launch) | `firecrawl_search({ query: "competitor.com site:g2.com reviews" })` → returns candidate review-page URLs to scrape next |

**Sequencing**: always map before scraping — scraping without a map risks missing key pages (integrations, changelog) or wasting calls on irrelevant ones (careers, legal).

## DataForSEO (Phase 2: SEO & market data)

| Tool | Purpose | Example call |
|---|---|---|
| `backlinks_summary` | Domain authority, total backlinks, referring domains, spam score | `backlinks_summary({ target: "competitor.com" })` |
| `backlinks_referring_domains` | Top referring domains — quality/pattern signal | `backlinks_referring_domains({ target: "competitor.com", limit: 20 })` |
| `dataforseo_labs_google_ranked_keywords` | Total organic keywords, top 3/10/100 counts, estimated traffic | `dataforseo_labs_google_ranked_keywords({ target: "competitor.com" })` |
| `dataforseo_labs_google_domain_rank_overview` | Domain-level organic metrics, traffic value, top keywords | `dataforseo_labs_google_domain_rank_overview({ target: "competitor.com" })` |
| `dataforseo_labs_google_keywords_for_site` | What keywords the domain targets — content-gap analysis input | `dataforseo_labs_google_keywords_for_site({ target: "competitor.com" })` |
| `dataforseo_labs_google_competitors_domain` | Their closest organic competitors — may surface competitors not yet on your list | `dataforseo_labs_google_competitors_domain({ target: "competitor.com" })` |
| `dataforseo_labs_google_relevant_pages` | Highest-traffic pages on the domain | `dataforseo_labs_google_relevant_pages({ target: "competitor.com" })` |

**Sequencing**: run `backlinks_summary` and `dataforseo_labs_google_domain_rank_overview` first — they're the cheapest, highest-signal calls and often determine whether deeper analysis (keyword-level, competitor-discovery) is worth the additional calls for a given competitor.

## Saving raw responses

Per the parent skill's directory layout: every Firecrawl scrape → `scrapes/<page-name>.md`; every DataForSEO response → `seo/<endpoint-name>.json`, verbatim, before any parsing into the synthesized profile. This makes every number in the final profile traceable back to the exact raw response it came from.

## If a tool isn't available

Neither Firecrawl nor DataForSEO connectors are guaranteed to be installed in every environment. Before starting Phase 1/2, check `ListConnectors`/`SearchMcpRegistry` (or the equivalent tool-discovery mechanism in the current environment) rather than assuming access. If unavailable, say so to the user and fall back to `WebFetch` for public pages (lower-fidelity than Firecrawl, but real) — never fabricate SEO metrics that would normally come from DataForSEO.
