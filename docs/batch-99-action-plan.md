# Batch 99 — action plan (second photo batch, 33 images)

Inputs: 5 inline images (Dora Vanourek 8 ways; CMO ChatGPT playbook; Gartner AEO metrics; McKinsey 7S; 22 Claude rules) and `88bc79d1-iCloud_Photos.zip` (28 images: "5 MCPs to Automate Your Life" 9-slide carousel, "Claude Code plugins nobody installs" 7 slides, "5 connectors that 10x your Claude for content" 6 slides, a 6-image replace.so GitHub set = cover + 5 repo cards).

## 1. Created (committed)
| Source | Skill | Command |
|---|---|---|
| 8 Ways to Build Executive Presence | executive-presence-8 | /exec-presence |
| CMO's ChatGPT Playbook (12 routines) | cmo-operating-cadence, cmo-plan-reviewer, cmo-monthly-review, cmo-brief-writer | /cmo-cadence |
| Gartner AEO diagnostic metrics | aeo-diagnostic-metrics | /aeo-score |
| McKinsey 7S + 6 tips | mckinsey-7s-model | /7s-audit |
| 22 Claude Rules (token limits) | claude-token-rules-22 | /token-audit |
| MCP life stack, content stack, security slide, plugin list | connector-starter-stacks | /connector-stack |

Design: templates `infographic-8-ways-grid`, `infographic-cadence-playbook-dark`, `infographic-7s-hexagon`, `infographic-rules-and-metrics`; themes `theme-playbook-night-lime`, `theme-dark-cream-carousel`, `theme-grid-paper-terracotta`. All templates rendered in headless Chromium and checked for overflow; themes checked at 900 px and 390 px, no horizontal overflow.

## 2. Executed
- Measured CLAUDE.md for rule 18/20: 1,807 words (limit 2,000) and 180 lines (limit 200). PASS, margins 193 words and 20 lines. Do not add much more to CLAUDE.md.
- Verified the five plugins exist in the official marketplace file `anthropics/claude-plugins-official` and are authored by the named vendors: paypal (PayPal), modern-web-guidance (Google Chrome), browser-use (Browser Use), lovable (Lovable), hyperframes (HeyGen).
- Verified with `git ls-remote` that all five repos exist: figranium/figranium, Vrun-design/openflowkit, ScrapeGraphAI/scrapecraft, bridge-mind/bridgeclip, knadh/listmonk.
- Checked connectors: Gmail, Google Calendar, Google Drive, Notion and Zapier are connected; Fathom is in the registry but not installed; Exa is available only as a flaky non-claude.ai MCP server this session; Apify and Apple-macOS are not in the registry.

## 3. Not done — needs you (with reason)
| Item | Why | Command / step |
|---|---|---|
| Install the five plugins | `/plugin` is an interactive command; I cannot run it | `/plugin install paypal@claude-plugins-official` and the four others in section G of batch-99-prompts.md. Install only what you will use: PayPal adds payment APIs. |
| Add five repos to setup-repos.sh | Blocked by the permission classifier (Untrusted Code Integration) | Append to the `repos=(...)` list: `figranium/figranium`, `Vrun-design/openflowkit`, `ScrapeGraphAI/scrapecraft`, `bridge-mind/bridgeclip`, `knadh/listmonk`. BridgeClip is a desktop app and Listmonk needs its own docker setup; cloning alone installs nothing. |
| Connect Fathom | Needs OAuth in claude.ai | claude.ai > Connectors > Fathom |
| Apify, Apple-macOS connectors | Not in the claude.ai registry | Apify: use its own MCP server from the vendor's site; macOS: a local MCP server, check the source before installing |
| Schedule the three recurring CMO routines (01, 02, 04) | They run daily or weekly on your account and cost tokens on every run, which conflicts with the 22-rules card (rule 12). Gmail routine would touch your mail. | Tell me "schedule routine 01" and I will create it as a draft-only Routine |
| .claude/settings.json entries from batch 98b | Classifier denied three times | See docs/batch-98-action-plan.md |

## 4. Claims to treat as unverified
- "41% of public MCP servers need no login" (one audit, no source on the card).
- "$5,725 of work a month on Opus vs $1,273 on Fable"; "4,784 tokens full screenshot vs under 100 cropped" (author's numbers).
- Plugin install counts (11 / 219 / 930 / 1,057 / 2,119) and "most installed: 1,134,112" are snapshots from one creator on one day.
- Modern Web Guidance "accuracy 50-57% without, 78-88% with" is the Chrome team's own figure.
- Repo star counts on the replace.so cards (Figranium 762, OpenFlowKit 833, ScrapeCraft 708, BridgeClip 364, Listmonk 23,708) were not re-checked.
- The replace.so cover says "6 GitHub repositories" but only 5 repo cards were in the upload.
- Rule 10 on the token card ("Paste Anthropic's two sentences") does not say which sentences; none were invented.
