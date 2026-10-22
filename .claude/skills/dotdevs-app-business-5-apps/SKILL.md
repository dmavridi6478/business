---
name: dotdevs-app-business-5-apps
description: The @dotdevs "5 apps that run my entire app business" carousel (RevenueCat, Resend, PostHog, Plausible, TestFlight) with what each does, its site, and what is new here versus the existing app-launch skill. Use when choosing billing, email, analytics and beta-testing tools for a small app. Opinion list with no usage or revenue data.
---

# 5 apps that run an app business (@dotdevs carousel)

Source: 7 slides (cover, five apps, a follow slide). The author's one-line promise is kept; nothing else is claimed.

| App | Site | Slide promise | Role | Already covered |
|---|---|---|---|---|
| RevenueCat | revenuecat.com | "subscriptions without writing billing code" | In-app subscriptions and entitlements | `app-launch-6-tools-ella` |
| Resend | resend.com | "emails that land in the inbox" | Transactional email API | **new here** |
| PostHog | posthog.com | "see where users actually drop off" | Product analytics, funnels, session replay | `app-launch-6-tools-ella` |
| Plausible | plausible.io | "web analytics without the cookie banner" | Privacy-friendly website analytics | **new here** |
| TestFlight | developer.apple.com/testflight | "beta testers before the App Store" | iOS beta distribution | `app-launch-6-tools-ella` |

## Read critically
- **[Certain]** "Without the cookie banner" depends on your setup and jurisdiction; Plausible avoids personal-data cookies, but PostHog and many SDKs do not.
- **[Certain]** Deliverability ("lands in the inbox") is decided by your domain setup (SPF, DKIM, DMARC) and sending behaviour, not by the API alone.
- **[Likely]** RevenueCat charges a share of tracked revenue above a threshold; check current pricing before you commit.
- Use `/app-launch-check` to review launch readiness. Prices and free tiers were not checked here.
