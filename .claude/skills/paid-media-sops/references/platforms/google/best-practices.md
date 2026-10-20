# Google Ads — Best Practices

## Tactical Playbook by Campaign Type

This document provides specific, actionable best practices for each Google Ads campaign type. Read `algorithm-overview.md` first to understand the systems these practices are built on.

---

## Account Structure (Ecommerce)

### Recommended Structure

```
Google Ads Account
│
├── Brand Search Campaign
│   ├── Brand exact match keywords
│   ├── Competitor brand keywords (optional, separate ad group)
│   └── Bid strategy: Target Impression Share (90%+) or Manual CPC
│       ⚠️ Keep budget small. Most brand conversions are non-incremental.
│
├── Non-Brand Search Campaign
│   ├── Ad Group 1: High-intent keywords (buy, best, near me, [product])
│   ├── Ad Group 2: Category keywords (general product terms)
│   ├── Ad Group 3: Problem/solution keywords (what the product solves)
│   └── Bid strategy: Target CPA or Maximize Conversions (once 30-50 conv/month)
│
├── Standard Shopping Campaign (optional, for control)
│   ├── Product Group 1: Hero products (highest margin, best sellers)
│   ├── Product Group 2: All other products
│   └── Bid strategy: Target ROAS or Maximize Conversion Value
│
├── Performance Max Campaign
│   ├── Asset Group 1: Product Category A (with audience signals + search themes)
│   ├── Asset Group 2: Product Category B
│   └── Bid strategy: Maximize Conversion Value with Target ROAS
│       ⚠️ Exclude brand terms. Monitor channel breakdown.
│
├── YouTube / Demand Gen (if budget allows)
│   ├── Prospecting audiences (in-market, custom intent)
│   └── Bid strategy: Maximize Conversions or Target CPA
│
└── Display Remarketing Campaign
    ├── Audience: Site visitors 1-30 days, exclude converters
    └── Bid strategy: Target CPA
        ⚠️ Low budget. Test incrementality with holdout.
```

### Campaign Priority Guidelines

**Where to spend first (highest confidence of incremental value):**

1. **Non-brand Search** — Users are actively searching for what you sell. Highest intent. Start here.
2. **Standard Shopping / PMax (feed-only)** — Product-level targeting for purchase-intent queries. High intent.
3. **Performance Max (full assets)** — Cross-channel reach. Add once Search and Shopping are optimized.
4. **YouTube / Demand Gen** — Upper funnel. Add when bottom-funnel campaigns are maxed out.
5. **Display Remarketing** — Keep small. Test incrementality.
6. **Brand Search** — Defensive only. Keep budget minimal.

---

## Search Campaign Best Practices

### Keyword Strategy

**Start narrow, expand with data:**

1. Launch with exact match and phrase match keywords for your highest-intent terms
2. After accumulating 30-50+ conversions, add broad match versions paired with Smart Bidding
3. Review search term reports weekly and add negative keywords aggressively

**Negative keyword management is non-negotiable:**
- Review the search term report every week (daily for high-spend accounts)
- Add irrelevant queries as negative keywords at the campaign or ad group level
- Create a shared negative keyword list for terms that apply across campaigns (e.g., "free," "jobs," "how to," "DIY," competitor names you don't want to bid on)
- For PMax, use account-level negative keywords (campaign-level negatives require a Google rep)

### Ad Copy

**Responsive Search Ads (RSAs):**
- Provide 10-15 headlines and 4 descriptions per ad group
- Pin your strongest headline to Position 1 if you have a clear winner
- Include the primary keyword in at least 2-3 headlines
- Include the offer/value proposition in at least 2 headlines
- Include a clear CTA in at least 1 description
- Test different angles: benefit-focused, feature-focused, social proof, urgency
- Review the asset report to see which headlines and descriptions are rated "Best," "Good," or "Low"

**Ad extensions (now called "assets"):**
Always enable: sitelinks, callouts, structured snippets, price extensions (ecommerce), promotion extensions (when running sales). These increase ad real estate and improve CTR at no additional cost.

### Bidding in Search

| Situation | Recommended Strategy | Notes |
|---|---|---|
| New campaign, no conversion data | Manual CPC or Maximize Clicks | Build data first. Switch to Smart Bidding at 30-50 conversions/month. |
| 30-50+ conversions/month | Maximize Conversions | Let Google find conversion volume. Move to Target CPA once stable. |
| Stable performance, known CPA target | Target CPA | Set at current average CPA, then tighten 5-10% per month. |
| Ecommerce with varied product values | Maximize Conversion Value → Target ROAS | Ensures high-value conversions get priority. |
| Brand defense | Target Impression Share (90%+) | You want visibility, not CPA optimization. |

### Search Campaign Troubleshooting

| Problem | Check | Fix |
|---|---|---|
| Low impression share | Impression Share Lost (Budget) vs. Lost (Rank) | If budget: increase budget or narrow targeting. If rank: improve Quality Score (better ad copy, LP, or raise bids). |
| High CPC | Quality Score breakdown | Improve expected CTR (better ad copy), ad relevance (tighter keyword-ad match), or LP experience (faster, more relevant page). |
| Clicks but no conversions | Search term report + landing page | Are queries relevant? Is the LP fast and congruent with the ad? |
| Smart Bidding spending wildly | Too few conversions for the algorithm | Revert to Manual CPC until conversion volume builds. |
| CTR dropping | Ad fatigue or keyword match drift | Check search terms — are broad match queries drifting? Refresh ad copy. |

---

## Shopping Campaign Best Practices

### Product Feed Optimization

**The feed is your most important lever in Shopping.** Optimize it before touching anything else.

**Product titles (most important):**
- Front-load the most important terms (Brand + Product Type + Key Attribute + Color/Size)
- Include terms customers actually search for
- Example: Instead of "BW-1200" → "Bose Wireless Headphones — Noise Cancelling Over-Ear, 20-Hour Battery, Black"
- Maximum 150 characters but front-load the first 70 (what's visible in the ad)

**Product images:**
- Primary image: Clean, white background, product only (Google's guidelines)
- High resolution (at least 800×800 pixels)
- Show the actual product clearly — no text overlays, no watermarks, no promotional badges

**Product descriptions:**
- Include relevant search terms naturally
- Describe features, benefits, and use cases
- 500-1,000 characters recommended

**Product data quality:**
- GTIN/UPC codes are required for most products. Missing GTINs reduce visibility.
- Accurate pricing — mismatches between feed price and landing page price can get your products disapproved
- Shipping and tax information must be current
- Availability must match actual stock (advertising out-of-stock products wastes spend and harms trust)

### Shopping Structure

**Segment by product performance:**
- Hero products (top sellers, highest margin): Separate product group with higher bids or target ROAS
- Long-tail products: Group together with standard bidding
- Low-margin or low-performing products: Exclude or group with lower bids

**Use custom labels** in your feed to tag products by margin, season, best-seller status, or price point. Then bid differently based on these labels.

---

## Performance Max Best Practices

### Setup Checklist

- [ ] Conversion tracking verified and accurate (one primary conversion action, preferably Purchase with value)
- [ ] Product feed optimized in Merchant Center (titles, images, descriptions)
- [ ] Brand terms excluded via campaign-level negatives (request through Google rep) or account-level negatives
- [ ] Audience signals configured (customer match list, site visitors, in-market)
- [ ] Search themes added (15-25 relevant themes per asset group)
- [ ] Video assets uploaded (do NOT rely on auto-generated video)
- [ ] Asset groups organized by product category or audience, not lumped together

### Asset Group Strategy

**One asset group per distinct product category or audience:**

| Asset Group | Products | Audience Signal | Search Themes | Creative Focus |
|---|---|---|---|---|
| Skincare - Moisturizers | Moisturizer feed segment | Purchasers of moisturizers, in-market for skincare | "best moisturizer," "face cream for dry skin" | Moisturizer-specific images, benefits, testimonials |
| Skincare - Serums | Serum feed segment | Purchasers of serums, in-market for anti-aging | "vitamin c serum," "anti-aging serum" | Serum-specific imagery and messaging |

**Do not:** Create one asset group with all products and all messaging. The algorithm cannot learn which creative matches which product intent if everything is mixed together.

### PMax Monitoring Cadence

| Check | Frequency | What to Look For |
|---|---|---|
| Channel performance breakdown | Weekly | Is budget going to high-converting channels (Search, Shopping) or being burned on Display? |
| Search term insights | Weekly | Are queries relevant? Are brand terms leaking in despite exclusions? |
| Asset performance ratings | Biweekly | Replace "Low" rated assets. Build on "Best" rated patterns. |
| Audience signal contribution | Monthly | Which signals are driving the most conversions? Double down. |
| Conversion comparison (PMax vs. backend) | Monthly | Are PMax-reported conversions matching actual orders? Attribution inflation check. |

### Feed-Only vs. Full Assets Decision

**Start feed-only when:**
- Budget is under $5,000/month on PMax
- You want to keep spend in Shopping (highest conversion rate for ecommerce)
- You don't have quality video assets
- You want maximum control over where budget goes

**Add full assets when:**
- Feed-only campaigns are stable and you want to expand reach
- You have quality video and image assets ready
- Budget supports testing across YouTube and Display
- You've validated Shopping performance and want incremental reach

---

## YouTube Best Practices

### When to Invest in YouTube

YouTube makes sense when:
- Search and Shopping are optimized and you have remaining budget to allocate
- You have strong video creative (product demos, testimonials, founder stories)
- The client's product benefits from visual demonstration
- You want to build upper-funnel awareness that feeds into Search and Shopping downstream

### YouTube Creative for Ecommerce

**The first 5 seconds are everything** (users can skip after 5 seconds for skippable in-stream):
- Lead with the product or the problem it solves — not a logo intro
- Text overlay the key benefit immediately
- Show the product in action within the first 3 seconds

**Recommended video length:**
- 15-30 seconds for direct response
- 60-90 seconds for consideration/education
- 6 seconds for bumper ads (awareness only)

### YouTube Targeting

**Best targeting approaches for ecommerce:**
1. **Custom intent audiences:** Target people who have recently searched for your product terms on Google. This bridges search intent to video.
2. **In-market audiences:** People Google has identified as actively shopping in your product category.
3. **Customer match:** Upload your buyer list and target similar users on YouTube.
4. **Remarketing:** Show video ads to people who visited your site but didn't convert.

---

## Display Remarketing Best Practices

### Keep It Focused

Display remarketing should be a small, targeted effort — not a major budget line:

- **Budget:** 5-10% of total Google spend
- **Audience:** Site visitors in the last 7-30 days, excluding recent purchasers
- **Frequency cap:** 3-5 impressions per user per day (prevent ad fatigue)
- **Creative:** Dynamic remarketing using product feed (shows users the specific products they viewed)

### Incrementality Warning

Display remarketing is the single most over-attributed campaign type in Google Ads. The same people seeing your remarketing ads are also seeing your email campaigns, organic retargeting, and potentially coming back on their own. Run a holdout test before assuming Display remarketing is driving value.

---

## Conversion Tracking Setup

### The Foundation

Every strategy in this document depends on accurate conversion tracking. Set this up correctly before doing anything else.

**For ecommerce:**
- Track Purchases as the primary conversion action with dynamic value (actual order revenue)
- Track Add to Cart and Begin Checkout as secondary (observation only) conversion actions
- Implement Enhanced Conversions (sends hashed first-party data to Google for better matching)
- If running app + web, set up Web-to-App Connect

**For lead gen:**
- Track the highest-value action as primary (form submit, phone call >60 seconds, qualified lead)
- Do NOT track page views or button clicks as primary conversions — this pollutes Smart Bidding
- Import offline conversions if possible (CRM data showing which leads became customers)

### Conversion Value

**Send actual revenue as conversion value.** Without it, Smart Bidding treats a $20 order and a $200 order as equal.

**Advanced:** If you can pass contribution margin instead of revenue as the conversion value, you are training Google's algorithm to optimize for profit directly. This is the closest integration between ad optimization and business outcomes possible.

---

## Google Ads Specific to SOP Framework

### Time Windows on Google

Google's attribution is different from Meta — data-driven attribution (DDA) distributes credit across touchpoints rather than giving 100% credit to the last click or the last view.

**How to compare:** Pull conversion data under both DDA (default) and last-click attribution models. The gap tells you how much credit DDA is distributing to upper-funnel interactions. Large gaps on Display or YouTube campaigns suggest those campaigns are getting DDA credit for assisting conversions that Search or Shopping closed.

### The Five Core Metrics on Google

| Metric | Search | Shopping | PMax | YouTube | Display |
|---|---|---|---|---|---|
| **CPM** | Less relevant (CPC model) | Less relevant (CPC model) | Relevant (mixed model) | Very relevant | Very relevant |
| **CTR** | Critical — affects Quality Score and CPC | Critical — affected by product image, title, price | Monitored at asset level | View rate is the proxy | Low by nature (0.1-0.5%) |
| **CVR** | LP quality and ad-to-LP congruence | Product page quality and price competitiveness | Blended across channels | Lower (upper funnel) | Very low for prospecting |
| **AOV** | Influenced by keyword intent (high-intent → higher AOV) | Influenced by product group targeting | Blended | Lower (awareness traffic) | Lower (remarketing may be higher) |
| **CPA** | Primary optimization metric | ROAS often preferred (variable product values) | ROAS preferred for ecommerce | Higher — awareness channel | Remarketing: low but question incrementality |
