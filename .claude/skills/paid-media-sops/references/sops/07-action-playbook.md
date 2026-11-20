# 07 — Action Playbook

## What to Do When You Know What Broke

The diagnostic engine (04) tells you *what* broke. This document tells you *exactly what to do about it*. Every action is specific, sequenced, and testable.

---

## Playbook 1: CPM Too High

**Diagnosis:** Cost per 1,000 impressions has risen beyond the level where the account can maintain target CPA.

### Step 1: Identify the CPM driver (Day 1)

Pull a placement breakdown for the affected campaigns. Identify which placements are driving the CPM increase:

- **Export the placement report** from the platform (Facebook Feed, Instagram Stories, Audience Network, Reels, etc.)
- **Sort by CPM descending.** Identify any placement where CPM is 30%+ above the campaign average.
- **Cross-reference with CVR.** A high-CPM placement with high CVR may still be profitable. A high-CPM placement with low CVR is dead weight.

### Step 2: Check frequency and CPMr (Day 1)

- **Pull frequency data** for the last 7 and 14 days.
- **If frequency > 3.0 in a 7-day window:** Audience saturation is a primary driver. Proceed to Step 3a.
- **If frequency < 2.5 and CPMr is rising proportionally to CPM:** Market-level inflation. Proceed to Step 3b.

### Step 3a: Fix frequency-driven CPM (Days 2-5)

1. **Exclude high-frequency audiences.** Create an exclusion for users who have seen the ad 4+ times (if the platform supports frequency-based exclusions). On Meta, you can create a custom audience of people who engaged with the ad and exclude them.
2. **Refresh creative.** Launch 3-5 new ad variations with different hooks and visual styles. Keep the offer the same — you are fighting ad fatigue, not changing the strategy.
3. **Expand the audience.** If running interest-based targeting, add adjacent interests or switch to broad. If running lookalikes, test a larger seed (1-3% → 5-10%) or a new seed audience (purchasers → top 25% LTV customers).
4. **Test new placements.** If you have been running Feed-only, add Reels and Stories. Different placements reach different users even within the same audience.

### Step 3b: Fix market-driven CPM (Days 2-7)

1. **Check seasonal context.** If this is Q4, pre-holiday, or a competitive sales period (Prime Day, etc.), elevated CPMs are expected. Calculate whether the business can sustain current CPMs at current conversion rates.
2. **Test alternative placements.** Move 20-30% of budget to lower-CPM placements and measure whether CPA improves despite potential CTR/CVR differences.
3. **Test alternative platforms.** If Meta CPMs are inflated, test allocating budget to TikTok, Google Display, or YouTube where auction dynamics may be more favorable.
4. **Reduce spend temporarily.** If CPMs are seasonal and you cannot maintain target CPA, reducing spend during peak-cost periods and reinvesting during the post-peak dip is a legitimate strategy.
5. **Optimize bid strategy.** On Meta, test switching from "lowest cost" to "cost cap" at your target CPA. This tells the algorithm you would rather spend less than pay inflated CPMs. On Google, test target CPA or target ROAS bidding if not already using them.

---

## Playbook 2: CTR Too Low

**Diagnosis:** Click-through rate has dropped below the threshold where the account can generate enough clicks to hit conversion targets.

### Step 1: Determine the scope (Day 1)

- **All campaigns affected?** Likely a creative fatigue issue across the account or a broad audience problem.
- **Specific campaigns affected?** Isolate to those campaigns. The creative or audience within them is the issue.
- **Specific ads affected?** The individual ad is fatigued or underperforming. Kill it and replace.

### Step 2: Check creative health (Day 1)

- For video ads, pull hook rate and hold rate. See `05-creative-metrics.md` for the diagnostic matrix.
- For static ads, check engagement metrics (saves, shares, comments). Low engagement alongside low CTR confirms the creative is not resonating.
- **Check ad frequency at the ad level.** An ad with frequency > 4 over 14 days is almost certainly fatigued. Replace it.

### Step 3: Launch new creative (Days 2-4)

**For video ads:**

1. **Audit the top 3 performing hooks** from the last 90 days. What visual style, opening line, or format drove the best hook rates?
2. **Create 5 new hooks** using those winning patterns but with fresh execution:
   - New talent (different person on camera)
   - New setting (different location or background)
   - New angle on the same product benefit
   - New format (if UGC worked before, try product demo; if demo worked, try UGC)
   - New text overlay with a different curiosity hook
3. **Pair new hooks with the best-performing body and CTA** from existing creative. You are testing hooks, not rebuilding the entire video.
4. **Launch in the existing ad set** alongside the fatigued creative. Let the algorithm allocate based on performance. Kill the fatigued ad after 3-5 days if new creative is performing.

**For static ads:**

1. **Test 3-5 new images** with the same copy. Visual fatigue is the most common cause of static ad CTR decline.
2. **Test 2-3 new headline/primary text combinations** with the best-performing image. If images are fresh but CTR is still low, the copy is the problem.
3. **Test a format change.** If you have been running single-image ads, test carousel or collection ads. Different formats attract different attention patterns.

### Step 4: Review targeting (Days 3-7)

If new creative does not recover CTR within 5-7 days:

1. **Check audience overlap.** If multiple ad sets are targeting similar audiences, they may be competing against each other and inflating frequency without you realizing it. Use the platform's audience overlap tool.
2. **Test a new audience.** Build a new lookalike from a different seed (email list, high-LTV customers, add-to-cart events). Launch with the best-performing creative.
3. **Test broad targeting.** Remove all interest and lookalike constraints and let the algorithm find the audience. Monitor CTR and CVR carefully for the first 7 days.

---

## Playbook 3: CVR Too Low

**Diagnosis:** People are clicking through to the landing page but not converting.

### Step 1: Rule out technical issues (Day 1 — do this first, always)

1. **Click the ad yourself.** On mobile. With a slow connection if possible. Does the page load? Is the checkout functional? Can you complete a test purchase?
2. **Check page load speed.** Use Google PageSpeed Insights or the platform's LP quality tools. Target < 3 second load time on mobile. Every second above 3 costs you ~7% CVR.
3. **Check click-to-LP-view drop-off.** If more than 20% of clicks are not registering as LP views, you have a load speed or redirect issue that is killing conversions before they have a chance to happen.
4. **Check the pixel/conversion tracking.** Verify conversions are firing correctly. Use the platform's event testing tools (Meta Events Manager test events, Google Tag Assistant, etc.).

### Step 2: Audit ad-to-LP congruence (Day 1-2)

Side-by-side the ad and the landing page:

- **Does the LP headline match the ad's promise?** If the ad says "50% off first order" and the LP headline says "Premium skincare for discerning customers," there is a congruence gap.
- **Is the offer visible above the fold on mobile?** The majority of ad traffic lands on mobile. If the offer requires scrolling to find, you will lose people.
- **Does the LP visual style match the ad?** If the ad is bright and bold but the LP is minimal and muted, the transition feels jarring.
- **Is the CTA clear and prominent?** "Add to Cart" or "Buy Now" should be visible without scrolling on mobile.

### Step 3: LP optimization (Days 3-14)

If the LP itself is the problem:

1. **Simplify the page.** Remove navigation bars, footer links, and anything that distracts from the conversion action. The LP's job is one thing: convert the click into a sale.
2. **Add trust signals above the fold.** Reviews, ratings, "as seen in" logos, money-back guarantee — whatever reduces purchase anxiety for a first-time buyer.
3. **Test a dedicated LP for the campaign.** Rather than sending ad traffic to the homepage or a generic product page, create a purpose-built page that continues the ad's story. This is high-effort but high-impact.
4. **Optimize for mobile first.** Check button sizes (minimum 44x44px tap targets), form field usability, image load times, and scroll depth on mobile.
5. **A/B test changes.** Use a tool like Google Optimize, VWO, or the platform's built-in LP testing if available. Test one change at a time for clean learnings. Minimum 100 conversions per variant before calling a winner.

### Step 4: Evaluate audience quality (Days 3-7)

If the LP is functional and congruent but CVR is still low:

1. **Segment CVR by campaign type.** Prospecting CVR should be 1-2% for ecommerce. Retargeting should be 3-8%. If prospecting CVR is below 0.5%, the audience is too broad or the creative is attracting low-intent clicks.
2. **Check the search term report (Google).** For search campaigns, low CVR often means you are matching to irrelevant queries. Add negative keywords aggressively.
3. **Check the product-page match (Shopping).** For Google Shopping, ensure the ad is showing for queries relevant to the product. A low CVR on a specific product may mean the product listing needs optimization (title, images, price).

---

## Playbook 4: AOV Too Low

**Diagnosis:** Conversions are happening but the average order value is below target.

### Step 1: Check product-level data (Day 1)

- **Which products are being purchased through this campaign?** If the campaign is driving sales of your cheapest SKU, the creative or audience may be attracting price-sensitive buyers.
- **Is the product mix different from organic or direct traffic?** Compare ad-driven AOV to site-wide AOV. If ad-driven AOV is significantly lower, the ads are attracting a different buyer segment.

### Step 2: Creative adjustments (Days 2-5)

1. **Feature higher-value products in ad creative.** If ads show the $29 product but you want to sell the $79 bundle, change the creative to showcase the bundle.
2. **Lead with value, not price.** Creative that leads with "Starting at $19" attracts bargain shoppers. Creative that leads with the benefit ("Clear skin in 14 days") attracts value-oriented buyers who may spend more.
3. **Test bundle-specific ads.** Create dedicated campaigns for product bundles or higher-AOV offerings with creative that explains the bundle value.

### Step 3: On-site AOV optimization (Days 3-14)

These are not ad account changes — they are site changes. But the media buyer should advocate for them:

1. **Free shipping threshold.** Set it at 10-15% above current AOV. If AOV is $45, offer free shipping at $50-$55. This is one of the most reliable AOV levers.
2. **Post-add-to-cart upsell.** After someone adds a product to cart, show a relevant upsell ("Complete the set for 15% off"). This is high-conversion because intent is already established.
3. **Bundle pricing.** Show the per-unit savings of buying 2-3 at a time. "1 for $29 / 3 for $69 (save 20%)" encourages larger baskets.
4. **Minimum order incentives.** "Spend $75, get a free [accessory]" creates a concrete AOV target for the shopper.

### Step 4: Audience strategy (Days 5-10)

1. **Build lookalikes off high-AOV purchasers.** Export a list of customers with AOV > $X and create a lookalike audience. These models often find people with higher purchase intent and larger basket sizes.
2. **Separate campaigns by price tier.** Run dedicated campaigns for premium products targeting audiences with higher estimated income or interest in premium categories.

---

## Playbook 5: Spend Not Delivering

**Diagnosis:** The daily budget is not being fully spent. The platform cannot find enough impressions at the current settings.

### Step 1: Check the obvious (Day 1)

1. **Ad disapprovals.** Check if any ads were disapproved by the platform. A disapproved ad in a single-ad ad set means zero delivery.
2. **Audience size.** Is the target audience large enough to support the daily budget? A $100/day budget against a 10,000-person audience will exhaust quickly.
3. **Bid cap too restrictive.** If using cost cap or bid cap, the ceiling may be too low for the current auction environment. Raise it by 20-30% or switch to lowest cost temporarily to understand the current market clearing price.

### Step 2: Expand the opportunity set (Days 2-3)

1. **Broaden targeting.** Add placements, expand age ranges, add geos, move from interest to broad.
2. **Add creative.** More ad variations give the algorithm more options to find efficient impressions. Launch 3-5 new ads in the underdelivering ad set.
3. **Consolidate ad sets.** If you have 10 ad sets each with $50/day targeting similar audiences, the algorithm is fragmented. Consolidate into 2-3 ad sets with $200-$300/day each for better optimization.

### Step 3: Restructure if needed (Days 5-7)

If the campaign still will not spend after broadening:

1. **Kill the campaign and rebuild.** Sometimes campaigns enter a "dead" state where the algorithm has learned to avoid spending. Launch a fresh campaign with the same creative and targeting.
2. **Check account-level issues.** Billing problems, account restrictions, or policy violations can throttle delivery across the entire account.

---

## Playbook 6: Everything Looks Fine But the Client Says Revenue Is Down

**Diagnosis:** All five core metrics are stable or improving, but the client reports that actual business revenue is declining.

This is the gap between platform metrics and business reality. See `09-incrementality-bridge.md` for the full framework, but the immediate actions are:

### Step 1: Check attribution settings (Day 1)

- Confirm the attribution window has not changed. A shift from 7dc/1dv to 7dc/7dv can inflate reported conversions without any real change.
- Compare platform-reported conversions to actual orders in the client's system (Shopify, backend database, etc.).

### Step 2: Check for cannibalization (Days 1-3)

- Is the ad spend capturing demand that would have happened organically? Check whether organic and direct traffic decreased as ad spend increased.
- Is retargeting taking credit for purchases that were already in progress? Check the time-from-click-to-conversion distribution.

### Step 3: Run an incrementality test (Days 7-30)

- The only reliable way to know if ads are actually driving incremental revenue is to measure it causally. See `09-incrementality-bridge.md` for holdout test design.

---

## Decision Speed Guidelines

Not every diagnosis requires the same urgency:

| Situation | Response Time | Why |
|---|---|---|
| Site/checkout broken (CVR collapse) | Immediate — within hours | Every hour of downtime = lost revenue |
| Tracking break (conversions not firing) | Same day | Cannot optimize without data |
| Creative fatigue (gradual CTR decline) | Within 3-5 days | Not urgent but will get worse. Start new creative. |
| CPM inflation (seasonal) | Monitor for 1-2 weeks | May be temporary. Do not overreact to seasonal patterns. |
| Budget scale degradation | Evaluate after 5-7 days at new level | Algorithm needs time to learn. Give it a clean window. |
| AOV decline | Within 1-2 weeks | Slower-moving issue. Requires site changes, not just ad changes. |
| Incrementality concerns | Ongoing (test over 2-4 weeks) | This is strategic, not tactical. Design a proper test. |
