---
description: Create a reusable post TEMPLATE built around a chosen hook (Claude content-workflow skill 3/9, socialblueprint.ca)
argument-hint: [hook or topic to build a post template from]
---

# /post-writer

Source: "9 Essential Claude Skills" (socialblueprint.ca), skill 03 of 9.
Distinct from this repo's `content-script-writer` agent (which writes a
single finished post/script) — this one's job is to produce a reusable
**template shape** you can refill with new content, matching the source's
own framing exactly.

## What it does

Turns a chosen hook into a post *template* — a labeled structure (Hook,
Body beats, CTA) that can be reused for future posts on the same theme,
not just a one-off finished piece.

## Instructions

1. Take the hook (from `/hook-generator` or given directly) and the topic.
2. Output a labeled template, one line per beat, in this shape:
   ```
   HOOK  "[the opening line]"
   BODY  "[first supporting beat — the mechanism/insight]"
   BODY  "[second supporting beat — proof, example, or contrast]"
   CTA   "[the closing call-to-action]"
   ```
3. Below the template, fill it once with real copy for the current topic —
   the template is the reusable asset, the filled version is this week's
   post.
4. Note which part of the template is swappable per-topic (usually the
   BODY beats) vs. structural (the HOOK/CTA shape itself).

## Plain-text prompt

```
Create a post TEMPLATE built around this hook: "[HOOK]". Give me the
labeled structure (HOOK / BODY / BODY / CTA) as a reusable shape, then
fill it once with real copy for this topic: [TOPIC]. Tell me which parts
of the template I should swap out each time I reuse it.
```

Feeds into `/post-formatter` to adapt the filled template per platform.
