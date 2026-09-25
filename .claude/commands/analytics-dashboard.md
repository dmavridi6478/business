---
description: Turn content analytics into performance data you can use to improve future posts (Claude content-workflow skill 9/9, socialblueprint.ca)
argument-hint: [paste analytics data, or platform name to pull from]
---

# /analytics-dashboard

Source: "9 Essential Claude Skills" (socialblueprint.ca), skill 09 of 9,
closing the loop back to `/niche-research` and `/post-scorer`. This repo's
`content-analyst` agent already does the deeper version of this (reading
real performance data, retention patterns, format/hook/topic
combinations) — use that agent for a full performance review; use this
command for a fast single-number dashboard snapshot.

## What it does

Turns raw analytics numbers into a compact dashboard read, with direction
(up/down vs. the prior period) rather than just restating totals.

## Instructions

1. Take the pasted metrics or, if a connector is available for the
   platform in question, pull them directly rather than asking the user
   to copy-paste.
2. Output a compact grid, matching the source's own shape:
   ```
   [N]      [±%]        [N]      [±%]        [N]      [±%]
   REACH    ▲/▼ vs last  LIKES    ▲/▼ vs last  COMMENTS ▲/▼ vs last
   [N]      [±%]        [N]      [±%]        [N]      [±%]
   REPOSTS  ▲/▼ vs last  SAVES    ▲/▼ vs last  ENGAGE   ▲/▼ vs last
   ```
3. Below the grid, name the single biggest mover (up or down) and the
   most likely cause, tying back to a specific post/format if the data
   supports it — don't speculate past what the numbers actually show.
4. Close with one actionable recommendation for the next post, feeding
   back into `/niche-research` or `/post-scorer`.

## Plain-text prompt

```
Turn this analytics data into a dashboard: reach, likes, comments,
reposts, saves, engagement — each with % change vs. the prior period.
Tell me the single biggest mover and the most likely cause, and give me
one actionable recommendation for my next post.
Data: [PASTE METRICS]
```

For a deeper performance review across multiple posts (retention,
hook/format patterns), use this repo's `content-analyst` agent instead.
