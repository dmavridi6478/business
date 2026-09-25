---
description: Find relevant topics, stories, and conversations worth creating content around (Claude content-workflow skill 1/9, socialblueprint.ca)
argument-hint: [your niche or topic area]
---

# /niche-research

Source: "9 Essential Claude Skills" (socialblueprint.ca), skill 01 of 9 in a
content-creation workflow. This repo's `content-researcher` agent already
covers trend/competitor research at a deeper, multi-source level — reach
for that when the job needs live web research. This command is the fast,
single-turn version: a running topic/interest tracker for one niche.

## What it does

Given a niche or topic area, surface specific topics, stories, and ongoing
conversations worth building content around — ranked by how much interest
each is currently generating, not just relevance.

## Instructions

1. Ask for the niche/topic area if not given in `$ARGUMENTS`.
2. Ask (or infer from prior context) 2-3 recent pieces of content the user
   has published, to calibrate what "on-topic" means for them specifically.
3. Produce a table: **Topic | Interest** (a 1-5 or bar-style relative
   score, not a fabricated metric) — covering:
   - Recurring themes in their space right now
   - Specific stories/events worth reacting to
   - Workflow/system topics people in this niche are actively discussing
4. For each topic, add one line on the specific angle that would make it
   worth a post (not just "write about X" — the actual hook-worthy angle).
5. Flag which 1-2 topics are the strongest bet this week, and why.

## Plain-text prompt

```
Act as my niche researcher. My niche is [NICHE]. Recent posts I've made:
[LIST 2-3 RECENT TOPICS]. Give me a ranked table of topics, stories, and
conversations worth creating content around right now, with an interest
score and the specific angle that would make each one work — not generic
"write about X" advice.
```

Feeds into `/hook-generator` once a topic is picked.
