---
description: Run the one-person-business system end to end — idea, offer, content system, sales system, and scaling roadmap — using the one-person-* skill bundle sourced from a social prompt carousel.
argument-hint: [your skills/interests, or an existing idea/offer if you already have one]
---

Given what's described in "$ARGUMENTS" (ask the user for this if not provided — at minimum, their skills/interests and lifestyle goals, or the existing idea/offer they want to pick up from):

1. **Idea** — apply `one-person-business-idea` to find the intersection of what they know, enjoy, and what the market already pays for, generate 3 candidate models, validate each against real existing demand, and select the strongest with a one-sentence positioning statement. Skip this step if the user already has a validated idea and start at step 2.
2. **Offer** — apply `one-person-offer-architect` to turn the positioning statement into a priced offer that sells a transformation (never a service/deliverable), anchored to outcome value.
3. **Content system** — apply `one-person-content-system` to build the core-thesis-driven content engine that drives attention toward the offer, sized to what one person can sustain (under 2 hours/week for repurposing).
4. **Sales system** — apply `one-person-sales-system` to map the path from content viewer to paying client, with a lead-capture, nurture, and conversion mechanism that needs zero sales calls.
5. **Scaling** — apply `one-person-business-scaling` to audit which hours are still traded directly for money and design a digital-product/passive-income layer plus a 12-month roadmap with monthly revenue milestones, without recommending hiring.

Stop and ask before step 2 if the idea from step 1 failed its own validation check (no evidence anyone is already paying for that outcome) — don't build an offer around an idea already flagged as weak. Stop and ask before step 5 if steps 3–4 haven't actually produced anything yet (no content system or sales system running) — scaling a system that doesn't exist yet just produces a fantasy roadmap.

Each skill's own SKILL.md carries the original prompt verbatim (in a `Prompt (copy-paste)` section) if the user wants to run any stage directly in another assistant instead of through this command.
