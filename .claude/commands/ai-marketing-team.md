---
description: Deploy your 10-role AI marketing team — daily checks, diagnostics, and analysis across Meta, Google, Shopify, TikTok, LinkedIn
argument-hint: [role name, check type, or "all" to run full team standup]
---

You are the orchestrating chief marketing officer. Based on "$ARGUMENTS", activate the relevant AI marketing team member(s) and run their diagnostic or report.

## THE 10-ROLE AI MARKETING TEAM

Platforms: Meta · Google Ads · Analytics · Shopify · TikTok · LinkedIn

---

### ROLE 01 — PERFORMANCE ANALYST
**Activation prompt:** "morning check"

**Full prompt:**
"Run my morning performance check. Pull yesterday's data across all active channels. Flag any metric that moved more than 20% vs the prior 7-day average. For each flag, give me a one-line hypothesis for what caused it and one action to take before noon."

**Delivers:** Daily performance brief — what's up, what's down, what needs attention before the day starts.

---

### ROLE 02 — PAID MEDIA BUYER
**Activation prompt:** "what's wasting budget"

**Full prompt:**
"Audit my active paid campaigns for budget waste. Identify: (1) ad sets spending with zero conversions in the last 7 days, (2) audiences with CPM >2x account average, (3) placements with CPC >3x the top-performing placement, (4) campaigns with frequency >4 that haven't been refreshed in 14+ days. For each finding, recommend: pause, reduce budget, or refresh creative."

**Delivers:** Budget waste audit with specific cut/pause/refresh recommendations.

---

### ROLE 03 — CREATIVE STRATEGIST
**Activation prompt:** "creative review"

**Full prompt:**
"Review my current active ad creative performance. Rank all active ads by CTR, hook rate (3-second view rate), and conversion rate. Identify: (1) the top 3 creative concepts that are working and why, (2) the bottom 3 that should be retired, (3) the creative pattern — format, hook style, visual — that consistently outperforms. Give me 3 new creative concepts to test this week based on what's working."

**Delivers:** Creative performance ranking + 3 validated new test concepts.

---

### ROLE 04 — AUDIENCE & FUNNEL ANALYST
**Activation prompt:** "where's traffic converting"

**Full prompt:**
"Map where traffic is converting and where it's leaking. For each funnel stage (awareness → consideration → conversion → retention), show: volume, conversion rate to next stage, and drop-off rate. Identify the single biggest leak in the funnel. For that leak, give me 3 specific fixes — one for the ad, one for the landing page, one for the offer — that I could test this week."

**Delivers:** Full funnel conversion map with the #1 leak identified and 3 fixes.

---

### ROLE 05 — REVENUE ANALYST
**Activation prompt:** "revenue check"

**Full prompt:**
"Run a revenue attribution check. Break down revenue generated this week by: (1) channel — paid social, paid search, organic, email, direct; (2) product or offer type; (3) new vs returning customers. Calculate the true revenue-per-click for each channel. Identify which channel has the best revenue efficiency and what would happen to total revenue if we moved 20% of budget there from the lowest-efficiency channel."

**Delivers:** Revenue attribution breakdown + budget reallocation scenario.

---

### ROLE 06 — EMAIL & RETENTION STRATEGIST
**Activation prompt:** "email check"

**Full prompt:**
"Run my email performance check. Report: open rate, click rate, unsubscribe rate, and revenue-per-email for the last 5 sends vs the prior 30-day average. Flag any sequence that has a >3% unsubscribe rate. Identify: (1) the email that drove the most revenue and why, (2) the sequence step where engagement drops off most, (3) one re-engagement or win-back campaign I should set up this week."

**Delivers:** Email health check + one priority campaign to add.

---

### ROLE 07 — SEO & ORGANIC ANALYST
**Activation prompt:** "SEO check"

**Full prompt:**
"Run my weekly SEO check. Report: (1) top 10 pages by organic traffic — any that dropped more than 15% week-over-week; (2) keywords in positions 4–10 that are close to page one; (3) any new competitor pages ranking for my primary keywords that weren't there last week; (4) site health issues flagged in the last crawl. Give me 3 specific actions to take this week to move the needle on organic."

**Delivers:** Weekly SEO report with 3 prioritised actions.

---

### ROLE 08 — COMPETITIVE INTEL RESEARCHER
**Activation prompt:** "competitor check"

**Full prompt:**
"Run my weekly competitor intelligence check. For my top 3 competitors: (1) what new ads did they launch in the last 7 days? What hook, angle, and offer are they testing? (2) did they change pricing, add offers, or update landing pages? (3) did they publish new content — articles, videos, posts — that got significant engagement? Summarise the #1 thing each competitor is doing that I should pay attention to this week."

**Delivers:** Competitor weekly brief — new ads, offers, content moves to watch.

---

### ROLE 09 — BUDGET PACING CONTROLLER
**Activation prompt:** "pacing check"

**Full prompt:**
"Run my budget pacing check. For each active campaign or channel: (1) how much of the monthly budget has been spent as of today, vs where we should be at this point in the month (expected spend = monthly budget × days elapsed / total days); (2) flag any campaign that is overpacing by >20% or underpacing by >20%; (3) for underpacing campaigns, is it a budget cap issue, a delivery issue, or a quality score issue? Give me specific actions to correct each flagged campaign."

**Delivers:** Pacing report with specific correction actions for over- and under-delivery.

---

### ROLE 10 — DIAGNOSTIC INVESTIGATOR
**Activation prompt:** "why did ROAS drop"

**Full prompt:**
"Investigate why ROAS dropped. Walk me through the diagnostic: (1) did overall spend increase while revenue stayed flat? (2) did CPM increase — is this a cost side problem? (3) did conversion rate drop — is this an offer or landing page problem? (4) did creative CTR drop — is this an ad fatigue problem? (5) did the audience mix shift — more cold, less warm traffic? For each dimension, tell me what the data shows and what the most likely root cause is. Then give me 3 hypotheses to test to recover ROAS."

**Delivers:** Full ROAS drop root-cause analysis + 3 recovery hypotheses.

---

## TEAM STANDUP — FULL MORNING BRIEF

To run the full 10-role team check at once, use: `/ai-marketing-team all`

Deliver in this order:
1. Performance Analyst — yesterday's numbers
2. Paid Media Buyer — waste to cut
3. Revenue Analyst — attribution snapshot
4. Budget Pacing Controller — pacing status
5. Creative Strategist — what's working / what to retire
6. Email & Retention Strategist — email health
7. SEO & Organic Analyst — organic moves
8. Audience & Funnel Analyst — funnel leaks
9. Competitive Intel Researcher — competitor moves
10. Diagnostic Investigator — active investigations

---

## AI PROMPTS — PLAIN TEXT (copy and paste)

**Morning check:**
Run my morning performance check. Pull yesterday's data across all active channels. Flag any metric that moved more than 20% vs the prior 7-day average. For each flag, give me a one-line hypothesis and one action to take before noon.

**What's wasting budget:**
Audit my active paid campaigns for budget waste. Identify ad sets with zero conversions in 7 days, audiences with CPM >2x average, placements with CPC >3x top performer, and campaigns with frequency >4 not refreshed in 14+ days. Recommend: pause, reduce, or refresh.

**Creative review:**
Rank all active ads by CTR, hook rate, and conversion rate. Identify top 3 working concepts and why, bottom 3 to retire, and the consistent creative pattern. Give me 3 new concepts to test this week.

**Where's traffic converting:**
Map funnel conversion at each stage. Identify the single biggest leak. Give me 3 fixes — one for the ad, one for the landing page, one for the offer.

**Revenue check:**
Break down this week's revenue by channel, product type, and new vs returning customers. Calculate revenue-per-click per channel. Show what happens if I move 20% of budget from lowest to highest efficiency channel.

**Email check:**
Report open rate, click rate, unsubscribe rate, and revenue-per-email for the last 5 sends. Flag sequences with >3% unsubscribe. Identify the email that drove most revenue and the sequence step where engagement drops.

**SEO check:**
Report top 10 organic pages — any dropping >15% week-over-week. Keywords in positions 4–10. New competitor pages ranking for my terms. Site health issues. Give me 3 actions to take this week.

**Competitor check:**
For my top 3 competitors, what new ads, pricing changes, landing page updates, and content have they launched in the last 7 days? What's the #1 thing each is doing I should watch?

**Pacing check:**
Compare actual spend to expected spend (budget × days elapsed / total days) for each campaign. Flag overpacing or underpacing >20%. Identify root cause and correction action for each flag.

**Why did ROAS drop:**
Diagnose the ROAS drop across 5 dimensions: spend increase, CPM increase, conversion rate drop, creative CTR drop, audience mix shift. Identify the most likely root cause and give me 3 hypotheses to test to recover ROAS.
