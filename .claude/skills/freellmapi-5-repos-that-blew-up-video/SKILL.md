---
name: freellmapi-5-repos-that-blew-up-video
description: Notes from a 70-second @freellmapi video "5 GitHub repos that just blew up" (gods-eye-view, a leaked system prompts collection, a free LLM API aggregator, Microsoft MarkItDown, OpenStock) with the on-screen claims, licences read on 18 October 2026, and cautions about leaked prompts and free-token claims. Use to decide which to read; ends in a comment-for-links funnel.
---

# 5 GitHub repos that just blew up (@freellmapi video)

Source: a talking-head video with overlays, frames read; no transcript. The creator ends "Comment TRENDING and I'll send them directly" (a funnel; nothing was commented).

| # | Repo and claim | Licence read | Note |
|---|---|---|---|
| 1 | bilawalsidhu/gods-eye-view: a spy satellite simulator in your browser (3D globe, flight tracking, satellite tracking), "except the data is real"; 47,000+ stars | MIT | Already in `github-briefing-oct4-three` |
| 2 | A repo of leaked system prompts ("the hidden instructions" of Claude, ChatGPT, Gemini); 68k+ stars | **repo name not shown** | See the cautions below |
| 3 | A free LLM API aggregator: 32 free AI providers (later "34"), one /v1/chat/completions endpoint, "up to 7.4 billion free tokens a month", $0; 33k+ stars | **repo name not shown** | See `free-llm-api-providers-13` |
| 4 | microsoft/markitdown: turn PDFs, Word and Excel into clean Markdown for LLMs; 188k+ stars | MIT | Check the output on your own documents |
| 5 | Open-Dev-Society/OpenStock: stock tracking, alerts and company data "just like the paid platforms" (compared on screen with TradingView at $14.95/month and Bloomberg); 20K stars | AGPL-3.0 | Not an investing tool; data licensing and accuracy are unchecked |

## Read critically
- **[Certain]** Repo 2 and 3 are not named, so they could not be checked. Do not download a repo from a comment reply.
- **[Certain]** "Leaked" system prompts are unverifiable claims about proprietary text; they may be fabricated or outdated, and using them to craft jailbreaks breaches provider terms.
- **[Likely]** "7.4 billion free tokens a month" is the sum of many providers' free tiers with strict rate limits and data-use terms; do not send private data to them.
- **[Likely]** 188k stars for MarkItDown is far above what I would expect for that tool; verify on GitHub.
- Nothing was cloned or installed.
