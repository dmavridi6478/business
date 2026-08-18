---
name: outreach-campaign-design
description: Design the overall shape of an outbound campaign — generating multiple distinct messaging angles per ICP, architecting the full multi-channel/multi-touch campaign structure, and stress-testing the resulting plan for whether it would actually work before it ships. Use when moving from individual message copy to campaign-level structure (sequence design, channel mix, cadence, angle selection).
---

# Outreach Campaign Design

Source: reviewed from a social post showing a "Claude Code outreach project" skill tree (`campaign-angle-finder.md`, `outbound-campaign-architect.md`, `gtm-action-thinker.md`); no external repo existed to vendor, so this is written fresh for this repo, covering the same three concerns as one skill.

Sits between strategy/copy (individual message level) and execution (`outreach-channels`) — this is where those pieces get assembled into an actual campaign plan with a defined structure, not just a pile of good messages.

## 1. Campaign angle-finder: 3 angles per ICP

A single messaging angle run against an entire ICP produces uniform, easily-ignored copy and no way to learn what resonates. Generate at least 3 distinct angles per ICP — typically varying which pain/trigger leads (from `outreach-strategy`'s signal→pain map), not just varying the wording of the same angle. Split the list across angles (not send-everyone-everything) so results are actually comparable, and treat the angle as the unit of experimentation, not the individual sentence.

## 2. Outbound campaign architect: full structure

Define, before anything sends: channel mix and sequencing (e.g. email touch 1 → LinkedIn connection → email touch 2 → call → breakup email), cadence (days between touches — tight enough to stay top-of-mind, loose enough not to read as spam), what triggers a contact's exit from the sequence (reply, booked meeting, explicit opt-out, or reaching the final breakup message), and ownership of each step (which parts are automated via `outreach-automation` vs. manual). A campaign plan that only specifies message copy and skips this structure is the most common reason outbound underperforms even with good copy.

## 3. GTM stress test

Before launch, deliberately try to break the plan: Does the ICP in `outreach-strategy` actually have budget authority, or does this campaign target the wrong seniority for the deal size? Does the volume assumed in `outreach-list-building` actually exist at the stated quality bar, or will hitting target list size require diluting the ICP? Does the cadence account for the sales cycle length, or does the sequence end before a realistic decision timeline? This is a critique pass specifically looking for the reason the plan fails, not a confirmation pass — the value is in finding the weak assumption before spend, not validating what's already been decided.

## Related skills in this repo

- **outreach-strategy**: supplies the ICP/pain map this skill's angles and stress test are built against.
- **outreach-copywriting** / **outreach-channels**: execute the individual touches this skill's architecture sequences together.
- **outreach-replies-pipeline**: the exit conditions defined here (reply, booking, opt-out) are what that skill's reply-handler and pipeline-analysis track against.
- **business-decision-frameworks**: useful for prioritizing which angle/ICP combination to run first when resources don't allow testing everything at once.
