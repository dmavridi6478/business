---
description: Build a reusable voice profile from your language, phrasing, and preferences (Claude content-workflow skill 5/9, socialblueprint.ca)
argument-hint: [paste 2-3 samples of your own writing]
---

# /voice-builder

Source: "9 Essential Claude Skills" (socialblueprint.ca), skill 05 of 9.
Produces the same kind of artifact this repo's `hook-writer` skill calls a
"brand-profile" and reads before writing hooks — use this command to
actually generate that file, then keep it as project context so every
other content command in this repo reads it too.

## What it does

Analyzes real writing samples and outputs a reusable voice profile — tone,
structure, style, and point-of-view — that future content generation can
be built against, instead of re-describing "how I write" every time.

## Instructions

1. Ask for 2-3 samples of the person's own past writing (posts, emails,
   notes — the rawer the better; polished marketing copy written by
   someone else won't capture their actual voice).
2. Extract and output a compact profile in this exact shape:
   ```
   TONE        [e.g. Direct / Warm / Blunt / Playful]
   STRUCTURE   [e.g. Numbered / Narrative / Fragmented]
   STYLE       [e.g. Short lines / Long flowing sentences]
   POV         [e.g. First-person / Second-person / Third-person]
   ```
   Plus 3-5 bullet notes on recurring quirks (favorite words, sentence
   openers to avoid, punctuation habits, what they never say).
3. Save the profile to `.agents/voice-profile.md` (or `.claude/voice-
   profile.md`) so `/hook-generator`, `/post-writer`, `/post-formatter`,
   and this repo's `hook-writer` skill can all read it automatically going
   forward — check for it at the start of those commands.

## Plain-text prompt

```
Build a voice profile from my writing. Here are 2-3 samples:
[PASTE SAMPLES]
Give me TONE / STRUCTURE / STYLE / POV plus my recurring quirks, in a
format I can save and reuse so future content sounds like me by default.
```
