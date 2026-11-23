# 03 — Time Window Framework

## How to Read Performance Across Different Time Horizons

Different time windows answer different questions. Using the wrong window for the wrong question leads to bad decisions. This document defines the three standard analysis windows, when to use each, and how they work together.

---

## The Three Lenses

| Window | Comparison | Purpose | Question It Answers |
|---|---|---|---|
| **30-Day vs. Prior 30-Day** | Last 30 days vs. preceding 30 days | Trend identification | "Is this account getting better or worse over time?" |
| **7-Day vs. Prior 7-Day** | Last 7 days vs. preceding 7 days | Recency signal | "Has something changed recently?" |
| **Day-over-Day (DoD)** | Yesterday vs. the day before (or today vs. yesterday) | Anomaly detection | "Did something break or spike today?" |

---

## 30-Day vs. Prior 30-Day: Trend Identification

**When to use:** Weekly account reviews, monthly reporting, strategic planning, evaluating the trajectory of an account.

**What it tells you:** The 30-day window smooths out daily noise and gives you a reliable read on the direction of each core metric. This is where you identify structural changes: is CPM trending up? Is CTR eroding? Is CVR improving?

**How to use it:**

1. Pull all five core metrics for the last 30 days and the prior 30 days
2. Calculate the percentage change for each metric
3. Identify which metrics moved meaningfully (>10% change in either direction warrants investigation)
4. Cross-reference with known events: did you launch new creative? Change targeting? Is there a seasonal shift?

**Example:**

| Metric | Last 30d | Prior 30d | Change |
|---|---|---|---|
| Spend | $15,000 | $15,000 | 0% (held constant) |
| CPM | $18.50 | $16.20 | +14.2% ⚠️ |
| CTR | 1.8% | 1.9% | -5.3% |
| CVR | 2.1% | 2.3% | -8.7% |
| AOV | $65 | $63 | +3.2% |

**Reading:** CPM rose 14% — this is the primary driver. CTR dipped slightly and CVR dropped almost 9%. The CPM increase means we are paying more for impressions (likely competitive pressure or audience saturation). The CVR drop could be downstream of worse impression quality (CPM up → lower-quality placements → lower-intent users → lower CVR). AOV is slightly up, which is a partial offset but not enough.

**Action:** Investigate CPM drivers (audience overlap, frequency, placement mix). Check CPMr to see if this is a frequency issue. Review CVR alongside landing page view rate to separate LP issues from audience quality.

**Pitfalls:**

- **Do not compare 30-day windows that span different seasons.** Comparing November (pre-Black Friday) to December (post-holiday) will show dramatic shifts that are seasonal, not structural.
- **Do not use 30-day windows for fast-moving decisions.** If you launched new creative 3 days ago, the 30-day window is mostly old data. Use the 7-day window.
- **Account for spend changes.** If spend increased 50% between periods, CPM may rise simply due to the platform pushing into more expensive inventory to deliver the additional budget. Normalize where possible.

---

## 7-Day vs. Prior 7-Day: Recency Signal

**When to use:** Mid-week check-ins, evaluating recent changes (new creative, new audiences, bid changes), diagnosing sudden performance shifts.

**What it tells you:** The 7-day window is your early warning system. It captures recent changes before they show up in the 30-day trend. It is sensitive enough to catch real shifts but broad enough to avoid single-day noise.

**How to use it:**

1. Pull all five core metrics for the last 7 days and the prior 7 days
2. Calculate percentage change
3. If a metric moved >15%, investigate immediately
4. Cross-reference with changes you made in the account during that period

**Example:**

| Metric | Last 7d | Prior 7d | Change |
|---|---|---|---|
| Spend | $3,500 | $3,500 | 0% |
| CPM | $17.00 | $17.20 | -1.2% |
| CTR | 2.4% | 1.7% | +41.2% ⚠️ |
| CVR | 1.8% | 2.2% | -18.2% ⚠️ |
| AOV | $62 | $64 | -3.1% |

**Reading:** CTR jumped 41% while CVR dropped 18%. This pattern is classic: a new creative (or audience change) is attracting more clicks but those clicks are lower intent. The ad is compelling but it is either reaching a broader audience (more curiosity clicks) or the creative is overpromising relative to the landing page experience.

**Action:** Check if new creative launched in the last 7 days. Review the ad-to-LP congruence. If the creative changed but the LP did not, there may be a message mismatch. Check the click-to-LP-view drop-off to rule out page load issues.

**Pitfalls:**

- **Day-of-week effects.** Seven-day windows can be skewed if one period includes a holiday or atypical day. Be aware of what days are in each window.
- **Low spend accounts.** If weekly spend is under $500, the data may not be statistically meaningful. Widen to 14-day windows for low-spend accounts.
- **Overlapping with account changes.** If you made a change on day 4, the 7-day window includes 3 days of old performance and 4 days of new. Wait for a clean 7-day window post-change before drawing conclusions.

---

## Day-over-Day: Anomaly Detection

**When to use:** Daily monitoring, when something looks "off" in the account, investigating delivery issues, catching tracking breaks.

**What it tells you:** DoD is a noise detector. Most day-to-day fluctuations are normal variance — auction dynamics shift, user behavior varies by day of week, algorithm exploration causes swings. DoD is useful for catching *anomalies* — things that are clearly outside normal variance.

**How to use it:**

1. Compare yesterday's metrics to the day before
2. Flag any metric that moved >25% in a single day
3. Before reacting, ask: "Is this within the normal range of daily variance for this account?"
4. If the swing is truly anomalous, investigate immediately (tracking break, budget issue, ad disapproval, landing page down)

**Example:**

| Metric | Yesterday | Day Before | Change |
|---|---|---|---|
| Spend | $480 | $510 | -5.9% |
| CPM | $16.80 | $17.10 | -1.8% |
| CTR | 1.5% | 1.6% | -6.3% |
| CVR | 0.4% | 2.1% | -81.0% ⚠️⚠️ |
| AOV | $58 | $64 | -9.4% |

**Reading:** CVR dropped 81% in a single day. This is almost certainly not a performance issue — it is a tracking or site issue. A real CVR decline would be gradual (10-20% over a week). An 81% single-day drop means: the site went down, the checkout broke, the tracking pixel stopped firing, or there was a payment processing issue.

**Action:** Check the site immediately. Verify the pixel is firing. Check the checkout flow. Review server logs. Do not make any ad account changes until you have confirmed the site and tracking are functioning.

**Pitfalls:**

- **Do not make strategic decisions based on DoD data.** DoD is for anomaly detection only. It is too noisy for strategic conclusions.
- **Day-of-week variance is real.** Many ecommerce brands see 20-30% swings between weekdays and weekends. Monday vs. Sunday is not a trend — it is a pattern. Know your account's weekly rhythm.
- **Low volume amplifies noise.** If a campaign gets 5 conversions per day, going from 5 to 3 is a 40% drop that means nothing statistically. DoD is most useful for accounts with meaningful daily volume (50+ conversions per day for reliable signals).

---

## How the Three Windows Work Together

The three windows form a hierarchy. Start wide, then narrow in:

### Step 1: Set the baseline with 30-day data
> "Over the last month, CPM is up 12% and CVR is down 8%. The account is trending in the wrong direction."

### Step 2: Check recency with 7-day data
> "In the last 7 days specifically, CPM jumped another 6% and CVR stabilized. The CPM increase is accelerating but the CVR issue may have been resolved by the LP changes we made last week."

### Step 3: Scan for anomalies with DoD data
> "Yesterday, everything looked normal except spend was 30% below target. Check the daily budget — it may have been accidentally reduced, or a campaign hit a spend cap."

### Decision Matrix: Which Window Drives the Action?

| Situation | Primary Window | Why |
|---|---|---|
| Monthly account review | 30-day vs. prior 30-day | Structural trend analysis |
| "Performance dropped this week" | 7-day vs. prior 7-day | Recent shift detection |
| "Something looks wrong today" | Day-over-Day | Anomaly detection (tracking, site issues) |
| Evaluating a new creative after 5 days | 7-day vs. prior 7-day | Recency (but note small sample caveat) |
| Evaluating a new creative after 3 weeks | 30-day vs. prior 30-day | Enough data for trend |
| Client asks "are we up or down?" | Start with 30-day, supplement with 7-day | Full picture with recency overlay |
| Sudden CPA spike today | DoD first (rule out anomaly), then 7-day (check trend) | Triage, then context |

---

## Time Window Hygiene

**Always compare like-for-like:**
- Same day count in each period
- Account for holidays, weekends, and known events
- Normalize for spend changes when possible

**Be explicit about your window when communicating:**
- "CPA is up 15% over the last 30 days compared to the prior 30 days" is a clear statement.
- "CPA is up" is not. Up compared to what? Yesterday? Last week? Last year?

**Never mix windows in the same analysis:**
- Do not compare a 7-day CTR to a 30-day CVR. Use the same time window for all metrics in a given analysis so the data is internally consistent.

**Document your review cadence:**
- Daily: DoD scan for anomalies (5 minutes)
- Mid-week: 7-day vs. prior 7-day check-in (15 minutes)
- Weekly: Full 30-day vs. prior 30-day review with action items (30-60 minutes)
