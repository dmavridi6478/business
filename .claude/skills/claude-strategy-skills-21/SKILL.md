---
name: claude-strategy-skills-21
description: A 21-skill strategy toolkit organised by job (frame, size, decide, design, derisk, report, run) from a "107 Claude strategy agents" graphic, with an original method card for each skill (question answered, inputs, output, failure check), a chooser, and an honest note on what the graphic claims but does not show (the 107 count, the "$1,800,000 study" and the five prompts each are not in the image). Use when structuring a strategy engagement, a board decision or a transformation plan with Claude.
---

# 21 strategy skills, one engagement flow

Source: a terminal-style graphic, "107 Claude strategy agents, zero consultants: every skill in a $1,800,000 strategy study, 5 prompts each" (Batch 123, author's handle thecraftofai). The graphic lists 21 of the 107 skills and ends with a "comment AGENTS" lead-magnet prompt. The remaining 86 skills, the five prompts per skill and the "$1.8M study" are **not shown and not verified**. The method cards in `references/21-strategy-skills.md` are original: I wrote them from each skill's title and one-line description, not from the author's prompts.

## The 21, by job (names and descriptions as printed)

| Job | Skills |
|---|---|
| Frame | `problem-framing` (issue trees that split the real question), `fact-base` (the evidence pack behind every claim), `assumption-audit` (finds the load-bearing guess before it costs) |
| Size | `market-sizing` (TAM the way a case team builds it), `competitive-intel` (what rivals are doing, sourced), `customer-segmentation` (who actually pays, cut by behavior), `profit-pools` (where the margin sits in the chain) |
| Decide | `strategic-options` (three real paths, costed and compared), `pricing-strategy` (price moves with the math shown), `business-cases` (the model a CFO can pressure-test), `portfolio-review` (keep, fix, or kill, with reasons) |
| Design | `operating-model` (who does what after the decision), `initiative-priority` (sequenced by value and readiness), `transformation-roadmap` (waves, owners, and dates) |
| Derisk | `risk-mitigation` (named risks with a move for each), `war-gaming` (how competitors punch back, played out) |
| Report | `kpi-architecture` (the metric tree that proves progress), `stakeholder-alignment` (who must say yes, and their price), `executive-narrative` (the deck that carries the number), `board-memos` (the decision, written for the minutes) |
| Run | `operating-system` (the reusable cadence that keeps it alive) |

## How to use them as one flow
1. **Frame first, always.** Run `problem-framing`, then `fact-base`, then `assumption-audit`. If you skip this, later outputs are polished answers to the wrong question.
2. **Size with sources.** Market, rivals, segments and profit pools each need a named source and date per figure. Mark any number the model could not source as an assumption.
3. **Decide with the math visible.** Options, pricing and the business case must show inputs, formulas and a sensitivity range. A CFO should be able to change one input and see the result.
4. **Design, then derisk.** The roadmap and operating model come after the decision, then risks and war-gaming test them.
5. **Report once.** KPI tree, stakeholder map, narrative and board memo are written from the same fact base; contradictions between them are findings.
6. **Run.** The cadence skill turns a project into a routine, or the work decays.

## What the graphic overstates
- **"Zero consultants."** A model drafts structure quickly; it does not hold your data, your politics or the accountability. Keep a named human owner per skill and a review step before anything reaches a board.
- **Numbers.** Model-made market sizes, margins and price elasticities are plausible fiction unless tied to sources you can open. Ask for the source and date next to every figure and spot-check ten percent.
- **Count and cost.** 107 skills and a $1.8M study are marketing figures. Do not repeat them.
- **Lead magnet.** "Comment AGENTS" is an engagement hook; if you send your details for the pack, read what the skills contain before you install them and treat them as untrusted prompts.

## Overlap in this library
`mckinsey-frameworks-10`, `mckinsey-7s-model`, `product-strategy-session`, `business-decision-frameworks`, `startup-financial-modeling`, `market-sizing-analysis`, `competitive-landscape`, `board-dashboard-3-statement`, `kpi-dashboard-design` and the plugin skills under `strategy-frameworks:*` cover individual steps. This skill is the flow that connects them.

Run with `/strategy-skill <skill name or "flow"> <your situation>`.
