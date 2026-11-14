# Google Ads — Advanced Operations

## Tools, Tactics, and Protections That Separate Good From Great

This document covers the operational tools and advanced features that most media buyers either don't know about or don't use consistently. These are force multipliers — they protect budget from waste, help Smart Bidding react to known events, and automate monitoring that would otherwise require hours of manual checking.

**Read `algorithm-overview.md` and `best-practices.md` first.** This document assumes you understand the campaign types and bidding systems.

---

## 1. Exclusion Lists (Placement, Channel, and App Exclusions)

### Why This Matters

Performance Max, Display, YouTube, and Demand Gen campaigns can serve ads across millions of placements. Many of those placements are low-quality: spammy apps, made-for-advertising websites, kids' YouTube channels, and irrelevant content. Without exclusion lists, you are paying for impressions and clicks from users who will never convert.

**This is one of the highest-ROI activities in Google Ads management.** Applying a pre-built exclusion list on day one of any Display, YouTube, or PMax campaign immediately eliminates the worst offenders.

### Types of Exclusions

| Exclusion Type | What It Blocks | Where to Apply | Campaign Types |
|---|---|---|---|
| **Placement exclusions** | Specific websites and YouTube channels | Account level or campaign level | Display, YouTube, Demand Gen, PMax (account-level only) |
| **App category exclusions** | Entire categories of mobile apps | Campaign level (Display) | Display |
| **Topic exclusions** | Content topics (e.g., "sensitive subjects") | Campaign level | Display, YouTube |
| **Content suitability settings** | Brand safety categories (tragedy, conflict, mature) | Account level | All campaign types |

### Pre-Built Exclusion Lists

Maintain these as shared lists in the account. Apply to every new campaign on launch.

#### Mobile App Exclusions (Apply to Display and PMax)

Mobile app placements are notorious for accidental clicks (fat-finger clicks from game players, kids tapping ads). Unless you are specifically targeting app users, exclude mobile app inventory:

**How to exclude all app placements in Display:**
- Campaign Settings → Placements → Exclusions
- Add `adsenseformobileapps.com` as a placement exclusion
- This blocks all AdSense-for-mobile-apps inventory

**For PMax:** App exclusions are limited. Use account-level placement exclusions and contact your Google rep for additional options.

#### YouTube Channel Exclusion List

Maintain a shared list of YouTube channels that consistently produce wasted spend. Common categories to exclude:

- **Kids/nursery rhyme channels** — high impressions, zero purchase intent from the actual viewer (children)
- **ASMR / ambient noise channels** — users are listening/sleeping, not shopping
- **Music video compilations** — high-frequency views, low engagement with ads
- **Foreign language channels** (if targeting English-only markets)
- **Prank / clickbait channels** — low-quality audience for ecommerce
- **Auto-play/loop channels** — channels designed to rack up views through autoplay

**How to build the list:**
1. Run YouTube campaigns for 2-4 weeks
2. Pull the Placements report (Where Ads Showed)
3. Filter for placements with high spend and zero conversions
4. Add those channels to a shared exclusion list
5. Share the list across all YouTube and Demand Gen campaigns
6. Update the list monthly

**Industry resources:** Several community-maintained YouTube exclusion lists exist online. Search for "YouTube placement exclusion list" and start with one of these, then refine based on your own data.

#### Website/Display Placement Exclusion List

Similar approach for Display:

**Common categories to exclude:**
- **Parked domains** — websites with no real content
- **Made-for-advertising (MFA) sites** — sites that exist solely to serve ads, with no genuine content
- **Game/puzzle sites** — accidental clicks
- **Weather apps and sites** — high traffic, low commercial intent for most products
- **File converter/tool sites** — users are trying to complete a task, not shop

**How to build the list:**
1. Run Display campaigns for 2-4 weeks
2. Pull the Placements report
3. Sort by cost descending, filter for zero conversions
4. Visit the top-spending zero-conversion sites to assess quality
5. Add garbage sites to a shared exclusion list
6. Apply to all Display campaigns and update monthly

### Content Suitability Settings

**Set these at the account level on day one:**

Navigate to: Tools → Content Suitability

- **Exclude:** Sensitive social issues, tragedy and conflict, sexually suggestive content, sensational and shocking content
- **Exclude types:** Embedded videos, live streaming, games (for ecommerce accounts)
- Set the **Digital content label exclusions** to exclude DL-MA (mature audiences) at minimum

These settings apply across Display, YouTube, and Demand Gen.

---

## 2. Seasonality Adjustments

### What It Is

Seasonality adjustments let you tell Smart Bidding about *expected future changes in conversion rate* for short-term events. This is critical because Smart Bidding optimizes based on recent historical data — when a flash sale or promotional event causes a sudden CVR spike, the algorithm may take days to catch up. Seasonality adjustments let it respond immediately.

### When to Use

| Scenario | Use Seasonality Adjustment? | Why |
|---|---|---|
| 3-day flash sale with expected 40% CVR increase | **Yes** | Short event, known CVR change, Smart Bidding won't react fast enough |
| Black Friday weekend | **Yes** | Sharp, short CVR spike that Smart Bidding might under-bid for |
| The entire month of December | **No** | Smart Bidding already accounts for gradual seasonal trends. A 30-day adjustment will cause it to double-count. |
| New product launch with unknown CVR | **No** | You are guessing. Seasonality adjustments require a data-backed estimate. |
| Post-holiday CVR drop (January) | **Maybe** | If CVR drops sharply and you want Smart Bidding to pull back faster, a slight negative adjustment for the first few days can help. |

### How to Set It Up

1. Navigate to: Tools → Budgets and Bidding → Adjustments
2. Select "Seasonal" → Click the blue "+" button
3. Adjustment type: **Conversion Rate**
4. Name it clearly (e.g., "BFCM 2026 — Expected +50% CVR")
5. Set start and end dates (keep to 1-7 days)
6. Choose scope: All campaigns, specific campaign types, or specific campaigns
7. Enter the conversion rate modifier (e.g., 1.5 for a 50% expected increase)
8. Click Save

### Critical Rules

**Use historical data to set the modifier.** Pull last year's promotional period data. If CVR went from 2.0% to 3.2% during last year's Black Friday, that is a 60% increase. Set your modifier at 1.5-1.6 (being slightly conservative).

**Do not overestimate.** If you set a 100% CVR increase but only get a 30% increase, Smart Bidding will have bid too aggressively and your CPCs will spike without the conversion volume to justify them.

**Be aware of CPC impact.** When you tell Smart Bidding to expect higher CVR, it will bid more aggressively (higher CPCs) to capture that expected volume. This is intentional, but it means your spend will increase. Make sure budget is available to support the higher bid levels.

**No negative adjustment needed after the event.** Smart Bidding automatically reverts to pre-event behavior once the adjustment period ends. Do not create a separate "post-event" negative adjustment unless you have specific data showing CVR drops below the pre-event baseline.

**Maximum 14 days.** Seasonality adjustments are designed for 1-7 day events and become less effective beyond 14 days. For gradual seasonal changes (Q4 buildup, summer slowdown), let Smart Bidding handle it naturally.

### Seasonality Adjustment Calendar Template

Maintain this for each client:

| Event | Dates | Expected CVR Change | Modifier | Campaigns | Notes |
|---|---|---|---|---|---|
| Valentine's Day Sale | Feb 12-14 | +30% | 1.3 | Search, Shopping, PMax | Based on 2025 data |
| Spring Flash Sale | Apr 5-7 | +25% | 1.25 | All | First time — conservative |
| Memorial Day Sale | May 24-27 | +35% | 1.35 | Search, Shopping, PMax | Based on 2025 data |
| Prime Day (defensive) | Jul TBD | +20% | 1.2 | Shopping, PMax | Competitive pressure |
| Labor Day Sale | Aug 30 - Sep 1 | +30% | 1.3 | All | Based on 2025 data |
| Black Friday | Nov 27-29 | +60% | 1.5 | All | Based on 2025; be conservative |
| Cyber Monday | Nov 30 - Dec 1 | +50% | 1.4 | All | Slightly lower than BF historically |

---

## 3. Negative Keyword Strategy (Advanced)

### Shared Negative Keyword Lists

Create and maintain shared lists that apply across campaigns. This ensures new campaigns automatically inherit your exclusions.

**Recommended shared lists:**

#### List 1: "Universal Negatives"
Terms that are irrelevant for virtually any ecommerce account:

```
free
cheap
diy
homemade
how to make
tutorial
jobs
careers
salary
reviews (if you don't want review-intent traffic)
reddit
youtube
amazon (if you don't sell on Amazon)
ebay
walmart
used
refurbished
template
printable
coupon code (if you don't offer coupons)
class action
lawsuit
recall
scam
```

#### List 2: "Brand Defense Negatives" (Apply to non-brand campaigns only)
Your own brand name variations — prevents non-brand campaigns from spending on branded queries that the Brand Search campaign should handle:

```
[your brand name]
[your brand name misspellings]
[your brand name abbreviations]
```

#### List 3: "Competitor Negatives" (Apply selectively)
Competitor brand names — apply to campaigns where you do not want to bid on competitor terms:

```
[competitor 1 brand name]
[competitor 2 brand name]
```

#### List 4: Client-Specific Negatives
Industry-specific irrelevant terms. Build this from the search term report over the first 30-60 days.

### Negative Keyword Maintenance Cadence

| Account Spend | Search Term Review Frequency | Action |
|---|---|---|
| Under $5,000/month | Weekly | Add negatives, review match type drift |
| $5,000-$20,000/month | 2-3x per week | Same, plus check broad match expansion |
| $20,000+/month | Daily | Automated alerts + daily manual review |

---

## 4. Google Ads Scripts (Automated Monitoring)

### What Scripts Are

Google Ads Scripts are JavaScript snippets that run automatically in your account on a schedule. They can monitor performance, send alerts, make changes, and generate reports. For a media buyer, scripts replace hours of manual checking.

### High-Value Scripts to Implement

#### Script 1: Spend Pacing Alert
Sends an email alert if daily spend is significantly above or below the expected pace.

**What it does:** Checks if yesterday's spend was more than 30% above or below the expected daily budget. If so, sends an email alert.

**Why it matters:** Catches budget overdelivery (algorithm spending too fast), underdelivery (ads not running due to disapprovals or billing issues), and billing errors.

#### Script 2: CPA Spike Alert
Sends an alert if CPA exceeds a threshold over a rolling 3-day window.

**What it does:** Calculates the 3-day rolling CPA for each campaign. If any campaign exceeds 150% of its target CPA for 3 consecutive days, sends an alert.

**Why it matters:** Catches performance degradation before it becomes a trend. Faster than waiting for the weekly review.

#### Script 3: Landing Page / Link Checker
Checks all final URLs in active ads and alerts if any return an error code (404, 500, etc.).

**What it does:** Crawls all active ad final URLs once per day. If any URL returns a non-200 HTTP status code, sends an alert.

**Why it matters:** Broken landing pages waste 100% of ad spend directed to them. This catches site issues before you notice in the metrics.

#### Script 4: Search Term Auto-Negative
Automatically adds negative keywords for search terms that have spent above a threshold with zero conversions.

**What it does:** Reviews search terms from the last 14 days. If a term has spent more than 2x the target CPA with zero conversions, adds it as a negative keyword.

**Why it matters:** Automates the most tedious part of Search management. Use with caution — review the auto-added negatives weekly to catch false positives.

#### Script 5: Quality Score Tracker
Logs Quality Score for all keywords weekly to a Google Sheet, allowing you to track trends over time.

**Why it matters:** Quality Score changes are invisible in the default interface (you only see the current score, not the trend). Tracking over time reveals whether ad copy and LP changes are improving or degrading relevance.

### Where to Find Scripts

- Google Ads Scripts documentation: https://developers.google.com/google-ads/scripts
- Community script libraries (search "Google Ads scripts library")
- Ask Claude Code to write custom scripts based on your specific alert requirements

### Script Installation

1. Navigate to: Tools → Bulk Actions → Scripts
2. Click the "+" button to create a new script
3. Paste the script code
4. Authorize the script to access your account
5. Set a schedule (daily, hourly, or weekly depending on the script)
6. Test with "Preview" before enabling

---

## 5. Enhanced Conversions and Data Manager

### Enhanced Conversions

Enhanced Conversions sends hashed first-party customer data (email, phone, address) to Google alongside your conversion tag. This improves conversion measurement accuracy — especially for users who click on one device and convert on another, or who have privacy settings that block standard tracking.

**Setup checklist:**
- [ ] Enable Enhanced Conversions in Google Ads (Settings → Measurement → Enhanced Conversions)
- [ ] Implement via Google Tag Manager or the global site tag
- [ ] Ensure you are collecting email at the conversion point (checkout confirmation page)
- [ ] Verify in the Diagnostics tab that match rates are healthy (>60%)

### Data Manager

Data Manager (found under Tools) is Google's hub for connecting first-party data sources to your ads account. Key uses:

- **Customer Match uploads:** Upload your customer email list so Google can match them to signed-in Google users. Use for audience signals in PMax and remarketing.
- **Enhanced Conversions for Leads:** If running lead gen, connect your CRM to feed back which leads actually became customers. This trains Smart Bidding on *lead quality*, not just lead volume.
- **Offline conversion imports:** If conversions happen offline (phone orders, in-store), import them so the algorithm can optimize toward these high-value events.

**Why this matters for Smart Bidding:** Every additional data point you give Google improves the algorithm's ability to predict which users will convert. Enhanced Conversions and CRM integration are the biggest signal quality improvements you can make after basic pixel setup.

---

## 6. Campaign Groups and Shared Budgets

### Campaign Groups

Campaign groups let you set a shared performance target (CPA, ROAS) across multiple campaigns and track aggregate performance against that target.

**When to use:**
- When you have multiple campaigns that contribute to the same business goal (e.g., Search + Shopping both driving purchases)
- For aggregate budget management across campaigns
- For reporting to clients — shows total performance across campaign types

**How to set up:** Tools → Budgets and Bidding → Campaign Groups

### Shared Budgets

Shared budgets pool a single daily budget across multiple campaigns. Google allocates spend dynamically to whichever campaign is performing best at any given moment.

**When to use:**
- When you have several campaigns targeting similar audiences and want Google to optimize budget allocation between them
- For accounts where individual campaign budgets are too small for meaningful optimization

**When to avoid:**
- When campaigns have different objectives (don't share budget between a brand campaign and a prospecting campaign)
- When you need precise budget control per campaign type
- PMax campaigns — do not combine PMax with other campaign types in a shared budget

---

## 7. Google Ads Editor and Bulk Operations

### Google Ads Editor

Google Ads Editor is a free desktop application for making bulk changes offline, then uploading them to your account. Essential for:

- **Launching new campaigns** with many ad groups, keywords, and ads
- **Bulk bid adjustments** across hundreds of keywords
- **Copying campaign structures** between accounts (useful for similar clients)
- **Reviewing account structure** — Editor gives a clearer visual hierarchy than the web interface
- **Making changes during off-hours** — build changes offline, upload when ready

### Bulk Actions in the Web Interface

For smaller-scale bulk operations without Editor:
- **Bulk edits:** Select multiple campaigns/ad groups/ads → Edit → Change bids, status, budgets
- **Upload via spreadsheet:** Tools → Bulk Actions → Uploads → Download a template, make changes in a spreadsheet, re-upload
- **Automated rules:** Set conditions for automatic changes (e.g., "pause any keyword with CPA > $100 over the last 14 days")

---

## 8. Operational Cadence Summary

### Daily (15 minutes)
- [ ] Check spend pacing (automated script alert or manual check)
- [ ] Review any script alerts (CPA spikes, broken pages)
- [ ] Scan for ad disapprovals
- [ ] Check for billing or account issues

### Weekly (1-2 hours)
- [ ] Review search term report — add negative keywords
- [ ] Check PMax channel breakdown — flag excessive Display/YouTube spend
- [ ] Review placement reports (YouTube/Display) — add exclusions
- [ ] Check frequency and CPM trends
- [ ] Review creative/asset performance ratings
- [ ] Pull 7-day vs. prior 7-day metrics for all core KPIs

### Monthly (2-3 hours)
- [ ] Full 30-day vs. prior 30-day analysis
- [ ] Update exclusion lists based on new placement data
- [ ] Review and refresh seasonality adjustment calendar
- [ ] Audit conversion tracking accuracy (compare platform data vs. backend)
- [ ] Review Quality Score trends (from script-generated tracker)
- [ ] Evaluate campaign structure — consolidate or expand as needed
- [ ] Update shared negative keyword lists
- [ ] Check Enhanced Conversion match rates and Data Manager connections

### Quarterly (Half-day)
- [ ] Full account audit — structure, settings, tracking, attribution
- [ ] Incrementality assessment — compare platform-reported vs. backend data
- [ ] Budget allocation review based on contribution margin by campaign
- [ ] Creative library refresh and production planning
- [ ] Exclusion list overhaul — review all placements, channels, apps
- [ ] Seasonality adjustment planning for next quarter
