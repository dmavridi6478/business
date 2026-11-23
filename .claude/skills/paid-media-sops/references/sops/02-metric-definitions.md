# 02 — Metric Definitions

## The Five Core Metrics (and Their Variants)

This document provides precise definitions for each core metric, what "good" looks like in context, and the critical distinctions between variants that most media buyers overlook.

---

## 1. Spend

**Definition:** The total dollar amount invested in a campaign, ad set, or ad over a given time period.

**Why it matters:** Spend is the only metric you directly control. It is the input to the entire revenue chain. All other metrics describe what happened *after* you spent the money.

**Key considerations:**

- Spend is not a performance metric — it is a decision. Evaluating "was this spend good?" requires looking at what the other four metrics did with it.
- Underspending can be as costly as overspending. If a campaign is delivering strong unit economics (low CPA, high ROAS), not scaling spend is leaving money on the table.
- Spend pacing matters. A campaign that spends its entire daily budget by 2 PM is behaving differently than one that paces evenly across the day. Rapid spend-down often signals the algorithm is finding cheap (but potentially low-quality) impressions early in the day.

**What to watch for:**

- **Spend not delivering:** The platform is struggling to find impressions within your targeting and bid constraints. This is usually a CPM or audience size issue.
- **Spend accelerating unexpectedly:** CPMs may have dropped (more impressions available at the same budget) or the algorithm found a new pocket of inventory. Check whether quality metrics (CTR, CVR) held up.
- **Spend concentrated in one ad set or ad:** The algorithm is picking winners aggressively. This is fine if performance is strong, but it can mask underexplored opportunities.

---

## 2. CPM — Cost Per Mille (Cost Per 1,000 Impressions)

**Definition:** The cost to serve 1,000 impressions of your ad.

**Formula:** `(Spend / Impressions) × 1,000`

**What it reflects:** CPM is a measure of **inventory cost** — how expensive it is to get your ad in front of people. It is determined by:

- **Auction dynamics:** How many other advertisers are competing for the same audience at the same time
- **Audience targeting:** Narrower audiences = more competition per impression = higher CPMs
- **Placement:** Instagram Stories vs. Facebook Feed vs. Audience Network all carry different CPMs
- **Seasonality:** CPMs spike during high-competition periods (Q4, Black Friday, elections)
- **Ad quality:** Platforms reward engaging ads with lower CPMs (relevance score, quality ranking)

### CPM vs. CPMr (Cost Per 1,000 Reached Users)

This distinction is critical and most media buyers ignore it.

| Metric | Formula | What It Measures |
|---|---|---|
| **CPM** | (Spend / Impressions) × 1,000 | Cost per 1,000 ad *serves* (includes repeat views to the same person) |
| **CPMr** | (Spend / Reach) × 1,000 | Cost per 1,000 *unique people* reached |

**Why the distinction matters:**

If your CPM is $15 and your CPMr is $45, that means on average each person is seeing your ad 3 times. This has major implications:

- **High frequency inflates CPM without expanding reach.** You are paying more per impression but not reaching new people.
- **Frequency fatigue degrades CTR and CVR.** After 2-3 exposures, most audiences experience diminishing returns. The ad feels stale. They stop clicking. Those who do click are less likely to convert.
- **CPMr rising while CPM is flat = frequency creep.** The algorithm is re-serving to the same people because it has exhausted the audience. This is a signal to broaden targeting or refresh creative.

**Diagnostic shortcut:**

| CPM Trend | CPMr Trend | Likely Cause | Action |
|---|---|---|---|
| Stable | Rising | Frequency creep — same people seeing ads more often | Broaden audience, refresh creative |
| Rising | Rising | Market-level CPM inflation (competition, seasonality) | Evaluate new placements, adjust bids, ride it out if seasonal |
| Rising | Stable | Impression quality shifting — more expensive placements | Check placement breakdown, exclude high-CPM placements if low-performing |
| Falling | Falling | Less competition or improved ad relevance | Monitor quality — cheaper impressions are not always better |

**Benchmarks (directional, varies by vertical and platform):**

CPM benchmarks are notoriously unreliable because they vary enormously by industry, platform, placement, geo, and time of year. Instead of chasing a benchmark, track your *own* CPM trends over time and diagnose changes using the framework above.

That said, rough ranges for context:

- **Meta (US, ecommerce):** $8–$25 typical. Q4 can spike to $35–$50+.
- **Google Display:** $2–$8 typical.
- **TikTok:** $5–$15 typical.
- **YouTube (in-stream):** $10–$20 typical.

These are approximate. Your account history is a better benchmark than industry averages.

---

## 3. CTR — Click-Through Rate

**Definition:** The percentage of impressions that result in a click.

**Formula:** `(Clicks / Impressions) × 100`

**What it reflects:** CTR measures whether your ad is earning attention. It sits at the intersection of three factors:

1. **Targeting:** Are you showing ads to people who care about this product/offer?
2. **Creative:** Is the ad itself compelling enough to stop the scroll and earn a click?
3. **Offer:** Is the value proposition clear and motivating?

**CTR is a signal of message-market fit.** A high CTR means the right message is reaching the right people. A low CTR means one (or more) of those three factors is off.

### Outbound CTR vs. All Clicks CTR

Most platforms report multiple click metrics. The distinction matters:

| Metric | What It Counts |
|---|---|
| **CTR (All Clicks)** | Every click on the ad: link clicks, profile clicks, "see more" clicks, reactions, comments, shares |
| **Outbound CTR** | Only clicks that take the user off-platform to your landing page |

**Always use Outbound CTR (or Link CTR) for performance analysis.** All-clicks CTR is inflated by engagement actions that do not drive conversions. A high all-clicks CTR with a low outbound CTR means people are engaging with the ad but not visiting the site — that is a different problem than low engagement overall.

**Diagnostic shortcut:**

| CTR (All) | Outbound CTR | Interpretation |
|---|---|---|
| High | High | Strong creative and clear CTA — people are engaging and clicking through |
| High | Low | Ad is entertaining or engaging but not driving action. The CTA is weak or the offer is unclear. |
| Low | Low | Ad is not resonating. Creative, targeting, or offer needs work. |
| Low | High | Unusual. May indicate a highly targeted audience with low volume but high intent. |

**Benchmarks (directional):**

- **Meta (ecommerce, link click CTR):** 1.0%–2.5% is solid. Below 0.8% is a flag. Above 3% is strong.
- **Google Search:** 3%–8% depending on keyword intent and position.
- **Google Shopping:** 0.5%–1.5% typical.
- **TikTok:** 0.5%–1.5% typical (platform-native creative tends to outperform).
- **YouTube (in-stream):** CTR less relevant; view rate and click-through on end screens matter more.

---

## 4. CVR — Conversion Rate

**Definition:** The percentage of clicks (or landing page views) that result in a purchase or desired action.

**Formula:** `(Conversions / Clicks) × 100` — or, more precisely, `(Conversions / Landing Page Views) × 100`

**Important distinction:** Clicks ≠ Landing Page Views. Not every click results in a page load. Users bounce mid-load, connections drop, redirects fail. If your platform reports Landing Page Views, use that as the denominator for a more accurate CVR.

**What it reflects:** CVR measures what happens *after* someone leaves the ad platform. It is influenced by:

1. **Landing page quality:** Load speed, design, clarity of the offer, trust signals, mobile experience
2. **Offer strength:** Price, promotion, product-market fit
3. **Audience intent:** Someone who clicked a retargeting ad has higher intent than someone who clicked a prospecting ad
4. **Congruence:** Does the landing page deliver what the ad promised? Mismatches between ad creative and LP content destroy CVR.

### Click-to-LP-View Drop-Off

Before diagnosing low CVR, check the click-to-landing-page-view rate:

| Clicks | LP Views | Drop-Off | Likely Cause |
|---|---|---|---|
| 1,000 | 900 | 10% | Normal. Some drop-off is expected. |
| 1,000 | 600 | 40% | Problem. Slow page load, broken redirect, or bot/accidental clicks. |
| 1,000 | 400 | 60% | Severe. Investigate page speed, tracking setup, and whether clicks are legitimate. |

If the drop-off is high, your "low CVR" problem is actually a landing page delivery problem, not a conversion problem. Fix the page load before changing anything else.

### CVR by Funnel Position

CVR varies dramatically by audience type. Always segment when diagnosing:

| Funnel Position | Typical CVR Range | Why |
|---|---|---|
| Retargeting (site visitors) | 3%–10% | High intent — they already know the brand |
| Retargeting (cart abandoners) | 5%–15% | Highest intent — they were about to buy |
| Prospecting (broad/lookalike) | 0.5%–2.5% | Low intent — they are learning about the brand for the first time |
| Prospecting (interest-based) | 1%–3% | Moderate intent — some pre-qualification from targeting |

Comparing prospecting CVR to retargeting CVR is meaningless. They are different jobs.

**Benchmarks (directional, ecommerce):**

- **Blended CVR (all traffic):** 2%–4% is solid for most ecommerce.
- **Prospecting CVR:** 1%–2% is typical. Below 0.5% is a flag.
- **Retargeting CVR:** 3%–8% is typical. Below 2% suggests the retargeting pool is low-quality or the LP has issues.

---

## 5. AOV — Average Order Value

**Definition:** The average revenue generated per conversion (purchase).

**Formula:** `Total Revenue / Total Conversions`

**What it reflects:** AOV measures the economic output of each conversion. It is influenced by:

1. **Product mix:** Which products is the campaign driving sales of?
2. **Upsell/cross-sell:** Is the checkout experience encouraging larger baskets?
3. **Offer structure:** Discounts, bundles, free shipping thresholds, BOGO
4. **Audience segment:** New customers often have lower AOV than returning customers

### Why AOV Matters for Unit Economics

AOV and CPA are the two sides of the profitability equation:

```
Profit Per Conversion = AOV - COGS - CPA
```

You can improve profitability by:
- Increasing AOV (upsells, bundles, higher-priced products)
- Decreasing CPA (better CPM, CTR, or CVR)
- Decreasing COGS (not a media buyer's lever, but worth noting)

**Critical insight:** There is a floor to how low you can push CPA. Creative and targeting optimization have diminishing returns. AOV, on the other hand, can often be improved significantly through offer structure, landing page design, and product merchandising. When CPA optimization stalls, shift attention to AOV.

### AOV by Campaign Type

| Campaign Type | AOV Behavior | Why |
|---|---|---|
| Prospecting (broad) | Often lower | New customers try entry-level products |
| Prospecting (high-value lookalikes) | Can be higher | Modeled off high-LTV customers |
| Retargeting (browse abandonment) | Varies | Depends on what they browsed |
| Retargeting (cart abandonment) | Higher | They already selected products |
| Brand search | Often highest | Returning customers buying what they know |

**What to watch for:**

- **AOV dropping over time:** The campaign may be reaching a less affluent audience, or discounting is pulling down average basket size. Check product-level data.
- **AOV spiking suddenly:** A few large orders can skew AOV. Check order count alongside revenue — a $200 AOV from 2 orders is not the same signal as a $200 AOV from 200 orders.
- **AOV varies widely across ad sets:** This tells you different ad sets are driving different product mixes. This may be intentional (if you are promoting specific products) or it may reveal that certain creatives are attracting bargain shoppers.

---

## Derived Metrics Quick Reference

These metrics are all built from the five core inputs. When any of these moves, decompose it.

| Metric | Formula | Core Inputs | What to Decompose |
|---|---|---|---|
| CPC | Spend / Clicks | CPM, CTR | If CPC rises: is CPM up, or CTR down? |
| CPA | Spend / Conversions | CPM, CTR, CVR | If CPA rises: which of the three moved? |
| ROAS | Revenue / Spend | CPM, CTR, CVR, AOV | If ROAS drops: decompose CPA and check AOV |
| MER | Total Revenue / Total Ad Spend | All (blended) | Directional only — affected by non-ad revenue |
| LTV:CAC | Customer Lifetime Value / CPA | CPA + downstream data | Requires cohort analysis, not just ad metrics |
| **CM** | **Revenue - COGS - Variable Costs - Spend** | **All + unit economics** | **The true output. See `10-contribution-margin.md`** |

> **Important:** ROAS and CPA are *correlation* metrics — they reflect what the platform *attributes* to your ads, not what your ads *caused*. This is why retargeting and brand search always show the highest ROAS: they intercept demand that already existed. Contribution margin combined with incrementality measurement is the only way to understand the true economic value of ad spend. See `10-contribution-margin.md` for the full framework.

---

## The Golden Rule

**Never troubleshoot a derived metric. Decompose it into the five core metrics and troubleshoot those.**

If someone says "CPA is too high," the correct response is: "Which of CPM, CTR, or CVR moved?" That decomposition is where the answer lives.
