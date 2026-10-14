---
name: vibe-coding-plugin-layers-5
description: The "5 Claude Plugins for Vibe Coding" stack as five layers - eyes (Playwright CLI), data (Supabase), security (Strix), design (SkillUI), docs (Context7) - with what each really is, how to install it from its own README, what this repo already has configured, and the risk each adds. Use when the user vibe-codes with Claude Code, asks which five plugins to install, or wants a browser check, database, security scan, design extraction and live docs wired in.
---

# 5 plugins for vibe coding - checked

Source: an infographic by @boscokat (image supplied in a batch, 12 October 2026). Checked against each project's README and LICENSE that day.

| Layer | Tool | What it is | Install (from its README) | Already in this repo? | Risk to know |
|---|---|---|---|---|---|
| Eyes | **Playwright CLI** (`microsoft/playwright-cli`, Apache-2.0) | Browser automation CLI so the agent can open and screenshot your app | `npm install -g @playwright/cli@latest` (README), then `playwright-cli screenshot`; `playwright-cli install --skills` adds its skills | The Playwright **MCP** is in `.mcp.json`; the `playwright` MCP covers the same job | Opens real pages; do not point it at logged-in accounts. The slide's install line (`npm i -g @playwright/cli`) matches the README |
| Data | **Supabase** | Database plus edge functions, driven from the agent | Supabase MCP (already connected in this workspace) | `supabase` in `.mcp.json`, set to `read_only=true` | **Keep read-only** unless you need writes; a migration run by an agent changes real data |
| Security | **Strix** (`usestrix/strix`, Apache-2.0) | AI agents that probe your app like an attacker, then report findings | README: needs Docker running; `strix --target ./app-directory`. The README's installer is `curl -sSL https://strix.ai/install | bash` (a piped script: read it first, or use the pipx / uv route its update note names: package `strix-agent`) | Not installed | It sends traffic to the target and may send code to a model provider: test only systems you own, on a copy |
| Design | **SkillUI** (real repo `amaancoderx/npxskillui`, MIT) | CLI that extracts a site's colours, type and spacing into a SKILL.md and DESIGN.md | `npm install -g skillui` (README); ultra mode needs `npm install playwright` and `npx playwright install chromium` | Not installed. The slide gave no repo path; the one above was found by search, not from the slide | Copying a design system from a live site may breach that site's rights: use it for your own sites or for reference only |
| Docs | **Context7** (`upstash/context7`, MIT) | Pulls current library docs into the prompt | Add `use context7` to a prompt; MCP URL `https://mcp.context7.com/mcp` | `context7` in `.mcp.json` and connected here | Docs are third-party text: treated as data, not instructions |

## Corrections to the slide

- "Plugins" is loose: three of the five are CLIs or MCP servers, not Claude plugins.
- The slide's SkillUI has no repo path; the real one differs from the likely guess (`amaanbuilds/skillui` returns 404).
- "Attacks your app like a real hacker" is marketing. Findings need human triage; some will be false positives.

## Use order

1. Context7 (free, no side effects).
2. Playwright check after each change.
3. Supabase read-only, then write access for one session only.
4. Strix on a staging copy before launch.
5. SkillUI when you want a house style from a site you have rights to.

## Command

`/addon-pick vibe coding` lists which of these to add for the project and the first command for each.
