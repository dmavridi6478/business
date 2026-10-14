---
name: claude-code-addons-top5
description: The five Claude Code add-ons the @awayfromlovable carousel ranks by GitHub stars (Superpowers, Matt Pocock skills, ECC, Karpathy-derived CLAUDE.md, Anthropic document skills), with the exact install commands checked against each README on 12 October 2026, what each changes about how Claude behaves, which overlap, and which to install first. Use when the user asks which Claude Code plugins or skills to add, wants the install commands, or wants to avoid stacking overlapping add-ons.
---

# Top 5 Claude Code add-ons (by stars) - checked

Source: @awayfromlovable carousel, 7 slides. Star counts on the slides (297,407 / 285,381 / 276,838 / 218,668 / 180,426; Claude Code itself 150,137) are the author's and were **not** re-checked; stars measure attention, not quality.

| Rank | Add-on | What it does | Install (README-confirmed) | Licence |
|---|---|---|---|---|
| 1 | **Superpowers** (Jesse Vincent) | Claude asks what you want first, plans in small tasks, writes the test before the code | `/plugin install superpowers@claude-plugins-official` | MIT |
| 2 | **Matt Pocock skills** | `/grill-me`: it questions you about every branch of a plan until nothing is open | `claude plugin install mattpocock-skills@claude-plugins-official` (also `npx skills@latest add mattpocock/skills`) | MIT |
| 3 | **ECC** | 71 agents, 311 skills, 97 command shims, hooks, memory, AgentShield | `/plugin marketplace add https://github.com/affaan-m/ECC` then `/plugin install ecc@ecc` | MIT |
| 4 | **Karpathy-derived CLAUDE.md** | One file, four rules: think before coding, simplicity first, surgical changes, goal-driven execution | `/plugin marketplace add forrestchang/andrej-karpathy-skills` then `/plugin install andrej-karpathy-skills@karpathy-skills` (or `curl -o CLAUDE.md <raw url>`) | **No licence file found at the repo root** on 12 Oct 2026; check before redistributing |
| 5 | **Anthropic document skills** | Word, PDF, PowerPoint, Excel skills | `/plugin marketplace add anthropics/skills` then `/plugin install document-skills@anthropic-agent-skills` | Source-available for the file skills (per the slide), not open source |

## Corrections to the slides

- #4 is **not made by Andrej Karpathy**. The README says it turns his public observations on LLM coding mistakes into a CLAUDE.md. The slide says the same.
- Counts for ECC differ inside its own README (71/311/97 in the headline table, 67/281/94 in an older release note). Use the current table.
- ECC warns to install only from its listed official channels and **not to stack a manual install on the plugin**.
- The slide commands are accurate for #1, #2, #3, #4 and #5 as of the READMEs, but each needs the marketplace added first where shown.

## Which to install, in order

1. **Karpathy rules** (4 lines of behaviour, near-zero context cost) - merge into your own CLAUDE.md rather than replacing it. This repo's CLAUDE.md is a hyperresearch contract; append, never overwrite.
2. **Superpowers** if you build software here. It overlaps with the 4 rules and with `/grill-me`; run one workflow at a time.
3. **/grill-me** for non-code plans (this repo already has `/grill-me`).
4. **Anthropic document skills** when you need files (this repo already vendors `pdf`, `docx`, `xlsx`, `pptx`).
5. **ECC** last: it is a whole system with hooks and many skills; it competes for context and changes behaviour broadly. Scan it first (`skillspector-preinstall-scan`).

## Overlap already in this repo

`superpowers:*` skills are loaded; `grill-me`, `pdf`, `docx`, `xlsx`, `pptx`, `ecc-guide`, `configure-ecc` exist. Do not install a second copy of the same plugin.

## Command

`/addon-pick <what you are building>` returns the one or two add-ons worth installing for that job and the order.
