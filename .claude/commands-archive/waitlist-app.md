---
description: Build a full waitlist app end to end — scaffold, drip email sequence, referral position engine, and (once the core build ships) an admin dashboard — using the waitlist-app-builder skill's four prompts.
argument-hint: [product name, one-sentence description, target user, and tone]
---

Given what's described in "$ARGUMENTS" (ask the user for this if not provided — at minimum, a working product name to check availability of, a one-sentence description of what it does, the target user, and a tone preference for the drip emails):

1. **Scaffold** — apply the `waitlist-app-builder` skill's Prompt 1 to build the schema and core signup flow (React + Vite frontend, Express backend, PostgreSQL, Resend for email, unless the user specifies a different stack — adapt the schema/logic to it rather than forcing this one). Confirm the app name is actually available before continuing.
2. **Drip sequence** — apply Prompt 2 to write the 3-email drip sequence using the product name/description/audience/tone from $ARGUMENTS.
3. **Referral engine** — apply Prompt 3 to build the position-recalculation system (priority tier at 3 referrals, guaranteed at 10) and the polling status endpoint. Steps 2 and 3 touch different files and can run in either order once step 1 is done.
4. **Admin dashboard** — apply Prompt 4 only after steps 1–3 are working end to end (signup → email → referral → position change all verified) — this is explicitly a "add after core build ships" step, not a parallel one. Skip it for this pass if the user just wants the collecting waitlist live first, and offer to run it as a follow-up.

Before finishing, walk through the "Getting it live fast" checklist in the skill (env vars, domain verification, full-loop test, same-day launch) rather than leaving deployment as an afterthought. Once real signups exist, the skill's "what to do once signups arrive" section (batched invites, surveying top referrers) is the next step — not part of this command's initial build.
