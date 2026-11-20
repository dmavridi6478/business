# 04 — Diagnostic Engine

## Identifying What Broke and Why

This is the core operational document. When performance changes, this is where you come to figure out what happened and what to do about it.

---

## The Diagnostic Flow

```
Performance changed
       │
       ▼
Pull the 5 core metrics (CPM, CTR, CVR, AOV + Spend)
for the appropriate time window (see 03-time-windows.md)
       │
       ▼
Which metric(s) moved?
       │
       ├── CPM moved ──────────► Section 1
       ├── CTR moved ──────────► Section 2
       ├── CVR moved ──────────► Section 3
       ├── AOV moved ──────────► Section 4
       ├── Multiple moved ─────► Section 5
       └── None moved ─────────► Section 6
```

---

## Section 1: CPM Moved

### CPM Increased

**Decision Tree:**

```
CPM is up
    │
    ├── Is CPMr also up?
    │      │
    │      ├── YES → Market-level inflation
    │      │         • Auction competition increased (seasonal, new competitors)
    │      │         • You are reaching new people, but they cost more
    │      │         • Action: Check placement breakdown, test new placements,
    │      │           evaluate if the cost increase is sustainable given CPA
    │      │
    │      └── NO → Frequency creep
    │               • You are paying more per impression but NOT reaching new people
    │               • The algorithm is re-serving to exhausted audiences
    │               • Action: Check frequency metrics, broaden targeting,
    │                 refresh creative, exclude high-frequency audiences
    │
    └── Did you change targeting or budget recently?
           │
           ├── YES → The change pushed you into more expensive inventory
           │         • Broader audiences can paradoxically raise CPM if they
           │           include premium placements the algorithm wants to explore
           │         • Higher budgets force the algorithm into more expensive
           │           auction slots to spend the money
           │         • Action: Monitor for 3-5 days. If CPM stabilizes at the
           │           new level but CPA is still acceptable, this may be fine.
           │
           └── NO → External factor
                    • Competitor activity, seasonal demand, platform algorithm change
                    • Action: Check industry CPM trends, review auction insights
                      (if available), evaluate alternative placements or platforms
```

### CPM Decreased

A CPM decrease is not always good news. Investigate:

- **Did placement mix shift?** Cheaper placements (Audience Network, right column) often have lower CPMs but also lower intent. Check CTR and CVR alongside the CPM drop.
- **Did quality degrade?** Lower CPMs can mean the algorithm is buying cheaper, lower-quality impressions. If CTR and CVR also dropped, the "savings" on CPM are costing you on performance.
- **Seasonal softening?** Post-holiday CPM drops are normal. Take advantage by testing new audiences while inventory is cheap.

---

## Section 2: CTR Moved

### CTR Decreased

**Decision Tree:**

```
CTR is down
    │
    ├── Did creative change recently?
    │      │
    │      ├── YES → New creative is underperforming
    │      │         • The new ads are not resonating with the audience
    │      │         • Action: Compare CTR of new vs. old creative directly.
    │      │           If old creative was stronger, revert or iterate.
    │      │           Check hook rate if video (see 05-creative-metrics.md).
    │      │
    │      └── NO → Creative fatigue or audience shift
    │
    ├── Has frequency increased?
    │      │
    │      ├── YES → Creative fatigue
    │      │         • The audience has seen these ads too many times
    │      │         • Action: Introduce new creative variations.
    │      │           Do not just change the thumbnail — change the hook,
    │      │           the angle, or the format entirely.
    │      │
    │      └── NO → Audience or offer issue
    │
    ├── Did targeting change?
    │      │
    │      ├── YES → New audience is less responsive
    │      │         • Broader audiences often have lower CTR because they
    │      │           include less-interested people. This is expected.
    │      │         • Action: Check if CVR held. Lower CTR + stable CVR
    │      │           at scale is often acceptable. Lower CTR + lower CVR
    │      │           means the audience is wrong.
    │      │
    │      └── NO → Continue diagnosis
    │
    └── Check outbound CTR vs. all-clicks CTR
           │
           ├── Outbound CTR down, all-clicks stable → CTA is weak
           │   • People are engaging with the ad but not clicking through
           │   • Action: Strengthen the CTA. Make the next step obvious.
           │
           └── Both down → Creative is not stopping the scroll
               • Action: Test new hooks, new formats, new first frames.
                 See 05-creative-metrics.md for video-specific diagnosis.
```

### CTR Increased

Check whether the increase is productive:

- **CTR up + CVR stable or up = genuine improvement.** More people clicking AND converting. Scale spend.
- **CTR up + CVR down = curiosity clicks.** The creative is attracting attention but not the right kind. The ad may be overpromising, or the new audience is lower intent.
- **CTR up + CPM up = the algorithm is chasing engagement.** If CPA held, this is fine. If CPA rose, the higher CTR is not compensating for the higher CPM.

---

## Section 3: CVR Moved

### CVR Decreased

**Decision Tree:**

```
CVR is down
    │
    ├── Check click-to-LP-view drop-off first
    │      │
    │      ├── Drop-off increased (>20% of clicks not reaching LP)
    │      │   • This is NOT a conversion problem — it is a delivery problem
    │      │   • Action: Check page load speed (target <3 seconds).
    │      │     Check for broken redirects. Check mobile experience.
    │      │     Verify tracking pixel placement.
    │      │
    │      └── Drop-off is normal (<15%)
    │          • Proceed to LP and audience diagnosis
    │
    ├── Did the landing page change?
    │      │
    │      ├── YES → LP change is the likely cause
    │      │         • Action: A/B test old vs. new LP if possible.
    │      │           Check if the change affected mobile specifically
    │      │           (most ad traffic is mobile).
    │      │
    │      └── NO → Continue diagnosis
    │
    ├── Did the audience or targeting change?
    │      │
    │      ├── YES → New audience is lower intent
    │      │         • Broader prospecting audiences naturally have lower CVR
    │      │         • Action: Segment CVR by campaign type (prospecting vs.
    │      │           retargeting). If prospecting CVR dropped but retargeting
    │      │           held, the prospecting audience needs refinement.
    │      │
    │      └── NO → Continue diagnosis
    │
    ├── Is the decline across all campaigns or specific ones?
    │      │
    │      ├── ALL campaigns → Site-wide issue
    │      │   • Checkout broken, payment processor down, promo expired,
    │      │     site speed degraded, trust signals removed
    │      │   • Action: Check the site. Go through the full checkout flow
    │      │     yourself. On mobile. Right now.
    │      │
    │      └── SPECIFIC campaigns → Campaign-level issue
    │          • Creative-to-LP mismatch, audience quality, offer relevance
    │          • Action: Review the specific campaign's targeting, creative,
    │            and LP alignment.
    │
    └── Check if CVR dropped suddenly (DoD) or gradually (7d/30d)
           │
           ├── Sudden (DoD) → Technical issue or external event
           │   • Tracking break, site outage, major competitor sale, bad press
           │   • Action: Rule out technical issues first. Always.
           │
           └── Gradual (7d/30d) → Audience fatigue or market shift
               • The same audience is being re-served and has already decided
               • Action: Refresh offers, test new landing pages,
                 expand audience pools
```

### CVR Increased

Verify the increase is real and sustainable:

- **Did AOV drop?** A discount or lower-priced product promotion can boost CVR while reducing revenue per conversion. Check net impact on CPA and ROAS.
- **Did the audience narrow?** Retargeting-heavy spend naturally shows higher CVR. If prospecting spend decreased as a proportion, the blended CVR rise is artificial.
- **LP improvement?** If you made site changes, this may be a genuine win. Monitor for 14+ days to confirm it holds.

---

## Section 4: AOV Moved

### AOV Decreased

```
AOV is down
    │
    ├── Check product-level data
    │      │
    │      ├── Campaign is driving sales of lower-priced products
    │      │   • The creative or audience is attracting bargain shoppers
    │      │   • Action: If this is intentional (entry-point product strategy),
    │      │     monitor LTV of these customers. If unintentional, adjust
    │      │     creative to feature higher-value products.
    │      │
    │      └── Same product mix, lower prices
    │          • Discounting is pulling down AOV
    │          • Action: Evaluate whether the volume increase from the discount
    │            offsets the margin hit. Calculate revenue impact, not just CVR.
    │
    ├── Check audience segments
    │      │
    │      ├── New customer AOV lower than returning customer AOV
    │      │   • This is normal and expected. New customers test with smaller
    │      │     orders. The question is whether they come back.
    │      │   • Action: Track cohort LTV. If first-order AOV is low but
    │      │     repeat rate is strong, this is fine.
    │      │
    │      └── AOV declining across all segments
    │          • Broad market softening, or offer structure needs adjustment
    │          • Action: Test bundles, free shipping thresholds, minimum order
    │            incentives. Review upsell/cross-sell flows on site.
    │
    └── Is AOV decline offset by CVR increase?
           │
           ├── YES → Total revenue may be stable or up
           │         • More conversions at lower value can equal more total revenue
           │         • Action: Check total revenue and margin. If margin held,
           │           this is acceptable. If margin eroded, address pricing.
           │
           └── NO → Revenue declining
                    • Both fewer dollars per order AND no volume offset
                    • Action: This needs immediate attention. Review offer,
                      product mix, and audience quality simultaneously.
```

### AOV Increased

- **Fewer but larger orders?** If conversion count dropped while AOV rose, you may be losing volume customers. Check total revenue, not just AOV.
- **Upsell working?** If conversion count held and AOV rose, something on-site is working. Identify what changed and double down.
- **Outlier orders?** A handful of large orders can spike AOV. Check median order value alongside AOV for a more robust signal.

---

## Section 5: Multiple Metrics Moved

When two or more metrics shift simultaneously, the question is: which is the *root cause* and which is the *downstream effect*?

### Common Multi-Metric Patterns

| Pattern | Root Cause | Downstream Effect | Interpretation |
|---|---|---|---|
| CPM ↑, CTR ↓ | Audience saturation | Fatigued users click less | Refresh creative and/or broaden targeting |
| CPM ↑, CVR ↓ | Higher CPMs buying lower-quality impressions | Less-qualified traffic converts less | Check placement mix; exclude low-quality placements |
| CTR ↑, CVR ↓ | Creative change attracting broader audience | More curious (but less intent) clicks | Tighten creative messaging to qualify clicks better |
| CTR ↓, CVR ↑ | Fewer but more qualified clicks | Only high-intent users are clicking | If CPA improved, this is fine. If volume is too low, loosen creative. |
| CPM ↓, CTR ↑ | Better ad relevance OR cheaper placements | Algorithm rewarding engaging ads | Verify quality — check if CVR held. If so, scale. |
| CVR ↓, AOV ↓ | Site-wide issue or audience degradation | Both fewer conversions and lower value per conversion | Urgent. Check site first, then audience quality. |
| CTR ↑, AOV ↓ | Creative attracting deal-seekers | Lower-intent traffic buys cheaper items | Adjust creative to feature hero products, not just deals. |

### The Root Cause Rule

When multiple metrics move, look for the metric that is *earliest in the chain* (Spend → CPM → CTR → CVR → AOV). That is most likely the root cause, and metrics later in the chain are downstream effects.

**Example:** CPM rose 20% and CVR dropped 15%. The root cause is likely CPM — the algorithm is buying more expensive (and potentially lower-quality) impressions, which is degrading the quality of traffic reaching the site. Fix the CPM issue first; CVR may self-correct.

**Exception:** If a metric later in the chain changed due to an independent cause (e.g., the site team changed the checkout flow, crashing CVR), it is not downstream of CPM. Always cross-reference with known changes before assuming causality.

---

## Section 6: No Core Metric Moved (But Performance Changed)

If CPA or ROAS shifted but the five core metrics are stable, check:

1. **Attribution window changed.** Did someone change the reporting settings from 7dc/1dv to 1dc? This can dramatically shift reported CPA/ROAS without any real performance change. See `08-attribution-windows.md`.
2. **Conversion lag.** Some platforms report conversions with a delay. A "CPA spike" today might resolve tomorrow as conversions come in.
3. **Mix shift.** If you are looking at blended metrics across multiple campaigns, the mix of spend between high-CPA and low-CPA campaigns may have shifted even though individual campaign metrics are stable.
4. **External attribution data.** If you are looking at analytics (GA4, etc.) alongside platform data, discrepancies in attribution methodology can create phantom performance shifts.

---

## Scenario Walkthroughs

### Scenario 1: "CPA doubled overnight"

**Step 1: DoD check (anomaly detection)**

Yesterday's metrics vs. day before:

| Metric | Yesterday | Day Before | Change |
|---|---|---|---|
| Spend | $520 | $500 | +4% |
| CPM | $17.00 | $16.50 | +3% |
| CTR | 1.6% | 1.7% | -6% |
| CVR | 0.3% | 2.1% | -86% ⚠️ |
| AOV | $55 | $62 | -11% |

**Diagnosis:** CVR collapsed 86% in one day. CPM and CTR are essentially flat. This is not a media issue — this is a site or tracking issue.

**Action sequence:**
1. Check the website — is the checkout functional? Test it yourself on mobile.
2. Check the pixel — is it firing on the conversion page? Use the platform's pixel helper or check real-time events.
3. Check the payment processor — any outages or errors?
4. Check for site changes — did the dev team push a new build? Did a plugin update break something?

**Resolution:** The checkout page had a JavaScript error introduced in a site update at 11 PM the previous night. Mobile users could not complete purchase. Dev team rolled back the change. CVR returned to normal the next day.

**Lesson:** When CVR drops more than 50% in a single day, check the site before touching the ad account.

---

### Scenario 2: "ROAS has been declining for 3 weeks"

**Step 1: 30-day review**

| Metric | Last 30d | Prior 30d | Change |
|---|---|---|---|
| Spend | $20,000 | $20,000 | 0% |
| CPM | $22.50 | $18.00 | +25% ⚠️ |
| CTR | 1.4% | 1.8% | -22% ⚠️ |
| CVR | 1.9% | 2.0% | -5% |
| AOV | $68 | $66 | +3% |

**Step 2: 7-day check**

| Metric | Last 7d | Prior 7d | Change |
|---|---|---|---|
| CPM | $24.00 | $21.50 | +12% |
| CTR | 1.2% | 1.5% | -20% |

**Diagnosis:** Two metrics moved: CPM is up significantly and CTR is declining. CVR and AOV are essentially stable. The 7-day data shows the trend is *accelerating* — CPM continues to rise and CTR continues to fall.

This is a classic **audience saturation + creative fatigue** pattern. The algorithm has exhausted the current audience (driving CPM up via frequency) and the creative has been seen too many times (driving CTR down).

**Check:** Pull CPMr and frequency data.
- CPMr: Up 40% over 30 days (confirming some frequency, but also genuine CPM inflation)
- Frequency: 3.8 over the last 30 days (up from 2.4 in the prior period)

**Action sequence:**
1. **Immediate (Day 1):** Launch 3-5 new creative variations with different hooks and angles. Do not just swap images — change the message.
2. **Short-term (Day 2-3):** Expand audience targeting. If running interest-based, test broad. If running lookalikes, test new seed audiences. If running broad, test new geos or demographics.
3. **Medium-term (Week 2):** Monitor CPM and CTR in the 7-day window. If CPM stabilizes with new audiences and CTR recovers with new creative, the issue is resolved.
4. **If CPM stays elevated despite audience expansion:** This may be market-level inflation (Q4, competitive pressure). Evaluate whether the account can sustain the higher CPMs or if budget should be reallocated to lower-CPM platforms/placements.

---

### Scenario 3: "CTR is great but we're not getting conversions"

**Step 1: 7-day review**

| Metric | Last 7d | Prior 7d | Change |
|---|---|---|---|
| Spend | $5,000 | $5,000 | 0% |
| CPM | $14.00 | $14.50 | -3% |
| CTR | 2.8% | 1.6% | +75% ⚠️ |
| CVR | 0.8% | 2.1% | -62% ⚠️ |
| AOV | $70 | $68 | +3% |

**Diagnosis:** CTR spiked and CVR cratered — the inverse relationship is stark. New creative launched 6 days ago that is getting significantly more clicks, but those clicks are not converting.

**Deeper investigation:**
- Click-to-LP-view rate: 92% (normal — people are reaching the page)
- LP bounce rate: 68% (up from 45% in the prior period)
- Time on page: Down 40%

**Diagnosis refined:** People are clicking through and landing on the page, but they are bouncing quickly. The creative is setting an expectation that the landing page is not meeting. This is a **congruence problem**.

**Action sequence:**
1. Review the new creative side-by-side with the landing page. What does the ad promise? What does the LP deliver?
2. If the creative promises a specific offer, discount, or benefit, ensure it is above the fold on the LP.
3. Test a dedicated LP that matches the new creative's message.
4. If you cannot change the LP quickly, revert to the old creative and iterate on new concepts that align with the existing LP.

---

### Scenario 4: "We scaled budget 50% and CPA got worse"

**Step 1: 7-day review (post-scale vs. pre-scale)**

| Metric | Post-Scale 7d | Pre-Scale 7d | Change |
|---|---|---|---|
| Spend | $7,500 | $5,000 | +50% (intentional) |
| CPM | $21.00 | $17.00 | +23.5% ⚠️ |
| CTR | 1.5% | 1.7% | -12% |
| CVR | 1.8% | 2.0% | -10% |
| AOV | $64 | $65 | -1.5% |

**Diagnosis:** All three efficiency metrics degraded: CPM +23%, CTR -12%, CVR -10%. This is the **scale tax** — when you increase budget, the algorithm must push into more expensive inventory and broader audiences to spend the additional dollars.

This is expected. The question is: **is the marginal CPA acceptable?**

**Calculation:**
- Pre-scale CPA: ~$28.50
- Post-scale CPA: ~$38.90
- Marginal CPA (cost of the incremental conversions from the budget increase): ~$55.60

**Action sequence:**
1. Calculate the marginal CPA (not just the blended CPA). If the marginal CPA is within the brand's target CAC, continue scaling.
2. If the marginal CPA is too high, scale back to the original budget and find efficiencies first — new creative, new audiences, better LP — before attempting to scale again.
3. Consider scaling in 15-20% increments rather than 50%. Smaller increases give the algorithm time to learn without forcing it into poor inventory.
4. Check if the CPM increase is uniform across placements or concentrated in one. You may be able to scale on high-efficiency placements while capping low-efficiency ones.
