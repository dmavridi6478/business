---
name: modelsignal-free-swaps-22
description: The @modelsignal "paid tool -> free GitHub repo" series, Part 5 (10 swaps, "replacing $100M+ software companies") and Part 11 (12 swaps, "save $5,419/year") - all 22 pairs with the slide's price and stars, the licence read from each repo's LICENSE file on 15 October 2026, the savings arithmetic, and the catch the slide omits (hosting and admin time, copyleft, source-available licences, features that do not match).
---

# 22 paid-to-free swaps (@modelsignal, Parts 5 and 11)

Source: two carousels. Part 5 = 12 slides (cover, ten swaps, summary "8 of 10. Save it." - Comment "GIT"); Part 11 = 14 slides (cover, twelve swaps, summary "8 of 12. Save it." - Comment "FREE"). Each card shows paid price, annual cost, free alternative at "$0", stars, contributors, last push, and "Our call, not theirs". Prices were "read 11-12 Oct" by the author; stars and push dates are the author's and **unverified here**. Licences below were read from each repo's root LICENSE file on 15 October 2026 (repo slug in the table).

**Arithmetic check:** Part 5's ten annual figures sum to $4,608 (the slide's headline), although its summary slide lists only eight ($4,500). Part 11's twelve sum to $5,419 (matches; the summary lists eight, $5,171). Combined: 22 swaps, $10,027 a year, **before** the cost of running them.

## Part 5

| Category | Paid (slide $/yr) | Free alternative | Repo | Licence | Catch |
|---|---|---|---|---|---|
| Team chat | Microsoft Teams ($48) | Rocket.Chat | RocketChat/Rocket.Chat | MIT | Teams is usually bundled with Microsoft 365, so the saving is often $0; check for enterprise-licensed folders |
| Short links | Short.io ($60) | YOURLS | YOURLS/YOURLS | MIT | Basic: analytics and team features are thinner |
| Help desk | Zoho Desk ($84) | UVdesk | uvdesk/community-skeleton | OSL-3.0 | Network-use copyleft; check feature parity (SLAs, automations) |
| Invoicing | Bonsai ($108) | Invoice Ninja | invoiceninja/invoiceninja | Elastic License | **Source-available, not open source**; self-hosted branding removal is a paid licence |
| PDFs | Smallpdf ($144) | Stirling-PDF | Stirling-Tools/Stirling-PDF | MIT | Check for non-MIT folders if you modify or resell |
| Photo library | SmugMug ($240) | PhotoPrism | photoprism/photoprism | AGPL-3.0 | Personal library, not client-gallery sales; you own backups |
| DevOps | GitLab ($348) | OneDev | theonedev/onedev | MIT | Different ecosystem and runners; migration cost |
| HR | Gusto ($588) | Frappe HR | frappe/hrms | GPL-3.0 | **Does not file payroll taxes or run compliance for you**; Gusto's value is payroll filing |
| Doc chat | CustomGPT ($1,188) | AnythingLLM | Mintplex-Labs/anything-llm | MIT | You still pay for the model API or run a local model |
| Tracing | Honeycomb ($1,800) | Jaeger | jaegertracing/jaeger | Apache-2.0 | Jaeger traces; it is not Honeycomb's query and analysis product; you pay for storage and ops |

## Part 11

| Category | Paid (slide $/yr) | Free alternative | Repo | Licence | Catch |
|---|---|---|---|---|---|
| Git hosting | GitHub ($48) | Gitea | go-gitea/gitea | MIT | Loses GitHub Actions marketplace, Copilot, network effects |
| Passwords | Dashlane ($48) | Passbolt | passbolt/passbolt_api | AGPL-3.0 | Self-hosting a password manager makes you responsible for its security and backups |
| Link pages | Linktree ($72) | LinkStack | LinkStackOrg/LinkStack | AGPL-3.0 | Smaller project; slide shows push 8 days old |
| Wiki | Slab ($80) | BookStack | BookStackApp/BookStack | MIT | Structured books/shelves, not freeform pages |
| Meeting notes | Fireflies ($120) | Meetily | Zackriya-Solutions/meeting-minutes | MIT | Local transcription: check language support (e.g. Greek) before relying on it; slide shows push 26 days old |
| Links | Rebrandly ($132) | Shlink | shlinkio/shlink | MIT | Needs a domain, PHP/DB or Docker |
| Mail testing | Mailosaur ($240) | Mailpit | axllent/mailpit | MIT | Local capture tool; Mailosaur is hosted for end-to-end CI |
| API gateway | Zuplo ($300) | Kong | Kong/kong | Apache-2.0 | Zuplo is managed; Kong means you run gateway infrastructure |
| Vector DB | Weaviate Cloud ($540) | Milvus | milvus-io/milvus | Apache-2.0 | Different API; a cluster to operate; managed offerings exist if you want ops done |
| Localization | Crowdin ($600) | Tolgee | tolgee/tolgee-platform | Apache-2.0 | Check enterprise-only folders and the hosted-plan differences |
| Remote access | TeamViewer ($1,451) | RustDesk | rustdesk/rustdesk | AGPL-3.0 | You run the relay server; an exposed remote-access server is a security risk to patch |
| Translation | Lokalise ($1,788) | Weblate | WeblateOrg/weblate | GPL-3.0 | Self-host needs admin; Weblate also sells hosting |

## How to use this honestly

1. Per swap, add the real cost of the free option: server (about $5-20/month for a small VPS), your hours (updates, backups, security), and any model or storage bills. A $48/yr tool is almost never worth an hour a month.
2. The big-ticket rows (TeamViewer, Lokalise, Honeycomb, CustomGPT, Weaviate, Crowdin) are the only ones where the maths can clearly win - and they are the ones with the most operations work.
3. Copyleft (GPL/AGPL/OSL) is no problem for internal use; if you modify and offer the software to others, read the licence. Elastic License (Invoice Ninja) forbids offering it as a managed service.
4. Run `/swap-stack-check <tool>` or `/self-host-swap` for a specific tool, and `/repo-licence-check` before any commercial use. Nothing here was installed.

See also `open-source-swap-stack-8`, `swap-5-dotdevs-subscriptions`, `self-hosted-docker-stack`, `free-vs-paid-tool-decision` (procedure).
