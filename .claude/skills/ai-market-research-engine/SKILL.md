---
name: ai-market-research-engine
description: How to build a high-performing AI market research engine where Perplexity finds sourced information and Claude Code directs it using your context files (The Blueprint Weekly, socialblueprint.ca) - the architecture, the four reasons to connect them and the 6-step weekly loop (audience, sources, content gaps, analysis, Notion report, repeat). Use when setting up recurring market, audience or competitor research with sourced findings, or when building the market-research-engine agent.
---

# AI market research engine: Perplexity researches, Claude Code directs

Source: infographic "How to Build a High-Performing AI Market Research Engine" from The Blueprint Weekly.

## Architecture

- Claude Code side (context it already holds): About Me file, target audience, content strategy, research preferences, brand positioning, and the Notion report as the output.
- Perplexity side (what it returns): audience problems, search trends, industry reports, original research and stats, competitor content.
- Link: Perplexity API, with Claude Code as the manager. The loop repeats weekly or monthly.

## Why connect them

1. It knows your context (About Me, audience, content strategy are already written).
2. AI talks to AI better: Claude briefs Perplexity more precisely than you would.
3. Better requests: no re-explaining your business and goals every time.
4. Link them by API and let Claude Code manage the research.

## The 6 steps

| Step | Do | Output |
|---|---|---|
| 1 Research your audience | Claude Code asks Perplexity for pain points | Common questions, community problems, objections before buying |
| 2 Find reliable sources | Perplexity returns recent research with dates and links; Claude Code checks each source | Industry reports, original research, market surveys, each marked verified or not |
| 3 Identify content gaps | Compare what competitors post with your strategy | Unanswered questions, hot industry problems, advice worth challenging |
| 4 Analyze the research | Compare findings, flag conflicts | Repeated patterns, conflicting information, topics worth exploring |
| 5 Organize your findings | Compile a final report and save it in Notion beside your content calendar | Markdown report: research topic, main findings, content ideas |
| Repeat | Save as a reusable workflow in Claude Code and schedule weekly, biweekly or monthly | Standing cadence |

## What exists here

- Agent: `market-research-engine` (does steps 1 to 5; works with Perplexity if connected, otherwise Exa, Consensus, Semrush, Ahrefs and web search).
- Command: `/market-research-engine [topic] [audience]`.
- n8n draft: "Weekly market research engine (Perplexity to report)" - Monday 08:00, calls the Perplexity API, posts the draft to Slack. Needs a Perplexity API key stored in n8n; not published.
- Perplexity is not in the connector registry here and is not added to `.mcp.json`; the n8n workflow calls its API directly. See `perplexity-research-workflow` for manual prompts.

## Guardrails

- Perplexity output is a lead, not evidence: open each cited source before using a number, and say when a source could not be checked.
- Keep the About Me and audience files short; they are re-sent every run.
- A schedule costs tokens and API credits on every run; start monthly.
