# Google Ads — How the Algorithm Works

## Official Sources and Last Updated

This document is sourced primarily from Google Ads Help Center documentation, Google AI Blog, and Google Marketing Live announcements. Key sources:

- [About Smart Bidding](https://support.google.com/google-ads/answer/7065882) (Google Ads Help)
- [Your Guide to Smart Bidding](https://support.google.com/google-ads/answer/11095984) (Google Ads Help)
- [Google Ads Highlights of 2025](https://support.google.com/google-ads/answer/16756291) (Google Ads Help)
- [About Performance Max Campaigns](https://support.google.com/google-ads/answer/10724817) (Google Ads Help)
- [About Ad Rank](https://support.google.com/google-ads/answer/1722122) (Google Ads Help)
- [2026: AI Drives Performance — Google Ads](https://blog.google/products/ads-commerce/) (Google Blog)

**Last reviewed: March 2026.** Google Ads updates frequently. Verify against current documentation before relying on this for strategic decisions.

---

## Why Google Is Different From Meta

On Meta, you are working with essentially one system — a feed-based algorithm that decides which ads to show in a social content stream. You provide creative and let the system find the audience.

On Google, you are working with **multiple distinct systems** that share a bidding infrastructure but operate on fundamentally different logic:

| Campaign Type | Primary Inventory | How Users Encounter Ads | Targeting Logic |
|---|---|---|---|
| Search | Google Search results | User searches for something → your ad appears | **Intent-based:** you target keywords that match what people search |
| Shopping | Google Search, Shopping tab | User searches for a product → your product listing appears | **Feed-based:** your product data determines when you appear |
| Performance Max (PMax) | All Google properties (Search, Shopping, YouTube, Display, Gmail, Maps, Discover) | Algorithm decides where and when to show your ad | **AI-driven:** you provide assets and signals, Google handles everything |
| YouTube | YouTube video (in-stream, in-feed, Shorts) | User watches video → your ad plays before/during/alongside | **Interest + intent:** targeting by audience, topic, or search behavior |
| Display | Websites in Google Display Network | User browses a website → your banner/image ad appears | **Audience-based:** targeting by interest, remarketing, or placement |
| Demand Gen | YouTube, Discover, Gmail | User browses content → your visual ad appears in feed | **Interest + behavior:** similar to Meta, visual-first, discovery-oriented |

**This means a single diagnostic framework won't work for all Google campaign types.** A CTR problem in Search is a completely different beast from a CTR problem in Display. This document covers the shared systems first, then breaks down each campaign type individually.

---

## Shared System: Smart Bidding

Smart Bidding is Google's auction-time machine learning system that sets bids for every individual auction in real-time. It is the engine that powers most campaign types.

### How It Works

For every search, every YouTube impression, every Display placement — Smart Bidding runs a prediction:

> "How likely is this specific user, at this specific moment, on this specific device, in this specific location, to take the desired action — and what should we bid?"

**Signals Smart Bidding uses (partial list from Google's documentation):**

- Device (mobile, desktop, tablet)
- Location and location intent
- Time of day and day of week
- Browser and operating system
- Language preferences
- Search query (exact query, not just keyword)
- Remarketing list membership
- Ad creative characteristics
- Historical conversion data from the account
- Cross-account conversion patterns (Google's aggregate data)

### Smart Bidding Strategies

| Strategy | What It Optimizes For | When to Use |
|---|---|---|
| **Maximize Conversions** | Highest number of conversions within budget | New campaigns or scaling phases where volume is the priority |
| **Target CPA** | Conversions at a specific cost-per-acquisition | Established campaigns with 30-50+ conversions/month and a known CPA target |
| **Maximize Conversion Value** | Highest total conversion value within budget | Ecommerce accounts where different conversions have different values |
| **Target ROAS** | Conversion value at a specific return on ad spend | Established ecommerce accounts with 50+ conversions/month and a ROAS goal |
| **Maximize Clicks** | Highest number of clicks within budget | Top-of-funnel traffic campaigns (not conversion-focused) |
| **Target Impression Share** | Appearing in a target percentage of auctions | Brand defense campaigns where visibility matters more than CPA |

### Critical Requirements for Smart Bidding

1. **Conversion tracking must be accurate.** Smart Bidding optimizes toward whatever you tell it is a "conversion." If your tracking is broken, duplicated, or tracking the wrong event, the algorithm optimizes toward garbage.

2. **Minimum conversion volume.** Google recommends 30-50 conversions in the past 30 days for Smart Bidding to work effectively. Below this threshold, the algorithm does not have enough data to make reliable predictions. Use Maximize Conversions (unconstrained) or Manual CPC for low-volume campaigns.

3. **Learning phase is real.** After launching or making significant changes (budget >20%, bid strategy change, conversion action change), the campaign enters a learning phase of approximately 7-14 days. Performance may fluctuate. Do not make additional changes during this period.

4. **Do not set aggressive targets too early.** A Target CPA that is 50% below your current average will cause the algorithm to stop spending because it cannot find conversions at that price. Start targets at or slightly above your current average, then tighten gradually.

### What Smart Bidding Cannot Do

- It cannot overcome bad creative, bad landing pages, or bad offers
- It cannot create demand that does not exist (if no one is searching for your product, there are no auctions to bid on)
- It cannot tell you if the conversions are incremental
- It does not optimize for profit unless you feed it profit signals (via conversion value)

---

## Shared System: The Google Ads Auction

### How Ad Rank Works (Search)

When someone searches on Google, an auction runs to determine which ads appear and in what order. The winning ad is determined by **Ad Rank**:

```
Ad Rank = Bid × Quality Score × Expected Impact of Extensions
```

**Quality Score components:**
- **Expected CTR:** How likely is the ad to be clicked based on historical data
- **Ad Relevance:** How closely the ad matches the user's search intent
- **Landing Page Experience:** How useful, relevant, and fast the landing page is

**Key insight:** Unlike Meta, Google's auction system is heavily influenced by *relevance*. A highly relevant ad with a lower bid can outrank a less relevant ad with a higher bid. This means:

- Ad copy that closely matches the search query lowers your CPC
- Landing pages that are fast, relevant, and useful lower your CPC
- High CTR ads get rewarded with lower costs over time

---

## Campaign Type: Search

### How It Works

Search campaigns show text ads to people actively searching for specific terms on Google. This is **intent-based advertising** — the user has declared what they want by typing a query.

**The search ads pipeline:**

```
User types a query
       │
       ▼
Google matches the query to eligible keywords in your account
(based on match type: exact, phrase, broad)
       │
       ▼
Smart Bidding sets a bid for this specific auction
       │
       ▼
Ad Rank determines if your ad shows and in what position
       │
       ▼
User sees the ad, decides whether to click
```

### Match Types

| Match Type | Syntax | Behavior |
|---|---|---|
| **Exact Match** | [running shoes] | Triggers on searches that have the same meaning as your keyword |
| **Phrase Match** | "running shoes" | Triggers on searches that include the meaning of your keyword |
| **Broad Match** | running shoes | Triggers on searches related to your keyword, including synonyms, related topics, and inferred intent |

**The trend in 2025-2026:** Google is pushing hard toward Broad Match + Smart Bidding. The logic is that Smart Bidding can evaluate each query individually and bid appropriately, even on queries you wouldn't have thought to target. Broad Match gives the algorithm more queries to bid on; Smart Bidding ensures you only pay for the ones likely to convert.

**The risk:** Broad Match can match to irrelevant queries if Smart Bidding doesn't have enough data. For low-volume accounts or new campaigns, start with Exact and Phrase match, then expand to Broad once you have 50+ conversions/month.

### Search-Specific Metrics

- **Impression Share:** What percentage of eligible impressions your ad actually appeared in. Below 50% means you're missing significant opportunity.
- **Search Impression Share Lost (Budget):** Impressions lost because your budget ran out. Signals you should increase budget or narrow targeting.
- **Search Impression Share Lost (Rank):** Impressions lost because Ad Rank was too low. Signals you need better Quality Score or higher bids.
- **Search Term Report:** The actual queries that triggered your ads. Review weekly and add irrelevant queries as negative keywords.

### What to Watch for in Search

- **Brand search cannibalization:** If you're bidding on your own brand name, check what percentage of those clicks would have gone to your organic listing for free. Brand search ROAS is almost always inflated. See `09-incrementality-bridge.md`.
- **Query sculpting with negatives:** Regularly review the search term report and add negative keywords to prevent spend on irrelevant queries. This is one of the highest-ROI activities in Search management.
- **Ad copy testing:** Test 2-3 RSA (Responsive Search Ad) variations per ad group. Google's system tests combinations of headlines and descriptions, but you control the messaging inputs. Test different value propositions, CTAs, and proof points.

---

## Campaign Type: Shopping (Standard Shopping)

### How It Works

Shopping campaigns display product listing ads (PLAs) — the product images with price, name, and store name that appear in search results and the Shopping tab. The targeting is driven by your **product feed**, not keywords.

**The Shopping pipeline:**

```
User searches for a product
       │
       ▼
Google matches the query to products in your Merchant Center feed
(based on product title, description, attributes)
       │
       ▼
Smart Bidding sets a bid based on the product, query, and user
       │
       ▼
Your product listing appears (or doesn't) in Shopping results
```

### Why the Product Feed Is Everything

In Shopping, there are no keywords. Google reads your product feed to determine when to show your products. This means:

- **Product titles** are the most important optimization lever. A title of "Blue Widget" will match far fewer queries than "Blue Widget — Wireless Bluetooth Speaker for Home Office, 20-Hour Battery"
- **Product descriptions** provide additional matching signals
- **Product images** directly impact CTR (clear, high-quality, white-background images outperform lifestyle shots in Shopping)
- **Price competitiveness** affects both click-through and conversion rate. Google surfaces your price alongside competitors.
- **Product categories and attributes** (color, size, material, brand) improve matching accuracy

### Standard Shopping vs. Performance Max (for Shopping)

| | Standard Shopping | PMax (Shopping) |
|---|---|---|
| **Targeting** | Query matching via product feed; manual bid adjustments | AI-driven across all surfaces |
| **Transparency** | Full search term visibility, product-level bidding | Improved but still limited vs. Standard |
| **Control** | High — bid by product, query, device, location | Lower — algorithm makes most decisions |
| **Inventory** | Search and Shopping tab only | Search, Shopping, YouTube, Display, Gmail, Maps, Discover |
| **Best for** | Precise product-level control, high-value SKUs | Maximum reach, discovery, scaling |

**Recommendation for ecommerce:** Many sophisticated advertisers run both — Standard Shopping for top products where you want granular control, and PMax for broader reach and discovery. Monitor for cannibalization between the two.

---

## Campaign Type: Performance Max (PMax)

### How It Works

PMax is Google's AI-driven, cross-channel campaign type. You provide creative assets, audience signals, and conversion goals. Google's machine learning handles targeting, placement, bidding, and creative assembly across all Google properties.

**The PMax pipeline:**

```
You provide: Assets + Audience Signals + Conversion Goals + Product Feed (if ecommerce)
       │
       ▼
Google's AI assembles ad combinations from your assets
       │
       ▼
The system identifies users across all Google properties
who are likely to convert (using Smart Bidding + audience modeling)
       │
       ▼
Ads are served across Search, Shopping, YouTube, Display,
Gmail, Maps, and Discover — wherever the algorithm predicts
the highest conversion probability
       │
       ▼
The system learns from results and continuously optimizes
```

### Asset Groups

Asset groups are PMax's creative building blocks. Each asset group contains:

- Up to 15 headlines (30 characters each)
- Up to 5 long headlines (90 characters each)
- Up to 5 descriptions (90 characters each)
- Up to 20 images (various aspect ratios)
- Up to 5 videos (if you don't provide video, Google will auto-generate low-quality ones — always upload your own)
- Up to 5 logos
- A final URL and display path

**Each asset group should represent a distinct product category, audience, or message.** Do not put all products and all messaging into one asset group.

### Audience Signals

Audience signals are *directional hints*, not hard targeting. They tell Google "people like this tend to convert for us" — and the algorithm starts there, then expands.

**Strongest signals (in order of value):**
1. Customer Match lists (email list of actual buyers)
2. Website visitors / remarketing audiences
3. Converters from other campaigns
4. In-market audiences (people actively researching your category)
5. Custom segments (based on search terms or competitor URLs)

### Search Themes

Added in 2024-2025, search themes let you specify up to 25-50 keyword themes per asset group. These act like broad match keywords — they guide PMax toward relevant search queries.

**Always add search themes.** Without them, PMax relies entirely on the algorithm's interpretation of your assets and signals, which can lead to irrelevant query matching.

### Feed-Only vs. Full Asset Groups

For ecommerce, a critical decision:

- **Feed-only asset groups:** Only your product feed, no creative assets. Limits PMax to Shopping and Dynamic Remarketing placements. Forces budget into your highest-converting channel.
- **Full asset groups:** Product feed plus headlines, descriptions, images, videos. Enables PMax to serve across all channels including YouTube and Display.

**Recommendation:** Start with feed-only for new PMax campaigns. Add full assets once the campaign is stable and you want to expand reach. Adding full assets from day one often means Google spends budget testing Display and YouTube placements that have lower conversion rates for direct response.

### PMax Pitfalls

1. **Brand cannibalization:** PMax can claim credit for branded search queries that your Search campaign (or organic results) would have captured. Use brand exclusions and campaign-level negative keywords.
2. **Budget allocation opacity:** You cannot control how much PMax spends on YouTube vs. Display vs. Search. Use channel-level reporting (available since 2025) to monitor where budget is going.
3. **Auto-generated creative:** If you don't upload video, Google creates low-quality auto-generated videos from your images. Always upload your own.
4. **Learning period:** PMax needs 2-4 weeks and 50+ conversions to stabilize. Do not make major changes during this period.

---

## Campaign Type: YouTube

### How It Works

YouTube ads appear before, during, or alongside YouTube videos. The targeting combines audience signals (who the user is) with content signals (what they're watching).

**Main YouTube ad formats:**

| Format | How It Works | When It's Skippable | Best For |
|---|---|---|---|
| **Skippable In-Stream** | Plays before/during a video; user can skip after 5 seconds | After 5 seconds | Brand awareness + consideration; pay only when watched 30 seconds or clicked |
| **Non-Skippable In-Stream** | 15-second ad that must be watched | Not skippable | Reach and frequency; pure awareness |
| **In-Feed (Discovery)** | Appears in search results and related videos | N/A (user chooses to click) | Consideration; drives to your YouTube content |
| **YouTube Shorts** | Appears between Shorts videos | Swipeable | Reaching younger audiences on mobile |
| **Bumper** | 6-second non-skippable ad | Not skippable | High-frequency awareness at low cost |

### YouTube Metrics

- **View Rate:** Percentage of impressions where the user watched 30 seconds or the full ad (whichever is shorter). This is YouTube's equivalent of CTR for engagement.
- **Cost Per View (CPV):** What you pay per view. Typically $0.03-$0.10 for skippable in-stream.
- **View-Through Conversions:** People who saw your ad and later converted without clicking. Same incrementality caveats as Meta view-through attribution.

### YouTube for Ecommerce

YouTube is primarily an upper/mid-funnel channel. It drives awareness and consideration more than direct response. Use it alongside Search and Shopping, not as a replacement.

**When YouTube works for DR:** Product demos, testimonials, and offer-driven video ads with clear CTAs can drive direct conversions, but expect higher CPAs than Search or Shopping.

---

## Campaign Type: Display

### How It Works

Display campaigns show image and responsive ads across Google's Display Network — millions of websites, apps, and Google properties.

**Display is primarily a reach and remarketing channel.** Prospecting on Display tends to have very low CVR and should be evaluated with incrementality in mind.

### Display for Remarketing

Display remarketing (showing ads to people who visited your site) is Display's strongest use case. The targeting is precise (you know who these people are) and the creative can be personalized to what they viewed.

**Incrementality caveat:** Like Meta retargeting, Display remarketing is at high risk of taking credit for conversions that would have happened organically. Run holdout tests to validate.

### Display for Prospecting

Prospecting on Display reaches people who have not visited your site. Targeting options include interests, in-market audiences, custom audiences, and topic targeting.

**Expect:** Low CTR (0.1-0.5%), low CVR, low cost per impression. Display prospecting is an awareness play, not a conversion play. Evaluate it on reach and brand lift, not CPA.

---

## Campaign Type: Demand Gen

### How It Works

Demand Gen is Google's answer to Meta's feed-based advertising. It serves visual ads (images and video) across YouTube, Discover, and Gmail — environments where users are browsing content rather than searching with intent.

**Demand Gen feels most like Meta advertising** — you provide creative, target audiences, and the algorithm finds people in a content consumption mindset. It is designed for mid-funnel consideration and discovery.

### When to Use Demand Gen

- When you want to run visual/video ads on Google's properties in a way that is similar to Meta's approach
- When you have strong creative assets (images, video) that perform well in feed environments
- When Search and Shopping are maxed out and you need to expand into upper-funnel inventory
- When the client has budget for awareness and consideration, not just bottom-funnel conversion

### Demand Gen vs. PMax

| | Demand Gen | PMax |
|---|---|---|
| **Inventory** | YouTube, Discover, Gmail only | All Google properties |
| **Control** | More creative and audience control | Less control, more automation |
| **Optimization** | Conversions, clicks, or conversion value | Conversions or conversion value only |
| **Best for** | Mid-funnel, visual storytelling, brand awareness | Full-funnel, maximum reach, direct response |

---

## Google's "Power Pack" (2025-2026)

Google now recommends running three campaign types together:

1. **Performance Max** — Full-funnel performance across all inventory
2. **Demand Gen** — Mid-funnel awareness and consideration
3. **AI Max for Search** — Enhanced Search with AI-driven query matching and creative

**Our take:** For most ecommerce accounts, PMax + standard Search is the core. Demand Gen is additive if you have the creative and budget for upper-funnel investment. AI Max for Search is still maturing — test cautiously.

---

## How This Connects to the SOP Framework

| SOP Concept | Google Ads Connection |
|---|---|
| **CPM** (02) | Less relevant for Search (CPC-based) but critical for Display, YouTube, and Demand Gen |
| **CTR** (02) | Directly impacts Quality Score in Search → lower CTR = higher CPCs. Critical in Shopping (product image, title, price). |
| **CVR** (02) | Landing page experience is a Quality Score factor. Google rewards pages that convert. |
| **Creative Metrics** (05) | Video view rate and engagement on YouTube. Asset performance ratings in PMax. RSA headline/description testing in Search. |
| **Attribution** (08) | Google defaults to data-driven attribution which distributes credit across touchpoints. Compare DDA to last-click for context. |
| **Incrementality** (09) | Brand Search and Display remarketing are the highest-risk campaign types for attribution inflation. PMax can also cannibalize existing campaigns. |
| **Contribution Margin** (10) | Use conversion value tracking to send revenue or margin data to Smart Bidding. This enables value-based optimization. |

---

## Recommended Reading (Primary Sources)

- Google Ads Help Center: https://support.google.com/google-ads/
- Google Ads Blog: https://blog.google/products/ads-commerce/
- Think with Google: https://www.thinkwithgoogle.com/
- Google Merchant Center Help: https://support.google.com/merchants/
