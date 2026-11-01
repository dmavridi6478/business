# 05 — Creative Metrics (The Layer Beneath CTR)

## Video and Ad-Level Diagnostics

CTR tells you *whether* people are clicking. Creative metrics tell you *why* — or why not. This document covers the sub-metrics that explain CTR performance, particularly for video ads.

---

## The Creative Funnel

Every ad — especially video — has its own internal funnel:

```
Impression
    │
    ▼
Hook (Did they stop scrolling?) ──── Hook Rate
    │
    ▼
Hold (Did they keep watching?) ───── Retention Rate / Hold Rate
    │
    ▼
Act (Did they click through?) ────── Outbound CTR
    │
    ▼
Convert (Did they buy?) ──────────── View-Through or Click-Through CVR
```

When CTR is low, the answer is somewhere in this funnel. A media buyer who only looks at CTR is looking at the output without understanding the process.

---

## Metric Definitions

### Hook Rate

**Definition:** The percentage of people who watched the first 3 seconds of a video ad (sometimes defined as first 2 seconds, depending on platform).

**Formula:** `(3-Second Video Views / Impressions) × 100`

**What it measures:** Whether the first frame (or first few seconds) of the video stops the scroll. This is the most important creative metric because if you lose the viewer in the first 3 seconds, nothing else matters.

**Benchmarks:**
- Below 20%: The hook is weak. The first frame is not compelling enough to interrupt scrolling behavior.
- 20%–30%: Acceptable. There is a hook, but it may not be differentiated enough.
- 30%–45%: Strong. The opening is grabbing attention effectively.
- Above 45%: Exceptional. Usually indicates a highly pattern-interrupting or emotionally resonant opening.

**What drives hook rate:**
- **Visual contrast:** Bright colors, unusual imagery, movement in the first frame
- **Text overlays:** A bold, curiosity-driven statement in the first second
- **Pattern interruption:** Something unexpected that breaks the monotony of the feed
- **Face and eye contact:** Human faces looking at the camera tend to stop scrolling
- **Relevance:** A hook that immediately signals "this is for you" to the target audience

**Common hook failures:**
- Logo or brand intro in the first 3 seconds (no one stops scrolling for a logo)
- Slow fade-in or ambient opening (the feed is fast; your ad must be faster)
- Generic stock footage (nothing to differentiate from surrounding content)
- No text overlay on a video that requires audio context (most users have sound off)

---

### Hold Rate (Retention Rate)

**Definition:** The percentage of hooked viewers who continue watching to a meaningful midpoint (usually 50% of the video, or to the 15-second mark — whichever is more relevant for the video length).

**Common formulas:**
- `(15-Second Video Views / 3-Second Video Views) × 100`
- `(ThruPlays / 3-Second Video Views) × 100` (Meta-specific: ThruPlay = 15 seconds or video completion, whichever comes first)
- `(Video Watches at 50% / 3-Second Video Views) × 100`

**What it measures:** Whether the content after the hook is engaging enough to keep the viewer watching. A strong hook with weak hold means you earned attention but wasted it.

**Benchmarks (15-second hold rate):**
- Below 20%: Content is losing people immediately after the hook. The transition from hook to message is weak.
- 20%–35%: Average. There is a story but it is not compelling enough to retain most viewers.
- 35%–50%: Strong. The narrative is working — viewers are engaged through the value proposition.
- Above 50%: Exceptional. Usually indicates highly relevant, entertaining, or informative content.

**What drives hold rate:**
- **Narrative structure:** A clear story arc (problem → tension → solution) keeps people watching
- **Pacing:** Rapid cuts (every 2-3 seconds) maintain visual interest
- **Information delivery:** Revealing new information progressively gives viewers a reason to stay
- **Music and rhythm:** Even with sound off, visual rhythm matters. With sound on, music drives pacing.
- **Relevance:** The content must deliver on the promise of the hook. If the hook is "3 mistakes killing your skin," the next 10 seconds better be about those mistakes.

**Common hold failures:**
- Hook promises something the body does not deliver
- Long, static talking-head segments without visual variety
- Repetitive messaging (same point made three times = viewer leaves)
- No progression — the viewer at second 10 has not learned anything new since second 3

---

### View-Through Conversion Rate

**Definition:** The percentage of people who *viewed* an ad (without clicking) and subsequently converted within the attribution window.

**Formula:** `(View-Through Conversions / Video Views) × 100`

**What it measures:** The "passive" conversion power of a video ad — whether the ad influenced a purchase even when the viewer did not click on the ad itself. This is particularly relevant for awareness and upper-funnel campaigns.

**Important context:** View-through conversions are the most debated metric in digital advertising. They are real (people do see ads and later buy), but they are also the most easily inflated by attribution (the ad may get credit for conversions that would have happened anyway). See `08-attribution-windows.md` for more on this.

**How to use it:**
- Compare view-through CVR across different creatives to understand which videos are most persuasive even without a click
- Use as a signal for creative quality, not as a standalone performance metric
- If view-through conversions make up more than 50% of a campaign's total attributed conversions, the campaign may be taking credit for organic demand. Investigate with holdout tests.

---

## The Creative Diagnostic Matrix

When CTR is low, use this matrix to pinpoint where the creative funnel is breaking:

| Hook Rate | Hold Rate | CTR | Diagnosis | Action |
|---|---|---|---|---|
| Low | Low | Low | Ad is invisible — no one stops, no one watches, no one clicks | Start over. New concept, new hook, new format. |
| Low | High | Low | The few who stop are engaged, but most people scroll past | The hook is weak but the content is strong. Test 5-10 new opening frames on the same body. |
| High | Low | Low | Hook grabs attention but the content loses them | The hook-to-body transition is broken. Restructure the first 10 seconds after the hook. |
| High | High | Low | People watch but do not click | The CTA is weak or missing. The ad entertains but does not drive action. Add a clear, urgent CTA. |
| High | Low | High | Hook drives clicks before people watch the full video | The hook itself is the CTA. This works for direct response but may indicate the video body is unnecessary — test shorter formats. |
| High | High | High | Everything is working | Protect this creative. Scale it. Do not touch it. Start building variations to extend its lifespan. |

---

## Creative Testing Framework

### How to Test Hooks

The hook is the highest-leverage variable. Test it systematically:

1. **Create 3-5 hook variations for the same video body.** Change only the first 3 seconds. Same product, same message, same CTA — different opening.
2. **Run all variations in the same ad set** with equal budget distribution (or use dynamic creative if the platform supports it).
3. **Evaluate after 1,000+ impressions per variation** (minimum for directional signal on hook rate).
4. **Kill variations with hook rate below 20%** after 2,000 impressions.
5. **Scale the winner.** Then create new hook variations to beat it.

**Hook formula templates:**
- **Problem-agitation:** "Stop doing [common mistake] with your [product category]"
- **Curiosity gap:** "The reason your [pain point] isn't getting better"
- **Social proof:** "I tried 12 [products] and this is the only one that [result]"
- **Demonstration:** Show the product doing something unexpected in the first frame
- **UGC reaction:** Genuine reaction shot (surprise, delight) as the opening frame

### How to Test Body Content

Once you have a winning hook, test the body:

1. **Long vs. short:** Test 15-second, 30-second, and 60-second versions with the same hook.
2. **Format variation:** Talking head vs. b-roll vs. screen recording vs. lifestyle footage.
3. **Information structure:** Problem → Solution vs. Benefit → Proof vs. Testimonial → Offer.
4. **Evaluate hold rate.** The winning body is the one that retains the most viewers through to the CTA.

### How to Test CTAs

The CTA determines whether viewing converts to clicking:

1. **Verbal CTA vs. visual CTA vs. both.** Test whether a spoken CTA, text overlay CTA, or combined approach drives more clicks.
2. **CTA timing:** Test placing the CTA at the 10-second mark vs. the end of the video. Some audiences respond better to early CTAs (they have already decided by second 10).
3. **CTA specificity:** "Shop now" vs. "Get 20% off today" vs. "See which [product] is right for you." Specific, benefit-driven CTAs typically outperform generic ones.

---

## Static Image Ad Metrics

Not all ads are video. For static images, the diagnostic is simpler but still follows the same logic:

**Key metrics for static ads:**
- **CTR (outbound):** The primary creative performance metric. Is the image + copy + CTA combination driving clicks?
- **Engagement rate:** Likes, comments, shares, saves. Not a conversion metric, but a signal of resonance.
- **Frequency:** How many times each person has seen this image. Static ads fatigue faster than video — typically after 3-4 exposures.

**Static ad diagnostic:**

| CTR | Engagement | Diagnosis | Action |
|---|---|---|---|
| Low | Low | Ad is not resonating at all | New concept needed. Test a completely different visual approach. |
| Low | High | People like the ad but are not clicking | CTA is weak or the offer is unclear. Test stronger copy and a clearer value proposition. |
| High | Low | Ad drives clicks but no emotional connection | Functional but not memorable. Fine for DR, but this creative will fatigue faster. |
| High | High | Strong on all dimensions | Scale and protect. Build variations to extend lifespan. |

---

## Creative Lifespan and Refresh Cadence

All creative fatigues. The question is when.

**Signals that a creative is fatiguing:**
- Hook rate declining over 2+ weeks
- CTR declining while frequency is rising
- CPM rising on a specific ad (platform is working harder to deliver it)
- Comment sentiment shifting from positive to "I've seen this 100 times"

**Typical lifespans (rough ranges):**
- **Meta (high-spend account, $1K+/day on a single ad):** 2-4 weeks
- **Meta (moderate spend, $200-$500/day):** 4-8 weeks
- **TikTok:** 1-3 weeks (faster creative churn)
- **YouTube:** 4-12 weeks (longer-form content fatigues slower)
- **Google Display:** 4-8 weeks

**Refresh strategy:**
- Always have 2-3 creative concepts in testing while 1-2 proven concepts carry the majority of spend
- Do not wait for creative to fully fatigue before launching replacements. Start testing new concepts when the current winner shows the first signs of decline (hook rate or CTR down 10-15% from peak).
- Keep a "creative library" of winning hooks, angles, and formats. When building new creative, remix winning elements from past performers rather than starting from scratch every time.

---

## Platform-Specific Notes

### Meta
- 3-second video views are the standard hook metric
- ThruPlays (15-second views or completion) are available for hold rate calculation
- Dynamic Creative Testing (DCT) can automate hook/body/CTA combinations but reduces your ability to isolate variables. Use structured testing for learning, DCT for scaling.

### TikTok
- Hook rate is even more critical — the platform's UX is pure vertical scroll. You have 1-2 seconds to stop the thumb.
- "Spark Ads" (boosted organic posts) often outperform traditional ads because they feel native to the feed.
- Sound-on is more common on TikTok than Meta. Audio hooks matter more here.

### YouTube
- Different creative model — users chose to watch (or are waiting through a pre-roll). Hook rate is less about stopping the scroll and more about preventing the "Skip" button click.
- Retention curves are available in YouTube analytics — use them to identify exact drop-off points in the video.
- Longer-form creative (30-60 seconds) performs better on YouTube than on Meta or TikTok.

### Google (Display, Demand Gen)
- Primarily static or short-form video. Creative diagnostic is closer to the static image framework.
- Responsive display ads test headline/image/description combinations automatically. Monitor which combinations the algorithm favors and build dedicated ads around winning combos.
