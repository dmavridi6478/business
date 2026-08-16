---
description: Run a cold-outbound campaign end to end — strategy, list-building, copywriting, and campaign design — producing a single outreach brief, using the outreach-* skill bundle.
argument-hint: [product/offer and target market description]
---

Given the product/offer and target market described in "$ARGUMENTS" (ask the user for this if not provided — at minimum, what's being sold and who it's for):

1. **Strategy** — apply `outreach-strategy` to produce a trigger-based ICP, one persona card per buying-committee role, the signal→pain map, and the offer statement per persona. Don't skip to copywriting on a vague or purely-firmographic ICP — push back and ask for the actual trigger events first.
2. **List-building** — apply `outreach-list-building` against the ICP from step 1. If this session can't reach the actual sourcing tools (check with the `mcp-integration-scout` agent or `outreach-data-connections`), produce the filter/search criteria as a spec the user runs themselves rather than fabricating a contact list.
3. **Copywriting** — apply `outreach-copywriting` to draft the first-touch, follow-up, and breakup sequence (plus a VP-toned variant if the persona set includes an executive buyer) for at least the top-priority persona. Run the refiner checklist before presenting it as finished, then a `humanizer` pass.
4. **Campaign design** — apply `outreach-campaign-design` to generate 2-3 angles, architect the multi-touch structure (channel mix, cadence, exit conditions), and run the GTM stress test against the resulting plan. Report the stress test's findings even if they're unflattering to the plan just built — that's the point of running it.
5. **Assemble the brief** — write a single `outreach-brief.md` deliverable containing the ICP/personas/offer, the list-building spec or list, the messaging sequence(s), and the campaign structure with its stress-test notes. This is the canonical brief referenced by the other outreach skills' outputs.

Stop and ask before step 2 if the ICP is still vague after step 1, and before step 5 if the stress test in step 4 surfaced a finding serious enough that shipping the plan as-is would be a bad idea (e.g. the targeted seniority can't actually authorize the deal size) — flag it rather than writing a brief around a plan already known to be flawed.

Once replies start coming in on a shipped campaign, use `outreach-replies-pipeline` (not this command) to triage them and read pipeline health.
