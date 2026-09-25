---
name: camofox-browser
description: Anti-detection browser server for AI agents — gives an agent a real Firefox instance with C++-level fingerprint spoofing (via Camoufox) so it can browse sites that block headless Chrome/Playwright, without building stealth logic that itself becomes the fingerprint. Install with npm, runs at localhost:9377. Use when an agent needs to scrape or interact with sites that detect and block headless browsers.
---

# Camofox Browser

Source: [`jo-inc/camofox-browser`](https://github.com/jo-inc/camofox-browser) — MIT license.
Built by the team behind [Jo](https://askjo.ai), a personal AI agent.

## The problem it solves

AI agents need to browse the real web. The problem:

- Playwright → gets blocked (detected as headless)
- Headless Chrome → fingerprinted by site detection scripts
- Chrome stealth plugins → the plugin itself becomes the fingerprint

Camofox sidesteps this by using **Camoufox** — a Firefox fork that implements fingerprint spoofing at the C++ level, not the JavaScript level. Site detection scripts see a plausible, humanlike browser fingerprint because the browser's internals actually produce one.

## Quick start

```bash
git clone https://github.com/jo-inc/camofox-browser
cd camofox-browser
npm install && npm start
# → http://localhost:9377
```

The server runs locally and exposes a browser API your agent calls to navigate, click, fill forms, and scrape — against sites that would block a standard Playwright/Puppeteer session.

## When to use this vs. other browser-automation tools

| Tool | Best for |
|---|---|
| `camofox-browser` | Sites that actively detect and block headless/automated browsers |
| `microsoft/playwright-mcp` | Sites that don't block headless; structured MCP-based browser control |
| `browserbase/stagehand` | Mixed code + natural-language instructions; production workflows |
| `steel-dev/steel-browser` | Durable remote browser sessions (cloud-hosted, not local) |

Use Camofox when the root problem is **detection and blocking**, not just "I need browser automation."

## Before turning it loose on a real site

Apply the `web-task-scoping` skill's four-step discipline:
1. **Target** — define exactly what the agent needs (URL, data, action)
2. **Limit** — restrict tools and permissions to that scope only
3. **Run** — execute with monitoring
4. **Review** — verify output before acting on it

Fingerprint spoofing makes the agent look human; it doesn't make the agent's actions appropriate on every site. Respect robots.txt and terms of service.
