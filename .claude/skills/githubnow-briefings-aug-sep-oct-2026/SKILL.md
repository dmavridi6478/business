---
name: githubnow-briefings-aug-sep-oct-2026
description: Three daily GitHub trending briefings (11 August, 29 September and 15 October 2026) from @3hship and @githubnow covering 11 repos including xerj, obra/superpowers, WeKnora, reclip, worktrunk, NVIDIA SkillSpector, nvm, manim, transformers, diagram-design and anthropics/skills, with licences read on 16 October 2026.
---

# GitHub trending briefings, three days

Sources: three card sets (cover, one card per repo, a "tomorrow's drop lands at the same time" card). Star gains ("today", "this month") are the cards' own and **unverified**. Licences were read from each repo's LICENSE file on 16 October 2026.

## 15 October 2026, "Your AI agents are wasting tokens. Try these three." (@githubnow)
| Repo | Card figure | Licence | Summary |
|---|---|---|---|
| xerj-org/xerj | +725 today | Apache-2.0 | Local AI search engine: indexes a folder with one command so coding agents get file:line passages; one static Rust binary with an Elasticsearch-compatible API; MCP and CLI; `xerj init` wires Claude Code and Cursor |
| obra/superpowers | +534 today | MIT | Agentic skills framework: ask what you are building, write a spec in chunks, plan with red/green TDD, YAGNI and DRY, then subagents work each task and review; skills trigger automatically |
| Tencent/WeKnora | +11,159 this month | Apache-2.0 | RAG, agent and wiki platform: parses 10+ formats into a hybrid search index with citations; sandboxes (Docker, E2B, Cube); MCP tools; workspace RBAC with four roles |
The closing card says "Start with xerj; the README gets you running in ten minutes." That is the author's claim.

## 29 September 2026, "Tools that solve problems you didn't know you had" (@githubnow)
| Repo | Card figure | Licence | Summary |
|---|---|---|---|
| averygan/reclip | +114 today | MIT | Self-hosted video downloader (about 150 lines of Python and Flask, plain HTML front end) for 1000+ sites, MP4 or MP3. **Downloading from YouTube, TikTok and similar sites can breach their terms or copyright; use only content you own or may copy** |
| max-sixty/worktrunk | +44 today | Apache-2.0 | Git worktree manager: `wt list`, switch, remove; hooks on create or remove; copy-on-write build cache; gives each AI agent its own branch and directory |
| NVIDIA/SkillSpector | +3,493 this month | Apache-2.0 | Scans AI agent skills for 71 vulnerability patterns in 17 categories (prompt injection, data exfiltration, supply chain); static pass plus optional LLM review; risk score 0-100; terminal, JSON, Markdown and SARIF reports; live CVE lookups from OSV.dev. The card shows literal `**` markdown marks in its headline |
Closing card: "Start with reclip." Relevant here: this repo vendors many skills, and SkillSpector is a way to scan them. It was not run (see the install script).

## 11 August 2026, "What devs are watching today" (@3hship)
| Repo | Card figure | Licence | Summary |
|---|---|---|---|
| nvm-sh/nvm | +18 today | MIT | A sourced POSIX shell function for many Node versions under ~/.nvm; sh, dash, ksh, zsh, bash, not fish; no native Windows build |
| 3b1b/manim | +246 today | MIT | The 3Blue1Brown ManimGL engine; separate from the community edition that forked in 2020, so do not mix install instructions (see `manim`) |
| huggingface/transformers | +69 today | Apache-2.0 | Model definition framework for text, vision, audio, video and multimodal; Pipeline API; PyTorch 2.5+ |
| cathrynlavery/diagram-design | +1.6k today, +27% spike | MIT | Claude Code skill that emits self-contained HTML and SVG diagrams across 29 types; export PNG or SVG |
| anthropics/skills | +468 today | no LICENSE at the repo root | Folders with a SKILL.md loaded on demand. Its README says many skills are Apache-2.0, the document-creation skills are source-available, and all are demonstration examples. Read each skill folder's own licence |

The "Comment/Star/Fork" style calls to action were not followed. Run `/trending-pick` or `/repo-licence-check` before adopting any of these.
