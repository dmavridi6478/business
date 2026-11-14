# Batch 109 (files numbered 113) - action plan

Inputs: two inline images ("AI Growth for Corporate Leaders & Businesses", 60 tools in 6 categories, @mshee; "Best Prompts for Excel/PPT tasks", 15 prompts) and `c4a04de1-iCloud_Photos.zip` with 16 JPEGs from two carousels: @aiclawbots "7 GitHub repos that could save you months building AI agents" (cover, 7 repo slides, a "Comment HERMES" slide) and @buildwithkenny "Trending on GitHub this week" (cover, 5 repo slides, a closing slide).

## 1. Created (committed)
| Source | Skill | Command |
|---|---|---|
| 60-tool AI map | ai-growth-tools-60 | /ai-tool-pick |
| 15 Excel/PPT prompts | excel-ppt-prompts-15 | /excel-ppt-prompt |
| Trending 5 (rea, security-audit-skill, orca, graphify, opencode) | github-trending-5-oct2026 | /repo-vet (any repo) |
| 7 agent repos (already covered by agent-github-repos-4 and agent-memory-repos) | agent-repos-licence-ledger (adds licences and warnings) | /agent-stack-plan |
Agent: `agent-stack-architect`. Workbook: `Artifacts/business/finance-models-starter.xlsx`. Design: `repo-rank-dark-orange`, `tool-map-six-categories`, `prompt-sheet-green`, `theme-ink-orange-condensed`, `theme-pastel-category-map`. User-run `scripts/batch113-install.sh` (clones only; syntax checked, not run).

## 2. Executed
- Built the workbook for prompts 1, 2, 4, 6, 7, 8, 9 with live formulas; recalculated in LibreOffice and checked 18 values against an independent Python calculation (all pass; the anomaly sheet flags exactly the two planted outliers).
- Confirmed with `git ls-remote` that 14 repos exist; read the licence file for 11 of them (the `yenanjing` harness list has none at LICENSE or LICENSE.md; `ai-boost` and `walkinglabs` were not read).
- Checked 24 tool names from the 60-tool map against the connector registry.

## 3. Workflows
None created: nothing in the images describes a workflow to build. The Browser Use slide's "multi-step workflow" is an illustration.

## 4. Connectors (cannot be installed from this session; each needs your sign-in at claude.ai under Connectors)
- Connected already: Notion, Canva, Adobe (Firefly), Figma, AI Producer by OpusClip, Fathom, Fireflies, Zapier, n8n, Clay.
- Installable, not installed: Jasper, ElevenLabs (voice-agent product), Descript, HyperFrames by HeyGen, Make, Otter.ai, Granola.
- Half-connected: Wispr Flow.
- Searched, not in registry: Perplexity, Surfer SEO, Grammarly, Midjourney, Synthesia, Taskade, Limitless, Lindy, Browserbase, Luma AI, VEED.io, Leonardo AI, Recraft, Ideogram. The registry's "Runway" is runway.team (release management), not Runway ML.
- No `.mcp.json` change.

## 5. Not done - needs you
| Item | Why | Step |
|---|---|---|
| Install any connector above | Needs your sign-in | claude.ai > Connectors |
| Clone or install any repo | Cloud session cannot touch your machine | `scripts/batch113-install.sh`, answer per step |
| The Hermes setup guide | A lead magnet offered to commenters; not in the archive | Comment on the original post if you want it |
| Check which "Awesome Harness Engineering" the card means | Three repos share the name; card shows no owner | Compare to `yenanjing/awesome-harness-engineering` (resolved in an earlier batch) |

## 6. Claims to treat as unverified
- All star counts (379k, 221k, 135k, 105k, 44.9k) and the "+78.6K in a week" claim: screenshots, not checked. 44.9k stars with 14 commits is unusual.
- "160+ research skills" for Scientific Agent Skills.
- The 60-tool map has no criteria; inclusion is not an endorsement.
- "Anthropic Cybersecurity Skills" is owned by an individual account (`mukul975`), not Anthropic.
