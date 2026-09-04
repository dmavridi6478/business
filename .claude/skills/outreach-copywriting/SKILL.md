---
name: outreach-copywriting
description: Write and refine cold-outbound email copy — signal-led first-touch messages under 100 words, a follow-up sequence including a breakup email, an executive/VP-toned variant, a strict quality-checklist pass, and benchmarking copy against aggregate outbound performance patterns. Use for writing or reviewing cold email sequences specifically (not warm/lifecycle email — see the emails skill for that).
---

# Outreach Copywriting

Source: reviewed from a social post showing a "Claude Code outreach project" skill tree (`copywriting-first-touch.md`, `copywriting-follow-up.md`, `copywriting-VP-sequence.md`, `copywriting-refiner.md`, `copywriting-analyzer.md`); no external repo existed to vendor, so this is written fresh for this repo, covering the same five concerns as one skill.

Consumes `outreach-strategy`'s persona cards and offer statements, and `outreach-list-building`'s per-contact trigger data. Distinct from the `cold-email` skill (installed via the marketingskills plugin) in scope — this one is specifically the multi-touch sequence + refiner + benchmarking system for a defined ICP/persona set, not general cold-email writing technique.

## 1. First touch: signal-led, under 100 words

Open with the specific trigger from the list (not a generic compliment or "I noticed you're in [industry]") — the trigger is proof the email isn't mass-blasted. State the implied pain in one sentence, the outcome-framed offer in one sentence, and a low-friction ask (a question, not "let's book 30 minutes") in one sentence. Under 100 words total — anything longer reads as a pitch, not a message from a person who did their homework.

## 2. Follow-up sequence + breakup email

Touch 2 adds new information rather than repeating touch 1 (a relevant proof point, a different angle on the same pain) — a follow-up that just re-sends the ask reads as pressure, not persistence. The final message in the sequence is an explicit breakup email: state that this is the last outreach, remove the pressure ("no hard feelings if now isn't the time"), and leave one easy path back in. Breakup emails routinely outperform the messages before them because removing pressure lowers the reply bar.

## 3. VP/executive-level sequence variant

Rewrite for a persona with less time and less patience for detail: shorter (VP touch-1 should beat the standard under-100-word bar, not just meet it), lead with business outcome over tactical detail, and drop any line that requires the reader to understand the product before understanding why it matters. Match the tone to the persona card from `outreach-strategy`, not a single fixed "executive voice."

## 4. Refiner: strict checklist pass

Before any sequence ships, check it against: exactly one CTA per message (not "let me know if you have questions AND want to book time"), no unverifiable superlatives ("industry-leading," "revolutionary"), the trigger/personalization is specific enough that it couldn't be copy-pasted to a different prospect unchanged, sentence length varies (a wall of same-length sentences reads as templated), and the ask matches the touch number (touch 1 asks less than touch 3).

## 5. Analyzer: benchmark against outbound performance data

Compare a sequence's structure against known outbound patterns — first-touch length, personalization depth, CTA friction, and touch-count — flagging where it deviates from what reliably performs (e.g., first touches over 150 words, sequences with no breakup email, identical CTA repeated across all touches) versus deviations that are a deliberate, justified choice for this specific ICP.

## Related skills in this repo

- **outreach-strategy**: supplies the persona/offer/pain inputs this skill writes from.
- **outreach-list-building**: supplies the per-contact trigger used for first-touch personalization.
- **outreach-channels**: LinkedIn/call/video outreach reuse this skill's messaging strategy, adapted per channel constraints.
- **humanizer**: run as a final pass on any drafted sequence — cold outbound is exactly the kind of copy that reads as AI-written if this step is skipped.
- **cold-email** (marketingskills plugin): general cold-email writing technique; use this skill instead when the task is specifically a multi-touch sequence for a defined outbound campaign.
