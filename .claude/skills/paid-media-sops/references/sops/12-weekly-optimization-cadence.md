# 12 — Weekly Optimization Cadence and Budget Management

## The 7-Day Rhythm: Why We Optimize Weekly, Not Daily

This document defines how and when we make changes to ad accounts. The core principle: **we optimize on a 7-day cadence, not daily.** Every budget change, creative swap, and targeting adjustment follows a disciplined weekly rhythm designed to work with the platform's learning phase rather than against it.

---

## Why Weekly, Not Daily

Three platform realities drive this cadence:

**1. Attribution windows are 7 days.** Meta's default attribution is 7-day click. A conversion that happens on day 6 after a click will not appear in your data until day 6. If you make a decision on day 2 based on what you see, you are missing 5 days of conversion data that has not yet materialized. You are making decisions on incomplete information.

**2. The learning phase needs 7 days.** Meta (and TikTok) need approximately 50 conversion events in a 7-day window to exit the learning phase. Every significant change (budget, audience, creative) resets or disrupts learning. Making changes every 2-3 days means the algorithm never stabilizes — it is perpetually learning and never optimizing.

**3. Emotions are the enemy of optimization.** When a business owner manages their own account, they check it daily, see a bad day, panic, and make changes. Then the next day looks worse (because the change reset learning), so they change again. This spiral is the single most common way accounts get destroyed. The 7-day cadence removes emotion from the process. You evaluate a full week of data, make a deliberate decision, and then leave it alone for another week.

**Exception cases exist** (see section below), but the default is weekly.

---

## The Budget Change Framework

When it is time to make a weekly optimization (once per week, same day each week), use this framework to determine budget changes:

### The Rules

| Performance vs. Target | Action | Why |
|---|---|---|
| **Within +/-10% of target CPA/ROAS** | Increase spend by 10% | Performance is on target. Reward it with modest growth. A 10% increase will not shock the system. |
| **Below target by 0-10%** (CPA slightly above target, or ROAS slightly below) | Keep spend the same | Performance is close but not quite there. Do not punish it — give it another week to settle. Small fluctuations are normal. |
| **Above target by 11%+** (CPA well below target, or ROAS well above) | Increase spend by 19% | Performance is strong. Scale more aggressively — but still under the 20% threshold that risks resetting the learning phase. 19% is deliberate: it is the maximum change you can make without significant learning disruption. |
| **Below target by 11-20%** (CPA moderately above target) | Keep spend the same | Performance is soft but not alarming. Do not cut yet — investigate the cause first (creative fatigue? CPM spike? LP issue?). Use the diagnostic engine (04). Give it one more week while you prepare a fix. |
| **Below target by 20%+** (CPA significantly above target) | Reduce spend by 10% | Performance has genuinely degraded. A modest 10% cut signals to the algorithm to tighten up without causing a drastic reset. Simultaneously investigate and address the root cause. |

### Why These Specific Thresholds

**Why 10% increases, not 20% or 50%:** The platforms' learning algorithms are sensitive to budget changes. Meta's documentation warns that changes greater than 20% can reset the learning phase. Staying at 10-19% keeps you under that threshold while still growing spend meaningfully. Over 4-6 weeks of consistent 10% increases, you are doubling the budget — that is aggressive growth, just done responsibly.

**Why 19% max increase:** This is the maximum change that stays safely under the learning phase reset threshold. At 20%, you risk triggering a reset. At 19%, you are pushing the boundary but staying safe. The 1% difference matters.

**Why only 10% decreases:** Cutting budget aggressively (30-50%) is just as disruptive as increasing it aggressively. A 10% cut is enough to signal a pullback without shocking the system. If performance continues to degrade the following week, cut another 10%. Gradual is always better than sudden.

**Why we keep spend the same in the -10% to -20% range instead of cutting:** Because the cause of the underperformance matters more than the symptom. If CPM spiked because of seasonal competition, cutting budget will not fix the CPM — it will just reduce your volume while the underlying issue persists. Diagnose first, then act. Cutting budget is a response to sustained underperformance after the diagnosis has been addressed, not a first reaction.

### Visualization of the Framework

```
                    Performance vs. Target (7-day comparison)
                    
     ◄── Underperforming ──────────── On Target ──────────── Outperforming ──►
     
     -20% or worse     -11% to -20%    -10% to +10%    +11% or better
          │                  │                │                │
          ▼                  ▼                ▼                ▼
     Reduce 10%        Hold steady      Increase 10%    Increase 19%
     + Diagnose        + Investigate     (steady growth)  (accelerate)
     the cause         the cause
```

---

## The Weekly Optimization Process

### What Day to Optimize

Pick one day per week and stick to it. We recommend **Monday or Tuesday** — this gives you a full 7-day window (Mon-Sun or Tue-Mon) and aligns with the start of most business reporting cycles.

**Do not optimize on different days each week.** The point is consistency. The algorithm needs a stable 7-day rhythm.

### The Weekly Checklist

Every optimization day, for each client:

**Step 1: Pull 7-day vs. prior 7-day data (5 minutes)**
- Pull all five core metrics: Spend, CPM, CTR, CVR, AOV
- Calculate CPA and ROAS for the current 7-day window
- Compare to the prior 7-day window and to the target

**Step 2: Diagnose any significant changes (10 minutes)**
- If any core metric moved >15%, use the diagnostic engine (04) to identify the cause
- Check frequency and CPMr for creative fatigue signals
- Check the search term report (Google) for query drift
- Check creative performance for fatigue (declining CTR, rising frequency)

**Step 3: Determine the budget action (2 minutes)**
- Apply the budget change framework above
- Document the decision and the reasoning

**Step 4: Make creative decisions (5 minutes)**
- Are any creatives fatiguing? (CTR down 15%+ from peak, frequency > 3.0)
- Are there new creatives ready to launch?
- Schedule creative refreshes — do not launch new creative AND change budget in the same week if possible. One variable at a time.

**Step 5: Execute changes (5 minutes)**
- Make the budget change
- Launch or pause creatives as decided
- Do NOT touch anything else until next week's optimization

**Step 6: Run /finish-session (2 minutes)**
- Log everything in the session notes

**Total time per client: 20-30 minutes per week**

---

## Exception Cases: When to Break the Weekly Cadence

The 7-day rhythm is the default. These are the situations where faster action is justified:

### Emergency Exceptions (Act Immediately)

| Situation | Action | Why Weekly Rules Don't Apply |
|---|---|---|
| **Site/checkout is broken** | Pause all spend immediately | Every dollar spent is wasted if people cannot buy |
| **Tracking/pixel broke** | Pause conversion campaigns or fix immediately | The algorithm is optimizing on bad data |
| **Ad account suspended or billing failed** | Fix immediately | Ads are not running at all |
| **CPA doubled overnight (DoD)** | Investigate immediately (but do not change budget yet) | Likely a technical issue, not a performance issue. Fix the cause, not the budget. |

### Planned Exceptions (Accelerate on a Schedule)

| Situation | How to Handle |
|---|---|
| **BFCM / Major sale event** | Treat as a separate operating mode. Pre-set budgets and bid adjustments before the event. During BFCM, you may optimize daily — this is essentially "day trading." Set seasonality adjustments in Google. Return to weekly cadence after the event. |
| **Product launch / Movie release / Time-sensitive push** | Pre-scale budgets 7-14 days before the launch to build audience data. During the launch window (3-7 days), you may increase budgets more aggressively (20-30%) if performance supports it. The client's timeline overrides the weekly cadence, but communicate the risk. |
| **New campaign launch** | Give it a full 7-14 days before evaluating. Do not touch it. The learning phase needs uninterrupted time. |
| **Client requests an immediate change** | If the client asks for a budget cut or increase outside the weekly cadence, explain the learning phase risk. If they insist, make the change and document that it was client-directed. |

### BFCM: The Exception to Everything

Black Friday / Cyber Monday is a fundamentally different operating environment. For the 5-7 day window around BFCM:

- Daily optimization is acceptable
- Budget increases of 50-100%+ may be appropriate
- Creative refresh cadence compresses to daily
- Seasonality adjustments should be pre-set in Google (see `platforms/google/advanced-operations.md`)
- The goal shifts from "steady efficiency" to "capture maximum demand while it exists"
- After BFCM, return to weekly cadence immediately. Do not let the BFCM intensity become the new normal.

---

## Budget Management in the Context of Client Constraints

### Scenario 1: Fixed Budget Client

The client gives you a set monthly budget (e.g., $10,000/month) with no flexibility. Your weekly optimization adjusts spend within that ceiling.

**How to handle:**
- Calculate the daily target: $10,000 / 30 = $333/day
- Weekly budget target: $333 × 7 = $2,333/week
- Apply the budget change framework within the weekly target
- If performance is strong and you hit the monthly ceiling early, you cannot scale further — communicate this to the client as a missed opportunity

### Scenario 2: Performance-Based Budget (Preferred)

The client allows budget to grow as long as incremental contribution margin targets are met. No fixed ceiling.

**How to handle:**
- Set a CPA or ROAS target tied to contribution margin
- Apply the budget change framework weekly
- As long as performance is within target, budget grows 10-19% per week
- Over 8 weeks of consistent 10% increases: budget doubles
- This is the ideal client relationship — you are a growth partner, not a vendor spending a fixed allocation

### Scenario 3: Hybrid

The client has a soft budget range ($8K-$15K/month) with flexibility to exceed it if results justify it.

**How to handle:**
- Start at the lower end of the range
- Scale using the weekly framework
- When approaching the upper end, proactively show the client the data: "We are at $14K this month. Performance is hitting X ROAS / $Y CPA. Based on the trend, we recommend going to $18K next month. Here is the incremental CM projection."
- Let the data make the case for more budget, not your salesmanship

---

## What This Cadence Produces Over Time

The discipline of weekly optimization compounds. Here is what consistent 10% weekly budget increases look like:

| Week | Weekly Budget (starting at $2,000/week) |
|---|---|
| Week 1 | $2,000 |
| Week 2 | $2,200 (+10%) |
| Week 3 | $2,420 |
| Week 4 | $2,662 |
| Week 8 | $3,897 (~2x starting) |
| Week 12 | $5,706 (~2.85x starting) |
| Week 16 | $8,354 (~4.2x starting) |

In 16 weeks (4 months) of disciplined 10% weekly increases, you have quadrupled the budget — and done so without ever resetting the learning phase or shocking the algorithm. Every week the algorithm had stable conditions to optimize within, and every week you scaled just enough to grow without breaking what was working.

**This is how accounts scale profitably.** Not by doubling budget overnight. By compounding small, disciplined increases that the algorithm can absorb.

---

## How This Connects to the SOP Framework

| SOP Concept | Weekly Cadence Connection |
|---|---|
| **Time Windows** (03) | The 7-day vs. prior 7-day comparison is the primary window for weekly optimization. 30-day is for monthly reviews. DoD is for anomaly detection only. |
| **Diagnostic Engine** (04) | Every weekly optimization starts with a diagnostic check. Budget decisions follow the diagnosis, not the other way around. |
| **Metric Interactions** (06) | When scaling budget, expect the scale tax (CPM ↑, CTR ↓, CVR ↓). The 10% increment minimizes this. Monitor marginal CPA. |
| **Action Playbook** (07) | The playbook actions are executed within the weekly cadence. One change per week. Diagnose → decide → execute → wait 7 days → evaluate. |
| **Creative Volume** (11) | Creative refreshes should be staggered with budget changes. Do not launch 10 new creatives AND change budget in the same week. One variable at a time. |
| **Contribution Margin** (10) | Budget scaling decisions should ultimately be validated against contribution margin, not just platform ROAS. The weekly review is where you check whether scaling is still profitable. |
