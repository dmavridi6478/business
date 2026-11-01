# Meta (Facebook & Instagram) — How the Algorithm Works

## Official Sources and Last Updated

This document is sourced primarily from Meta's official engineering blog, Meta for Business announcements, and Meta AI research publications. Key sources:

- [Meta Andromeda Engineering Blog](https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/) (Dec 2024)
- [AI Innovation in Meta's Ads Ranking](https://www.facebook.com/business/news/ai-innovation-in-metas-ads-ranking-driving-advertiser-performance) (Meta for Business, 2025)
- [GEM Engineering Blog](https://engineering.fb.com/2025/11/10/ml-applications/metas-generative-ads-model-gem-the-central-brain-accelerating-ads-recommendation-ai-innovation/) (Nov 2025)
- [Meta Lattice AI Blog](https://ai.meta.com/blog/ai-ads-performance-efficiency-meta-lattice/) (Meta AI)
- [Meta Ad Auction Overview](https://www.facebook.com/business/ads/ad-auction) (Meta for Business)
- [2026: AI Drives Performance](https://about.fb.com/news/2026/01/2026-ai-drives-performance/) (Meta Newsroom, Jan 2026)

**Last reviewed: March 2026.** Meta's ad systems evolve continuously. If this document is more than 6 months old, verify against current Meta engineering publications before relying on it for strategic decisions.

---

## The Ad Delivery Pipeline

When someone opens Facebook or Instagram, Meta's system decides which ad to show them through a multi-stage pipeline. Understanding this pipeline is critical because it tells you *what the algorithm is optimizing for* at each stage — and therefore what inputs you can control.

```
Tens of Millions of Eligible Ads
          │
          ▼
┌─────────────────────┐
│  1. RETRIEVAL        │  ◄── Andromeda
│  (Narrow to ~1,000s) │      Picks the shortlist of candidate ads
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  2. RANKING          │  ◄── GEM + Lattice
│  (Score & order)     │      Predicts which ad delivers the most value
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  3. AUCTION          │  ◄── Total Value calculation
│  (Pick the winner)   │      Bid × Estimated Action Rate + User Value
└──────────┬──────────┘
           │
           ▼
     Ad is shown
```

Each stage has different inputs, different optimization logic, and different implications for how you manage accounts.

---

## Stage 1: Retrieval — Andromeda

### What It Does

Andromeda is the first stage in Meta's ad delivery pipeline. Its job is to take the tens of millions of eligible ads in the system and narrow them to a few thousand candidate ads that are relevant to a specific user at a specific moment.

Think of it as the bouncer at the door: Andromeda decides which ads even get a chance to compete in the auction. If your ad does not pass retrieval, it will never be shown — regardless of your bid, budget, or targeting.

### How It Works

Andromeda uses deep neural networks running on custom hardware (NVIDIA Grace Hopper Superchips and Meta's proprietary MTIA processors) to process massive amounts of data about both users and ads. Key technical details:

- **Hierarchical indexing:** Rather than scanning every ad equally, Andromeda organizes ads into a hierarchical index that allows it to search efficiently. The index and the retrieval model are jointly trained, meaning the system's understanding of relevance is baked into how it organizes ads.

- **Dense feature representations:** Andromeda builds compact "profiles" of what is likely to resonate with each user, drawing on behavioral signals, ad features, and historical engagement patterns.

- **10,000x model complexity increase:** Compared to Meta's previous retrieval system, Andromeda uses models that are 10,000 times more complex. This allows far more sophisticated personalization at the retrieval stage.

- **Model elasticity:** The system automatically adjusts its complexity in real-time based on the predicted value of the impression. For high-value users (high predicted conversion probability), it deploys more compute. For lower-value impressions, it uses lighter models.

### Results (Per Meta)

- +6% improvement in retrieval recall (finding relevant ads that would have been missed)
- +8% improvement in ad quality on selected segments
- Enables Advantage+ automation and generative AI creative tools to scale

### What This Means for Media Buyers

**Creative is the new targeting.** Andromeda retrieves ads based on predicted relevance to a specific user. The more diverse and distinct your creative portfolio, the more "entry points" Andromeda has to match your ads to different user segments. If you have one ad with one angle, Andromeda has one chance to match. If you have 10 ads with 10 distinct angles, you have 10 chances.

**Simplified structure helps, not hurts.** Andromeda performs better when it can draw from a larger pool of creative within a single campaign. Fragmenting your budget across many narrow ad sets limits the data each ad set generates, which limits Andromeda's ability to learn.

**Creative diversity must be meaningful.** Uploading 20 variations of the same ad with slightly different text overlays is not creative diversity. Andromeda needs conceptually distinct angles — different hooks, different value propositions, different formats (UGC, demo, lifestyle, testimonial) — to learn which messages resonate with which user segments.

**The algorithm cannot fix weak creative or bad offers.** Andromeda retrieves ads efficiently, but it retrieves *what you give it*. If the creative is weak, the offer is unclear, or the landing page is slow, Andromeda will efficiently deliver a bad experience.

---

## Stage 2: Ranking — GEM and Lattice

### GEM (Generative Ads Recommendation Model)

#### What It Does

GEM is Meta's largest foundation model for ad recommendations. It sits at the top of the ranking hierarchy and acts as the "central brain" that teaches the rest of the system what good performance looks like.

GEM is trained on ad content and user engagement data from both paid ads *and* organic content across Facebook, Instagram, and Messenger. This means the ad system learns from how people engage with all content on the platform, not just ads.

#### How It Works

- **Sequence learning:** GEM analyzes the *order* and *timing* of user actions — not just what they did, but the sequence of steps before and after engaging with an ad. This allows the system to understand purchase journeys and predict future behavior based on behavioral patterns.

- **Cross-surface learning:** Previously, Meta's models for Instagram optimization did not share learnings with Facebook models. GEM unifies this — insights from one surface inform predictions on all others.

- **LLM-scale architecture:** GEM is built at the scale of large language models (trained across thousands of GPUs) but is purpose-built for ad recommendation rather than text generation. The "generative" in GEM refers to generating predictions, not generating ad content.

- **InterFormer design:** GEM uses a parallel structure that processes long user behavior sequences (thousands of past interactions) while maintaining access to the complete user journey. This prevents the information loss that happens when older systems compressed behavioral data into compact summaries.

#### Results (Per Meta)

- Up to 5% increase in ad conversions on Instagram
- Up to 3% increase in ad conversions on Facebook Feed
- 4x efficiency improvement over prior generation ranking models
- Q4 2025: Meta doubled the GPUs used to train GEM; adopted more efficient sequence-learning architecture; drove 3.5% lift in ad clicks on Facebook and 1%+ gain in conversions on Instagram

#### What This Means for Media Buyers

**The algorithm learns from behavior sequences, not just demographics.** Meta no longer just knows that someone is a 35-year-old woman interested in skincare. It knows that she browsed skincare content yesterday, watched a 45-second review video, visited a competitor's site, and added a product to a cart but didn't buy. GEM uses this sequence to predict what ad will close the loop.

**Clean event data is critical.** GEM's power comes from learning sequences of actions — but it can only learn from actions it can observe. If your Conversion API (CAPI) is not implemented, if your pixel fires inconsistently, or if your event match quality is low, GEM has a weaker signal to learn from. The quality of your tracking directly impacts the quality of the algorithm's optimization.

**Cross-surface learning means multi-placement campaigns benefit.** Running campaigns across Feed, Stories, Reels, and Messenger gives GEM more data points to learn from. Restricting to a single placement limits the system's ability to find the best audience-surface combination.

### Lattice

#### What It Does

Lattice is Meta's unified ad ranking architecture. Before Lattice, Meta used dozens of separate models — one for each combination of campaign objective (clicks, conversions, video views) and surface (Feed, Stories, Reels). Each model was trained in isolation, which meant learnings from one did not benefit others.

Lattice consolidates these into a single system that learns across all objectives and surfaces simultaneously.

#### How It Works

- **Cross-objective learning:** If the system learns that a certain user segment responds well to conversion-optimized ads on Reels, it can apply that learning to click-optimized ads for similar users on Feed.

- **Cold start solution:** New products, new advertisers, and new placements start with limited data. Lattice handles this by generalizing from data across the broader system, so new campaigns can optimize faster.

- **Delayed feedback handling:** Purchases can happen hours or days after an ad impression. Lattice uses temporal modeling to capture both real-time intent signals (clicks, engagement) and slower conversion signals (add-to-cart, purchase days later).

- **Sequence Learning integration:** What Meta sometimes describes separately as "Sequence Learning" is a capability within Lattice. It enables the system to understand the order of user actions across time — critical for modeling the purchase journey and determining the right ad to show at the right stage.

#### Results (Per Meta)

- ~12% increase in ad quality
- Up to 6% increase in ad conversions
- Nearly 3% gain in conversions for app ads after rollout
- Consolidation of hundreds of separate models into one system

#### What This Means for Media Buyers

**The learning phase matters more than ever.** Lattice needs data to learn across objectives and surfaces. Disrupting the learning phase by making frequent changes (budget, targeting, creative) prevents the system from building a reliable model. After launching or making significant changes, allow 7+ days before evaluating.

**Fewer, larger campaigns outperform many small ones.** Lattice benefits from data density. Consolidating spend into fewer campaigns with broader targeting gives the system more data to work with. The era of running 15 ad sets each targeting a different interest group is over.

**The system gets smarter over time.** Unlike manual optimization where you start fresh with each campaign, Lattice carries learnings forward. An established account with months of conversion data will generally outperform a brand-new account running the same creative to the same audience.

---

## Stage 3: The Auction

### How It Works

After retrieval (Andromeda) selects the candidate ads and ranking (GEM + Lattice) scores them, the final decision of which ad to show is made by the auction.

Meta's auction is **not** a simple highest-bidder-wins system. The winning ad is determined by **Total Value**:

```
Total Value = (Advertiser Bid × Estimated Action Rate) + User Value
```

**Advertiser Bid:** How much you are willing to pay for your desired outcome. This is handled dynamically by Meta's bidding system unless you use manual bid caps. Most advertisers should let Meta bid dynamically (Lowest Cost / Highest Volume).

**Estimated Action Rate (eAR):** Meta's prediction of how likely this specific user is to take the desired action (click, purchase, etc.) based on historical data and behavioral signals. You cannot see eAR directly, but ad relevance diagnostics (Quality Ranking, Engagement Rate Ranking, Conversion Rate Ranking) are indicators.

**User Value:** How good is the experience for the user? This considers:
- Positive engagement (likes, comments, saves, shares, actions taken after clicking)
- Negative signals (hiding the ad, reporting the advertiser)
- Landing page experience (load time, bounce rate, time on site)
- Overall advertiser quality score (based on historical performance and occasional user surveys)

### The Implication

**You can win auctions without the highest bid.** An ad with a lower bid but higher estimated action rate and better user value score can beat a higher-bidding competitor. This is why creative quality and landing page experience directly impact your CPMs — they are inputs to the auction formula.

**Poor post-click experience raises your costs.** If users click your ad and then bounce immediately (slow page, broken checkout, misleading creative), Meta registers this as a poor user experience. Over time, your User Value score decreases, which means you need a higher bid to win the same auctions. Your CPMs go up.

**The auction rewards consistency.** Advertisers who consistently create engaging ads with strong post-click experiences build a better Advertiser Score over time. This creates a compounding advantage — better scores → lower CPMs → more efficient spend → more data for the algorithm → even better scores.

---

## The Breakdown Effect

The "Breakdown Effect" is not an official Meta term but describes a well-documented phenomenon in Meta's auction system:

**When you segment or break down performance by a dimension (age, gender, placement, device), the reported metrics for each segment may not reflect the true value of that segment.**

This happens because:

1. Meta's algorithm optimizes *holistically* — it considers the entire user journey across segments
2. A user might see an ad on Instagram Stories (attributed to Stories) but convert after seeing it again on Facebook Feed (attributed to Feed)
3. Breaking down by placement and then cutting "underperforming" placements can actually harm total performance because you are removing touchpoints the algorithm was using strategically

**Practical implication:** Be cautious about making optimization decisions based on placement, age, or gender breakdowns alone. The breakdown view shows you *where* conversions were attributed, not *where* they were caused. Use breakdowns for directional understanding, not for surgical cuts.

---

## Meta's Recommended Account Structure (Aligned With the Algorithm)

Based on how Andromeda, GEM, Lattice, and the auction work together, Meta's recommended structure has converged around simplification:

### Campaign Structure

1. **Fewer campaigns, broader targeting.** Use Advantage+ Shopping Campaigns (ASC) or broad-targeted campaigns with Advantage+ audience. Let the algorithm find the audience.

2. **8-15 distinct creative variations per ad set.** Provide the system with enough creative to learn which messages resonate with which user segments. Refresh every 7-14 days.

3. **Consolidate ad sets.** Rather than fragmenting budget across many small ad sets, consolidate into 2-3 ad sets with sufficient daily budget ($100+ per ad set) for meaningful learning.

4. **Use Advantage+ placements.** Let the system deliver across Feed, Stories, Reels, Messenger, and Audience Network. Restricting placements limits the algorithm's optimization surface.

5. **Allow the learning phase.** After launching or making significant changes, allow 7+ days (approximately 50 optimization events) before evaluating performance.

### Signal Strength

6. **Implement Conversion API (CAPI).** Server-side event tracking is essential. Pixel-only tracking is increasingly unreliable due to iOS privacy changes. CAPI data provides the clean signal GEM needs to learn.

7. **Prioritize event match quality.** Meta's Event Match Quality score (visible in Events Manager) indicates how well your event data matches Meta's user data. Higher match quality = better optimization.

8. **Feed the algorithm clean conversion data.** If you can pass contribution margin or customer value data back to Meta (via value optimization or value-based custom events), the system can optimize for profit, not just conversion count.

---

## What the Algorithm Cannot Do

Understanding the algorithm's limitations is as important as understanding its capabilities:

1. **It cannot fix a bad offer.** The most sophisticated retrieval and ranking system in the world cannot sell a product nobody wants at a price nobody will pay.

2. **It cannot fix a broken landing page.** If the LP is slow, confusing, or does not match the ad's promise, no amount of algorithmic sophistication will generate conversions.

3. **It cannot create demand that does not exist.** For products with no existing market awareness, paid media alone may not be sufficient. The algorithm can find people who are likely to be interested, but it cannot manufacture interest.

4. **It cannot overcome poor tracking.** Garbage in, garbage out. If conversion events are firing incorrectly, duplicated, or missing, the algorithm optimizes on bad data and makes bad decisions.

5. **It cannot tell you if the conversions are incremental.** Meta's system optimizes for the most attributed conversions at the lowest cost. It does not (and cannot) distinguish between conversions it caused and conversions it claimed credit for. That distinction requires external measurement (see `/sops/09-incrementality-bridge.md`).

---

## How This Connects to the SOP Framework

| SOP Concept | Meta Algorithm Connection |
|---|---|
| **CPM** (02) | Determined by auction competitiveness, ad quality score, and estimated action rate. Better creative → lower CPMs. |
| **CTR** (02) | Influenced by retrieval quality (Andromeda matching your ad to the right users) and creative quality. |
| **CVR** (02) | GEM's sequence learning optimizes for conversion, but CVR is ultimately determined by LP quality and offer strength. |
| **Creative Metrics** (05) | Hook rate and hold rate directly influence Andromeda's retrieval decisions and the auction's estimated action rate. |
| **Attribution Windows** (08) | Meta's default 7dc/1dv window applies. GEM learns from the full attribution window, so understand what it is optimizing toward. |
| **Incrementality** (09) | The algorithm optimizes for attributed conversions, not incremental conversions. Always validate with holdout tests. |
| **Contribution Margin** (10) | Use value optimization or custom conversion events to push margin signals back to Meta, enabling the algorithm to optimize for profit rather than volume. |

---

## Recommended Reading (Primary Sources)

Keep these bookmarked. When Meta publishes updates, re-read and update this document:

- Meta Engineering Blog: https://engineering.fb.com/
- Meta for Business News: https://www.facebook.com/business/news
- Meta AI Blog: https://ai.meta.com/blog/
- Meta Newsroom: https://about.fb.com/news/
- Meta Ad Auction: https://www.facebook.com/business/ads/ad-auction
