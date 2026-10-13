---
name: oss-swap-savings-table-10
description: The "10 free GitHub repos replacing $100M+ software companies, Part 2" swap table (Cloudinary to imgproxy, GitBook to Docusaurus, Pinecone to Qdrant, Zapier to Activepieces, CircleCI to Woodpecker CI, Notion to AppFlowy, Dropbox to Seafile, Docker Desktop to Podman, HubSpot to Odoo, Okta to Authelia) with the real licence of each free tool, the arithmetic error on the closing slide, what the "$0" leaves out (hosting, time, upgrades, support), and which swaps are worth doing for a small business. Use when the user asks whether to replace a paid tool with a self-hosted one, wants the licence consequence, or wants to check a savings claim.
---

# 10 paid-to-free swaps - checked

Source: @modelsignal carousel, 12 slides (pages 01 to 12), prices "read 11 Oct" and repos "checked 11 Oct" by the author. On 13 October 2026 I read each free tool's repository and licence file. **Paid prices and star counts were not re-checked.** The author's own line is "our call, not theirs".

## Table

Prices are per year for one seat or the entry plan, as the slides show them.

| Swap | Paid (slide) | Free tool's licence (from the repo) | What the swap really means |
|---|---|---|---|
| Cloudinary to **imgproxy** | $1,068 | Apache-2.0 (LICENSE file); a paid imgproxy Pro exists | You host an image-resizing server and cache. Great for developers, no help for a marketer who used Cloudinary's media library |
| GitBook to **Docusaurus** | $780 | MIT | A static docs site you build and host (Node, Git). Strong fit for developer docs, weaker for non-technical editors |
| Pinecone to **Qdrant** | $240 | **Not confirmed from the repo.** I know Qdrant as Apache-2.0, but its LICENSE file could not be fetched here; confirm before relying on it | A vector database you run. Only useful if you already build search or RAG |
| Zapier to **Activepieces** | $240 | **MIT, except the `ee` directories**, which have a separate licence | Self-hosted automation. Fewer ready-made connectors than Zapier; check your apps exist |
| CircleCI to **Woodpecker CI** | $180 | Apache-2.0 | CI runner you host. Only for teams that already use Git hosting like Gitea or GitHub |
| Notion to **AppFlowy** | $120 | **AGPL-3.0** | Notes and docs app. Self-hosting is a separate guide; the cloud and sharing features differ |
| Dropbox to **Seafile** | $120 | Server licence **not confirmed from the repo** (secondary sources say the community server is AGPL-3.0 and Professional is proprietary; older pages say GPLv2) | You run a file server and own backups. Read the official licence page before client use |
| Docker Desktop to **Podman** | $108 | Apache-2.0 | Container engine. Real saving only if your company must pay for Docker Desktop. As I understand Docker's terms, larger companies must and small ones may not; confirm against Docker's current terms |
| HubSpot to **Odoo** | $84 | **LGPL-3.0** for the community edition (per the repo's LICENSE); Enterprise is proprietary | A whole ERP, not a CRM. Heavy to run and customise |
| Okta to **Authelia** | $72 | Apache-2.0 | Self-hosted single sign-on and 2FA. Security infrastructure: a mistake locks everyone out or lets the wrong person in |

## Corrections to the closing slide

- **The total does not match the list.** The slide shows 8 rows and says "8 of 10" and "Save $3,012 a year". The 8 rows add to **$2,856**. $3,012 is the sum of **all ten** (adding HubSpot's $84 and Okta's $72).
- **The prices are single-seat.** Okta at $72 a year is $6 a month for one user; HubSpot at $84 is $7 a month. A team's real saving scales with seats, while self-hosting cost stays fixed per server.
- **"$0" means no licence fee, not no cost.** Left out: a server to run it on, backups, upgrades, security patches, uptime, and your own hours. One bad weekend can cost more than a year of the paid plan.
- Cloudinary, Dropbox and Notion are used for features the free tool may not replicate (CDN delivery, sharing links, collaboration). The slide compares names, not features.

## Decision rule

Swap only when all three hold: (1) you have a person who will own the server, (2) the free tool covers the features you actually use, (3) a failure does not stop the business. By that rule, for a small business:

- **Worth trying:** Docusaurus (docs you control), Podman (if Docker licence applies to you), AppFlowy for a private notes space, Activepieces for a few simple flows.
- **Only with a technical owner:** imgproxy, Qdrant, Woodpecker CI.
- **Do not self-host casually:** Authelia (identity), Odoo (ERP scope), Seafile (your files and backups).

## Overlap already in this repo

`open-source-swap-stack-8`, `ms365-free-alternatives`, `lean-software-stack`, `self-hosted-docker-stack` and `oss-alternatives` cover related swaps. This skill adds the licence reading and the arithmetic check.

## Command

`/swap-savings <the paid tools you use and your seat counts>` returns which swaps pass the decision rule, the licence consequence and the real yearly saving.
