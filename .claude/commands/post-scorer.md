---
description: Review a finished post against your content standards and past performance data (Claude content-workflow skill 7/9, socialblueprint.ca)
argument-hint: [paste the finished post to score]
---

# /post-scorer

Source: "9 Essential Claude Skills" (socialblueprint.ca), skill 07 of 9.

## What it does

Scores a finished piece of copy against a fixed rubric before it goes out
— a pre-publish quality gate, not a general content critique.

## Instructions

1. Take the finished post from `$ARGUMENTS`.
2. Score each dimension 1-10, with a one-line reason for each score (not
   just the number):
   ```
   HOOK      [score]/10  — does the first line earn the next line?
   CLARITY   [score]/10  — is the point obvious on one read?
   VALUE     [score]/10  — does the reader learn/gain something real?
   FORMAT    [score]/10  — line breaks, length, platform conventions
   CTA       [score]/10  — is the ask clear and low-friction?
   ```
3. If any dimension scores below 7, give the specific rewrite that would
   fix it — not generic advice ("make it punchier") but the actual
   replacement line/section.
4. If past-performance data is available (this repo's `content-analyst`
   agent, or numbers pasted directly), weight the scoring against what's
   actually worked before for this account, not a generic rubric.

## Plain-text prompt

```
Score this post against my content standards. Give me HOOK / CLARITY /
VALUE / FORMAT / CTA, each out of 10 with a one-line reason. For anything
scoring below 7, give me the actual rewrite, not generic advice.
Post: [PASTE POST]
```

For scoring against real published-performance data rather than a fixed
rubric, use this repo's `content-analyst` agent instead — it reads actual
analytics.
