---
name: five-repos-agent-tools-nov2026
description: Checked briefing on the "5 GitHub repos everyone starred this week" carousel (@your.aimentor, November 2026) - Claude Code Game Studios, Craft Anything, Scrapling, Zed and agent-desktop - with each repo's licence read from its own file, the install lines read from its README, the claims that were and were not verified, and the warnings the carousel leaves out (reverse-engineering scope, scraper bot-bypass, desktop control, a piped installer). Use before installing any of the five, when asked what each does, or when choosing between them and tools this repo already has.
---

# Five repos from one carousel: what they are, what they cost, what to watch

Source: a cover plus five repo cards and five detail slides. Checked 7 November 2026: each repo exists (`git ls-remote`), the licence was read from the repo's file, install lines and claims were read from the README or the vendor's own page. Star, fork and issue counts are from the cards and could not be checked (the GitHub API was blocked from the cloud container).

| # | Repo | What it is | Licence (read) | Install (from the README) |
|---|---|---|---|---|
| 1 | `Donchitos/Claude-Code-Game-Studios` | A Claude Code template: 49 agents and 74 skills organised as directors, leads and specialists, with engine sets for Godot, Unity and Unreal | MIT | `git clone https://github.com/Donchitos/Claude-Code-Game-Studios.git my-game`, open Claude Code in that folder, run `/start` |
| 2 | `storytold/craft-anything` | A desktop app, CLI and MCP server: study a website, app or game, have your signed-in coding agent build a new project, then check it against the original | MIT OR Apache-2.0 per the README badge (the Apache file was read) | `git clone` then `cargo run --release -p craft-anything` (Rust 1.97+); CLI: `cargo install --path apps/craft-anything-cli`, then `craft-anything-cli doctor` |
| 3 | `D4Vinci/Scrapling` | A Python scraping framework from one request to a full crawler, with an MCP server | BSD-3-Clause | `pip install "scrapling[fetchers]"`; `scrapling install` only for browser pages; MCP: `pip install "scrapling[ai]"` and the `scrapling-mcp` command (v0.4.13 or later) |
| 4 | `zed-industries/zed` | A Rust code editor from the makers of Atom and Tree-sitter, with agents inside it | GPL-3.0-or-later, with Apache-2.0 components where marked | Download from zed.dev/download; the Linux docs give `curl -f https://zed.dev/install.sh \| sh` |
| 5 | `vercel-labs/agent-desktop` | A CLI that reads an app's accessibility tree as JSON so an agent can act on it without screenshots; no model inside | Apache-2.0 | `npm install -g agent-desktop`, `agent-desktop status`, `agent-desktop permissions --guide` (macOS); MCP: `agent-desktop mcp` over stdio |

## What was checked, and what was not

- **Claude Code Game Studios.** The README states 49 agents and 74 skills and a `modes.rigor` setting whose default is `minimal`. Its own measurement lists one document before the first line of code for `minimal` and 30 for `standard`, and says two blind reviewers and a human playtest ranked the `standard` build last. That is the authors' test, not an independent one, and the README says four games were built while its table shows two rows.
- **Craft Anything.** The README says early alpha, and the `doctor` command on the card exists. Clean room is the default and means the tool offers only what you can see as a visitor. The README states that this is a rule about what the tool offers, not an operating-system sandbox, and that an agent you run still acts as you.
- **Scrapling.** The card's run (100 items, 10 pages, 1.1 seconds) is the authors' own test on `quotes.toscrape.com`, a practice site built for scrapers; not reproduced here.
- **Zed.** Pricing read from zed.dev/pricing on 7 November 2026: Personal $0, Pro $10 a month with a free trial, Business $30 per seat per month. The card's line that Claude Agent and Codex run inside Zed was not checked against Zed's docs.
- **agent-desktop.** 60 command names and Windows, macOS and Linux support (Ubuntu 24.04 or later) read from the README.

## Warnings the carousel omits

1. **Craft Anything is a reverse-engineering engine.** The README describes 320 tools and, in Deep mode, reading a program's code and a website's JavaScript, with Ghidra when installed. Recreating someone else's site, app or game can infringe copyright, trademarks or terms of service. The card says the agent is told to leave logos, photos and text alone; that is an instruction to the agent, not legal cover (inference).
2. **Scrapling advertises bot-protection bypass.** Its README describes a stealth browser, CAPTCHA handling and a Cloudflare solver for the MCP server. Its disclaimer says it is for educational and research purposes and that you must follow the law, each site's terms and `robots.txt`; the `robots_txt_obey` option is optional, so you must switch it on. Scraping pages with personal data brings GDPR duties.
3. **agent-desktop lets an agent operate your desktop apps.** Anything you grant, it can click and type as you. Its README warns that snapshots, clipboard reads and screenshots can contain private desktop content and should stay out of public logs and uploads. Do not point it at banking, password-manager or admin windows.
4. **The Zed Linux installer pipes a script into a shell.** Prefer the download page or your package manager, or download the script and read it first.
5. **Zed is GPL-3.0-or-later**, so code that links to it carries copyleft terms; using the editor does not.

## Already in this repo

- Related skills: `computer-use`, `data-scraper-agent`, `lead-scraper`, `browser`, `autobrowse`, `agent-github-repos-4`.
- Related agent: `unity-developer`. The studio structure is covered by `game-studio-chain-of-command` and the `game-studio-planner` agent.
- Run `/repo-vet owner/repo` on any of the five before installing.

## Not done

Nothing was cloned, installed or run. No connector was added to `.mcp.json`: Scrapling and agent-desktop each ship an MCP server, but neither is installed in the cloud container, and each grants real capability (scraping with bot bypass; desktop control). The exact entries are in `docs/batch-114-action-plan.md` for you to add locally.
