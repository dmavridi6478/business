---
name: startup-stack-2gb-ram
description: A 14-tool self-hosted startup stack (Kamal, Bun, Hono, Postgres, Valkey, Meilisearch, Umami, Uptime Kuma, Netdata, GlitchTip, Better Auth, Listmonk, n8n, OpenProfit) from a @raphal3494 "runs on 2 GB of RAM" carousel, plus five web-UI libraries from @dotdevs (Radix, Motion, TanStack Query, Tailwind, Zustand) and three trending repos from @githubnow (AFFiNE, Ghost-Downloader-3, plannotator), with what each replaces, what is already in this library, licence catches and the limits of the memory claims. Use when choosing a low-cost self-hosted stack for a small product or deciding which paid SaaS to replace.
---

# Startup stack on 2 GB of RAM, plus web UI and trending repos (Batch 132, 23 November 2026)

Sources: three carousels. Stars below are as printed on the cards; none was re-read on GitHub in this session (the fetch tool was rate-limited), so re-check before quoting. Licences are from general knowledge, marked [Likely].

## A. The 14-tool stack (@raphal3494)

| Tool | Card says it replaces | Job | Licence [Likely] | In this library | Catch |
|---|---|---|---|---|---|
| Kamal | Coolify | Deploy a web app from your laptop with one command; server runs a small proxy for HTTPS and zero-downtime deploys | MIT | `rails-patterns`, `agent-production-readiness` | Deploy tool, not a control panel; no UI |
| Bun | Node.js | Fast JS runtime, TypeScript as is, built-in SQLite | MIT | mentions only | Card says Anthropic bought it; check current ownership and Node compatibility for your packages |
| Hono | Express | Tiny web framework on Web Standards; runs on Node, Cloudflare and others | MIT | none dedicated | "Under 14 kB" is the tiny preset only |
| Postgres | Supabase | One database for the app and several tools | PostgreSQL licence | `postgresql-table-design`, `postgres-patterns` | Supabase is Postgres plus auth, storage and realtime; replacing it means replacing those too |
| Valkey | Redis Cloud | Cache and job queue; Linux Foundation fork of Redis | BSD-3 | cloud docs only | Check your client library supports it |
| Meilisearch | Algolia | Search-as-you-type, results "under 50 ms" | MIT (community edition) | none | Some features are in paid cloud or enterprise editions |
| Umami | Google Analytics | Privacy-first web analytics, no cookies | MIT | `self-hosted-docker-stack` | You own the database and backups |
| Uptime Kuma | UptimeRobot | Checks as often as every 20 s, alerts to Slack, Discord, email, status page | MIT | `swap-5-dotdevs-subscriptions`, `oss-alternatives` | A monitor on the same server dies with the server |
| Netdata | Datadog | Per-second CPU, memory, disk for host and containers, disk-full warnings | GPL-3 agent; cloud parts are not open [Likely] | none | Agent is open; the hosted dashboard is a product |
| GlitchTip | Sentry | Error tracking that works with Sentry SDKs | MIT | none | Fewer features than Sentry; no performance suite |
| Better Auth | Clerk | Auth framework inside your app and database; passkeys, magic links, Google | MIT | `oss-swap-part-18` | Auth is security-critical: you own patches and session handling |
| Listmonk | Mailchimp | Newsletters and lists from your own server; you pay only your sending provider | AGPL-3 | `self-hosted-docker-stack` | AGPL; deliverability and consent are yours |
| n8n | Zapier | Workflows and agents, 1,500+ connectors | Sustainable Use (fair-code), not OSI open source | many `n8n-*` skills | Free for internal use; hosting it for others or reselling needs a licence |
| OpenProfit | a spreadsheet | Joins Stripe, OpenAI, Vercel costs into profit per product | MIT on the card | none | Needs read-only API keys to billing systems; create restricted keys |

**The 2 GB claim.** Card figures: Postgres peaked about 270 MB with 20 clients; n8n about 420 MB ("heaviest tool here"); Valkey and job queue about 14 MB. These are one author's test, with no stated workload, and no total is shown. [Guessing] Fourteen services on one 2 GB server leaves little headroom for your own app, backups, updates or a traffic spike. Treat it as "possible for a demo", then test with your load before relying on it.

**Single-server risk.** Monitoring, errors, auth, mail and the database all on one machine means one outage takes the product and the tools that would tell you. Keep Uptime Kuma or an external ping off the box, and keep offsite database backups.

## B. Five web-UI libraries (@dotdevs, all MIT on cards)

| Library | Card stars | Job | In this library |
|---|---|---|---|
| Radix Primitives | 19,523 | Unstyled accessible components | `tailwind-design-system` |
| Motion | 35,315 | Animate React and plain JS | `motion-patterns`, `better-ui` |
| TanStack Query | 50,575 | Fetch, cache and update server data | `react-state-management` |
| Tailwind CSS | 98,772 | Utility classes instead of custom CSS | `tailwind-design-system` |
| Zustand | 58,943 | Small React state manager | `react-state-management` |

All five already have guidance in this library; nothing new to add except that they work together (Tailwind for styling, Radix for behaviour, Motion for animation, TanStack Query for server state, Zustand for client state).

## C. Three trending repos (@githubnow, 19 November 2026)

| Repo | Card | Does | Care |
|---|---|---|---|
| `toeverything/AFFiNE` | +170 stars today | Docs, whiteboards and databases on one canvas; local-first, self-hostable | Compare with `lean-software-stack`; self-hosting means you run sync and backups |
| `XiaoYouChR/Ghost-Downloader-3` | +432 stars today | One download manager for HTTP, magnet/BT, FTP, M3U8, DASH, eD2k; RPC API | Torrent and video-site downloading can breach copyright or site terms; the card's screenshot is a Chinese-language UI; read the install source |
| `backnotprop/plannotator` | +689 stars today | Local browser review of agent plans and diffs; comments go back as the agent's next turn; works with Claude Code, Codex, Gemini CLI, OpenCode | Feeds your comments into an agent: do not paste secrets into annotations; read the plugin before enabling |

## Pick order for a small product

1. Postgres, Hono or your existing framework, Better Auth, Kamal.
2. Uptime Kuma (off-box), GlitchTip, Umami.
3. Meilisearch, Valkey, Listmonk only when the feature is needed.
4. n8n and OpenProfit last; both touch third-party accounts.

## D. Part 2 from @raphal3494: "The Rust stack that runs on 657 MB of RAM" (Batch 135)
Same series, a Rust-based variant: app, search, backups, analytics, error tracking and monitoring on one server. Tools shown beyond Part 1 (card text, figures not verified):

| Tool | Card says it replaces | Job | Catch |
|---|---|---|---|
| Axum | Express | Rust web framework from the Tokio team; "your whole backend, sign-in included, ran on 6 MB" | Rust skills needed; the 6 MB is one author's test |
| SQLx | Supabase | Checks SQL at compile time; talks to SQLite | It is a library, not a hosted backend |
| axum-login | Clerk | Sign-up, log-in and sessions for an Axum app, users in your SQLite file | Auth is security-critical: you own patches and reviews |
| Litestream | Backups | Streams every SQLite change to cheap S3 storage; restore to the last transaction | Test restores; S3 credentials need least privilege |
| Beszel | Datadog | CPU, memory, disk per server and Docker container with alerts; about 56 MB, "a third of Netdata" | Lighter than Netdata, fewer features |
| Gatus | UptimeRobot | Checks sites around the clock; alerts on Slack, Discord, email; set up in one YAML file | Monitor from a different machine |
| Docmost | Notion | Wiki edited in real time; imports Notion and Confluence | Check licence edition (open core) |
| RustDesk | TeamViewer | Open-source remote desktop on your own server | Remote access to machines: lock down who can connect |
| Cal.com | Calendly | Scheduling; free plan unlimited event types; Stripe or PayPal | Self-hosting is yours to secure; hosted free plan is a vendor |
| Documenso | DocuSign | E-signatures; 5 free documents a month or self-host | Legal validity of e-signatures varies by country and document type |
| Formbricks | Typeform | Surveys and forms; free plan 250 responses a month | You store respondents' data |
| Twenty | Salesforce | CRM you own; self-host free or pay $9 a user | Customer data: backups and access control |
| Vaultwarden | 1Password | Bitwarden-compatible password server | Unofficial; a password vault is your highest-value target: back up and update promptly |
| LobbyStack | Smith.ai | AI receptionist: answers calls 24/7, books appointments | Not open source on its card; call recording and AI disclosure rules apply |

Total claimed: 657 MB for the whole stack. Same cautions as Section A: one test, no workload, one server as a single point of failure.


Run with `/stack-pick <product, traffic, budget>`. Related: `self-hosted-docker-stack`, `oss-alternatives`, `swap-5-dotdevs-subscriptions`, `lean-software-stack`, `trial-repo`, `n8n-self-hosting`, `local-first-app-stack`.
