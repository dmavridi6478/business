---
name: app-in-24-hours
description: A @dotdevs 24-hour app-build timetable (Figma wireframe, Bolt scaffold, Supabase backend and auth, Stripe or RevenueCat payments, Vercel deploy) plus five repos to star first (shadcn/ui, Drizzle ORM, tRPC, Better Auth, PostHog). Use when planning a fast MVP, choosing a stack for a first app, or turning the timetable into a checklist.
---

# How I'd Build an App in 24 Hours

Source: @dotdevs TikTok carousels. Hour ranges are the post's; treat them as a pacing guide, not a promise.

| Hours | Step | Tool shown |
|---|---|---|
| 1-2 | Wireframe | Figma |
| 3-6 | Scaffold the app | Bolt (bolt.new) |
| 7-14 | Backend and auth | Supabase |
| 15-20 | Payments | Stripe or RevenueCat |
| 21-24 | Deploy and post the teaser | Vercel |

## Five repos to star before the build

| Repo | Role | Card note |
|---|---|---|
| shadcn-ui/ui | UI components you own | copy into your repo |
| drizzle-team/drizzle-orm | Typed database layer | "in an afternoon" |
| trpc/trpc | Type-safe APIs, no schema files | |
| better-auth/better-auth | Authentication framework | "auth without the headache" |
| PostHog/posthog | Self-hostable product analytics | |

Existence of all five GitHub repos was confirmed with `git ls-remote` on 7 Oct 2026. Star counts on the cards (for example Better Auth about 30k) were not re-checked. Licences were not verified for these five; check before commercial use.

## Checklist

1. Write the one-sentence value and the three screens (hour 0).
2. Wireframe the three screens in Figma. Stop at hour 2.
3. Scaffold; connect Supabase; enable row-level security before storing real data.
4. Add one payment path only. Test with Stripe test keys.
5. Deploy; add analytics (PostHog); publish a short teaser.

Safety: use test keys, never paste production secrets into an AI app builder, and read the generated auth code before launch. Command: `/app-24h`.
