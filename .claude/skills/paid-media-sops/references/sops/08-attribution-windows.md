# 08 — Attribution Windows

## Understanding What the Numbers Actually Mean

Every metric in your ad account is filtered through an attribution model. If you do not understand the attribution settings, you do not understand your data. This document explains attribution windows, why they matter, and how to use them for better decision-making.

---

## What Is an Attribution Window?

An attribution window defines the period of time after a user interacts with your ad during which a conversion can be credited to that ad.

**Example:** If your attribution window is "7-day click," and someone clicks your ad on Monday and purchases on Thursday (4 days later), the conversion is attributed to the ad. If they purchase the following Tuesday (8 days later), it is not.

---

## Attribution Window Types

### Click-Through Attribution

A conversion is credited to the ad if the user **clicked** the ad within the specified window and then converted.

| Window | Notation | Meaning |
|---|---|---|
| 1-Day Click | 1dc | User clicked the ad and converted within 24 hours |
| 7-Day Click | 7dc | User clicked the ad and converted within 7 days |
| 28-Day Click | 28dc | User clicked the ad and converted within 28 days (Meta legacy) |

### View-Through Attribution

A conversion is credited to the ad if the user **saw** (but did not click) the ad within the specified window and then converted.

| Window | Notation | Meaning |
|---|---|---|
| 1-Day View | 1dv | User saw the ad (no click) and converted within 24 hours |
| 7-Day View | 7dv | User saw the ad (no click) and converted within 7 days |

### Engaged View Attribution

A conversion is credited if the user **watched a meaningful portion of a video ad** (typically 10+ seconds or 97%+ completion) and then converted within the window. This sits between click-through and view-through — the user engaged with the ad more than a passive impression but did not click.

| Window | Notation | Meaning |
|---|---|---|
| 1-Day Engaged View | 1dev | User watched 10+ seconds of video ad and converted within 24 hours |

---

## Common Attribution Configurations

### Meta (Facebook/Instagram)

Default: **7-Day Click, 1-Day View (7dc/1dv)**

This means:
- If someone clicks your ad and buys within 7 days → attributed
- If someone sees your ad (no click) and buys within 1 day → attributed
- If someone sees your ad and buys 2 days later without clicking → NOT attributed (outside the 1-day view window)

Available settings: 1dc, 7dc, 1dv, 7dv (can be combined). You can also view results broken down by 1dc only, 7dc only, 1dv only in the reporting columns.

### Google Ads

Default varies by campaign type. Google uses model-based attribution (data-driven attribution as default) which distributes credit across multiple touchpoints.

Key windows:
- **Search/Shopping:** 30-day click, 1-day view for YouTube
- **PMax:** 30-day click, multiple model options
- **YouTube:** 1-day view, 1-day engaged view, 30-day click

### TikTok

Default: **7-Day Click, 1-Day View (7dc/1dv)**

Available: 1dc, 7dc, 14dc, 1dv, 7dv. Also supports view-through for video-specific reporting.

---

## Why Attribution Windows Matter for Decision-Making

### The Same Campaign Looks Different Under Different Windows

Consider a campaign that generated these interactions last week:

- 500 clicks, 200 of which led to a purchase within 1 day
- 150 more of those clicks led to a purchase between days 2-7
- 10,000 impressions (no click), 50 of which led to a purchase within 1 day
- 100 more impressions led to a purchase between days 2-7

Here is how the campaign's "performance" changes depending on the attribution window:

| Attribution Window | Attributed Conversions | CPA (at $5,000 spend) | ROAS (at $65 AOV) |
|---|---|---|---|
| 1-Day Click only | 200 | $25.00 | 2.6x |
| 7-Day Click only | 350 | $14.29 | 4.55x |
| 7dc + 1dv | 400 | $12.50 | 5.2x |
| 7dc + 7dv | 500 | $10.00 | 6.5x |

**The campaign did not change. The measurement lens changed.**

A media buyer looking at 7dc/7dv sees a 6.5x ROAS hero campaign. A media buyer looking at 1dc sees a 2.6x ROAS campaign that may or may not be profitable. Same spend, same actual customer behavior, radically different conclusions.

---

## The Incrementality Spectrum

Attribution windows exist on a spectrum of *likely incrementality*:

```
Most Likely Incremental ◄─────────────────────► Least Likely Incremental

1-Day Click     7-Day Click     1-Day Engaged View     1-Day View     7-Day View
```

**Why this spectrum exists:**

- **1-Day Click** conversions happened within 24 hours of a deliberate action (clicking the ad). The ad very likely played a causal role. But this window misses legitimate delayed conversions (someone who clicked, researched, and bought 3 days later).

- **7-Day Click** captures delayed conversions from clickers. Many of these are real — people research before buying. But as the window extends, the risk increases that the conversion would have happened without the ad (especially for branded search).

- **1-Day Engaged View** captures people who watched a video ad meaningfully and then converted within a day without clicking. Some of these are genuinely influenced. Others were already planning to buy and happened to see the ad in their feed.

- **1-Day View** captures anyone who saw an impression and converted within a day. This is where incrementality gets questionable. The ad may have been a 0.5-second flash in a scroll session that the user did not consciously process.

- **7-Day View** is the loosest window. Anyone who saw an impression in the last 7 days and converted gets attributed. At scale, this will capture a significant number of conversions that would have happened anyway — especially for well-known brands with organic demand.

---

## How to Use Attribution Windows Operationally

### Rule 1: Set a consistent default and do not change it

Pick one attribution window as your default reporting view and stick with it. Changing attribution settings mid-campaign makes period-over-period comparison impossible.

**Recommended default:** 7-Day Click, 1-Day View (7dc/1dv). This is the platform default on Meta and TikTok, and it provides a reasonable balance between capturing real conversions and avoiding excessive view-through inflation.

### Rule 2: Always check multiple windows for context

Even though you report on 7dc/1dv by default, periodically pull results under 1dc only. The gap between 7dc/1dv and 1dc tells you how much of your reported performance depends on delayed attribution and view-throughs.

| Scenario | 7dc/1dv CPA | 1dc CPA | Gap | Interpretation |
|---|---|---|---|---|
| A | $30 | $35 | 17% | Small gap. Most conversions happen within 1 day of a click. Attribution is relatively tight. |
| B | $30 | $60 | 100% | Large gap. Half the reported conversions come from delayed clicks and view-throughs. Incrementality risk is higher. |
| C | $30 | $150 | 400% | Extreme gap. The vast majority of attributed conversions are view-throughs. This campaign may be taking credit for organic demand. |

**When the gap is large (Scenario B or C):**
- Do not assume the campaign is underperforming (the 1dc view may be too narrow)
- Do not assume the campaign is a hero (the 7dc/1dv view may be too generous)
- This is a signal to run an incrementality test to understand the campaign's true contribution

### Rule 3: Compare like-for-like across campaigns

When comparing two campaigns, use the same attribution window. A prospecting campaign on 1dc will always look worse than a retargeting campaign on 7dc/1dv. That comparison is meaningless.

### Rule 4: Be especially skeptical of view-through heavy campaigns

If more than 40-50% of a campaign's total attributed conversions come from view-through (not click-through), treat the reported CPA/ROAS with caution. These campaigns are the most likely to be claiming credit for organic conversions.

**Common offenders:**
- Brand awareness campaigns with broad targeting
- Video campaigns optimized for views rather than clicks
- Retargeting campaigns with large audience pools
- Display/Audience Network placements

This does not mean these campaigns are valueless. It means their *platform-reported value* is likely overstated. The only way to know the true value is through incrementality measurement.

---

## Attribution and Retargeting: A Special Case

Retargeting campaigns deserve extra scrutiny on attribution:

**The retargeting attribution trap:**
1. A user visits your site organically (saw a friend's recommendation, searched on Google, typed in the URL)
2. They browse but do not buy
3. They are now in your retargeting audience
4. They see a retargeting ad the next day
5. They return to the site and purchase
6. The retargeting ad takes 100% credit for the conversion

**Was the retargeting ad incremental?** Maybe. The user was already aware of the brand and had shown purchase intent. The retargeting ad may have been the nudge that closed the sale — or the user may have come back on their own regardless.

**How to evaluate:**
- Check the time-from-impression-to-conversion distribution. If most retargeting conversions happen within 1-2 hours of the ad view, the ad may be "credit-stealing" from users who were already on a purchase path.
- Run a retargeting holdout test: suppress retargeting ads to 10-20% of eligible users and measure the conversion difference. This is the gold standard for retargeting incrementality.
- Compare retargeting CPA on 1dc vs. 1dv. If the 1dv number is dramatically lower (more conversions attributed via view-through), the campaign is likely over-credited.

---

## Platform-Specific Attribution Nuances

### Meta
- **Modeled conversions:** When iOS14+ privacy changes block conversion tracking, Meta "models" (estimates) conversions it cannot directly observe. These modeled conversions are included in your reporting and can make actual performance appear better than it is.
- **Aggregated Event Measurement (AEM):** Meta's privacy-compliant framework limits the number of conversion events and attribution windows you can optimize for. Understand which events are prioritized in your Events Manager.
- **Conversion API (CAPI):** Server-side event tracking that supplements the browser pixel. CAPI data is generally more reliable than pixel-only data, especially on iOS. Ensure CAPI is implemented and deduplicated with pixel events.

### Google
- **Data-Driven Attribution (DDA):** Google's default model distributes credit across multiple touchpoints using machine learning. This makes it harder to evaluate individual campaign performance but theoretically gives a more "fair" credit distribution.
- **Last-click vs. DDA:** You can still view results under last-click attribution in reporting. Compare DDA to last-click to understand how Google is distributing credit. Large gaps between the two suggest the campaign is getting credit from earlier touchpoints, not just the final click.

### TikTok
- **View-through attribution is aggressive on TikTok.** The feed is fast — users see many ads in a session. 1dv on TikTok can capture a lot of "impressions" that were sub-second exposures. Be cautious with view-through heavy TikTok reporting.
- **Self-Attributing Network (SAN):** TikTok is a SAN, meaning it reports its own conversions independently. Third-party attribution tools (Rockerbox, Triple Whale, etc.) may show different numbers than TikTok's own reporting.

---

## Checklist: Attribution Window Review

Use this checklist when onboarding a new client or auditing an existing account:

- [ ] What attribution window is set as the default in the ad account?
- [ ] Is the same window used across all campaigns? (If not, comparisons are unreliable.)
- [ ] What percentage of total attributed conversions are view-through vs. click-through?
- [ ] How large is the gap between 1dc and 7dc/1dv CPA?
- [ ] Is Conversion API (CAPI) implemented and deduplicated with the pixel?
- [ ] Are modeled conversions a significant percentage of total reported conversions?
- [ ] Has anyone changed the attribution settings recently? (This invalidates period-over-period comparisons.)
- [ ] Does the client understand that platform-reported ROAS is not the same as true ROAS?
