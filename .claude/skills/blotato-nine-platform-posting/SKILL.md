---
name: blotato-nine-platform-posting
description: Post one carousel/reel to 9 social platforms (Instagram, TikTok, YouTube, LinkedIn, X, Facebook, Threads, Bluesky, Pinterest) through the Blotato MCP connector, drafts first, from the @aiemergence 10-slide guide. Use when asked to cross-post, schedule one piece of content to many platforms, or set up Blotato in Claude or Claude Code. Covers setup, the per-platform required fields, the one-prompt workflow and the honest limits (paid plan, public media URL, draft-before-publish).
---

# Blotato: 1 prompt -> 9 native posts

Source: @aiemergence carousel (10 slides). Prices, plan limits and the connector URL are as printed on the slides; verify on blotato.com before paying.

## Setup (user does the login; nothing posts during setup)
1. Sign up for Blotato on a **paid plan**. The free trial has no MCP access (slide 9).
2. Connect the 9 accounts in Blotato once (slide shows 9 of 20 used).
3. Claude app: Customize -> Connectors -> Add custom connector -> name `Blotato`, URL `https://mcp.blotato.com/mcp` -> approve the OAuth popup. No API key.
4. Claude Code: `claude mcp add --transport http Blotato https://mcp.blotato.com/mcp`, then `/mcp` -> Blotato -> Authenticate. This repo's `.mcp.json` already carries the entry (OAuth still has to be approved by you).

## Workflow
Prompt (slide 4): "Here's today's carousel and reel. Turn them into posts for all 9 platforms, each in its native format. Schedule for [DAY] [TIME]. Show me drafts first."
Tools named on the slides: `blotato_list_accounts` -> read the media -> `blotato_create_post` x9.

## Required fields per platform (slide 6; Claude reads them from list_accounts)
| Platform | Field | Value |
|---|---|---|
| TikTok | privacyLevel | PUBLIC_TO_EVERYONE |
| TikTok | isAiGenerated | true (label AI content honestly) |
| YouTube | title + privacyStatus | required |
| Pinterest | boardId | required |
| Facebook | pageId | required |
| Instagram | firstComment | optional comment POST |
Example formats from the schedule slide: Instagram 12-slide carousel; TikTok photo carousel; YouTube Short; LinkedIn PDF carousel (personal profile); X 4-post thread (268/280 chars); Facebook page post; Threads 3-post thread; Bluesky 2-post thread (296/300 chars); Pinterest pin + link.

## Honest limits (slide 9) and house rules
- Media needs a **public URL**: host images/video first.
- Analytics: 8 of 9 platforms (LinkedIn returns none). Comments/DMs: Instagram and Facebook only.
- It posts live to real audiences. **Always ask for drafts; never publish or schedule without an explicit yes** for the exact text, platform and time. In this repo that also means passing `docs/marketing-context/proof.md` and `banned.md` (see `governed-marketing-team`) before approval.
- Do not report a post as scheduled until the tool result confirms it.
