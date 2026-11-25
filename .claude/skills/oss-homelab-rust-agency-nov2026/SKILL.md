---
name: oss-homelab-rust-agency-nov2026
description: Checked register of 25 slides from three creators - @mapplebox.com "5 free tools that watch your homelab" (Uptime Kuma, ntfy, Beszel, Dozzle, What's Up Docker plus the alert setup), @raphal3494 "6 repos written in Rust" (Codex, Firecracker, Pingora, Microsoft Edit, Vaultwarden, RustDesk) and "7 open-source tools to start an agency" (Activepieces, LobbyStack, Twenty, Postiz, Documenso, InvoiceShelf, Cap), and @dotdevs "Free design tools for devs who can't design" (Realtime Colors, Fontshare, Coolors, Squoosh, Excalidraw, Crest bonus) - with licences read from 22 repos, what is new versus already registered, and the cautions the cards omit (mixed licences, ntfy topics as passwords, Pingora is a library, e-signature and invoicing compliance, a non-commercial colour tool repo). Use before choosing a self-hosted monitor, proxy, signing, invoicing or scheduling tool.
---

# Homelab, Rust and agency tool cards (read 25 November 2026)

Repos, default branches and licence files read on 25 November 2026 (`git ls-remote`, raw licence files). Star counts and usage figures on the cards were **not** verified (GitHub API blocked). Nothing was cloned or run.

## Already registered (not duplicated)

Uptime Kuma, Dozzle, What's Up Docker, Beszel (see `oss-devops-docker-ai-stack-nov2026`, `self-hosted-docker-stack`, `dev-repos-to-clone`), Vaultwarden, RustDesk, Twenty, LobbyStack, Cap, Excalidraw, Coolors, Realtime Colors, Fontshare, Codex (runner templates). The "Instead of" card layout already exists as `Artifacts/templates/instead-of-dark-card.html`. New here: **ntfy, Pingora, Microsoft Edit, Firecracker, Activepieces, Documenso, InvoiceShelf, Postiz (first full entry), Squoosh, Crest**.

## Homelab watch (@mapplebox.com, 5 slides + bonus)

| Tool | Repo (branch) | Licence (read) | Note |
|---|---|---|---|
| Uptime Kuma | `louislam/uptime-kuma` (master) | MIT | Checks services 24/7. Has a built-in ntfy notification provider (server URL, topic, optional access token) |
| ntfy | `binwiederhier/ntfy` (main) | Apache-2.0 and GPLv2 (dual) | Push to phone from any script by HTTP. On the free public server the topic name is effectively the password (ntfy docs): anyone who knows it can read or post. Use a long random topic, or self-host with access control. Never put secrets in messages |
| Beszel | `henrygd/beszel` (main) | MIT | CPU, RAM, disk history per server, alerts |
| Dozzle | `amir20/dozzle` (main) | MIT | Live Docker logs in a browser; logs can contain secrets |
| What's Up Docker | `getwud/wud` (main) | MIT | Tells you a container has a newer image. Alert, then update on purpose |
| Alert setup | mapplebox.com/alerts | not supplied | The "Uptime Kuma + ntfy step by step" slide is a title card only; the steps were not in the files |

## Rust six (@raphal3494)

| Tool | Repo (branch) | Licence (read) | Caution the card omits |
|---|---|---|---|
| Codex | `openai/codex` (main) | Apache-2.0 | Your code goes to OpenAI; "comes with your ChatGPT plan" is a vendor claim |
| Firecracker | `firecracker-microvm/firecracker` (main) | Apache-2.0 | A virtual-machine monitor for building platforms, not an app. "15 trillion functions, boots under 125 ms" is AWS's figure, unverified |
| Pingora | `cloudflare/pingora` (main) | Apache-2.0 | A Rust **framework** to build proxies, not a drop-in Nginx replacement. "Instead of Nginx" needs you to write Rust. The 40M requests/s figure is Cloudflare's, unverified |
| Microsoft Edit | `microsoft/edit` (main) | MIT | Terminal editor; "under 250 kB" and "ships with Windows 11" are the card's claims, unverified |
| Vaultwarden | `dani-garcia/vaultwarden` (main) | AGPL-3.0 | Unofficial Bitwarden-compatible server. You own backups, updates and uptime for your password vault |
| RustDesk | `rustdesk/rustdesk` (master) | AGPL-3.0 | Remote access is a high-value attack target: strong password, 2FA where offered, your own relay if you can |

## Agency seven (@raphal3494, "Instead of ...")

| Tool | Repo (branch) | Licence (read) | Caution the card omits |
|---|---|---|---|
| Activepieces (Zapier) | `activepieces/activepieces` (main) | MIT outside `packages/ee`; enterprise folders under a separate licence | "Host it yourself for free" holds for the MIT part only. "770+ apps" unverified |
| LobbyStack | not reachable anonymously (batch 128) | not read | Verify the real source before relying on it. Selling an AI receptionist: call recording and consent rules apply |
| Twenty (HubSpot) | `twentyhq/twenty` (main) | Mostly AGPL-3.0 with exceptions | "Free when you host it yourself" excludes your admin time |
| Postiz (Hootsuite) | `gitroomhq/postiz-app` (main) | AGPL-3.0 | Posting to 30+ networks needs each network's API approval and tokens; the card shows a paid trial for the hosted service |
| Documenso (DocuSign) | `documenso/documenso` (main) | AGPL-3.0 | "Fully compliant signatures" is the vendor's claim. Which signature level (simple, advanced, qualified under EU eIDAS) a document needs is a legal question; self-hosting means your own certificates and storage |
| InvoiceShelf (FreshBooks) | `InvoiceShelf/InvoiceShelf` (3.x) | AGPL-3.0 | Slide shows "latest stable 2.4.7" while the default branch is 3.x. Tax-compliant invoicing rules differ by country (in Greece, transmission to AADE myDATA): not checked here; ask your accountant before replacing invoicing software |
| Cap (Loom) | `CapSoftware/Cap` (main) | AGPL-3.0 for most code; MIT only for `cap-camera*` and `scap-*` crates | "Your Loom videos come with you" (import) not tested; the card also shows a paid cloud service |

## Free design tools (@dotdevs)

| Tool | Link | Licence | Note |
|---|---|---|---|
| Realtime Colors | realtimecolors.com; repo `juxtopposed/realtimecolors` | Repo: **CC BY-NC-ND 4.0** | Free to use as a website; the code is non-commercial and no-derivatives, so do not fork it into a product |
| Fontshare | fontshare.com | Font licence not read | "Free" is the foundry's licence, not open source; read it before commercial or embedding use |
| Coolors | coolors.co | Closed service | Free tier; Pro features paid |
| Squoosh | `GoogleChromeLabs/squoosh` (dev) | Apache-2.0 | Runs in the browser; the app can be used offline once loaded (README, not tested) |
| Excalidraw | `excalidraw/excalidraw` (master) | MIT | An Excalidraw MCP connector exists in the directory (not installed here) |
| Crest (bonus) | App Store: "CREST: PR Tracker, 1RM Log" | Closed iOS app | Free listing by an individual developer; the store lookup showed 0 ratings (slide shows 2). A fitness log, not a design tool; treat as unverified |

## Source problems

- Titles promise "free" and "instead of": operating cost, backups, compliance and your time are not free.
- "Open source" is mixed: AGPL (network copyleft), enterprise folders, non-commercial colour tool code.
- All figures (stars, requests per second, boot times, app counts) are the creators'; none were measured.

## Not done

Nothing installed or run; Fontshare licence, LobbyStack source and the alert-setup steps not read. Use `/homelab-alerts-plan`, `/free-app-pick`, `/repo-vet owner/repo`, `/repo-licence-check`.
