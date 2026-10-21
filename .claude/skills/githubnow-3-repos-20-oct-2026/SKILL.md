---
name: githubnow-3-repos-20-oct-2026
description: The @githubnow briefing of 20 October 2026 "Nobody told you about 635 free AI models" (tashfeenahmed/freellmapi, cathrynlavery/diagram-design, ruvnet/ruflo) with the card claims and licences read on 21 October 2026. It also names the free LLM API aggregator that was unnamed in an earlier video. Use to decide what to read first.
---

# @githubnow, 3 repos gaining mass today (20 October 2026)

Source: a 5-slide dark briefing (cover "Nobody told you about 635 free AI models", three repo cards, outro). The "635" is the cover's own number and is not defined on the cards. Star gains are the briefing's and unverified.

| Card | Repo | Claim | Licence read |
|---|---|---|---|
| 1/3 Free LLM API router | tashfeenahmed/freellmapi | One /v1 endpoint, **34** free LLM providers; routes OpenAI-compatible requests across free tiers and fails over when rate-limited; provider keys stored encrypted; per-key usage tracked; "personal experimentation only"; +8,213 stars this month | MIT |
| 2/3 Editorial diagram skill | cathrynlavery/diagram-design | Diagrams as one self-contained HTML file; **45 diagram types**; direct SVG output; brand colours and fonts pulled from your URL; +1,813 stars today | MIT |
| 3/3 Agent meta-harness | ruvnet/ruflo | The harness around Claude Code and Codex: coordination layer for agent swarms, persistent memory, federation across machines; MCP via `npx -y ruflo@latest mcp start`; +146 stars today | MIT |

## Read critically
- **[Certain]** freellmapi is the repo behind "repo 3" of the earlier video summarised in `freellmapi-5-repos-that-blew-up-video` (34 providers, one endpoint).
- **[Certain]** Its own card says personal experimentation only: free tiers carry strict rate limits and data-use terms, so do not route private or customer data through it.
- **[Certain]** diagram-design is now "45 types"; earlier cards said 29 and 44 (see `your-aimentor-6-claude-repos`). The count changes as the repo grows or the cards copy stale numbers.
- **[Likely]** An `npx -y ...@latest` command runs whatever the latest published package is; pin a version and read the package before running it.
- Nothing was cloned or run.
