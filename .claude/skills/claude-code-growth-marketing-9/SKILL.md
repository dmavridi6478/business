---
name: claude-code-growth-marketing-9
description: The 9 growth-marketing systems a marketer can build with Claude Code without engineering (Google Ads automation, Figma creative plugin, Meta Ads connection, ad testing system, creative performance tracker, competitor monitor, programmatic SEO, landing page builder, marketing analytics), each with its tool stack, a build brief, and which connectors are connected, installable or missing in this account. Use when planning or building a marketing automation with Claude Code, or when deciding which connector to install first.
---

# Claude Code for growth marketing: 9 builds

Source: infographic "Claude Code for Growth Marketing: 9 things marketers can build without engineering" (also noted in README under Emilia Moller). Tools are those on the slide.

| # | Build | What it does | Slide tools | Connector status here |
|---|---|---|---|---|
| 1 | Google Ads automation | Pull performance data, find wasted spend, recommend or apply bid, budget and ad changes | BigQuery, Google Ads, GA4 | Supermetrics connected (Ads, GA4 read). Adspirer and Windsor.ai installable; BigQuery needs auth |
| 2 | Figma creative plugin | One winning concept to 50 on-brand variations in Figma | Meta, Figma, Google Drive | Figma, Google Drive connected |
| 3 | Meta Ads connection | Ask "why did CAC spike yesterday?" and it investigates | Claude, Meta, GA4 | Supermetrics and Motion Creative Analytics connected |
| 4 | Ad testing system | Run tests, store every result, use history to choose the next test | PostHog, Meta, Google Ads | PostHog installable; Amplitude connected as alternative |
| 5 | Creative performance tracker | Find which words, hooks, visuals and formats correlate with performance | Figma, Meta, GA4 | Motion Creative Analytics, Figma, Supermetrics connected |
| 6 | Competitor monitor | Track competitor pages, messaging and AI visibility; alert on change | Slack, Searchable, Firecrawl | Slack, TinyFish, Ahrefs connected; Firecrawl installable |
| 7 | Programmatic SEO | Find opportunities, build and publish pages at scale, add schema and internal links, monitor | DataForSEO, Webflow, Google Search Console | Semrush, Ahrefs connected; Webflow installable |
| 8 | Landing page builder | Campaign brief to built, deployed, iterated page | Figma, GitHub, Vercel | Figma, GitHub connected; Vercel half-connected |
| 9 | Marketing analytics | "What caused our pipeline drop?" across acquisition, CRM, search and AI visibility | GA4, BigQuery, Searchable | Supermetrics, HubSpot, Semrush connected |

## Build brief pattern (use for any row)

1. State the question the system must answer weekly, in one sentence.
2. List the data it reads and the one place it writes (a report, never live ad spend).
3. Start read-only; add write actions (bids, budgets, publishing) only with a human approval step.
4. Schedule it only after two manual runs give results you trust.

## Reading it critically
- "Recommend or apply" in build 1 is the risky half: applying bid or budget changes spends money. Keep it recommend-only until trusted.
- Programmatic SEO at scale risks thin-content penalties; use `programmatic-seo` guardrails.
- Use `/growth-build [number]` to get the brief and connector steps for one build.
