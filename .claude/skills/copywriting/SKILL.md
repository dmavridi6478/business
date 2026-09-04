---
name: copywriting
description: Write clear, persuasive copy that converts — landing-page headlines, product descriptions, email copy, pricing pages, CTAs, and offer positioning. Use this whenever the user needs an individual piece of marketing/sales copy written or improved, not a content plan (see content-strategy for that) or a full sales deck (see sales-enablement for that). Trigger on "write a headline," "improve this CTA," "write product copy," "make this convert better," "write email copy," or when a landing page/offer/pricing page needs actual words, not just structure.
---

# Copywriting

Source: "5 Skills [that make Claude write better content]" carousel (@ai_slacker), Skill 02. Gives Claude a real copywriting process instead of guessing at tone and structure.

## Goal

Write clear, persuasive copy that converts — not just copy that sounds nice.

## Principles

**Clarity. Benefit. Proof. Action.** In that order of importance. A clear sentence about a real benefit beats a clever sentence about a vague one. Every principle exists to move the reader toward the action, not to demonstrate cleverness.

## The framework: Problem → Promise → Proof → CTA

| Step | What it does | What to write |
|---|---|---|
| **Problem** | Name the real problem | State the reader's actual pain in their language — not a generic category problem. If unsure what it is, pull it from `product-marketing-context` or discovery notes, don't invent one. |
| **Promise** | Show the better future | State the specific outcome the reader gets, not a feature. "Cut reporting time by 80%," not "AI-powered analytics." |
| **Proof** | Add credibility and results | A number, a named customer, a specific result — something a skeptical reader would find hard to dismiss. Never fabricate a metric; if none is available, say so and flag the gap rather than inventing one. |
| **CTA** | Make the next step obvious | One action, stated plainly. Compare: weak CTA "Learn more" (vague, no commitment) vs. stronger CTA "See how the system works" (specific, describes what happens next). |

## Tone

Helpful, confident, human. Not salesy, not robotic, not hedging. Write like a person who's confident in what they're offering, explaining it to someone they respect.

## Do

- Lead with the benefit, not the feature.
- Make it scannable — short sentences, clear structure, no wall of text.
- Be specific: a real number beats "significantly," a named outcome beats "better results."

## Don't

- Vague claims ("industry-leading," "revolutionary") without a specific backing.
- Jargon that a real customer wouldn't use in conversation.
- Fluff — any sentence that could be cut without losing meaning should be cut.

## Applying the framework by use case

| Use case | Emphasis |
|---|---|
| Landing-page headline | Promise, compressed to one sentence — the Problem is implied by who's reading |
| Product description | Benefit-first, Proof second, feature details last |
| Email copy | Problem/Promise in the subject + opening line, Proof in the body, one CTA at the end |
| Pricing page | Promise reinforced per tier, Proof (logos/results) placed near the price, CTA per tier |
| CTA button copy | Describe the outcome of clicking, not the mechanism ("See your results" beats "Submit") |
| Offer positioning | Problem stated sharply first — a well-named problem does most of the persuasive work before Promise even appears |

## Output conventions when using this skill

- Draft using the four-step framework explicitly — don't skip straight to polished copy without naming what problem/promise/proof/CTA the copy is built on, since that reasoning is what makes copy defensible and editable later.
- When a stronger psychological lever would sharpen the Promise or Proof step, pull from `marketing-psychology` rather than reaching for a generic persuasion trick.
- Run `humanizer` on the draft before calling it final — this skill's own "Tone: human" principle is easiest to violate by accident in a first draft.

## Related skills in this repo

- **content-strategy**: Decides *what* to write (topics, pillars, calendar) — this skill writes the individual piece once a topic is chosen.
- **marketing-psychology**: Supplies the behavioral principle (framing, social proof, anchoring, loss aversion, etc.) that sharpens this framework's Promise and Proof steps — pick the principle that fits the message, don't default to the same one every time.
- **sales-enablement**: Uses this skill's framework for one-pagers, deck copy, and CTAs — reach for `sales-enablement`'s deck-frameworks/one-pager-templates references for the surrounding structure, this skill for the words themselves.
- **product-marketing-context**: The source of truth for the real value proposition and differentiators the Promise/Proof steps should draw from — don't invent positioning here that contradicts it.
- **humanizer**: Run on the finished draft to strip AI-writing tells before publishing.
- **campaign-page-one-shot** / **frontend-design**: Build the actual landing page once this skill's copy exists.
- **outbound-campaign-brief**: Uses this skill's framework for the actual outreach message once a target list and channel are defined — this skill writes the words, that one owns the targeting → drafting → approval-gated-send workflow.

## Notes

Source: "Claude is too dumb to write your content. These 5 Skills fix it." carousel (@ai_slacker), Skill 02 (`marketingskills/copywriting`, `copy_framework.md`).
