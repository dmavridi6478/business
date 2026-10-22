---
description: Run the six-tool launch checks (native flow, TestFlight task test, Supabase second-account test, PostHog funnel, Sentry crash repeat, RevenueCat entitlement) against an app and say what is proven and what is not
argument-hint: <app name or path> <platform ios/android/web>
---

Use the skill `app-launch-6-tools-ella` and the `app-launch-reviewer` agent. Input: "$ARGUMENTS".

1. Inspect the project read-only (auth and data layer, RLS policies, analytics events, error reporting, purchase code) and fill the skill's table: configured / tested / not found.
2. For each tool give the exact test from the card and the pass condition; mark anything you could not run as unproven. Do not call connectors (Supabase, Sentry) unless the user has authorised them in this session.
3. Output a go / no-go: the first thing to fix, and the order of checks. Never include secrets or user data in the report.
