# 09 — The Incrementality Bridge

## Connecting Platform Metrics to True Business Impact

Platform metrics tell you how the ads are performing *within the platform's measurement framework*. Incrementality tells you whether the ads are actually driving business outcomes that would not have happened without them. This document bridges the gap.

---

## The Fundamental Problem

Every ad platform has a structural incentive to over-report its own value. This is not fraud — it is the natural consequence of attribution models that give credit to ads for conversions they may not have caused.

**The question that attribution cannot answer:**

> "What would have happened if we had not run this ad?"

This is the counterfactual — and no amount of click tracking or view-through attribution can answer it. Only causal measurement can.

---

## When Platform Metrics Lie (Common Scenarios)

### Scenario 1: The Retargeting Illusion

A retargeting campaign reports a 10x ROAS. It looks like the best-performing campaign in the account. But:

- The retargeting audience is built from site visitors who arrived via organic search, direct traffic, or other paid channels
- These users already had purchase intent before seeing the retargeting ad
- A holdout test reveals that 70% of them would have purchased anyway without the retargeting ad
- The *incremental* ROAS is closer to 3x — still positive, but dramatically different from the reported 10x

**Implication:** If you allocate more budget to retargeting based on the reported 10x ROAS, you are likely over-investing in a channel that is primarily claiming credit for organic demand. The incremental dollars would generate more value in prospecting.

### Scenario 2: The Brand Search Trap

A Google brand search campaign reports a 20x ROAS. Looks incredible. But:

- These are people who typed your brand name into Google. They already know who you are.
- Without the brand search ad, most of them would click the organic result directly below it
- A holdout test shows that brand search ads produce 5-15% incremental conversions — the rest would have happened organically
- You are paying for clicks that were free

**Implication:** Brand search is rarely worth significant budget. A small defensive budget to prevent competitors from bidding on your brand terms is reasonable. Scaling brand search budget based on reported ROAS is lighting money on fire.

### Scenario 3: The Great-Looking Prospecting Campaign

A Meta prospecting campaign reports a 3x ROAS on 7dc/1dv. It looks like solid prospecting performance. But:

- 60% of the attributed conversions are view-through (1dv), not click-through
- The 1dc-only ROAS is 1.2x
- A geo holdout test reveals the campaign's incremental ROAS is 1.8x
- The campaign is real but moderately over-credited by the attribution model

**Implication:** The campaign is incremental and worth running, but the true value is lower than reported. Budget allocation decisions should be based on the incremental figure, not the platform figure.

---

## Incrementality Measurement Methods

### Method 1: Geo Holdout Tests

**How it works:** Split your addressable market into test and control geographies. Run ads in the test geos and suppress ads in the control geos. Measure the difference in business outcomes (revenue, orders, new customers) between test and control.

**Strengths:**
- Gold standard for causal measurement
- Works at the campaign, channel, or total-spend level
- Does not depend on platform tracking or attribution

**Considerations:**
- Requires sufficient geographic scale (multiple DMAs or regions)
- Test duration: typically 2-4 weeks for ecommerce
- Results can be noisy for small-spend accounts
- Need clean geographic separation (no spillover)

**When to use:** Evaluating the incremental value of an entire channel (e.g., "Is our Meta spend actually driving incremental revenue?") or a significant campaign type (e.g., "Are retargeting ads incremental?").

### Method 2: Conversion Lift Tests (Platform-Native)

**How it works:** The platform (Meta, Google, etc.) randomly assigns users to test (sees the ad) and control (does not see the ad) groups and measures the conversion difference.

**Strengths:**
- User-level randomization (cleaner than geo-based)
- Easy to set up within the platform
- Platform handles the statistical analysis

**Considerations:**
- The platform is both the advertiser and the measurement tool — conflict of interest
- iOS14+ privacy changes have reduced the reliability of Meta's conversion lift studies
- Results are platform-specific and do not account for cross-channel effects

**When to use:** Quick directional reads on individual campaign incrementality. Use as a supplement to, not a replacement for, independent measurement.

### Method 3: Media Mix Modeling (MMM)

**How it works:** A statistical model that uses historical data (spend, revenue, seasonality, promotions, external factors) to estimate the contribution of each marketing channel to total revenue.

**Strengths:**
- Evaluates all channels simultaneously
- Not affected by cookie/tracking limitations
- Captures offline and long-term effects

**Considerations:**
- Requires significant historical data (12+ months ideal)
- Model quality depends on data quality and methodology
- Results are estimates with confidence intervals, not precise numbers
- Slow to update — not useful for day-to-day optimization

**When to use:** Strategic budget allocation across channels. Understanding which channels are over- or under-invested at a portfolio level.

### Method 4: Always-On Causal Analysis

**How it works:** Continuous measurement using a combination of geo-level data, synthetic controls, and statistical models to estimate ongoing incrementality without requiring constant holdout tests.

**Strengths:**
- Persistent measurement rather than point-in-time studies
- Lower operational burden than repeated holdout tests
- Can track incrementality trends over time

**Considerations:**
- Requires robust data infrastructure
- Model assumptions matter — understand the methodology
- Best used alongside periodic holdout tests for validation

**When to use:** Ongoing incrementality monitoring for mature accounts with sufficient data volume.

---

## Bridging Operational Metrics and Incrementality

The five core metrics (CPM, CTR, CVR, AOV) are your operational cockpit. Incrementality is your altimeter — it tells you whether you are actually flying or just taxiing.

### How to use both:

**Day-to-day optimization: Use the five core metrics.**
- Diagnose performance shifts using the diagnostic engine (04)
- Execute the action playbook (07) based on what the metrics tell you
- Optimize creative, targeting, and bids using platform data

**Weekly/monthly strategic review: Layer in incrementality.**
- Are the campaigns with the best platform metrics also the most incremental?
- Is retargeting actually driving value or just claiming credit?
- Are we over-invested in channels that look good on attribution but are low incrementality?

**Quarterly budget allocation: Use incrementality as the decision framework.**
- Shift budget toward channels and campaigns with the highest incremental ROAS (iROAS)
- Reduce budget on channels where platform-reported ROAS significantly exceeds incremental ROAS
- Fund holdout tests for any channel or campaign type where incrementality is unknown

---

## The iROAS (Incremental ROAS) Framework

iROAS is the metric that connects platform metrics to business reality:

**Formula:** `iROAS = Incremental Revenue / Ad Spend`

Where "Incremental Revenue" is the revenue that would not have occurred without the ad spend, as measured by a holdout test or causal model.

**How to interpret iROAS:**

| iROAS | Interpretation | Action |
|---|---|---|
| > 3.0x | Highly incremental — ads are driving significant new revenue | Scale spend. This is working. |
| 2.0x–3.0x | Moderately incremental — ads are contributing meaningful revenue | Maintain or cautiously scale. Monitor for diminishing returns. |
| 1.0x–2.0x | Marginally incremental — ads are driving some new revenue but efficiency is low | Optimize before scaling. Look for waste (non-incremental retargeting, brand search). |
| < 1.0x | Not incremental — spending more than the ads are generating in new revenue | Cut or restructure. The money is better spent elsewhere. |

**Important:** iROAS thresholds depend on margin structure. A brand with 70% gross margins can be profitable at 1.5x iROAS. A brand with 30% gross margins needs 3x+ iROAS to break even. Always calculate the breakeven iROAS based on the client's unit economics.

---

## The Confidence Interval Reality

Incrementality measurements are estimates, not precise numbers. They come with confidence intervals.

**Example:** A holdout test shows an estimated iROAS of 2.5x with a 90% confidence interval of [1.8x, 3.2x].

This means:
- We are 90% confident the true iROAS is between 1.8x and 3.2x
- The point estimate is 2.5x, but the true value could be meaningfully higher or lower
- If the breakeven iROAS is 1.5x and the lower bound is 1.8x, we can be fairly confident the campaign is profitable
- If the breakeven iROAS is 2.0x and the lower bound is 1.8x, profitability is uncertain

**Rule:** Make decisions based on the confidence interval, not just the point estimate. If the lower bound of the confidence interval is above your breakeven, proceed with confidence. If the lower bound is below breakeven, the result is inconclusive and warrants further testing.

---

## When Operational Metrics and Incrementality Disagree

| Platform Metrics Say | Incrementality Says | What Is Happening | What to Do |
|---|---|---|---|
| CPA is excellent (low) | iROAS is low | Campaign is claiming credit for conversions that would have happened anyway (attribution inflation) | Reduce spend on this campaign. Reallocate to higher-incrementality efforts. |
| CPA is mediocre | iROAS is high | Campaign is driving genuinely new customers but the attribution model under-credits it (common for upper-funnel prospecting) | Maintain or increase spend despite the "bad" CPA. The campaign is more valuable than it looks. |
| CPA is good and iROAS is good | Aligned | Rare but ideal. The campaign performs well on both operational and causal metrics. | Scale. |
| CPA is bad and iROAS is bad | Aligned | The campaign is truly underperforming on all dimensions. | Cut or dramatically restructure. |

The most dangerous quadrant is **low CPA + low iROAS** — it looks great on the dashboard but is not actually driving the business. This is where most wasted ad spend hides.

---

## Practical Incrementality Playbook

### For a New Client (Month 1-2)

1. **Audit attribution settings** across all platforms (see checklist in 08-attribution-windows.md)
2. **Compare platform-reported conversions to backend data** (Shopify, CRM, etc.). Calculate the discrepancy.
3. **Flag campaigns with high view-through conversion percentages** (>40% of attributed conversions are view-through)
4. **Identify the highest-spend campaign types** that have never been tested for incrementality
5. **Design and schedule a holdout test** for the highest-risk, highest-spend campaign type

### For an Established Client (Ongoing)

1. **Run holdout tests quarterly** on the top 2-3 campaign types by spend
2. **Maintain an iROAS tracker** that shows both platform-reported ROAS and measured iROAS for each major campaign type
3. **Use iROAS data to inform budget allocation** at the quarterly planning stage
4. **Flag any campaign where the gap between reported ROAS and iROAS exceeds 2x** for investigation

### Red Flags That Suggest Non-Incrementality

- Campaign's ROAS on 1dv is dramatically higher than on 1dc
- Retargeting campaigns with ROAS > 8x (likely over-attributed)
- Brand search with ROAS > 15x (likely capturing organic demand)
- CPA that looks "too good to be true" relative to industry benchmarks
- Total ad-attributed conversions exceed total actual orders in the backend
- Turning off a campaign produces no measurable decline in business revenue

---

## Summary

- Platform metrics are the operational layer — use them for day-to-day optimization
- Incrementality is the truth layer — use it for strategic budget allocation
- Never take platform-reported ROAS at face value for strategic decisions
- Run holdout tests to understand the true causal impact of your ad spend
- iROAS (incremental ROAS) is the north star metric for budget allocation
- Make decisions based on confidence intervals, not point estimates
- The most dangerous waste is in campaigns that look great on the dashboard but are not actually incremental

---

## Closing the Loop in Practice

The methodology in this doc is the foundation. The hard part is doing it consistently — designing tests properly, running holdouts on a cadence, integrating causal results back into the optimization workflow, and making sure the team actually changes behavior based on what the tests reveal. Most teams stop at "we ran a holdout once" instead of building incrementality into the operating cadence.

We built **[Stella](https://www.stellaheystella.com)** to close this gap: a marketing measurement platform that operationalizes incrementality and turns causal insights into actions teams can take. If you're trying to run the framework in this doc on a real account, that's what Stella exists for.
