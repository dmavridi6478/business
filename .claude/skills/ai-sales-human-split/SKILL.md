---
name: ai-sales-human-split
description: 'Where AI and sales meet - a Venn model of what AI does best (prospect research and enrichment, CRM updates, prep briefs, follow-up drafts at scale, pipeline reporting), what humans do best (discovery conversations, reading the room, live objection handling, presenting proposals, negotiating price and terms) and six collaboration patterns (AI drafts, human personalises). Use to decide what to automate in a sales process and what must stay human, or to audit an AI sales workflow. Source: "Where AI And Sales Meet" infographic.'
---

# Where AI and sales meet

| AI does best ("free up your selling time") | How they collaborate | Human does best ("build trust that closes the deal") |
|---|---|---|
| Prospect research and enrichment | **Call prep**: AI researches, human builds the angle | Discovery conversations that build trust |
| CRM updates and call logging | **Follow-up emails**: AI drafts, human personalises | Reading the room in live calls |
| Meeting prep briefs and agendas | **Discovery notes**: AI captures, human flags what matters | Real-time objection handling |
| Follow-up email drafts at scale | **Proposal building**: AI structures, human writes the narrative | Presenting proposals |
| Pipeline reporting and forecasting | **Deal strategy**: AI surfaces patterns, human makes the call | Negotiating price and terms |
| | **Pipeline prioritisation**: AI scores, human decides the focus | |

## Rules this implies for this repo
- Any step where a person is persuaded, trusted or negotiated with stays human; AI output on those steps is a draft that a person edits and sends. This matches the draft-only design of the `os-*` and `gtm-*` agents.
- Scores and forecasts are inputs, not decisions: the human owns "decide the focus".
- Audit prompt: list each step of your sales process, label it AI, human or collaborate, and name the human check for every collaborate step.

## Plain-text prompt (copy and paste)
```
Here is my sales process, step by step: [LIST STEPS]. For each step classify it as AI-led, human-led or collaborate, using this rule: AI does research, enrichment, logging, prep briefs, drafting at scale and reporting; humans do discovery, reading the room, live objections, presenting and negotiating; for collaborate steps say what the AI produces and what the human must check. Flag any step where I am automating something that needs trust. Give me the three steps where AI would free the most selling time.
```
Related: `ai-sales-prep-15min`, `sales-workflow-catalog`, `gtm-ops-diagnostic`. Rendering: `design-templates` > `venn-two-circles.html`.

## Keywords
AI and sales, human in the loop, call prep, follow-up, pipeline, collaboration model
