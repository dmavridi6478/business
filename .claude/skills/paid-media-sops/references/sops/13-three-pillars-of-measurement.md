# 13 — The Three Pillars of Marketing Measurement

## MTA Is Only 40% of the Picture

No single measurement approach tells you the full truth about your marketing. Every tool has blind spots. This document defines the three pillars of measurement, what percentage of the picture each reveals, and how to combine them for the best possible decision-making — even when you don't have access to all three.

---

## The Framework

```
┌──────────────────────────────────────────────────────────────┐
│                   THE FULL PICTURE (100%)                     │
│                                                              │
│  ┌─────────────────┐                                         │
│  │  PILLAR 1: MTA   │  40% of the picture                    │
│  │  (Multi-Touch     │  Click-level data, user paths,         │
│  │   Attribution)    │  platform-reported metrics              │
│  └─────────────────┘                                         │
│                                                              │
│  ┌─────────────────┐                                         │
│  │  PILLAR 2:        │  20% of the picture                    │
│  │  QUALITATIVE      │  Post-purchase surveys, customer       │
│  │  (Surveys &       │  interviews, "how did you hear         │
│  │   Voice of        │  about us?" data                       │
│  │   Customer)       │                                        │
│  └─────────────────┘                                         │
│                                                              │
│  ┌─────────────────┐                                         │
│  │  PILLAR 3:        │  40% of the picture                    │
│  │  CAUSAL           │  Incrementality tests, MMM,            │
│  │  MEASUREMENT      │  holdout studies, geo-lift,            │
│  │                   │  causal impact analysis                │
│  └─────────────────┘                                         │
│                                                              │
│  MTA alone = right less than half the time                   │
│  MTA + Qualitative = right more than half the time (60%)     │
│  MTA + Qualitative + Causal = as close to truth as possible  │
└──────────────────────────────────────────────────────────────┘
```

---

## Pillar 1: MTA (Multi-Touch Attribution) — 40% of the Picture

### What It Is

MTA tracks user-level click paths across your marketing channels. It sees that User A clicked a Meta ad on Monday, a Google ad on Wednesday, and purchased on Friday. It assigns credit to each touchpoint based on a model (last-click, data-driven, linear, etc.).

This includes: platform-reported metrics (Meta Ads Manager, Google Ads), third-party attribution tools (Triple Whale, Northbeam, Rockerbox), Google Analytics, and any system that tracks clicks and conversions at the user level.

### What It Gets Right

- **Click-level paths:** MTA can show you the sequence of clicks that led to a purchase. This is real data about real user behavior.
- **Relative channel comparison:** Which channels are driving more clicks and conversions than others (directionally).
- **Creative and campaign performance:** Within a single platform, MTA is useful for comparing ad A vs. ad B, campaign X vs. campaign Y.
- **Real-time data:** Available immediately, no waiting for study results.

### What It Misses (The 60% It Cannot See)

- **Impressions:** MTA tracks clicks, not views. A user who saw your YouTube ad 5 times, your podcast ad 3 times, and your Instagram Story but never clicked — and then Googled your brand and purchased — gets attributed entirely to Google Search. The entire awareness journey is invisible.
- **Cross-device journeys:** User sees an ad on their phone, purchases on their laptop. MTA often cannot stitch these together.
- **View-through influence:** Platforms report view-through conversions, but these are modeled estimates, not observed click paths. And they are systematically inflated.
- **Offline and word-of-mouth:** A friend recommends your product in person. The buyer goes home and searches your brand. MTA credits the search ad, not the friend.
- **Incrementality:** MTA cannot tell you what would have happened without the ad. It tracks correlation (ad → purchase) not causation (ad *caused* purchase). This is why retargeting and brand search always look like heroes — they intercept demand that already existed.

### The Danger of MTA-Only Decision Making

**If you use MTA as your sole measurement tool, you will be right less than half the time.**

MTA systematically over-credits bottom-funnel channels (brand search, retargeting, email) and under-credits upper-funnel channels (YouTube, CTV, native, podcasts, influencers). If you allocate budget based purely on MTA, you will shift money from the channels that create demand to the channels that capture it — and total demand will shrink over time.

This is the most common way brands stall. ROAS looks great. CPA looks efficient. But revenue plateaus because you starved the top of the funnel.

---

## Pillar 2: Qualitative (Post-Purchase Surveys & Voice of Customer) — 20% of the Picture

### What It Is

Asking customers directly: How did you hear about us? Why did you buy? What almost stopped you from buying?

This is the simplest and most underused measurement tool in marketing. It requires no technology, no data science, and no statistical modeling. It just requires asking.

### What It Reveals

- **The invisible touchpoints MTA misses.** When customers say "I saw your ad on TikTok" or "a friend told me" or "I heard your podcast ad," they are telling you about channels that MTA cannot see.
- **The persuasion story.** MTA tells you *where* they clicked. Surveys tell you *why* they bought. "I saw your founder talking about the product on Instagram and it felt genuine" is insight no pixel can capture.
- **Objection data.** "What almost stopped you from buying?" reveals landing page issues, price concerns, trust gaps, and competitive weaknesses that no click data will ever show.
- **Channel discovery.** If 15% of customers say "podcast," and you are spending $0 on podcast ads, someone else's podcast is driving your sales. If 30% say "TikTok" but MTA credits 5% to TikTok, your TikTok investment is massively under-valued by MTA.

### How to Implement

**Post-purchase survey (minimum viable version):**

Add a single question to the order confirmation page or post-purchase email:

> "How did you first hear about us?"

Options (customize per client):
- Facebook / Instagram ad
- TikTok
- Google Search
- YouTube
- Friend / family recommendation
- Podcast
- Influencer / creator
- Blog or article
- Game ad (AppLovin/Axon)
- I've known about you for a while
- Other (free text)

**Enhanced version (3 questions):**

1. "How did you first hear about [brand]?" (discovery channel)
2. "What convinced you to buy today?" (persuasion trigger)
3. "Was there anything that almost stopped you from purchasing?" (objection data)

**Tools:** Fairing (formerly EnquireLabs), KnoCommerce, or a simple Shopify post-purchase survey app. Most cost $50-$200/month and are worth every penny.

### What It Gets Right

- Captures channels MTA cannot see (word of mouth, podcasts, organic social, in-store)
- Reveals the "why" behind purchasing decisions
- Provides objection data for LP and offer optimization
- Directional validation of channel investment

### What It Misses

- **Self-reported data is imperfect.** Customers do not always remember where they first saw you. They may say "Instagram" when it was actually TikTok. Recency bias favors the last touchpoint they remember, not the first.
- **Response rates are partial.** Typically 30-50% of customers answer post-purchase surveys. The non-respondents might have different channel exposure.
- **Cannot quantify incremental impact.** "15% of customers said TikTok" does not tell you the *incremental revenue* from TikTok. It tells you TikTok was part of the journey — but not whether those customers would have bought anyway without TikTok.

### Why It Is Still 20% of the Picture

Qualitative data is directional, not precise. It tells you "TikTok is part of the story" but not "TikTok drove $X in incremental revenue." Combined with MTA (which gives you the click data), you now have 60% of the picture — you know where people clicked AND where they say they were influenced. But you still do not know what is truly incremental.

---

## Pillar 3: Causal Measurement — 40% of the Picture

### What It Is

Causal measurement answers the question MTA cannot: **"What would have happened if we had not run this ad?"**

Methods include:
- **Geo holdout tests:** Suppress ads in control markets, compare revenue to test markets
- **Platform conversion lift studies:** Platform-native randomized control groups
- **Media Mix Modeling (MMM):** Statistical model estimating each channel's contribution using historical data
- **Causal impact analysis:** Statistical methods (synthetic controls, difference-in-differences) to estimate the causal effect of a marketing change
- **Always-on incrementality:** Continuous causal measurement using geo-level or audience-level holdouts

### What It Reveals

- **Whether ads actually caused conversions** (not just correlated with them)
- **The incremental value of each channel** — how much revenue would disappear if you turned it off
- **Which channels are over- and under-credited by MTA**
- **The true ROI of upper-funnel investments** (YouTube, CTV, native) that MTA systematically under-values

### What It Requires

- **Sufficient volume.** Most causal methods need meaningful conversion volume to produce statistically significant results. A brand doing 10 orders/day cannot run a reliable geo holdout.
- **Time.** Holdout tests typically run 2-4 weeks. MMM requires 12+ months of historical data. These are not real-time tools.
- **Data infrastructure.** MMM and causal impact analysis require structured data (spend, revenue, external factors by day and/or geo).
- **Willingness to sacrifice some revenue.** A holdout test means turning off ads in some markets — the brand must accept short-term revenue loss in those markets for the sake of learning.

### Who Qualifies

Not every client can run causal measurement. Here is a rough guide:

| Annual Revenue | Viable Methods | Notes |
|---|---|---|
| Under $1M | Post-purchase surveys only | Not enough volume for causal studies. Focus on Pillars 1 and 2. |
| $1M-$5M | Surveys + directional causal reads | Can attempt small-scale geo tests or on/off tests for specific channels. Results will be directional, not statistically robust. |
| $5M-$10M | Surveys + geo holdouts + basic MMM | Enough volume for meaningful holdout tests on major channels. MMM becomes feasible with 12+ months of data. |
| $10M+ | All methods | Full measurement stack: MTA + surveys + geo holdouts + MMM + always-on incrementality. |

### Directional Causal Reads for Smaller Clients

For brands in the $3-5M range, full-blown incrementality studies may not be statistically robust, but **directional reads are still valuable:**

- **On/off test for a new channel:** Turn on TikTok (or Native, or Axon, or CTV) for 4 weeks, then turn it off for 4 weeks. Compare total revenue, branded search volume, and direct traffic between the two periods. Not a clean experiment (seasonality, other changes), but directional.
- **Geo-level comparison:** If the client sells nationally, run the new channel in 5 states for 4 weeks while suppressing it in 5 similar states. Compare revenue per capita.
- **Pre/post analysis with synthetic control:** Use historical data to model what revenue "should have been" without the new channel, then compare to actual revenue with the channel running. Tools like Google's CausalImpact R package can do this.
- **Blended MER analysis:** Track total revenue / total ad spend (MER) before and after activating a new channel. If MER improves (or holds) as you add the new channel, the channel is likely additive. If MER degrades, the channel may not be incremental.

These are not the gold standard. But they are dramatically better than relying on MTA alone for channels like CTV, native, and YouTube where MTA is structurally blind.

---

## How to Use the Three Pillars Together

### The Decision Matrix

| Decision | Which Pillars to Consult | Why |
|---|---|---|
| "Should I pause this Meta campaign?" | Pillar 1 (MTA) primarily | Operational decision within a platform. MTA is sufficient for campaign-level optimization. |
| "Should we invest in TikTok?" | All three | New channel investment requires MTA (can we see any signal?), surveys (are customers mentioning TikTok?), and ideally a causal test (is TikTok actually driving incremental revenue?). |
| "Is our retargeting actually working?" | Pillar 3 primarily | MTA will always say yes. Surveys are not helpful here. Only a holdout test reveals the true incremental value of retargeting. |
| "Why did revenue drop?" | Pillar 1 + Pillar 2 | Check platform metrics for performance changes. Check survey data for shifts in how customers are finding you. |
| "How should we allocate budget across channels?" | All three | MTA gives the operational baseline. Surveys reveal hidden channel influence. Causal measurement reveals true incremental contribution. Budget allocation should weight all three. |
| "Which creative is working best?" | Pillar 1 primarily | Within-platform creative testing is MTA's strength. Hook rate, CTR, CVR by creative are reliable for comparing ads against each other. |

### When You Only Have One or Two Pillars

| What You Have | Confidence Level | How to Compensate |
|---|---|---|
| MTA only | Low (~40%) | You will over-credit bottom funnel and under-credit top funnel. Hedge by not cutting upper-funnel channels even if MTA says they are underperforming. |
| MTA + Surveys | Moderate (~60%) | Better. Surveys correct MTA's biggest blind spot (invisible touchpoints). You can now identify which channels are under-credited. Still cannot quantify incrementality precisely. |
| MTA + Surveys + Causal | High (~80-90%) | The best available picture. You know what people clicked (MTA), what they say influenced them (surveys), and what actually caused the sale (causal). Nothing is 100%, but decisions made with all three are dramatically better. |
| Surveys only | Low (~20%) | Directional at best. Know what customers say but cannot see the data. Not sufficient for optimization decisions. |
| Causal only | Moderate (~40%) | Tells you what works incrementally but not the operational detail of which campaigns, creatives, and audiences within a channel are performing. |

---

## Where Each Pillar Lives in Our Workflow

### Pillar 1 (MTA) — Daily/Weekly

MTA data is what we use for day-to-day and weekly optimization. Pull it every optimization day (see `12-weekly-optimization-cadence.md`). It informs:
- Budget changes (the weekly framework)
- Creative decisions (what is working, what is fatiguing)
- Campaign structure decisions (consolidate, expand, pause)

### Pillar 2 (Surveys) — Weekly/Monthly

Review post-purchase survey results weekly or biweekly. Look for:
- Channel mentions that do not align with MTA (e.g., customers saying "podcast" but MTA shows 0% podcast attribution)
- Shifts in how customers are discovering the brand
- Objection data that informs creative or LP changes
- Store survey results in the client's GitHub folder (`clients/[name]/post-purchase-survey-results/`)

### Pillar 3 (Causal) — Monthly/Quarterly

Run or review causal measurement on a monthly or quarterly basis. This informs:
- Channel budget allocation (shift money toward highest incremental CM channels)
- Validation of MTA-based decisions (is what MTA says aligning with causal results?)
- New channel evaluation (was the TikTok test actually incremental?)

---

## How This Connects to the SOP Framework

| SOP Concept | Three Pillars Connection |
|---|---|
| **Philosophy** (01) | The five core metrics are Pillar 1 (MTA). This doc adds Pillars 2 and 3 as essential context for strategic decisions. |
| **Attribution Windows** (08) | Attribution windows are a Pillar 1 concern. Different windows change MTA's answer but do not change the causal truth. |
| **Incrementality Bridge** (09) | The incrementality bridge IS Pillar 3. This doc frames it within the broader measurement context. |
| **Contribution Margin** (10) | All three pillars should ultimately be evaluated in CM terms. Survey data informs the "why." Causal measurement validates the "how much." |
| **Weekly Optimization** (12) | Weekly optimization uses Pillar 1 for operational decisions. Pillars 2 and 3 inform the quarterly strategic review. |

---

## Operationalizing the Three Pillars

The framework above describes *what* the three pillars are. Running them in practice is where most teams break down — Pillar 1 (MTA) is the only one most teams have systematic infrastructure for, while Pillars 2 (Surveys) and 3 (Causal) get treated as one-off projects rather than recurring inputs.

We built **[Stella](https://www.stellaheystella.com)** to operationalize Pillars 2 and 3 alongside Pillar 1: a marketing measurement platform that handles post-purchase surveys, causal measurement (holdouts, geo lifts, MMM), and feeds the results back into the optimization workflow on a cadence — so the three pillars stop being three separate projects and become one connected system.
