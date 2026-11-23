# Meta (Facebook & Instagram) — Best Practices

## Tactical Playbook Aligned With Meta's Algorithm

This document translates the algorithm knowledge from `algorithm-overview.md` into specific, actionable best practices for managing Meta ad accounts. Everything here is grounded in how Andromeda, GEM, Lattice, and the auction actually work.

**Read `algorithm-overview.md` first.** These best practices make more sense when you understand the "why" behind them.

---

## Account Structure

### Campaign Architecture

**Default structure for most ecommerce accounts:**

```
Account
├── Advantage+ Shopping Campaign (ASC)
│   ├── 8-15 distinct creatives
│   ├── Broad targeting (minimal exclusions)
│   └── Majority of prospecting + retargeting budget
│
├── Prospecting CBO Campaign (if needed alongside ASC)
│   ├── Ad Set 1: Broad (no interests, no lookalikes)
│   │   └── 5-8 creatives
│   ├── Ad Set 2: Lookalike (1-5% from purchaser seed)
│   │   └── 5-8 creatives (can overlap with Ad Set 1)
│   └── Budget: $100+/day per ad set minimum
│
├── Retargeting Campaign (separate only if needed for messaging control)
│   ├── Ad Set: Site visitors 1-30 days, exclude purchasers
│   │   └── 3-5 creatives (different messaging than prospecting)
│   └── Budget: 10-20% of total Meta spend
│
└── Testing Campaign (for creative testing)
    ├── Ad Set: Broad targeting, cost cap
    │   └── New creatives being tested (3-5 at a time)
    └── Budget: 10-15% of total Meta spend
```

**Why this structure:**
- ASC gives Andromeda the broadest creative pool and audience to work with
- Broad targeting lets GEM and Lattice find the best audience without constraints
- Separate retargeting only if you need distinct messaging (not for performance reasons — ASC handles retargeting internally)
- Testing campaign with cost cap protects budget while exploring new creative

### Structure Anti-Patterns (What NOT to Do)

| Anti-Pattern | Why It Hurts |
|---|---|
| 10+ ad sets each targeting a different interest | Fragments data. Each ad set gets too little budget to exit learning phase. Andromeda cannot learn across fragmented pools. |
| Separate campaigns for every product | Same problem. Consolidate unless products have fundamentally different audiences. |
| Duplicating ad sets to "reset the algorithm" | Disrupts learning and creates internal auction overlap. The duplicate competes against the original. |
| Running identical ads in multiple ad sets | Creates auction overlap — your ads compete against themselves, driving up CPMs. |
| Restricting to a single placement | Limits GEM's cross-surface learning. Let Advantage+ placements optimize delivery. |

---

## Creative Strategy

### Creative Diversity (Feeding Andromeda)

Andromeda retrieves ads based on predicted relevance to a specific user. The more diverse your creative, the more "entry points" for the system to match your product to different user segments.

**Creative diversity means conceptual diversity:**

| Dimension | Examples |
|---|---|
| **Angle** | Problem/solution, social proof, founder story, product demo, objection-buster, urgency/offer, lifestyle, comparison, behind-the-scenes |
| **Format** | UGC talking head, b-roll product shots, screen recordings, carousel, static image, customer testimonial video, unboxing |
| **Hook** | Different opening 3 seconds — visual hook, text hook, audio hook, pattern interrupt |
| **Tone** | Educational, emotional, humorous, authoritative, aspirational, relatable |
| **CTA** | Shop now, learn more, see results, take the quiz, claim your offer |

**Target: 8-15 conceptually distinct creatives per ad set.** Not 8 versions of the same ad with different text overlays. Eight different *stories* about the same product.

### Creative Refresh Cadence

Andromeda's retrieval engine processes creative at high volume, which means creative fatigues faster than in previous Meta systems.

| Account Spend Level | Refresh Cadence | New Creatives Per Cycle |
|---|---|---|
| $1,000-$5,000/month | Every 3-4 weeks | 3-5 new creatives |
| $5,000-$20,000/month | Every 2-3 weeks | 5-8 new creatives |
| $20,000-$100,000/month | Every 1-2 weeks | 8-12 new creatives |
| $100,000+/month | Weekly | 10-15+ new creatives |

**Refresh does not mean replace.** Keep winners running. Add new creative alongside them. Let the algorithm decide when to shift spend from old to new.

### Creative Testing Protocol

1. **Launch 3-5 new ads** in the testing campaign (or directly in ASC)
2. **Use cost cap bidding** in the testing campaign to protect against runaway CPA during the learning phase
3. **Let each ad accumulate 1,000+ impressions** before evaluating hook rate. Let each accumulate 50+ link clicks before evaluating CTR.
4. **Kill clear losers after 3-5 days** (hook rate below 20%, CTR significantly below account average)
5. **Graduate winners** to the main campaign (or let ASC auto-allocate)
6. **Document what worked** — add winning hooks, angles, and formats to the creative library for future iteration

### Hot Ad Bias

Andromeda has a documented tendency to latch onto an early-performing creative and allocate the majority of budget to it, starving other ads before they reach statistical significance. This is known as "Hot Ad Bias."

**How to manage it:**
- Monitor spend distribution across ads. If one ad is getting 80%+ of spend within the first 48 hours, the others are being starved.
- If you believe a starved ad has potential, move it to a separate ad set with its own budget to give it room to learn.
- Expect this behavior — it is the system working as designed. The algorithm is pursuing what it believes will perform best. Sometimes it is right. Sometimes it over-indexes on early data.

---

## Targeting

### Default: Go Broad

With Andromeda and GEM, targeting is no longer the primary lever for finding the right audience. Creative is.

**Recommended approach:**
- Start with Advantage+ audience (broad) as the default
- Use age, gender, and geo restrictions only where they are truly necessary (e.g., product is only available in certain states, product is gender-specific)
- Lookalike audiences can serve as useful *signals* but not hard boundaries — the algorithm will expand beyond them

### When to Use Lookalikes

Lookalikes are still useful as seed signals in specific situations:

- **Cold start:** New account with no conversion data. A lookalike from the client's email list gives the algorithm a starting point.
- **High-value targeting:** Lookalike from top 25% LTV customers can help the system find higher-value prospects.
- **Testing a specific hypothesis:** If you want to test whether a specific customer segment responds to a specific message.

But even with lookalikes, use Advantage+ audience expansion so the algorithm can explore beyond the seed.

### Exclusions

Keep exclusions minimal. Each exclusion reduces the algorithm's optimization surface.

**Reasonable exclusions:**
- Purchasers in the last 7-30 days (prevents wasting spend on recent buyers for acquisition campaigns)
- Employees or internal audiences
- Geographic exclusions for products not available in certain areas

**Unnecessary exclusions:**
- Excluding interests or demographics "just in case"
- Excluding audiences from other campaigns to prevent overlap (the auction handles this)
- Excluding Audience Network or specific placements (let Advantage+ optimize)

---

## Bidding Strategy

### Default: Lowest Cost (Highest Volume)

For most campaigns, let Meta bid dynamically. The system has more data than you do about the current auction landscape and will find the cheapest conversions within your budget.

### When to Use Cost Cap

- **Testing new creative:** Cost cap protects budget during the learning phase when performance is uncertain.
- **Scaling:** When increasing budget, cost cap at your target CPA prevents the algorithm from paying inflated prices for marginal conversions.
- **Volatile periods:** During high-competition periods (Q4, major sales events), cost cap prevents runaway CPMs.

**How to set a cost cap:**
1. Start at 20-30% above your current average CPA
2. If delivery is strong, lower the cap by 10% per week
3. If delivery stalls, raise the cap by 10-20%
4. Never set a cost cap equal to or below your current CPA — the system needs room above the average to find conversions

### When to Use Bid Cap

- **Strict margin requirements:** If you have a hard CPA ceiling (contribution margin dictates maximum CPA), bid cap enforces it
- **"Mini learning lab" approach:** High daily budget + aggressive bid cap forces the algorithm to pursue only the cheapest, highest-probability conversions

### When to Use ROAS Goal (Minimum ROAS)

- **When you have strong conversion volume** (50+ purchases/week) and want to optimize for revenue, not just conversion count
- **Set it conservatively** — start at 50-70% of your current ROAS, not at your target. Let the system find its level.

---

## Conversion Tracking and Signal Strength

### Conversion API (CAPI) — Non-Negotiable

Every account must have CAPI implemented. Pixel-only tracking is unreliable post-iOS14.

**CAPI checklist:**
- [ ] Server-side events firing for all key actions (ViewContent, AddToCart, Purchase)
- [ ] Event deduplication enabled (CAPI + Pixel should not double-count events)
- [ ] Event Match Quality score above 6.0 (visible in Events Manager)
- [ ] Customer information parameters being passed (email, phone, external_id)

### Aggregated Event Measurement (AEM)

Post-iOS14, Meta limits the number of conversion events you can optimize for. Prioritize correctly:

1. **Purchase** (highest priority — always)
2. **Add to Cart** (secondary optimization event)
3. **Initiate Checkout** (tertiary)
4. **View Content** (lower priority, useful for upper-funnel campaigns)

### Feeding Value Data Back to Meta

If possible, pass actual revenue or contribution margin data with purchase events. This enables value optimization — where Meta optimizes for total revenue (or profit) rather than conversion count.

**Why this matters:** Without value data, Meta treats a $20 order and a $200 order as equal. With value data, the system can learn to find higher-value customers.

**Advanced:** If you can pass contribution margin as the value parameter (instead of revenue), you are literally telling the algorithm to optimize for profit. This is the closest you can get to aligning Meta's optimization with actual business outcomes.

---

## Scaling

### How to Scale Spend on Meta

1. **Increase budget in 15-20% increments** every 3-5 days. Larger jumps reset the learning phase.
2. **Monitor marginal CPA** (see `06-metric-interactions.md`). Blended CPA will rise, but the question is whether the marginal CPA is acceptable.
3. **Scale creative before scaling budget.** Adding more budget without new creative leads to faster fatigue and higher CPMs.
4. **Expand placements and surfaces.** If you have been running Feed-only, add Reels and Stories. If you have been running Facebook-only, add Instagram. More surfaces = more inventory = more room to scale.
5. **Test new audiences.** If you have saturated one lookalike, test new seeds. If lookalikes are exhausted, test fully broad.

### Signs You Have Hit a Scaling Ceiling

- CPM rising consistently despite creative refreshes
- Frequency above 3.0 in a 7-day window across all campaigns
- CPMr growing faster than CPM (audience saturation)
- Marginal CPA more than 2x the baseline CPA

When you hit the ceiling on Meta, the answer is often *not* "more budget on Meta" — it is "test a new channel" (TikTok, YouTube, Google).

---

## Reporting and Analysis on Meta

### Columns to Always Include in Your Default View

| Column | Why |
|---|---|
| Amount Spent | Budget tracking |
| Impressions | CPM calculation |
| Reach | CPMr calculation and frequency analysis |
| Frequency | Creative fatigue indicator |
| CPM | Cost of attention |
| Link Clicks (outbound) | Real clicks, not vanity engagement |
| CTR (link click-through rate) | Outbound CTR, not all-clicks |
| Landing Page Views | Click-to-LP drop-off diagnosis |
| Results (purchases) | Conversion volume |
| Cost Per Result | CPA |
| Purchase ROAS | Platform-reported ROAS |
| Purchases Conversion Value | Revenue |

### Attribution Window Columns

Add columns for both 7dc/1dv (default) and 1dc-only to see the gap:

| Column | Attribution | Purpose |
|---|---|---|
| Purchases (7dc/1dv) | Default | Standard reporting |
| Purchases (1dc) | Click-only, 1 day | Incrementality signal — tighter attribution |
| Purchases (1dv) | View-only, 1 day | View-through contribution |

The gap between 7dc/1dv and 1dc tells you how much of your reported performance depends on delayed and view-through attribution. See `08-attribution-windows.md` for the full framework.

### Breakdown Caution

Review breakdowns (placement, age, gender, device) for directional understanding, but **do not make surgical cuts based on breakdown data alone.** The Breakdown Effect means attributed performance by segment does not reflect the true contribution of that segment. See `algorithm-overview.md` for details.

---

## Common Meta-Specific Problems and Fixes

| Problem | Likely Cause | Fix |
|---|---|---|
| Ad stuck in "Learning" for 7+ days | Not enough conversion events (need ~50 in 7 days) | Consolidate ad sets, increase budget, move to a higher-funnel optimization event temporarily |
| Spend concentrated on one ad | Hot Ad Bias — Andromeda latched onto early winner | Monitor. If other ads deserve a chance, break them into a separate ad set. |
| CPM spiking suddenly | Seasonal competition, audience saturation, or ad disapprovals reducing eligible inventory | Check frequency/CPMr, check for disapprovals, check placement mix |
| CPA good but backend revenue is down | Attribution inflation — platform over-crediting conversions | Pull 1dc-only data, compare platform conversions to Shopify orders, run holdout test |
| New campaign launched but no spend | Audience too narrow, bid cap too low, ad rejected, or billing issue | Check ad status, check audience size, remove bid cap temporarily, verify billing |
| High CTR but low conversions | Creative-to-LP mismatch or LP issues | Click the ad yourself on mobile. Check LP speed. Check congruence. |
