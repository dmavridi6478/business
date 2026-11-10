---
name: waitlist-app-builder
description: Build a full-stack waitlist app with a viral referral mechanic (position jumps for referrals), an AI-written email drip sequence, and a password-protected admin dashboard — the pre-launch system that collects signups and validates demand before a product is finished. Use when someone wants to launch a waitlist before their product is ready, needs a referral-driven signup page, or asks to build a "coming soon" / early-access page with more than a static email form.
---

# Waitlist App Builder

Source: reviewed from an uploaded photo batch — a 12-slide carousel
(@earchoe, "build_with_ai") titled "Every major product launch uses a
waitlist. AI builds yours in one session." One claim on slide 2 ("3x
higher day-1 conversion... 62% of waitlist signups share the product...
if you give them a referral incentive") is presented with no source or
methodology — kept out of this skill's own reasoning as fact; the
underlying mechanics (visible position, specific rewards, referral
tiers) are widely-used growth patterns independent of that particular
statistic, so they're kept.

## What this builds

A waitlist app that does more than collect emails: every signup gets a
unique referral code, referring 3 people jumps them to the front 25% of
the queue (a "priority" tier), referring 10 guarantees access. A 3-email
drip sequence keeps waiting users engaged, and a password-protected admin
dashboard lets the operator see signups, referral leaderboard, and invite
people in controlled batches rather than all at once.

Stack assumed by the prompts below: React + Vite frontend, Express
backend, PostgreSQL, Resend for email. Adapt the prompts' stack details
if the project uses something else — the structure (schema, referral
logic, drip sequence, admin actions) carries over regardless of framework.

## Why a referral-driven waitlist (not just an email capture form)

A waitlist run before a product exists does three things at once: it
builds demand by making access feel scarce, it produces an email list
before there's a finished product to sell, and it tells the operator
whether anyone actually wants what's being built before they spend months
on it. What makes people share it compulsively, specifically:

- **Make position visible.** "You are #847 on the waitlist" motivates more
  than "you're on the waitlist" — a number the user can watch move is a
  reason to come back.
- **Make the reward specific.** "Refer 3 → jump to the top 25%" beats
  "refer friends for early access" — vague rewards don't get shared.
- **Show movement.** When a referral lands, tell the user immediately and
  show their new position. The dopamine hit is what drives the next share.
- **Make the link dead simple.** One URL with the referral code
  pre-embedded — no copy-paste friction, no second step.
- **Keep the wait meaningful.** If everyone gets in immediately, the
  waitlist loses its power. Be deliberately selective about batch sizes
  (see the post-launch section below).

## The four prompts

Run in this order: scaffold first: the drip-email and referral-engine
prompts can follow immediately after (they touch different files); the
admin dashboard prompt is meant to come **after the core build ships**,
not alongside it — it's the control layer for a system that already
works, not a blocker to getting the waitlist live.

### 1. Scaffold the full system

```text
Build a waitlist app — working name LaunchQueue, check availability. React + Vite frontend, Express backend, PostgreSQL, Resend for email. Schema: waitlist_entries (id, email, name, referral_code UNIQUE, referred_by referral_code, referral_count INT default 0, position INT, status ['waiting'|'invited'|'active'], created_at). On signup: generate a unique 8-char referral code, calculate position as COUNT(*)+1, if referred_by exists increment that user's referral_count and check thresholds (3=priority, 10=guaranteed), send welcome email via Resend. Start with scaffold and schema only.
```

### 2. The AI-written drip sequence

```text
Write a 3-email waitlist drip sequence for [product name]. What it does: [one sentence]. Target user: [who]. Tone: [excited but honest / calm and professional / conversational]. Email 1 (immediate): welcome, confirm their position [#X], explain the referral mechanic (share their link, get 3 = jump queue), one line on what they'll get when they're in. Email 2 (day 5): a specific piece of value related to the problem the product solves — teach them something useful even before launch. End with a soft referral nudge. Email 3 (access day): you're in. Here is your access link [link]. What to do first. One question to reply to.
```

### 3. The referral position engine

```text
Build the referral position recalculation system. When a user's referral_count increases: 1) if referral_count reaches 3 — move them to the front 25% of the waitlist (priority tier), 2) if referral_count reaches 10 — set their status to 'guaranteed' and move them to position 1, 3) after any tier change, send a congratulations email via Resend with their new position, 4) expose a GET /api/waitlist/status/:referral_code endpoint that returns: position, total_waitlist_size, referral_count, tier, referrals_needed_for_next_tier. Frontend polls this every 30 seconds on the user's status page.
```

### 4. The admin dashboard (add after core build ships)

```text
Build a password-protected admin dashboard at /admin. Show: total signups (live counter), today's signups, referral leaderboard (top 10 by referral_count), status breakdown (waiting / priority / guaranteed / invited / active). Actions: 1) "Invite batch" — select N users from the top of the waiting list, generate unique access codes, send email 3 to each, update status to 'invited', 2) "Export CSV" — download all waitlist entries. Password set via ADMIN_PASSWORD env var. No auth library needed — simple middleware check is fine.
```

## Files this produces

| File | What it holds |
|---|---|
| `src/pages/WaitlistSignup.jsx` | Name + email form, referral code in URL auto-applied |
| `src/pages/WaitlistStatus.jsx` | Live position, referral link, share buttons, tier progress |
| `src/pages/AdminDashboard.jsx` | Leaderboard, batch invite, CSV export, live counter |
| `server/routes/waitlist.js` | Signup, status, referral tracking, position recalculation |
| `server/routes/admin.js` | Password-protected admin endpoints + invite batch |
| `server/lib/email.js` | Resend wrapper — welcome, position update, access emails |

## Getting it live fast (Replit-specific, adapt for other hosts)

1. Add `RESEND_API_KEY`, `DATABASE_URL`, and `ADMIN_PASSWORD` to Replit
   Secrets (or the equivalent env-var store on another host).
2. Verify the sending domain in Resend so emails land in inbox, not spam
   — budget about 10 minutes for DNS propagation.
3. Test the full loop before posting anywhere: sign up → get the welcome
   email → share the referral link → confirm position changes.
4. Post the waitlist link the same day it's built. Every day of delay is
   signups not collected — there's no reason to sit on a working waitlist.

## What to do once signups arrive (worked at ~500 signups in the source)

- **Email before it feels ready.** A few hundred people waiting is itself
  the best reason to finish the build — don't wait for "done."
- **Survey the top referrers**, not a random sample — they're the most
  engaged users, and the ones most likely to have a sharp opinion on what
  the product should prioritize.
- **Invite in batches, never all at once.** Watch how each batch behaves,
  fix what breaks, then open the next batch. This is also what keeps the
  wait — and the referral incentive — meaningful (see the "keep the wait
  meaningful" principle above).
- **Make the invite email feel earned, not routine.** Subject line in the
  register of "Your access to [Product] is ready — you're in," never a
  generic "Welcome to [Product]."

## Related skills in this repo

- **one-person-business-sales-system**: covers the same lead-capture →
  nurture → conversion shape at the business-strategy level; this skill
  is the concrete implementation for the waitlist-specific case.
- **saas-idea-validator**: a waitlist's signup/referral numbers are real
  validation signal — run this skill's stress-test against what the
  waitlist actually shows once real numbers exist, not just the idea.
- **product-marketing-context**: capture the validated positioning here
  once the waitlist confirms real demand.
- **one-person-content-system**: the content engine that drives traffic
  to the waitlist signup page in the first place.
