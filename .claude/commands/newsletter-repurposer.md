---
description: Structure an email newsletter and repurpose existing content into newsletter copy (Claude content-workflow skill 6/9, socialblueprint.ca)
argument-hint: [topic, or paste existing post(s) to repurpose]
---

# /newsletter-repurposer

Source: "9 Essential Claude Skills" (socialblueprint.ca), skill 06 of 9 —
named `/newsletter` in the source; renamed here to avoid ambiguity with
this repo's existing `ai-newsletter-system` command, which is a different
tool (a 2-prompt weekly-writer + subject-line system for growing paid
subscribers, @earchoe). Use `ai-newsletter-system` to build a newsletter
audience from scratch; use this command to turn content you already have
into a structured issue.

## What it does

Two jobs: (1) structures a newsletter issue from a topic, (2) repurposes
already-published content (posts, threads, articles) into newsletter copy
instead of writing an issue from a blank page.

## Instructions

**Structuring a new issue:**
1. Ask for the topic and the newsletter's usual sections (if this repo
   already has a voice-profile/style file, read it first).
2. Output: subject line (2-3 options), preview text, then the issue body
   in this shape — a short hook paragraph, 2-3 content sections each with
   its own mini-header, a closing CTA.

**Repurposing existing content:**
1. Take the pasted post(s)/article(s).
2. Don't just copy-paste — adapt the pacing for an inbox read (shorter
   paragraphs than a blog post, a "why this matters" framing a social post
   doesn't need) and consolidate multiple posts into one coherent issue if
   more than one was given.
3. Output the same subject-line + preview-text + body shape as above.

## Plain-text prompt

```
Structure this week's newsletter issue on [TOPIC]. Give me 2-3 subject
line options, preview text, and the issue body (hook paragraph, 2-3
sections, closing CTA).
```

```
Repurpose this into newsletter copy — adapt the pacing for an inbox read,
don't just copy-paste it: [PASTE POST(S)/ARTICLE]
```
