---
name: app-store-toolchain-5
description: The @awayfromlovable "Top 5 Claude Code tools that turn your web app into an App Store app" - Expo plugin (15,861 installs), Mobile MCP (8,753 stars), RevenueCat plugin (3,381 installs), asc App Store Connect CLI (7,689 stars) and App Store Review skill (97 stars) - with the commands as shown, what each needs (accounts, a Mac, the $99 Apple fee), the order to use them in and a pre-submission checklist. Use when taking a web app to the iPhone App Store, adding subscriptions, testing on a simulator, or checking for review rejections.
---

# Web app to App Store: 5 tools

Numbers are the slides' own. Plugin commands on the slides use the marketplace name `claude-plugins-official`; in this environment the marketplace is `anthropic-plugin-directory`, so search with `/plugin` and check the publisher. Nothing was installed here.

| # | Tool | Does | Needs | Command as shown |
|---|---|---|---|---|
| 1 | **Expo** (official, 15,861 installs) | "turn my Vite app into an iPhone app": web UI in a native shell first, then converts screens one by one, builds and ships with Expo | free Expo account | `/plugin install expo@claude-plugins-official` |
| 2 | **Mobile MCP** (8,753 stars, free, OSS) | Claude taps, types and swipes through your app on a simulator, emulator or real phone and screenshots what looks broken | iPhone simulator needs a Mac | `/plugin marketplace add mobile-next/mobile-mcp` then `/plugin install mobile-mcp@mobile-mcp` |
| 3 | **RevenueCat** (official, 3,381 installs) | subscriptions and paywalls: products, paywalls and API keys for iPhone and Android (example: monthly $9.99, annual $79.99) | RevenueCat account; free until $2,500/month tracked revenue (slide) | `/plugin install revenuecat@claude-plugins-official` |
| 4 | **asc** (community, 7,689 stars) | App Store Connect busywork: TestFlight groups and testers, signing and certificates, screenshots and store listing, submit build for review | Apple developer account, $99 a year | `brew install asc && asc install-skills` |
| 5 | **App Store Review** (97 stars) | `/appstore-review` flags web-wrapper apps, missing Sign in with Apple, no way to delete an account; run before you submit | none | `/plugin marketplace add devsemih/appstore-review-skill` then `/plugin install appstore-review-skill` |

## Order
Expo (wrap) -> Mobile MCP (test on a simulator) -> RevenueCat (payments) -> App Store Review (pre-flight) -> asc (ship). Run the review check before asc submits anything.

## Safety
- asc and RevenueCat act on live accounts: use a TestFlight/sandbox build first; require your approval before submit, price changes or certificate creation.
- Third-party marketplaces (Mobile MCP, App Store Review, asc) are unofficial: read the plugin files; the 97-star skill especially is not Apple guidance.
- A thin web wrapper is the commonest rejection (guideline 4.2 minimum functionality); add real native features, Sign in with Apple if you offer other social login, and in-app account deletion.
Related: `alinacoding-app-business-6`, `/app-business-check`, `app-building-method-7-steps`, `ios-icon-gen`, `paywalls`, `aso`. Command: `/appstore-preflight`.
