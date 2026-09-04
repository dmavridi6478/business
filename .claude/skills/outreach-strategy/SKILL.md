---
name: outreach-strategy
description: Define who a cold-outbound campaign targets and why, before any list gets built or copy gets written — trigger-based ICP (not static firmographics), contact-level persona cards, mapping a signal to the pain it implies, and defining the offer in terms of outcomes rather than features. Use when starting a new outbound/cold-outreach campaign, when reply rates are low and the targeting itself may be the problem, or when asked to define an ICP, buyer persona, or offer for outbound.
---

# Outreach Strategy

Source: reviewed from a social post showing a "Claude Code outreach project" skill tree (`icp-definer.md`, `persona-definer.md`, `pain-identifier.md`, `offer-definer.md`); no external repo existed to vendor, so this is written fresh for this repo, covering the same four concerns as one skill.

Cold outbound fails most often at targeting, not copy — a perfectly written email to the wrong person still gets ignored. This runs before `outreach-list-building` and `outreach-copywriting`, and its output (ICP + personas + pain map + offer framing) is what those two consume.

## 1. Trigger-based ICP, not static firmographics

"B2B SaaS, 50-500 employees" is a filter, not an ICP — it describes millions of companies with wildly different buying urgency. A trigger-based ICP instead names the **events** that predict someone is about to have the problem the product solves: a funding round, a leadership hire in a relevant function, a tech-stack change (new tool adopted, old one deprecated), rapid headcount growth in a specific team, a public complaint or review mentioning the problem. Firmographics (size, industry, geography) narrow the *pool*; triggers tell you **when** someone in that pool is actually in-market. List-building should filter on both.

## 2. Persona cards, per role in the buying committee

One persona per distinct role that touches the decision — economic buyer, technical evaluator, day-to-day user, and often a blocker (security/procurement/IT) — not one generic "decision maker" card. Each card: what they're measured on, what a bad outcome looks like for them personally, where they get information, and what objection is unique to their seat (a VP's objection to a tool is rarely the same as the end-user's).

## 3. Signal → pain map

For each trigger identified in step 1, state the specific pain it implies — not the product's feature list. "Just raised a Series B" doesn't imply "needs software," it implies specific pressures (scaling a process that worked at 10x smaller, proving ROI to a new board). The map should be falsifiable: if the signal doesn't actually predict that pain reliably, drop it rather than keep it because it's easy to find in a data source.

## 4. Offer definition: outcomes, not features

Outbound copy that leads with what the product *does* reads as generic; outbound copy that leads with the outcome a specific persona gets, tied to their specific pain from step 3, reads as relevant. Write the offer as "[persona] gets [outcome] instead of [status quo pain]," not as a feature list — the feature list is reference material for objection-handling later, not the opening pitch.

## Output

A short strategy brief: the trigger-based ICP definition, one persona card per buying-committee role, the signal→pain map, and the offer statement per persona. This is what `/outreach-campaign` uses to seed list-building and copywriting.

## Related skills in this repo

- **product-marketing-context**: the foundational "who's the customer" doc — pull from it rather than re-deriving personas from scratch if it already exists.
- **outreach-list-building**: consumes the trigger-based ICP directly as its filter criteria.
- **outreach-copywriting**: consumes the persona cards and offer statements as the substance of first-touch messages.
- **competitor-profiling**: if the pain map includes "currently using a competitor," that skill's battle-card output sharpens the objection-handling angle.
- **sales-enablement**: MEDDPICC/BANT qualification criteria overlap with the buying-committee persona cards here — reuse rather than duplicate.
