---
description: Run a cold-outbound campaign end to end — planning, list-building, copywriting, and campaign design — producing a single outreach brief, using the outreach-planning and outreach-execution skill bundle.
argument-hint: [product/offer and target market description]
---

Given the product/offer and target market described in "$ARGUMENTS" (ask the user for this if not provided — at minimum, what's being sold and who it's for):

1. **Strategy & ICP** — apply `outreach-planning` steps 1–4 to produce a trigger-based ICP, one persona card per buying-committee role, the signal→pain map, and the offer statement per persona. Don't skip to copywriting on a vague or purely-firmographic ICP — push back and ask for the actual trigger events first.
2. **Pre-flight check** — apply `outreach-planning` step 5 to verify which sourcing and execution tools are actually reachable in this environment. If key tools are unconnected, produce the filter/search criteria as a spec the user runs themselves rather than fabricating a contact list.
3. **List-building** — apply `outreach-planning` steps 6–9 to source and assemble a deduplicated CSV with company, contact name, title, verified trigger, and source. If this session can't reach the actual sourcing tools, produce the spec.
4. **Campaign architecture** — apply `outreach-planning` steps 10–12 to generate 2–3 angles, architect the multi-touch structure (channel mix, cadence, exit conditions), and run the GTM stress test. Report the stress test's findings even if unflattering — that's the point of running it.
5. **Copywriting** — apply `outreach-execution` Part 1 to draft the first-touch, follow-up, and breakup sequence (plus a VP-toned variant if the persona set includes an executive buyer) for at least the top-priority persona. Run the refiner checklist before presenting it as finished, then a `humanizer` pass.
6. **Assemble the brief** — write a single `outreach-brief.md` deliverable containing the ICP/personas/offer, data-connection status, list-building spec or list, the messaging sequence(s), and the campaign structure with its stress-test notes. This is the canonical brief referenced by the other outreach skills' outputs.

Stop and ask before step 3 if the ICP is still vague after step 2, and before step 6 if the stress test in step 4 surfaced a finding serious enough that shipping the plan as-is would be a bad idea (e.g. the targeted seniority can't actually authorize the deal size) — flag it rather than writing a brief around a plan already known to be flawed.

Once replies start coming in on a shipped campaign, use `outreach-execution` Part 3 (not this command) to triage them and read pipeline health. To automate a validated manual process, use `outreach-execution` Part 4.
