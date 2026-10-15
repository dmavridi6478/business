---
name: app-launch-6-tools-ella
description: Six tools to take an app beyond the preview (an @ella.tries1 video) - Newly, TestFlight, Supabase, PostHog, Sentry, RevenueCat, each with the one-paragraph procedure from the video word for word, the check that proves it worked, and the licence or catch behind each (Sentry is source-available, not open source; Supabase and PostHog are not the same as the hosted service). Use when moving a prototype to a real app.
---

# 6 tools to take an app beyond the preview

Source: a short vertical video by @ella.tries1 (a title card plus six tool cards; frames read, audio not transcribed). Licences read from each repo's LICENSE file on 15 October 2026; Newly, TestFlight and RevenueCat's service were not verified.

| # | Tool | Procedure (as on the card) | Proof it worked |
|---|---|---|---|
| 1 | **Newly** (newly.app) | "For a native iPhone or Android app, use newly.app. Describe one complete flow and the data it should save. Test it on your phone, then follow its publishing steps." | One flow works end to end on a real phone and the saved data is still there after you close the app |
| 2 | **TestFlight** | "Give three TestFlight testers one task without explaining the buttons. Ask for a screen recording. Fix the first confusing step and send another build so they can repeat it." | The same three testers finish the task on the second build without help |
| 3 | **Supabase** | "Use Supabase for sign-in and stored data when you need a backend. Protect private records by user ID. Test the same record link with a second account; it should not reveal private data." | Account B cannot read or edit account A's records (row-level security on every table holding user data) |
| 4 | **PostHog** | "Track account created, first useful result and payment screen opened. Compare how many users reach each step. If they leave before the result, work on that screen before buying more traffic." | A three-step funnel with real counts; the biggest drop is named |
| 5 | **Sentry** | "Use Sentry to see which crashes users hit and the steps before them. Check the app version and phone type. Repeat the failed task after the fix instead of only closing the report." | The crash is reproduced, fixed, and the task repeated on the affected version and device |
| 6 | **RevenueCat** | "Use RevenueCat for subscriptions and paid access. Start with one paid entitlement. Test purchase, expiration and restore, then reopen a premium screen to check the access is right." | Purchase, expiry and restore each grant or remove the entitlement correctly |

## What each choice costs you

- **Supabase:** Apache-2.0 (root LICENSE). Row-level security is off by default on new tables unless you enable it; "protect records by user ID" means writing policies, then testing with a second account.
- **PostHog:** MIT at the repo root; some enterprise features live in separately licensed folders [Likely]. Analytics on EU users needs consent handling (GDPR/ePrivacy).
- **Sentry:** the repo licence is the **Functional Source License** (converts to Apache-2.0 after two years): source-available, not open source in the usual sense; self-hosting for your own use is allowed, competing hosted offerings are not. Crash reports can contain personal data: scrub it.
- **RevenueCat:** the SDKs are MIT (purchases-ios checked); the service is paid beyond a free revenue tier (check current pricing). Store rules still apply: Apple and Google take their fees.
- **TestFlight:** Apple only; needs an Apple Developer account; external testers need a beta review.
- **Newly:** unverified; treat generated native apps as a prototype until the checks above pass.

## Order that makes sense
Build one flow (1), lock the data (3), instrument it (4) and (5) *before* inviting testers, then test with real people (2), then charge (6). The video's order is a list, not a sequence.

## Connectors
Supabase and Sentry connectors exist in this account but need your authorisation; nothing was connected or queried. Use `/app-launch-check`, and the `app-launch-reviewer` agent for a read-only review of a project.

See also `app-building-method-7-steps`, `saas-mvp-24h`, `production-audit`.
