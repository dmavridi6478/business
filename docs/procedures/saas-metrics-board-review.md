# SaaS Metrics Board Review

SOP for a recurring board/investor metrics review built around the 5
SaaS growth-efficiency metrics in `saas-growth-efficiency-metrics`:
Magic Number, Rule of 40, Net Revenue Retention, LTV:CAC by channel, and
CAC Payback Period. Backs that skill and the `saas-metrics-analyst` agent.

## When this applies

Any recurring (monthly or quarterly) prep of a SaaS metrics packet for a
board, investor update, or internal growth/finance review — not a one-off
metric lookup, which the skill's reference alone covers.

## Cadence

Run this review **quarterly at minimum**, monthly if the board/investor
cadence requires it. Trend each metric over at least 3 quarters before
drawing a conclusion from it — a single-quarter reading, especially for
NRR, can be distorted by one large account churning or expanding.

## Steps

1. **Gather real inputs, not last quarter's numbers copy-pasted.** Net
   new ARR and prior-quarter S&M spend; growth rate % and margin % (name
   the margin type — FCF or EBITDA — and don't switch it between periods);
   starting/expansion/contraction/churn ARR; CAC, LTV, and spend broken
   out **by channel**; CAC, MRR per customer, gross margin %. Route this
   to `saas-metrics-analyst` once assembled.
2. **Compute in board-review order, not metric-list order:**
   - **Magic Number + Rule of 40 first** — the efficiency gate. If both
     read weak, flag that before spending review time on the rest; the
     downstream metrics don't matter much if the top-level growth
     engine is broken.
   - **NRR next**, presented as a waterfall (Starting → Expansion → Churn
     → Contraction → Ending), never as a single blended %.
   - **LTV:CAC by channel next**, as a scatter (LTV vs CAC, one point per
     channel) — never blend channels into one company-wide ratio.
   - **CAC Payback last** — the cash-timing check. Compute it even when
     LTV:CAC looks healthy; payback can reveal a cash problem LTV:CAC
     hides on a long enough time horizon.
3. **Cross-check the five against each other before writing the
   narrative.** The real finding is usually a contradiction between two
   metrics, not any single number — e.g. a strong Magic Number sitting on
   top of shrinking NRR means new-logo growth is masking a leaky
   existing-customer base; a great LTV:CAC on one channel with a CAC
   payback over 18 months means that channel's economics don't survive
   contact with the company's actual cash runway.
4. **Write the narrative to what changes, not just what happened.** Every
   metric section should end in an implication — pause/fix/scale for
   Magic Number, which lever (growth or margin) needs attention for Rule
   of 40, which channel gets more or less budget for LTV:CAC, whether the
   cash runway assumption needs updating for CAC Payback.
5. **Carry the prior period's numbers into every panel** so the board
   sees trend, not just a snapshot — a 118% NRR reads very differently
   next to 112%-115%-118% (improving) than next to 122%-120%-118%
   (declining from a stronger base).
6. **File the packet and the raw inputs together**, not just the
   computed metrics — the next quarter's review needs the same input
   definitions (what counted as "expansion," which margin type was used)
   to keep the trend line honest.

## Red flags to stop and reconsider

- Fewer than 3 quarters of data available for a metric being presented as
  a trend — say it's a single-quarter snapshot, don't imply a trend that
  isn't there.
- Margin type (FCF vs EBITDA) changed between quarters without a note —
  the Rule of 40 trend line is no longer comparable; recompute prior
  quarters on the new definition or flag the break explicitly.
- LTV:CAC presented as one blended number anywhere in the packet — send
  it back for a channel breakdown before it goes to the board.

## Related

- `saas-growth-efficiency-metrics` (skill) — the formulas and benchmark
  bands this review runs on.
- `saas-metrics-analyst` (agent) — runs steps 1-3 end to end on real
  inputs.
- `Artifacts/business/saas-growth-efficiency-dashboard.html` — the live
  dashboard template for presenting the output of this review.
- `business-intelligence-report`, `ceo-reporting-skill` — for formatting
  the narrative into a full report deck.
