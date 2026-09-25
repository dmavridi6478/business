---
description: 7-strategy LinkedIn system for converting cold traffic — profile, content calendar, DM follow-up, lead magnet, engagement, social proof, conversion (ContentSmash)
argument-hint: [your ICP, offer, or which of the 7 strategies to run]
---

# 7 LinkedIn Strategies Worth Implementing

Source: ContentSmash (contentsmash.io), "7 LinkedIn Strategies Worth Implementing." Distinct from this repo's other LinkedIn systems — `linkedin-optimizer-system` (Claude Project 5-step audit/rewrite), `linkedin-revenue-7steps` (Nader Alnajjar's monetization steps), `linkedin-monetize-by-stage` (follower-count-based offer ladder) — this one is a **cold-traffic conversion funnel**: it assumes strangers landing on your profile, not an existing audience you're monetizing.

## The 7 strategies, in funnel order

1. **Optimize your profile for cold traffic** — your profile is a landing page for strangers. Rewrite the headline to speak directly to your ICP's problem. Make the About section clear about what you solve. Add social proof and a strong CTA so visitors know what to do next.
2. **Build a content calendar** — stop posting randomly. Plan 4 weeks of content in advance. Define 3–4 content pillars. Know exactly what you're posting and when. Consistency beats perfection every time.
3. **Create a DM follow-up system** — track who engages with your content. Send personalized DMs to hot prospects. Start conversations, don't pitch immediately. Keep initial messages under 50 words. Track response rates and refine. (Use this repo's `linkedin-dm-funnel` for the 3-step DM sequence structure.)
4. **Distribute a lead magnet** — create one high-value resource your ICP actually wants. Promote it 3–4 times per week through posts. Use clear CTAs like "Comment FRAMEWORK for the template." Test different formats and double down on what converts.
5. **Build an engagement strategy** — engage with your ideal prospects' content within 30 minutes of posting. Leave comments that add value, not generic praise. Ask intelligent questions that spark discussion. Spend 20 minutes daily engaging strategically with your target audience.
6. **Collect social proof systematically** — gather testimonials and case studies from every client. Share client wins with specific numbers. Create posts highlighting measurable results. Use video testimonials when possible. Make proof impossible to ignore.
7. **Combine them for complete conversion** — profile attracts cold traffic → content brings awareness → engagement builds relationships → lead magnet captures interest → DMs start conversations → social proof builds trust → sales follows naturally.

## How the pieces map to skills already in this repo

| Strategy | This repo's skill/command |
|---|---|
| 1. Profile for cold traffic | `linkedin-profile-audit`, `linkedin-profile-rewrite` |
| 2. Content calendar | `linkedin-week-content-plan`, `content-week-framework` |
| 3. DM follow-up | `linkedin-dm-funnel` |
| 4. Lead magnet | `linkedin-lead-post-types` (Direct Offer post type) |
| 5. Engagement strategy | `linkedin-engagement-post-ideas` |
| 6. Social proof | — (net new; no dedicated skill yet) |
| 7. Combine/convert | `linkedin-profile-funnel` |

## Plain-text prompt to run the full 7-step audit

```
Audit my LinkedIn presence against the 7-strategy cold-traffic conversion
system: (1) is my profile written for a cold stranger or for people who
already know me, (2) do I have a 4-week content calendar with defined
pillars, (3) do I have a system for DMing people who engage, (4) do I have
one lead magnet I promote 3-4x/week, (5) am I engaging with my ICP's posts
within 30 minutes, (6) am I collecting and posting social proof
systematically, (7) does the full chain (profile -> content -> engagement
-> lead magnet -> DM -> proof -> sale) actually connect, or does it break
somewhere? Name the weakest link and what to fix first.
Context: [PASTE PROFILE URL / NICHE / OFFER]
```

## Social-proof post template (step 6 — the one gap with no existing skill)

```
Write a LinkedIn post sharing a client win with specific numbers, for
this result: [PASTE RESULT/METRIC]. Structure: hook naming the
transformation, 2-3 sentences of context on the starting point, the
specific measurable outcome (numbers, not adjectives), one sentence on
what made the difference, and a soft CTA inviting similar prospects to
reach out. No generic praise language ("amazing," "incredible") — let
the number do the work.
```
