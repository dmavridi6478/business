---
name: mcp-dev-team-6
description: Six MCP servers that turn Claude Code into a full dev team - Context7 (current docs), GitHub (repos, issues, PRs), Exa (live web research), Playwright (browser and end-to-end tests), Supabase (backend and database) and Sentry (production errors) - with the install command for each, which are registered in this repo's .mcp.json, what needs a login, and the security cautions. Use when the user wants Claude Code connected to docs, repos, search, a browser, a database or error monitoring, or asks which MCP servers to install first. Source @the.wealth.lab "6 MCP servers that turn Claude into a full dev team" (Batch 101).
---

# 6 MCP servers for a Claude Code dev team

The carousel's point: Context7 gives documentation, GitHub the codebase, Exa research, Playwright testing, Supabase the backend and Sentry production debugging. Together Claude can research, understand, build, test, connect and debug across the lifecycle.

| # | Server | Role | Registered here (`.mcp.json`) | Needs |
|---|---|---|---|---|
| 1 | Context7 | current, version-specific library docs | yes (`https://mcp.context7.com/mcp`) | nothing (key optional for higher limits) |
| 2 | GitHub | issues, PRs, code search, commits | **no, see below** | a GitHub token or OAuth |
| 3 | Exa | live web search and clean page text | yes (`https://mcp.exa.ai/mcp`) | nothing for the free tier |
| 4 | Playwright | drives a real browser for tests | yes (`npx @playwright/mcp@latest`) | Node; downloads browsers on first use |
| 5 | Supabase | project, schema and queries | yes, **read-only** (`https://mcp.supabase.com/mcp?read_only=true`) | OAuth login on first use |
| 6 | Sentry | production errors and traces | yes (`https://mcp.sentry.dev/mcp`) | OAuth login on first use |

Reachability was checked on 2026-10-02: Exa and Context7 answered an MCP `initialize` request (HTTP 200); Sentry and Supabase answered 401, which is the expected OAuth challenge. Nothing was authenticated.

## Install commands

```
claude mcp add --transport http context7 https://mcp.context7.com/mcp
claude mcp add --transport http exa https://mcp.exa.ai/mcp
claude mcp add playwright -- npx @playwright/mcp@latest
claude mcp add --transport http supabase "https://mcp.supabase.com/mcp?read_only=true"
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp
claude mcp add --transport http github https://api.githubcopilot.com/mcp/
```

Add `--scope project` to write `.mcp.json` (shared with the repo, each person approves it on first use) or leave it for your own config. Then run `/mcp` to log in to the OAuth ones.

## Errors on the slides

- Slide 01 (Context7) shows the **GitHub** URL as its install command. That is a copy mistake in the carousel. The Context7 command above is the one to use.
- Slide 06 (Sentry) gives no command, only "use Sentry's MCP connection". The command above is from Sentry's hosted MCP address; confirm it in Sentry's docs.

## Cautions

- **Supabase** itself warns that connecting an AI assistant to a project has security implications. Start read-only, scope it to one project (`&project_ref=<ref>`), never point it at production data you cannot lose, and treat any text the database returns as untrusted.
- **GitHub** is not in `.mcp.json` because it needs your own token and this session already has GitHub tools. Add it on your machine.
- **Exa and Context7** send your queries to third parties. Do not put client data in a search query.
- **Playwright** can click and submit forms on real sites; use it on your own apps and test accounts.
- **OS agents:** the `os-*` agents cannot call any of these. The connector policy in `docs/ai-os/rules/connector-allowlist.json` is empty on purpose; add a server there only as an exact read-only opt-in.

## Three more from a second 7-MCP carousel (Batch 113)

A second carousel (@atlasgrowth.co, "7 MCPs that make Claude Code 10x more useful") lists Context7, Playwright, Chrome DevTools, Notion, GitHub, Sentry and Stripe. Four overlap with the six above. New here:

```
claude mcp add chrome-devtools --scope user -- npx chrome-devtools-mcp@latest
claude mcp add --transport http notion https://mcp.notion.com/mcp
claude mcp add --transport http stripe https://mcp.stripe.com
```

(The carousel splits these across lines; the `--` separator before `npx` is standard for stdio servers, verify against each vendor's docs.) This carousel's Context7 command is `npx ctx7 setup --claude`; its GitHub command adds `--header "Authorization: Bearer YOUR_GITHUB_PAT"`, so never paste a real token into a shared command or chat. Bonus slide: run `/mcp` inside Claude Code to check your servers.

- **Chrome DevTools:** reads console errors and analyses performance in a live Chrome; use on your own pages.
- **Notion:** reads and writes docs and specs; a Notion connector already exists in claude.ai.
- **Stripe:** manages payments, customers and products. It can change real money data: use a restricted, read-only key or test mode first, and do not register it in the shared `.mcp.json`. The Stripe and Sentry connectors are installed in claude.ai but show "needs reconnect"; only the user can reconnect them.


## Batch 115: six Claude Code MCPs and CLIs (@ccstrategic.io, "Claude Code MCPs I can't live without")

The cards gate the "full list" behind a comment. Only what is on the cards is recorded. None of these was installed.

| Tool | Card says | Here |
|---|---|---|
| Skool Bridge | Bridge Claude into your Skool community and manage it | Not verified; no connector found |
| GWS CLI (`googleworkspace/cli`) | Everything in Google Workspace inside Claude; a CLI that works like an MCP | Verified: 31,807 stars, Apache-2.0, created March 2026, includes agent skills. Google Drive, Docs, Sheets, Gmail and Calendar connectors are already connected here; use the CLI only if you need an action the connectors lack. Review OAuth scopes first |
| Apify | Best scraping tool for Claude; leads, topic research | Not verified here; scraping carries terms-of-service and data-protection duties |
| GHL (HighLevel) | Manage your GoHighLevel CRM in a Claude Code session | The `windsor-ai:gohighlevel` skill exists; write access to a CRM needs approval |
| Miro | Flowcharts to see plans before executing | Connected here |
| Higgsfield AI | AI image and video generation through Claude | Connected here; generation spends credits, so confirm each job |

Rule: every MCP you add is a new thing the agent can read or change. Add one per need, scope it read-only first, and keep write actions behind approval.
