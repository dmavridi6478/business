# 01 — Paid Media Management Philosophy

## The Operating System for Performance Marketing

This document outlines the foundational thinking behind how we manage paid media accounts. Everything in this SOP library builds on the principles laid out here. Read this first.

---

## Core Principle: The Revenue Chain

Every dollar of ad spend flows through a single causal chain before it becomes revenue. Understanding this chain is the key to diagnosing any performance problem in any ad account on any platform.

```
Spend → Impressions → Clicks → Conversions → Revenue
```

Each link in this chain is governed by a single metric:

| Chain Link | Governing Metric | What It Tells You |
|---|---|---|
| Spend → Impressions | **CPM** (Cost Per Mille) | How much are we paying for attention? |
| Impressions → Clicks | **CTR** (Click-Through Rate) | Are we earning engagement from that attention? |
| Clicks → Conversions | **CVR** (Conversion Rate) | Are we converting that engagement into action? |
| Conversions → Revenue | **AOV** (Average Order Value) | How much value does each conversion generate? |

**Spend** is the input. It is the only lever we directly control. The other four metrics are *outcomes* that we influence through strategy, creative, targeting, and landing page optimization.

---

## Why These Five Metrics Matter

Every derived metric in paid media is just arithmetic on these five inputs:

| Derived Metric | Formula | Built From |
|---|---|---|
| CPC (Cost Per Click) | CPM / (CTR × 1,000) | CPM, CTR |
| CPA (Cost Per Acquisition) | CPC / CVR | CPM, CTR, CVR |
| ROAS (Return on Ad Spend) | (CVR × AOV) / CPA | All five |
| MER (Marketing Efficiency Ratio) | Total Revenue / Total Spend | All five (blended) |

When a CPA rises or ROAS drops, the answer is *always* hiding inside one or more of the five core metrics. We do not troubleshoot CPA directly. We decompose it and find which link in the chain broke.

This is what separates a media buyer from a button-pusher. Anyone can see that CPA went up. The job is to know *why* — and that means knowing which of the five metrics moved.

---

## Platform Agnosticism

This framework applies to every paid media platform:

- **Meta (Facebook/Instagram):** Spend → Impressions (CPM) → Clicks (CTR) → Conversions (CVR) → Revenue (AOV)
- **Google (Search, Shopping, PMax):** Same chain. Search has keyword-level CPCs, but those CPCs are still a function of CPM and CTR.
- **TikTok:** Same chain. Creative metrics layer underneath CTR (hook rate, hold rate).
- **YouTube:** Same chain. View-based metrics map to the Impressions → Clicks link.
- **Reddit, Pinterest, Programmatic, Native:** Same chain. Always.

The platform changes what tactical levers you pull. The diagnostic framework does not change.

---

## The Fault Isolation Mindset

When performance changes — up or down — the first question is always:

> "Which link in the chain moved?"

This is fault isolation. It is borrowed from engineering, and it is the most important habit a media buyer can develop. Do not start changing things until you have identified the fault.

**The diagnostic flow:**

1. Performance changed (CPA up, ROAS down, spend not delivering, etc.)
2. Pull the five core metrics for the relevant time period
3. Identify which metric(s) moved
4. Determine the cause of the movement
5. Execute the appropriate response

This flow is covered in detail in `04-diagnostic-engine.md`. The key principle here is: **diagnose before you act.**

---

## The Role of the Media Buyer

A media buyer's job is not to "run ads." It is not even to "optimize ROAS." It is to **generate incremental contribution margin** for the client's business. This requires:

1. **Allocate spend** to the highest-value opportunities — where "value" means incremental profit, not attributed revenue
2. **Diagnose** performance shifts by decomposing derived metrics into the five core inputs
3. **Execute** the correct response based on the diagnosis
4. **Measure** whether the response worked — ideally through causal measurement, not just platform-reported attribution
5. **Own the full funnel** — ads, creative, landing pages, checkout, and upsells all affect whether ad spend generates profit

The platform is a tool. The algorithm is a tool. The media buyer's value is in the *decisions* — knowing what to change, when to change it, and when to leave it alone. And those decisions should always be in service of contribution margin, not vanity metrics.

For a deep dive on why ROAS is insufficient and how to think in contribution margin terms, see `10-contribution-margin.md`.

---

## A Note on Platform-Reported Metrics vs. Reality

Platform metrics (CPA, ROAS, etc.) are reported through an attribution model chosen in the ad account settings. These numbers are useful for relative comparison and directional optimization, but they are not ground truth.

A campaign with a reported 5x ROAS might be capturing demand that would have converted anyway (non-incremental). A campaign with a reported 1.5x ROAS might be driving entirely new customers the business would never have reached (highly incremental).

This SOP library treats platform metrics as the operational layer — the dials you turn day-to-day. But we always keep one eye on the incrementality layer — whether the spend is actually driving business outcomes that would not have happened without it.

More on this in `08-attribution-windows.md` and `09-incrementality-bridge.md`.

---

## The Three Pillars of Measurement

Platform-reported attribution (MTA) is only 40% of the full picture. If you make decisions using MTA alone, you will be right less than half the time. The full measurement framework requires three pillars:

1. **MTA (40%):** Click-level attribution data from platforms and third-party tools. Good for operational optimization within a platform. Blind to impressions, view-through influence, and causation.
2. **Qualitative / Post-Purchase Surveys (20%):** Let the customers tell you where they came from and why they converted. Reveals channels MTA cannot see (word of mouth, podcasts, organic social) and objections no pixel captures.
3. **Causal Measurement (40%):** Incrementality tests, MMM, and holdout studies that answer "what would have happened without this ad?" The only way to know if spend is truly driving outcomes.

Not every client will have all three. But the goal is always to get as close to the full picture as possible. See `13-three-pillars-of-measurement.md` for the complete framework.

---

## The Weekly Optimization Discipline

We optimize accounts on a 7-day cadence, not daily. This aligns with the 7-day attribution window, the 7-day learning phase, and the need to remove emotion from decision-making. Budget changes follow a strict framework tied to performance vs. target, with a maximum 19% increase to avoid resetting the learning phase. See `12-weekly-optimization-cadence.md` for the full protocol.

---

## Summary

- There are five atomic metrics: **Spend, CPM, CTR, CVR, AOV**
- Every other metric is derived from these five
- The revenue chain (Spend → Impressions → Clicks → Conversions → Revenue) is the universal diagnostic framework
- Diagnose before you act: identify which link in the chain broke before making changes
- This framework is platform-agnostic — it works everywhere, always
- Platform metrics (MTA) are only 40% of the picture — combine with surveys and causal measurement
- Optimize weekly, not daily — respect the learning phase and remove emotion from decisions
- The job is incremental contribution margin, not ROAS
