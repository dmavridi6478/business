---
description: Organize a voice memo or rough notes into clean, structured copy for a specific social platform (Claude content-workflow skill 4/9, socialblueprint.ca)
argument-hint: [platform] [raw voice memo or notes]
---

# /post-formatter

Source: "9 Essential Claude Skills" (socialblueprint.ca), skill 04 of 9.

## What it does

Takes messy raw input — a transcribed voice memo, bullet notes, a stream-
of-consciousness draft — and organizes it into clean, platform-formatted
copy, preserving the original voice rather than rewriting it into generic
AI-sounding prose.

## Instructions

1. Take the platform (LinkedIn, X/Twitter, Instagram caption, etc.) and
   the raw text from `$ARGUMENTS`.
2. Do NOT rewrite the substance or add ideas that weren't in the raw
   input — this is formatting, not ghostwriting. Preserve the person's
   actual phrasing and specific examples wherever possible.
3. Apply the platform's real formatting conventions:
   - **LinkedIn**: short paragraphs (1-3 lines), a line break before the
     payoff, hashtags minimal or none
   - **X/Twitter**: thread-broken into individual tweet-length chunks if
     long, first tweet must stand alone as a hook
   - **Instagram caption**: hook line, blank line, body, blank line, CTA
     + hashtag block at the end
4. Run this repo's `humanizer` skill's checklist over the output before
   returning it — strip AI tells (forced triads, "not X but Y" contrasts,
   inflated claims) that formatting passes tend to introduce.

## Plain-text prompt

```
Organize this voice memo/notes into clean, structured copy for [PLATFORM].
Don't rewrite my ideas or add anything I didn't say — just format it
properly for the platform and clean up the phrasing. Here's the raw
input: [PASTE VOICE MEMO OR NOTES]
```

Feeds into `/post-scorer` once formatted.
