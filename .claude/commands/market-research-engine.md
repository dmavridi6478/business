---
description: Run the 5-step AI market research loop (audience pain points, reliable sources, content gaps, analysis, report) on a topic, using the market-research-engine agent
argument-hint: [topic] [audience]
---

Use the skill `ai-market-research-engine` and the agent `market-research-engine`. Input: "$ARGUMENTS".

1. Read `.claude/skills/ai-market-research-engine/SKILL.md` and `docs/about-me.md` if it exists.
2. Run the agent for the topic and audience. It uses Perplexity if connected, else Exa, Consensus, Semrush, Ahrefs and web search.
3. Save the report to `research/market-research-YYYY-MM-DD-<topic-slug>.md` with sections: research topic, main findings, conflicts, content ideas, sources with a verified or unverified mark.
4. Ask whether to save it to Notion or schedule it weekly; do not do either without a yes.
