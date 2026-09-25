---
description: Create different hooks to open a LinkedIn post or other written copy (Claude content-workflow skill 2/9, socialblueprint.ca)
argument-hint: [topic or draft to write hooks for]
---

# /hook-generator

Source: "9 Essential Claude Skills" (socialblueprint.ca), skill 02 of 9.
This repo's `hook-writer` skill and `content-hook-writer` agent already do
this at more depth (brand-voice matching, truth-to-content checks, per-
platform variants) — reach for those on a real content-pipeline job. This
command is the fast version for a single post, matching the source's exact
worked pattern.

## What it does

Generates multiple hook options for a piece of written copy — different
angles/structures, not just different wording of the same idea.

## Instructions

1. Take the topic or draft from `$ARGUMENTS` (or ask for one).
2. Produce at least 5 hooks spanning distinct structures, not minor
   rewordings — pull from patterns like:
   - **Contrarian**: "Everyone's using AI wrong."
   - **Pattern-interrupt confession**: "This one prompt changed everything."
   - **Command**: "Stop scrolling. Start systemizing."
   - **Specific-number curiosity**: "[N] things nobody tells you about X."
   - **Before/after**: "I used to think X. Then I learned Y."
3. Each hook must be true to what the post actually delivers — no
   overpromising a payoff the content doesn't have (same non-negotiable
   this repo's `hook-writer` skill enforces).
4. Mark which hook is the strongest bet and why (specificity, tension, or
   relatability — name the actual mechanism, not just "this one's good").

## Plain-text prompt

```
Write me 5 different hooks for a post about [TOPIC/DRAFT]. Use distinct
structures — contrarian, confession, command, specific-number curiosity,
before/after — not 5 variations of the same idea. Every hook has to be
true to what the post actually delivers. Tell me which one is strongest
and why.
```

Feeds into `/post-writer` once a hook is chosen.
