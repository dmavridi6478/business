# TikTok — Paid Ads Best Practices

## Campaign Types, Creative Strategy, and Operational Playbook

This document covers TikTok's paid advertising ecosystem for brands driving traffic to their own website (Shopify, etc.) or running brand awareness campaigns. For TikTok Shop-specific advertising (GMV Max, Shop Ads), see `03-tiktok-shop.md`.

**Read `01-algorithm-overview.md` first** to understand the algorithm these practices are built on.

**Last reviewed: March 2026.**

---

## Campaign Types

### Smart+ Campaigns (Recommended Default)

Smart+ is TikTok's AI-powered campaign type that automates targeting, bidding, and creative testing. Announced in October 2025, Smart+ is TikTok's equivalent of Meta's Advantage+ Shopping Campaigns.

**How it works:** You provide creative assets, a conversion objective, and a budget. TikTok handles audience selection, bid optimization, and creative rotation automatically.

**When to use Smart+:**
- Default choice for most campaigns
- Best when you have proven creative and sufficient conversion history
- Brands spending under $10K/month should start here

**Key details:**
- No manual targeting — the algorithm decides
- Integrates with Symphony Creative Studio for automated creative variations
- Requires TikTok pixel with conversion events properly configured

### Web Conversion Campaigns (Sales Objective)

Standard conversion campaigns optimized for purchase events on your website. You control targeting, bidding, and creative more directly than Smart+.

**Campaign structure:**

```
Campaign (Sales Objective)
├── Ad Group 1: Prospecting (Broad)
│   ├── Targeting: Broad or minimal interest targeting
│   ├── Bid: Cost Cap at target CPA or Maximize Conversions
│   ├── Ad 1: UGC testimonial
│   ├── Ad 2: Product demo
│   ├── Ad 3: Problem/solution
│   └── Ad 4-6: Additional variations
│
├── Ad Group 2: Retargeting
│   ├── Targeting: Custom Audience (site visitors 1-30 days, exclude purchasers)
│   ├── Bid: Maximize Conversions
│   ├── Ad 1-3: Product-specific, offer-driven creative
│   └── Budget: 15-20% of campaign budget
│
└── Budget: Minimum $50/day per ad group
    (Algorithm needs ~50 conversions in 7 days to exit learning phase)
```

### Spark Ads

Spark Ads let you run existing organic TikTok posts (yours or a creator's) as paid ads. The engagement (likes, comments, shares) from the paid promotion accrues to the original organic post, building social proof.

**Why Spark Ads matter:**
- They look and feel native to TikTok (because they ARE native TikTok posts)
- Social proof from paid views transfers to the organic post
- Creator content run as Spark Ads typically outperforms brand-created content
- The algorithm treats Spark Ads more like organic content, often resulting in better distribution

**How to set up Spark Ads:**
1. The creator posts their video organically on TikTok
2. They generate an authorization code in TikTok's creator tools
3. You enter the authorization code in TikTok Ads Manager
4. Run the post as a Spark Ad with your targeting, budget, and objective

**Best practice:** For every campaign, test at least one Spark Ad from a creator alongside your brand-created content. Spark Ads consistently outperform non-Spark ads in CTR and CVR.

### Search Ads Campaign (New in 2025)

TikTok Search Ads let you target keyword searches within TikTok — similar to Google Search Ads but with video creative.

**Why this matters:** 40% of Gen Z prefer searching on TikTok over Google for product research. Search Ads capture this high-intent traffic.

**How it works:**
- Add keywords (exact, phrase, or broad match)
- Your video ad appears when users search those terms on TikTok
- Can drive to your website (Shopify) or TikTok Shop

**Best for:**
- High-intent product terms ("best face moisturizer," "protein powder for women")
- Brand defense (your brand name)
- Category terms where you want to capture active researchers

**Budget:** Start at $20-$40/day. Allow 5-7 days and 25-50 conversions before evaluating. Use TikTok's keyword suggestion tool and add negative keywords to filter irrelevant queries.

### Video View Campaigns (Awareness/Consideration)

Optimized for video views rather than conversions. Use for upper-funnel brand building.

**When to use:**
- Building awareness before running conversion campaigns
- Growing your audience of video viewers for downstream retargeting
- Testing creative concepts cheaply before scaling in conversion campaigns
- Seeding product awareness for a new launch

**CPM on view campaigns is extremely low** — often under $1. This makes it the cheapest way to build a video viewer audience pool that you can later retarget with conversion campaigns.

### Premium / Reservation Ad Formats

These are not auction-based. They are purchased directly through TikTok's sales team on a reservation basis (fixed CPM or flat fee). They are designed for maximum-impact awareness moments.

**TopView:**
The most premium placement on TikTok. A full-screen video ad that plays immediately when a user opens the app. 100% share of voice — your ad is the first thing every user sees.

- **Format:** Full-screen video, up to 60 seconds, sound-on by default
- **Placement:** First thing users see when they open TikTok
- **Buying model:** Reservation (contact TikTok sales team directly). Not available through self-serve Ads Manager.
- **Cost:** Premium pricing — typically $50,000-$150,000+ per day depending on market and timing. Priced per day for guaranteed reach.
- **Best for:** Major product launches, movie releases, tentpole brand moments, Black Friday/holiday campaigns where maximum awareness in a single day matters
- **Creative guidance:** You have guaranteed attention for the first 3-5 seconds. Use this to deliver a complete brand message, not just a hook. High production value is acceptable here (unlike in-feed ads) because the placement itself signals premium.
- **Reach:** A single TopView day can reach 50-80 million+ users in the US depending on the day.

**Branded Hashtag Challenge:**
A sponsored hashtag that encourages user-generated content around a branded theme. Appears on the Discover page with a custom banner.

- **Format:** Challenge page with brand video, hashtag, and user participation
- **Buying model:** Reservation (typically $150,000+ for a 6-day challenge)
- **Best for:** Building brand awareness through user participation. Entertainment, CPG, fashion.
- **Note:** Extremely expensive. The ROI is in earned media — user-created videos using your hashtag generate organic reach far beyond the paid placement.

**Branded Effect:**
Custom AR filters or effects that users can apply to their own videos, branded with your product.

- **Buying model:** Reservation
- **Best for:** Products with strong visual identity that lend themselves to AR (beauty, fashion, food)

**When to use reservation formats vs. auction-based:**

| Situation | Format | Why |
|---|---|---|
| Major product launch with date-specific timing | TopView | Guaranteed massive reach on a specific day |
| Always-on ecommerce performance | Auction (Smart+, Conversion) | Flexible budget, optimized for conversions |
| Cultural moment or tentpole event | TopView + Branded Hashtag | Maximum visibility + user engagement |
| Testing a new market or audience | Auction (Video Views) | Cheap impressions to build data before committing |

For most ecommerce brands, **auction-based campaigns (Smart+, Conversion, Search, Video Views) are the core playbook.** Reservation formats like TopView are relevant only for clients with large awareness budgets and specific launch moments.

---

## Targeting Strategy

### The Bottom Line: Broad Works, But Signals Help

TikTok's official best practices (updated September 2025) are clear:

> Campaigns reaching over 80% of potential users in a target country achieve 15% lower CPA and 20% higher conversion rates on average compared to narrower audiences.

**This means broad targeting is the default recommendation on TikTok — similar to Meta, and the opposite of YouTube where targeting is critical.**

However, "broad" does not mean "zero inputs." Here is how to think about it:

**What broad targeting means on TikTok:**
- Do NOT stack multiple narrow interest categories (e.g., "skincare" + "women 25-34" + "iPhone users" + "high income")
- DO keep targeting open to 80%+ of your target country's TikTok users
- The algorithm's behavioral prediction finds the right people based on creative engagement signals — over-constraining targeting starves it of data

**What audience signals still help:**
- **Custom Audiences** (customer email list, site visitors, video viewers) give the algorithm a starting point for who to prioritize
- **Lookalike Audiences** from your best customers help the algorithm understand the "type" of person to look for
- **Smart Targeting** (enabled by default) lets TikTok automatically expand beyond your targeting when it predicts better results

**The recommended approach by funnel stage:**

| Funnel Stage | Targeting Approach | Why |
|---|---|---|
| **Prospecting** | Broad (minimal restrictions) + Creative as the targeting lever | Let the algorithm find buyers. Different creative attracts different audiences. |
| **Retargeting** | Custom Audiences (site visitors, cart abandoners, video viewers) | These are known users — targeted retargeting makes sense. |
| **Search Ads** | Keywords (exact, phrase, broad match) | Intent-based — targeting is the whole point. |
| **Lookalike expansion** | Lookalike from purchasers, seeded at 1-5% | Gives the algorithm a signal without over-constraining. |

**What NOT to do:**
- Do not layer 5+ interest categories thinking you are "refining" the audience. You are shrinking the data pool.
- Do not restrict by device type or carrier unless the product requires it (e.g., iOS-only app)
- Do not use narrow age ranges unless the product has a genuine age restriction
- Do not copy your Meta audience structure onto TikTok — TikTok's interest categories are different and less refined than Meta's

**Why this is different from YouTube:** TikTok's algorithm processes behavioral signals from content engagement across the entire platform (what videos you watch, like, share, save). This is similar to Meta's social graph — rich behavioral data that enables broad targeting. YouTube's signals are weaker for this purpose (primarily search and watch history), which is why YouTube still benefits from tighter audience definition.

---

## Bidding Strategy

| Strategy | What It Does | When to Use |
|---|---|---|
| **Maximize Conversions** | Spends full budget to get as many conversions as possible | New campaigns building data, or when volume is the priority |
| **Cost Cap** | Sets a maximum CPA target | Established campaigns with known CPA targets |
| **Minimum ROAS** | Sets a floor for return on ad spend | Ecommerce with varied product values |
| **Maximum Delivery** | Spends budget as fast as possible | Flash sales, time-sensitive promotions |

**Progression:**
1. Start with Maximize Conversions to build data
2. Once you have 50+ conversions in 7 days, switch to Cost Cap at your target CPA
3. For ecommerce with varied AOV, use Minimum ROAS

**Budget rules:**
- Minimum $50/day per ad group (TikTok's recommendation)
- The algorithm needs ~50 conversion events in a 7-day window to exit the learning phase
- Do not change budget by more than 20-50% at a time
- Allow 5-7 days after any change before evaluating

---

## Creative Strategy

### The Golden Rule: Make TikToks, Not Ads

TikTok's own guidance is explicit: the ads that perform best are indistinguishable from organic content. Polished, corporate-looking video ads get scrolled past. Raw, authentic, creator-style content gets watched, shared, and converts.

### What Works on TikTok

| Creative Type | Description | Why It Works |
|---|---|---|
| **UGC testimonial** | Real person talking to camera about the product | Authenticity. Trust. Feels like a friend's recommendation. |
| **Problem → Solution** | Open with the problem, reveal the product as the answer | Creates a curiosity loop that drives completion rate |
| **"TikTok made me buy it"** | Framing the product as a TikTok discovery | Leverages social proof of the platform itself |
| **Tutorial / How-to** | Showing how to use the product | Education-as-entertainment. High save and share rates. |
| **Before/After** | Visual transformation using the product | Powerful for beauty, health, fitness, home products |
| **Trend-jacking** | Using a trending sound or format with your product integrated | Rides the algorithm's trend amplification. Short lifespan but huge reach. |
| **Unboxing / First impression** | Opening and trying the product for the first time | Authentic reaction content. High completion rate. |
| **Stitch/Duet style** | Reacting to or building on another video | Feels native. Can ride existing viral content. |

### Creative Structure: Hook → Body → CTA

```
SECONDS 1-3: THE HOOK (Survival)
│  71% of viewers decide to stay or leave in the first 3 seconds
│  Must create curiosity, surprise, or relevance immediately
│  Techniques: Bold statement, question, visual surprise, text overlay
│
▼
SECONDS 4-15: THE BODY (Value)
│  Deliver on the hook's promise
│  Show the product, demonstrate the benefit, tell the story
│  Keep visual variety (change angles, add b-roll, use text overlays)
│
▼
SECONDS 15-30: THE CTA (Action)
│  Clear, specific call to action
│  "Link in bio," "Shop now," "Click the product link"
│  Can include offer/urgency ("20% off this week only")
│
= Total length: 15-30 seconds for most DR ads
  (Can go longer for educational/tutorial content if retention holds)
```

### Hook Formulas That Work on TikTok

| Hook Type | Example | Why It Works |
|---|---|---|
| **Bold claim** | "This $12 product replaced my $80 serum" | Price contrast creates curiosity |
| **Question** | "Why is nobody talking about this?" | Curiosity gap — viewer needs to watch to find out |
| **Pattern interrupt** | [Unusual visual or sound in first frame] | Breaks the scroll pattern |
| **Social proof** | "POV: you finally try the thing TikTok won't shut up about" | Leverages FOMO and platform culture |
| **Negative hook** | "Stop buying [competitor category] — here's why" | Controversy drives engagement |
| **Direct address** | "If you have [problem], watch this" | Self-selection — the right audience self-identifies |
| **Trending sound** | [Popular audio clip] + product integration | Algorithm boosts content using trending sounds |

### Creative Production Tips

- **Film on a phone, not a camera.** iPhone/Android footage looks native. Cinema cameras look like ads.
- **Vertical only (9:16).** Never letterboxed or horizontal.
- **Sound-on design but subtitle everything.** Many users watch with sound, but add captions for those who don't.
- **Use TikTok's native editing tools** (CapCut, TikTok's in-app editor). Content edited with these tools often receives preferential distribution because it signals native content.
- **Test trending sounds.** Check TikTok Creative Center for trending sounds in your category. Using popular audio increases FYP distribution.
- **Batch produce.** Shoot 5-10 videos in one session. This gives you a week or two of content to test.

### Creative Testing Process

1. Launch 5-8 creative variations per ad group
2. Let each run for 3-5 days with at least 1,000 impressions
3. Kill creatives with completion rate below 15% and CTR below 0.5% after sufficient data
4. Scale winners by increasing their ad group budget
5. Introduce 3-5 new creatives every 1-2 weeks
6. Never stop testing — TikTok creative fatigues in 7-14 days for high-spend accounts

---

## Pixel and Tracking Setup

### TikTok Pixel (Required)

The TikTok pixel tracks user actions on your website and feeds conversion data back to the algorithm for optimization.

**Events to configure:**
- ViewContent (product page view)
- AddToCart
- InitiateCheckout
- CompletePayment (Purchase) — **must include value parameter**

**Advanced Match:** Enable Advanced Match to pass hashed email and phone data for better user matching (similar to Meta's Advanced Matching / CAPI).

**Events API:** TikTok's server-side tracking (equivalent to Meta's CAPI). Recommended for iOS accuracy. Sends events from your server directly to TikTok, bypassing browser limitations.

### Attribution Settings

TikTok defaults to **7-day click, 1-day view (7dc/1dv)** — the same as Meta.

**Same skepticism applies.** View-through attribution on TikTok can be even more inflated than Meta because TikTok's fast-scrolling feed generates enormous impression volumes. A user who scrolled past your ad in 0.5 seconds and bought the product 20 hours later through a Google search gets attributed to TikTok under 1dv.

**Recommendation:** Always pull 1dc-only data alongside 7dc/1dv to understand the gap. If more than 50% of attributed conversions are view-through, the campaign's reported ROAS is likely overstated.

TikTok is a self-attributing network (SAN) — third-party attribution tools (Triple Whale, Northbeam, etc.) may show different numbers than TikTok's dashboard. Cross-reference always.

---

## Scaling on TikTok

### The Scaling Playbook

1. **Start with 3-5 ad groups** at $50-$100/day each, each with 5-8 creative variations
2. **Let the learning phase complete** (7 days or 50 conversions)
3. **Identify winning creative** (highest completion rate + lowest CPA)
4. **Scale budget 20-30% every 5-7 days** on winning ad groups
5. **Continuously add new creative** — scale creative volume before scaling budget
6. **Launch new ad groups** with new creative angles rather than overloading one ad group

### Common Scaling Mistakes

| Mistake | Why It Hurts | Fix |
|---|---|---|
| Scaling budget 100%+ overnight | Resets learning phase, spikes CPA | Increase 20-30% every 5-7 days |
| Not refreshing creative | Fatigue kills performance within 2 weeks | New creative every 1-2 weeks |
| Too many ad groups with tiny budgets | Each ad group starved of data | Consolidate — fewer ad groups, more budget each |
| Changing targeting + budget + creative simultaneously | Cannot isolate what caused performance change | Change one variable at a time |
| Judging performance after 2 days | Not enough data for reliable signal | Wait 5-7 days minimum |

---

## TikTok vs. Meta: Key Operational Differences

| Dimension | Meta | TikTok |
|---|---|---|
| **CPM** | $9-$15 average | $2.60-$6.60 average — significantly cheaper |
| **Creative lifespan** | 2-4 weeks | 1-2 weeks — fatigues faster |
| **Creative style** | Polished UGC, product photos, carousels | Raw, native, creator-style video only |
| **Targeting** | Broad works, Advantage+ handles it | Broad works, but audience signals help more than on Meta |
| **Learning phase** | ~50 events in 7 days | ~50 events in 7 days (same) |
| **Attribution** | 7dc/1dv default | 7dc/1dv default (same) |
| **Audience overlap** | High with TikTok (same people use both) | High with Meta |
| **Best for** | Broad ecommerce, all product types | Visual products, younger demographics, trend-driven products |
| **Creative production cost** | Moderate (can use statics, carousels) | Higher volume needed (video only, fast fatigue) |

---

## Audience Building and Retargeting

### Building Audiences for Downstream Use

Similar to the YouTube audience strategy (see `youtube/youtube-advertising.md`), you can build TikTok video viewer audiences and use them for retargeting:

1. **Custom Audience from video views:** Create audiences of people who watched 25%, 50%, 75%, or 100% of your video ads
2. **Website Custom Audience:** Retarget site visitors, cart abandoners, product page viewers
3. **Engagement Custom Audience:** People who liked, commented, or shared your TikTok content

### Cross-Platform Audience Flow

```
TikTok Video Viewers (custom audience)
    │
    ├── Retarget on TikTok with conversion-focused creative
    ├── Export email matches → Meta Custom Audience
    └── Build lookalike on TikTok from video viewers
```

---

## Reporting Essentials

### Columns to Monitor

| Metric | Why |
|---|---|
| Impressions | Reach and frequency |
| Video Views (2s, 6s, full) | Creative engagement at each stage |
| Completion Rate | Creative health — the most important signal |
| CTR | Click-through intent |
| CPC | Cost of traffic |
| Conversions | Volume |
| CPA | Efficiency |
| ROAS | Revenue return |
| Conversion Value | Total revenue |

### Review Cadence

- **Daily:** Spend pacing, anomaly check
- **Every 3 days:** Creative performance — kill low performers, note trends
- **Weekly:** Full performance review (7d vs prior 7d), creative refresh planning
- **Biweekly:** 30-day trend analysis, audience performance review, scaling decisions
