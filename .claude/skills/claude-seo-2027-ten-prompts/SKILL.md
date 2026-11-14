---
name: claude-seo-2027-ten-prompts
description: The CiteRank infographic "10 Claude Prompts for a 2027 SEO Workflow" (Plan, Audit, Optimise, Act - strategy, keyword research, topical authority, AI SEO audit, technical SEO, competitor SEO, AEO, GEO, content refresh, 90-day action plan) with all ten prompts quoted, the data each one needs you to supply, and the limits of what a chat model can know about your rankings and AI-search visibility. Use when planning an SEO programme that includes AI search, or when choosing between this set and the existing 10-prompt SEO command.
---

# Ten Claude prompts for a 2027 SEO workflow (CiteRank)

Source: one legible infographic from CiteRank.com, a vendor of AI-search tracking, with a "Start tracking" banner at the bottom, so it is partly an advertisement. The ten prompts are quoted from the sheet. The data column and the cautions are my additions. This set is different from `/seo-prompts-10` (audit, TASM, search intent, programmatic SEO and others), so both are kept.

| Phase | # | Name | Prompt (as on the sheet) | Data you must supply (my addition) |
|---|---|---|---|---|
| Plan | 01 | 2027 SEO Strategy | "Draft a 2027 SEO strategy for [website] covering entity SEO, AI search, AEO and GEO" | Business goals, audience, current traffic and top pages |
| Plan | 02 | Keyword Research | "Map keywords for [niche] by intent, topic, entities and funnel stage" | Real volumes and difficulty from a keyword tool; the model cannot see them |
| Plan | 03 | Topical Authority | "Plan clusters for [topic]: pillar pages, internal links and content gaps" | Your existing URL list so gaps are real |
| Audit | 04 | AI SEO Audit | "Check [website] for gaps in LLM and Google AI Overview visibility" | Actual prompts and answers from AI tools, pasted in; a model cannot tell you whether it cites you |
| Audit | 05 | Technical SEO | "Review Core Web Vitals, crawling, indexing, schema and redirects" | Search Console and crawl exports, PageSpeed results |
| Audit | 06 | Competitor SEO | "Compare [competitors] on backlinks, keyword gaps and AI openings" | Backlink and keyword exports; it cannot fetch them reliably |
| Optimise | 07 | AEO Optimisation | "Rework [page] with direct answers, clear structure and questions" | The page text |
| Optimise | 08 | GEO Content | "Build a GEO plan so [brand] gets mentioned more across LLMs" | Where your brand is currently mentioned; evidence of what LLMs cite |
| Optimise | 09 | Content Refresh | "Order updates to old pages by rankings, traffic and freshness" | A page list with traffic and ranking data |
| Act | 10 | SEO Action Plan | "Turn every finding into a 90-day plan ordered by impact, urgency, effort and business value" | The findings from 01 to 09 |

## Cautions

- **Prompts 04, 06 and 08 ask for things a chat model cannot observe** (its own citations of you, competitor backlinks, brand mentions across other models). Without pasted data it will produce plausible-sounding guesses. Add this line to each: "Use only the data I paste. List what you could not check."
- **AEO and GEO are not settled disciplines.** The sheet gives no evidence that these tactics change citations. Treat them as experiments with a before-and-after measure.
- **"2027" is a label**, not a rule change; the fundamentals (useful pages, crawlable site, links, clear answers) are unchanged.
- **Vendor interest:** CiteRank sells tracking. Measure AI visibility yourself first (a fixed list of 20 prompts, asked monthly, results logged) before paying for a tool.

## Order

Run 01 to 03 once per quarter, 04 to 06 monthly with fresh data, 07 to 09 per page, and 10 last to merge everything into a ranked list. Related: `ai-seo`, `seo-audit`, `seo-aeo-geo-ultimate`, `aeo-diagnostic-metrics`, `/seo-prompts-10`.
