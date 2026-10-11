---
name: claude-official-plugins-3
description: Three plugins from the claude-plugins-official marketplace shown by @awayfromlovable with their install commands and numbers - Modern Web Guidance (Chrome team, agent accuracy 50-57% -> 78-88%, 102 web features/129 use cases, 219 installs), Browser Use (real browser, 930 installs), Lovable (/lovable:iterate, :build, :db, 1,057 installs) - plus the "big-company plugins nobody installs" framing (most installed 1,134,112; PayPal 11). Use when choosing Claude Code plugins for web code quality, browser testing or Lovable.
---

# Official plugins (rank on the carousel in brackets)
- [#2] **modern-web-guidance** - `/plugin install modern-web-guidance@claude-plugins-official`. Chrome team's guidance so Claude stops writing outdated web code. Slide figures (their own numbers): agent accuracy 50-57% without, 78-88% with; 102 web features, 129 use cases; no API key. Already available in this environment as the `modern-web-guidance` skill.
- [#3] **browser-use** - `/plugin install browser-use@claude-plugins-official`. Opens Chrome or a cloud browser, fills forms, clicks, screenshots: "Claude sees what your users see". Already available as the `browser-use` skill (connection timed out this session; reconnect before relying on it).
- [#4] **lovable** - `/plugin install lovable@claude-plugins-official`. `/lovable:iterate bigger signup button` (shows the diff before you publish), `/lovable:build a new app`, `/lovable:db`. Official, by Lovable; changes still use your Lovable credits.
Slides read later: [#1] **PayPal** `/plugin install paypal@claude-plugins-official` (payments, subscriptions, invoices, disputes via PayPal's APIs and MCP server; 11 installs on the slide) and [#5] **HyperFrames** `/plugin install hyperframes@claude-plugins-official` (HeyGen; HTML to video, website-to-video capture, captions, GSAP; 2,119 installs). Not installed. The `hyperframes` skill already exists here.

**Installed 11 Oct 2026 in this cloud session (user scope):** `lovable`, `modern-web-guidance`, `browser-use` from `anthropic-plugin-directory`. `claude-plugins-official` is not a configured marketplace in Claude Code 2.1.296, so use `@anthropic-plugin-directory`. browser-use connects; lovable needs OAuth (`/mcp`). Install counts change daily. Vet: official marketplace only, read what permissions a plugin asks for, one at a time.
