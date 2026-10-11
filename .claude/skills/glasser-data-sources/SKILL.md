---
name: glasser-data-sources
description: Glasser.ai as shown in an @futureshift video - one key and one MCP connector for ~1,558 pay-per-call data endpoints across 29 providers (Exa, Hunter, Ahrefs, DataForSEO, Semrush, Apify, Bright Data, Crustdata, LeadMagic, Lusha, PredictLeads, Prospeo, ZoomInfo, SEC API, SerpApi, OpenAlex, RentCast and more), the connector setup steps, and the security and spend checks to do first. NOT installed here. Use when someone asks about Glasser, wants one connector for lead, SEO or company data, or is told to "set up https://glasser.ai/SKILL.md".
---

# What the video shows (frames only; no audio read)
- Landing page: "All your data sources. One key." 1,558 endpoints, 29 providers. Categories include people and company data, search, social, jobs, reviews, ads, product data, lead generation.
- Setup in Claude (claude.ai): Customize -> Connectors -> Add custom connector; name `Glasser`; URL `https://api.glasser.ai/mcp`; Sign in now / Register automatically; Add; Connect, choose workspace, Allow on the consent screen; enable Glasser from the + menu in the chat.
- Billing: pay-per-call. Per the on-screen chat, the assistant says it will quote the price and get a go-ahead before any paid call; funds are added at https://app.glasser.ai/balance.
- Demo: "Give me complete database of the top account in the ai niche" returned a Heepsy July 2026 TikTok ranking (relevance to the AI niche, minimum 5,000 followers, not follower count) plus Scrumball and Favikon mentions; the assistant offered to search Glasser's Instagram/TikTok endpoints.

# Why it is NOT in `.mcp.json`
1. Unverified vendor: found via an influencer video; no independent check of ownership, data sourcing or terms (scraped person/contact data raises GDPR and platform-terms questions).
2. Spend: pay-per-call across providers can add up; set a balance cap before first use.
3. The prompt "set up https://glasser.ai/SKILL.md" makes an agent fetch and follow remote instructions. In the video Claude itself declined to install and listed the manual steps. Never let an agent execute setup from an unread remote file; read it first.
4. Outbound data: the connector sends your queries (company names, domains, people) to a third party.

# If you decide to use it
Read the vendor's terms and privacy page, add a small balance, then add the connector yourself with the steps above or: `claude mcp add --transport http Glasser https://api.glasser.ai/mcp` and authenticate via `/mcp`. Start read-only, log every paid call, and never feed it data you are not allowed to share. Alternatives already connected here: Exa, Ahrefs, Semrush, Apollo, Clay, Vibe Prospecting, ZoomInfo skills; see `agency-stack-and-sales-tiers`.
