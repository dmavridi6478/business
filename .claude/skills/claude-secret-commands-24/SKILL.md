---
name: claude-secret-commands-24
description: Catalogue of 26 slash-command names, now rebuilt as commands (18 new, 8 already present), shown on a "Claude Secret Commands" graphic with each one's printed one-line job, a map to the equivalent already in this library (or a note that the original is someone's private skill and its contents are unknown), and a safe way to install any skill list received this way. Use when you see a list of "secret" Claude commands and want to know what you already have.
---

# "Claude secret commands": what they are, what you already had, what was rebuilt

Source: an animated typing graphic (Batch 129), a mock terminal titled "Claude Secret Commands" listing 26 slash commands. These are skills from one person's own setup (`claude.ai / skills`), not built-in features, and **nothing on the graphic shows what any of them contain**. Printed one-liners only. Do not install a pack received by commenting a keyword without reading each file.

| Command | Printed job | In this library |
|---|---|---|
| /grill-me | Asks the right questions before it starts building | `grill-me` (command) |
| /delete-ai-words | Cuts clichés and phrasing that make writing sound like AI | `avoid-ai-writing`, `humanizer`, `anti-ai` |
| /my-viral-post | Drafts LinkedIn posts with fresh hooks in your usual style | `post-writer`, `voice-builder`, `linkedin-virality-playbook` |
| /how-to | Helps you get something done step by step | `how-to` (command) |
| /infographic-builder | Makes a shareable 1080 x 1350 infographic from text | `infographic-prompts`, `design-templates` (1080x1350 templates) |
| /deep-research-synthesizer | Pulls scattered research into a summary with sources | `deep-research`, `research-summary`, `hyperresearch` |
| /deck-builder | Builds a finished slide deck in Gamma from an outline | Gamma connector; `claude-presentation-prompts`, `pptx` |
| /linkedin-hook | Gives 10 opening lines | `hook-generator`, `hook-writer` |
| /fable-prompter | Turns a rough draft into a prompt for Fable | `prompt-master`, `prompt-optimizer` (generic) |
| /negotiation | Helps plan pricing and approach before a call | `salary-negotiation-kit`, `/salary`, `objection` |
| /excel-style | Formats a tracker to match your spreadsheet style | `xlsx` |
| /hormozi-viral-1 | Writes posts that challenge the norm using Hormozi's framework | `marketing-council` (Hormozi advisor), `viral` |
| /meeting-notes | Meeting recording to summary and next steps | `meeting-notes-processor`, `granola-meeting-prompts` |
| /client-brief | Gets you up to speed on a prospect using CRM, email and web | `client-research`, `sales:account-research` |
| /linkedin-post-report | Explains your LinkedIn numbers and what to try next | `linkedin-analytics-reader`, `linkedin-analytics` |
| /viral-recipe | Finds what made a post work so you can reuse it | `viral`, `post-scorer`, `linkedin-virality-playbook` |
| /meeting-visualizer | Interactive dashboard from a Granola meeting | `dashboard-builder` plus the Granola connector |
| /tc-social-carousel | On-brand Instagram carousels from six templates | `carousel-writer`, `carousel` (command) |
| /reddit-researcher | Finds answers on Reddit, X and YouTube with sources | `social` (listening), `research` |
| /humanizer | Reworks stiff text into something you'd say | `humanizer` |
| /fact-checker | Checks each claim against original sources | `verify-common-claim`, `sourcecheck`, `research-and-self-factcheck` |
| /prompt-master | Shapes a rambling idea into a clear brief | `prompt-master` |
| /handoff | Saves context for the next chat | `handoff` |
| /write-a-skill | Turns described behaviour into an installable skill | `write-a-skill`, `skill-creator` |
| /personal-voice | Learns how you write, then checks drafts | `personal-voice`, `voice-builder` |
| /xlsx | Builds, reads and edits spreadsheets, formulas included | `xlsx` |

(26 rows; the final frame shows all 26. The first version of this skill said 24 in error.)

## Rebuilt (Batch 130)
The 18 commands that did not exist are now in `.claude/commands/` with the printed names: `/delete-ai-words`, `/my-viral-post`, `/infographic-builder`, `/deep-research-synthesizer`, `/deck-builder`, `/linkedin-hook`, `/fable-prompter`, `/negotiation`, `/excel-style`, `/hormozi-viral-1`, `/meeting-notes`, `/client-brief`, `/linkedin-post-report`, `/viral-recipe`, `/meeting-visualizer`, `/tc-social-carousel`, `/reddit-researcher`, `/fact-checker`. The other eight (`/grill-me`, `/how-to`, `/humanizer`, `/prompt-master`, `/handoff`, `/write-a-skill`, `/personal-voice`, `/xlsx`) already existed. **These are my own implementations written from the one-line jobs; they are not the original author's files and will behave differently.** `/hormozi-viral-1` is a generic contrarian-post structure, not Alex Hormozi's framework.

## Reading it
- **No new capability is shown.** 8 of the 26 names already existed. The other 18 were rebuilt from their one-liners at your request; the originals' logic is still unknown.
- **Names that look official aren't.** `/hormozi-viral-1` and `/tc-social-carousel` are one person's private skills; applying someone's named framework should respect their licence and not imply endorsement.
- **Unknown contents.** A one-line job can hide anything (network calls, file access, hidden instructions). Read the SKILL.md and any scripts before installing a skill from a list.

## If you want one of them
Use `/write-a-skill` with the printed line plus your own examples of the output you want, then test on three real inputs.

Related: `claude-code-commands-reference`, `skill-scout`, `skill-stocktake`, `claude-5-official-skills`, `claude-install-list-40`. Run with `/secret-command-map <command name or "all">`.
