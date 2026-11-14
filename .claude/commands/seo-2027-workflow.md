---
description: Run one of the ten CiteRank 2027 SEO workflow prompts (strategy, keywords, topical authority, AI SEO audit, technical, competitors, AEO, GEO, content refresh, 90-day plan) - asks for the data it needs, never invents rankings or AI citations
argument-hint: [prompt number 1-10 or name] [website or niche] - no args lists all ten
---

Input: "$ARGUMENTS". If empty, list the ten prompts from `.claude/skills/claude-seo-2027-ten-prompts/SKILL.md` with the data each needs and ask which to run.

1. Run the chosen prompt with the user's website or niche. Before answering, list the data it needs (keyword exports, Search Console, crawl results, pasted AI answers, page text) and ask for it; if the user cannot supply it, say which parts of the answer would be guesses and label them.
2. Never state rankings, traffic, backlinks or whether an AI tool cites a site unless the user pasted the data.
3. End with the next prompt in the order (strategy, then audit, then optimise, then the 90-day plan ordered by impact, urgency, effort and business value) and `Not checked:` for anything not from the user's data.
4. Fetch, publish and change nothing on the site.
