# 7 GitHub Repos So Good They Shouldn't Be Free (Replace.so, Carousel 2)

Source: @replace.so (TikTok/Instagram). This repo already has one
`@replace.so` carousel documented in `github-repos-from-photos.md`
(deer-flow, excalidraw, memos, appsmith, Cap, listmonk, onlook, botpress,
apitable, umami, OpenHuman) — this is a **second, different** carousel from
the same creator. Only 5 of the claimed 7 slides were present in the source
photo batch (the title card and one repo slide were missing); the 5 below
are documented, the other 2 are not guessed at.

| Repo | Stars | What it does |
|---|---|---|
| [`BuilderIO/mitosis`](https://github.com/BuilderIO/mitosis) | 14,409★ | Build components in one codebase, compile them to React, Vue, Angular, Svelte, Solid, Alpine, Qwik, and more frameworks. |
| [`beto-rodriguez/LiveCharts2`](https://github.com/beto-rodriguez/LiveCharts2) | 5,473★ | Flexible, cross-platform .NET library for interactive charts, maps, and gauges across desktop, web, and mobile UI frameworks. MIT-licensed core, paid package for extended features. |
| [`microsoft/playwright`](https://github.com/microsoft/playwright) | 96,631★ | Reliable web automation for testing, scripting, and AI agents — one API to drive Chromium, Firefox, and WebKit. Ships `Playwright Test`, a token-efficient `Playwright CLI` for coding agents, and `Playwright MCP` for full agent browser control. Already referenced in this repo's `claude-code-tooling` skill as one of five browser-automation frameworks. |
| [`vuestorefront/storefront-ui`](https://github.com/vuestorefront/storefront-ui) | 2,682★ | Framework-agnostic Tailwind CSS UI library and design system for eCommerce (the "Alokai" brand) — accessible components, blocks, composables, React + Vue support. |
| [`honojs/hono`](https://github.com/honojs/hono) | 32,330★ | Small, ultrafast TypeScript web framework built on Web Standards — clean APIs, runs on any JS runtime (Cloudflare Workers, Deno, Bun, Node) and edge platforms. |

## Clone

```bash
mkdir -p ~/repos/replace-so-picks-2 && cd ~/repos/replace-so-picks-2
git clone --depth=1 https://github.com/BuilderIO/mitosis
git clone --depth=1 https://github.com/beto-rodriguez/LiveCharts2
git clone --depth=1 https://github.com/microsoft/playwright
git clone --depth=1 https://github.com/vuestorefront/storefront-ui
git clone --depth=1 https://github.com/honojs/hono
```

`microsoft/playwright` is the one with an immediate use here — it's already
flagged in `claude-code-tooling` as a recommended browser-automation
framework for agent workflows; `npx @playwright/mcp@latest` gives an agent
full browser control without cloning the repo at all.
