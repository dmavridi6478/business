---
name: claude-install-list-40
description: Catalogue of 40 add-ons for Claude Code from a "40 things to install" graphic (workflows, skills, memory and context, tools and connectors, prompts and usage) with verified repo paths, stars and licences, a risk note for each, overlap with this library, and a rule for installing at most a handful. Use when deciding which Claude Code add-ons to install, or when someone sends another "install these" list.
---

# 40 things to install in Claude: a catalogue, not an install order

Source: a "40 Things to Install in Claude" graphic by Charlie Hills (Batch 119; "a gift for Claude users"). Each repo was looked up on GitHub on 25 October 2026; stars and licences change daily. "not read" means the page returned no figure, so I do not quote one.

## The advice the graphic does not give
**Do not install forty add-ons.** [Certain] Every skill, plugin and MCP server adds context (its description loads every session) and every one is third-party code that can run commands or read files with your permissions. Several do the same job: three are memory systems, four are token compressors or output trimmers, five are workflow frameworks. Pick one per job, test it on a throwaway branch, measure, and remove what you do not use.

A sensible first set: one workflow framework (superpowers is already enabled in this environment), one documentation source (context7, already used here), one visibility aid (claude-hud), and one token-saving tool tested on a real task (rtk or headroom). Memory: this environment already uses Cognee; do not add claude-mem, agentmemory or beads on top.

Before installing anything from a list: open the repo, read the README and the licence, look at what permissions and hooks it adds, check the last commit and open issues, and ask who benefits from you installing it. Three repos have moved or redirect (graphify, beads, headroom); one (cc-switch) warns about impersonation sites.

Install commands change with each release; follow each repo's own README rather than a card. Nothing was installed by this skill.


## Workflows

| # | Name | Repo | Stars | Licence | What the card says | Care | In this library |
|---|---|---|---|---|---|---|---|
| 1 | learn-claude-code | `shareAI-lab/learn-claude-code` | 79,158 | MIT | Learn agent basics, one building block at a time | Learning repo, not a tool to install | referenced already |
| 2 | karpathy-skills | `multica-ai/andrej-karpathy-skills` | 223,517 | none shown | Use a CLAUDE.md to reduce coding mistakes | A single CLAUDE.md of guidelines, not a learning path (Batch 116) | referenced already |
| 3 | superpowers | `obra/superpowers` | 304,936 | MIT | Plan, build and test with a repeatable workflow | Heavy process; already enabled in this environment | referenced already |
| 4 | ponytail | `DietrichGebert/ponytail` | 175,786 | MIT | Keep code simple and reuse what already exists | Opinionated; test on a branch | referenced already |
| 5 | gstack | `garrytan/gstack` | 137,672 | MIT | Add planning, review and testing tools to Claude | 23 role-based tools: large surface | referenced already |
| 6 | ECC | `affaan-m/ECC` | 288,683 | see repo | Add skills, memory, security and research checks | An agent harness (Batch 113); large; read before installing | referenced already |
| 7 | oh-my-claudecode | `Yeachan-Heo/oh-my-claudecode` | 40,234 | MIT | Coordinate several agents working as a team | Multi-agent runs multiply token cost | referenced already |
| 8 | Archon | `coleam00/Archon` | 23,759 | MIT | Build coding workflows you can run again | Harness builder, branch is dev | new |

## Skills

| # | Name | Repo | Stars | Licence | What the card says | Care | In this library |
|---|---|---|---|---|---|---|---|
| 9 | taste-skill | `Leonxlnx/taste-skill` | 102,383 | MIT | Give Claude guidance for stronger visual designs | - | referenced already |
| 10 | anthropics' skills | `anthropics/skills` | 183,653 | mixed per skill | Browse Anthropic's official collection of skills | Check each skill's own licence | referenced already |
| 11 | mattpocock skills | `mattpocock/skills` | 302,818 | MIT | Find engineering skills for your coding workflow | - | referenced already |
| 12 | wshobson agents | `wshobson/agents` | 41,642 | MIT | Find specialist agents for different coding jobs | Large marketplace; install per plugin, not all | referenced already |
| 13 | claude-plugins | `anthropics/claude-plugins-official` | 44,378 | Apache-2.0 | Browse the official directory of Claude plugins | Official directory, but each plugin is third-party code | referenced already |
| 14 | addyosmani skills | `addyosmani/agent-skills` | 110,258 | MIT | Add engineering skills for production work | - | referenced already |
| 15 | ui-ux-pro-max | `nextlevelbuilder/ui-ux-pro-max-skill` | 140,305 | MIT | Design interfaces for different platforms | - | referenced already |
| 16 | awesome-claude-skills | `ComposioHQ/awesome-claude-skills` | 77,880 | none shown | Browse a curated list of skills and useful resources | A list: vet each entry | referenced already |

## Memory and context

| # | Name | Repo | Stars | Licence | What the card says | Care | In this library |
|---|---|---|---|---|---|---|---|
| 17 | planning-with-files | `OthmanAdi/planning-with-files` | not read | not read | Keep plans in files you can return to next session | Overlaps with project docs and memory | new |
| 18 | claude-mem | `thedotmack/claude-mem` | not read | not read | Bring relevant context back into future sessions | Stores session content: privacy; overlaps Cognee memory used here | referenced already |
| 19 | codegraph | `colbymchenry/codegraph` | 75,278 | see repo | Map code connections and update the index | Local code index; fine for repos you own | referenced already |
| 20 | graphify | `Graphify-Labs/graphify (moved from safishamsi/graphify)` | 134,473 | see repo | Connect code, documents and schemas | Repo has moved; use the new path | referenced already |
| 21 | repomix | `yamadashy/repomix` | not read | not read | Pack your entire repository into one AI-friendly file | Do not pack secrets or .env; check ignore rules | referenced already |
| 22 | agentmemory | `rohitg00/agentmemory` | 29,883 | Apache-2.0 | Give agents memory that lasts between runs | Pick one memory system, not three | referenced already |
| 23 | beads | `gastownhall/beads (moved from steveyegge/beads)` | 28,191 | MIT | Track tasks and progress across coding sessions | Repo has moved; 1,518 open issues | new |

## Tools and connectors

| # | Name | Repo | Stars | Licence | What the card says | Care | In this library |
|---|---|---|---|---|---|---|---|
| 24 | multica | `multica-ai/multica` | 53,739 | Other | Assign work to coding agents like teammates | Self-hostable; read the licence | referenced already |
| 25 | firecrawl | `firecrawl/firecrawl` | 195,233 | AGPL-3.0 | Turn website content into usable text | AGPL obligations if self-hosted and modified; respect robots.txt and site terms | referenced already |
| 26 | cc-switch | `farion1231/cc-switch` | 148,446 | MIT | Manage your coding tools from one desktop app | The repo says "only official website: ccswitch.io": impersonation risk, download only from the repo or that site | new |
| 27 | context7 | `upstash/context7` | 63,638 | MIT | Bring current library documentation into your task | Sends library queries to a hosted service; already used here | referenced already |
| 28 | vibe-kanban | `BloopAI/vibe-kanban` | 28,447 | Apache-2.0 | Organise agent tasks on a visual board | - | new |
| 29 | github-mcp | `github/github-mcp-server` | 33,942 | MIT | Work with GitHub repositories through Claude | Grant the narrowest token scope | referenced already |
| 30 | playwright-mcp | `microsoft/playwright-mcp` | 38,605 | Apache-2.0 | Let Claude interact with websites in a browser | A browser the agent controls: sandbox, no logged-in sessions | referenced already |
| 31 | serena | `oraios/serena` | 30,684 | Other | Find relevant code and make targeted edits | Read the licence; it edits code | new |
| 32 | claude-code-router | `musistudio/claude-code-router` | 37,839 | MIT | Choose where your model requests are routed | Routing sends your code to whichever provider you pick: check privacy and terms | referenced already |
| 33 | awesome-mcp-servers | `punkpeye/awesome-mcp-servers` | 89,670 | MIT | Browse a directory of tools and service connectors | A list; every MCP server is third-party code with your credentials | new |

## Prompts and usage

| # | Name | Repo | Stars | Licence | What the card says | Care | In this library |
|---|---|---|---|---|---|---|---|
| 34 | system-prompts-ai | `x1xhlol/system-prompts-and-models-of-ai-tools` | not read | not read | Explore system prompts from popular AI tools | Collects prompts of commercial products, some probably extracted without the owners' consent: treat as reading material and do not republish | new |
| 35 | best-practice | `shanraisshan/claude-code-best-practice` | 67,980 | MIT | Read practical guidance for Claude Code | - | new |
| 36 | codex-plugin-cc | `openai/codex-plugin-cc` | 34,565 | Apache-2.0 | Use Codex to review code or delegate tasks | Sends code to a second vendor; needs a Codex account | new |
| 37 | claude-hud | `jarrodwatts/claude-hud` | 28,838 | MIT | See context usage, tools and running agents | Display only; low risk | new |
| 38 | rtk | `rtk-ai/rtk` | 84,497 | Apache-2.0 | Trim command output before it fills the context | A proxy that drops output: verify it does not hide errors | referenced already |
| 39 | headroom | `headroomlabs-ai/headroom (path chopratejas/headroom redirects)` | 77,786 | Apache-2.0 | Compress tool outputs, logs and files for the model | Compression can drop details; test on a real task | referenced already |
| 40 | caveman | `JuliusBrussee/caveman` | 114,991 | Apache-2.0 | Get shorter replies using fewer words | Shorter output can lose nuance; use for chatter, not for specs | referenced already |

## How the overlap column was set
"Referenced already" means the repo name or path appears in an existing skill or command here (a mention, not proof it is installed). "New" means no mention. The Batch 113 and 116 notes on ECC and the Karpathy repo still apply.

## Related
`claude-code-tooling`, `claude-token-skills`, `claude-token-rules-22`, `claude-code-setup-plugin`, `ecc-guide`, `skill-scout`, `skill-stocktake`, `oss-alternatives`, `protect-mcp-setup`, `connector-starter-stacks`.
