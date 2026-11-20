# 10 GitHub Repos That Turn Claude Into a Productivity Beast

Source: @your.aimentor (TikTok).

Four of the ten are **already covered** elsewhere in this repo — flagged
below rather than re-added. The other six are net-new.

| # | Repo | What it does | Impact (source's framing) | Status |
|---|---|---|---|---|
| 01 | **Repomix** | Packs your full codebase into one AI-readable file. | Claude stops guessing from one file and finally sees the whole project. | **New** — [`yamadashy/repomix`](https://github.com/yamadashy/repomix) |
| 02 | **Everything Claude Code** | Gives Claude Code agents, skills, commands, hooks, rules, and MCP configs. | Turns Claude Code from a tool into a working system. | **New** — [`affaan-m/everything-claude-code`](https://github.com/affaan-m/everything-claude-code); also appears as #4 in `top-12-agent-skill-repos.md` |
| 03 | **Dify** | Build AI apps, agents, RAG tools, and workflows visually. | Enterprise-grade AI workflows without starting from scratch. | **Already documented** in `claude-code-tooling` skill |
| 04 | **Flowise** | Creates AI agents with drag-and-drop blocks. | Fast prototypes, less setup pain. | **Already documented** in `claude-code-tooling` skill |
| 05 | **Onyx** | Builds a self-hosted AI chat system connected to your knowledge sources. | Your data stays under your control. | **New** — [`onyx-dot-app/onyx`](https://github.com/onyx-dot-app/onyx) (formerly Danswer) |
| 06 | **Claude Skills by Anthropic** | Official skills that teach Claude task-specific workflows. | The foundation for making Claude more reliable and repeatable. | **Already documented** — `anthropics/skills`, upstream of this repo's `docx`/`pptx`/`xlsx`/`pdf` |
| 07 | **Awesome Claude Skills** | Curates community-built Claude skills across marketing, SEO, writing, design, security, and testing. | Shows what Claude can become once people stop treating it like a chatbot. | **New** — [`ComposioHQ/awesome-claude-skills`](https://github.com/ComposioHQ/awesome-claude-skills) (75k★, top of several similarly-named lists) |
| 08 | **Repo: Obsidian Skills** | Teaches Claude to work with Obsidian vaults, tags, Bases, Canvas, and notes. | Connects your thinking system to your execution system. | **Unverified** — no owner visible on screen; no confident match found in a live search |
| 09 | **NotebookLM Skill** | Helps Claude work with NotebookLM-style research outputs. | Turns research piles into usable knowledge faster. | **Already vendored** in this repo as the `notebooklm-skill` skill (`claude-world/notebooklm-skill`) |
| 10 | **Repo: Marketing Skills by Corey Haines** | Adds structured marketing workflows for SEO, copy, ads, analytics, and GTM. | Claude stops writing generic fluff and starts following real marketing systems. | **New** — [`coreyhaines31/marketingskills`](https://github.com/coreyhaines31/marketingskills), MIT |

## Clone the net-new ones

```bash
mkdir -p ~/repos/claude-productivity && cd ~/repos/claude-productivity
git clone --depth=1 https://github.com/yamadashy/repomix
git clone --depth=1 https://github.com/affaan-m/everything-claude-code
git clone --depth=1 https://github.com/onyx-dot-app/onyx
git clone --depth=1 https://github.com/ComposioHQ/awesome-claude-skills
git clone --depth=1 https://github.com/coreyhaines31/marketingskills
```

`coreyhaines31/marketingskills` is the highest-value one to actually
install into `.claude/skills/` for this repo specifically — it's a marketing
skill *pack* (SaaS positioning, landing pages, launch copy) that
complements rather than duplicates the marketing skills already here
(`content-strategy`, `copywriting`, `marketing-psychology`). Review its
license and individual skill files before vendoring, the way `contract-review`
and the GSAP pack were vendored in earlier batches.
