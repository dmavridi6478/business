---
name: claude-plugins-top5-installs
description: The @awayfromlovable "Top 5 Claude Code plugins by installs" ranking with the slide install numbers and commands - #1 frontend-design 1,134,112, #2 superpowers 1,009,371, #3 code-review 438,525 (5 parallel reviewers, posts only issues scored 80+), #4 context7 417,801, #5 code-simplifier 346,763 - plus which are installed in this environment and the marketplace-name caveat. Use when choosing or installing Claude Code plugins for UI quality, planning/TDD, PR review, current docs or code cleanup. Complements claude-official-plugins-3.
---

# Top 5 (slide numbers, unverified, change daily)
| # | Plugin | Installs | What it does | Status here |
|---|---|---|---|---|
| 1 | frontend-design | 1,134,112 | picks a design direction first, real font pairings, no default purple gradients; auto-on when Claude builds UI (Anthropic) | installed (user scope) |
| 2 | superpowers | 1,009,371 | /brainstorming, test first, root cause before fix (Jesse Vincent; the only top-5 plugin by one person) | installed |
| 3 | code-review | 438,525 | /code-review: 5 reviewers in parallel (bugs, CLAUDE.md rules, git history), posts only issues scored 80+ to the GitHub PR (Anthropic; the itsnextwork deck says 4 agents, 37,423 marketplace stars, Apache-2.0) | NOT installed: not published as `code-review` in the built-in marketplace; similarly named entries (`code-review-anthropics`, `code-review-16urls`) are unverified, read their source first |
| 4 | context7 | 417,801 | "use context7" pulls current library docs from source, any version, fewer made-up functions (Upstash) | installed (also in .mcp.json) |
| 5 | code-simplifier | 346,763 | "simplify this component": less nesting, clearer names, removes repeated code, keeps behaviour; works on recent changes (Anthropic) | installed |
Slides give `@claude-plugins-official`; in Claude Code 2.1.296 here the built-in marketplace is `anthropic-plugin-directory`. The repo already has a `code-simplifier` agent and the `/review-pr` command.
Companion slides: PayPal #1 of a "big-company plugins" list (11 installs), HyperFrames (HeyGen), Browser Use, Lovable: see `claude-official-plugins-3`. "Install count" measures popularity, not quality: read what a plugin runs before enabling it.
