---
name: outreach-replies-pipeline
description: Triage and respond to inbound replies from a cold-outbound campaign, benchmark outbound performance against aggregate data, and analyze the pipeline stage by stage (sent, opened, replied, booked, closed). Use when replies are coming in and need handling, when a campaign's numbers need interpreting, or when diagnosing where a pipeline is leaking (e.g. good reply rate but no bookings).
---

# Outreach Replies & Pipeline

Source: reviewed from a social post showing a "Claude Code outreach project" skill tree (`reply-handler.md`, `outbound-analyst.md`, `pipeline-analysis.md`); no external repo existed to vendor, so this is written fresh for this repo, covering the same three concerns as one skill.

Runs continuously once a campaign designed by `outreach-campaign-design` is live — this is the read side (interpreting what's happening) that feeds back into strategy/copy adjustments.

## 1. Reply handler: 8 reply types

Classify every reply before drafting a response — the right response depends entirely on type, and a generic reply to all of them wastes the highest-intent moment in the whole sequence:

1. **Interested / wants more info** — move fast, answer the specific question, propose a concrete next step.
2. **Wrong person, referred elsewhere** — thank them, ask for a warm intro if offered, don't just re-pitch the referral cold.
3. **Not now, timing objection** — respect it, ask for a reasonable check-back point, don't argue the timing.
4. **Price/budget objection** — this early, it's usually a qualification question in disguise; answer briefly and redirect to value, don't discount preemptively.
5. **Already using a competitor** — this is where `competitor-profiling` output earns its keep; differentiate specifically, don't disparage.
6. **Explicit no / not interested** — acknowledge and stop; don't push back, it only damages the sender's reputation for future campaigns.
7. **Unsubscribe / stop contacting** — action immediately and permanently; treat this as non-negotiable regardless of campaign performance pressure.
8. **Out-of-office / auto-reply** — not a real reply; note the return date and let the sequence continue rather than treating it as engagement.

## 2. Outbound analyst: benchmark against aggregate data

Compare a campaign's reply rate, positive-reply rate, and booking rate against known outbound benchmarks for the channel and sequence length used, adjusted for list quality (a highly-targeted small list should outperform a broad list on rate, even with fewer total replies). Flag when a number is being read as "good" or "bad" without that context — a 2% reply rate is a different result on a cold, broad list than on a tightly-triggered one.

## 3. Pipeline analysis: stage by stage

Track the funnel explicitly — sent → opened (if trackable) → replied → positive reply → meeting booked → meeting held → closed — and diagnose the stage where the drop is sharpest rather than treating the whole pipeline as one number. Good reply rate but no bookings usually means the ask in the sequence is wrong (too vague, too high-friction), not that the targeting or copy failed. High open, low reply usually means the message itself didn't land despite the subject/hook working.

## Related skills in this repo

- **outreach-campaign-design**: defines the exit conditions (reply, booking, opt-out) this skill tracks against.
- **outreach-strategy**: pipeline drop-off often traces back to a targeting or offer problem defined there — this skill's job is finding *where* it breaks, strategy's job is fixing *why*.
- **competitor-profiling**: feeds directly into reply type 5 above (already using a competitor).
- **business-intelligence-report**: for a pipeline report going to leadership rather than an internal working diagnosis, hand off to that skill's format.
