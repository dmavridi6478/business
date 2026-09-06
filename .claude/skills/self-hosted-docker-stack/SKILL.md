---
name: self-hosted-docker-stack
description: Curated directory of 10 self-hosted, Docker-deployable services covering game-server hosting, AI-powered local CCTV, media streaming, Docker stack management, PDF tooling, self-hosted AI chat, network-wide ad/tracker blocking, uptime monitoring, a self-hosted password manager, and self-hosted Git — each verified against its real GitHub/Codeberg repository. Use this when the user is planning a homelab, wants to self-host infrastructure instead of paying for a cloud/SaaS equivalent, asks "what should I run on my server," or is deciding between a hosted service and a self-hosted Docker alternative. Overlaps in part with lean-software-stack (both PDF tooling and password managers appear in both, as a desktop vs. server-hosted choice) — use that skill for desktop-app alternatives, this one for services meant to run continuously on a server/NAS.
---

# Self-Hosted Docker Stack

Source: "10 Docker Apps — Apps you'll actually use" carousel (@wellx.tech). Each entry's GitHub/Codeberg repo was verified by live web search (not taken from the carousel's branding alone) before being listed here.

## The 10 apps, by category

| # | App | Category | What it does | Verified repo |
|---|---|---|---|---|
| 1 | **Pterodactyl** | Game-server hosting | Free, open-source game server management panel — runs game servers (Minecraft, Rust, CS2, Valheim, etc.) in isolated Docker containers with a full admin/user UI | https://github.com/pterodactyl/panel |
| 2 | **Frigate** | Local AI CCTV | NVR with realtime local object detection for IP cameras — runs entirely on local hardware, no cloud dependency, MIT licensed | https://github.com/blakeblackshear/frigate |
| 3 | **Jellyfin** | Media server | Free, open-source personal media server (movies/TV/music/photos/live TV), multi-platform clients | https://github.com/jellyfin/jellyfin |
| 4 | **Dockge** | Docker stack management | Reactive, self-hosted `docker-compose.yaml` stack manager — create/edit/start/stop/update stacks from a web UI | https://github.com/louislam/dockge |
| 5 | **Stirling PDF** | PDF toolbox | Locally-hosted, self-hostable all-in-one PDF tool (merge, split, compress, convert, rotate, crop, reorder, watermark, protect/unlock, OCR, 50+ tools), REST API available | https://github.com/Stirling-Tools/Stirling-PDF |
| 6 | **Open WebUI** | Self-hosted AI chat | Self-hosted, privacy-first chat interface for local/API LLMs (Ollama, OpenAI-compatible APIs) — multi-model, RAG built in, MIT licensed | https://github.com/open-webui/open-webui |
| 7 | **AdGuard Home** | Network-wide ad/tracker blocking | DNS-level ad and tracker blocking for an entire network, not just one browser | https://github.com/AdguardTeam/AdGuardHome |
| 8 | **Uptime Kuma** | Uptime monitoring | Self-hosted uptime monitoring with status pages and alerting — a self-hosted alternative to a paid status-page SaaS | https://github.com/louislam/uptime-kuma |
| 9 | **Vaultwarden** | Password manager | Unofficial Bitwarden-compatible server written in Rust — lightweight self-hosted alternative to running the official (resource-heavy) Bitwarden server, compatible with official Bitwarden clients | https://github.com/dani-garcia/vaultwarden |
| 10 | **Forgejo** | Self-hosted Git | Lightweight, community-governed self-hosted Git service (a hard fork of Gitea) — repos, issues, pull requests; primary home is Codeberg, not GitHub | https://codeberg.org/forgejo (mirrors exist on GitHub, but Codeberg is the authoritative source) |

## When to reach for this list

- Planning a homelab or personal/small-team server stack, not just a single desktop tool.
- A recurring server-side cost (uptime monitoring SaaS, hosted password manager seats, hosted Git seats, a cloud CCTV subscription) is worth evaluating against a self-hosted equivalent — apply the `docs/procedures/free-vs-paid-tool-decision.md` procedure from `lean-software-stack` first (it generalizes past desktop apps to this list too: team size, sync needs, support-vs-portability trade-off, who owns maintenance).
- `the-leverage-stack-auditor` flags a recurring SaaS line item and this list has a matching self-hosted alternative.

## Overlap with `lean-software-stack`

Two categories appear in both lists — the choice between them is desktop-local vs. server-hosted, not a duplicate recommendation:

| Category | Desktop (`lean-software-stack`) | Server-hosted (this skill) |
|---|---|---|
| PDF tooling | PDFsam Basic — a local desktop app, no server/network exposure | Stirling PDF — runs continuously on a server, has a REST API for integrating into other systems |
| Password manager | KeePassXC — a local encrypted vault file, no server component | Vaultwarden — a server that syncs across devices/team members via the Bitwarden client protocol |

Pick the desktop option for a solo user with no sync/team need; pick the server-hosted option once multiple devices or people need shared access.

## How to use this list

- These are standalone server software, not skill files — same non-vendoring convention as `claude-code-tooling` and `lean-software-stack`. Running any of them requires actual server/NAS/homelab infrastructure this environment doesn't provide.
- Every repo URL above was verified via live search before being listed, not assumed from the source carousel's app names/logos alone — the carousel itself didn't show repo URLs.
- Forgejo's authoritative home is Codeberg (codeberg.org/forgejo), not GitHub — don't assume every self-hosted tool's primary repo lives on GitHub.
- Check current release activity/license before recommending one as production-critical — this is a snapshot, not a live-verified endorsement.

## Related skills in this repo

- **lean-software-stack**: The desktop-app sibling list, with the shared `free-vs-paid-tool-decision` procedure for deciding when self-hosting is worth the maintenance burden vs. paying for a managed service.
- **the-leverage-stack-auditor**: Check a recurring hosted-SaaS cost against this list before assuming a paid replacement is the only option.
- **claude-code-tooling**: Sibling curated-tool directory (Claude Code-specific tools) using the same standalone-software, non-vendoring convention.
- **attachment-intake**: This entry followed that procedure — inspected the carousel, then verified each tool's real repo via search before documenting anything, rather than trusting branding alone.

## Notes

Source: "10 Docker Apps — Apps you'll actually use" carousel (@wellx.tech). Unlike earlier tool-directory entries in this repo, the source material didn't display GitHub URLs directly — each repo listed above was located and confirmed via live web search, not carried over from the carousel's branding/logos alone.
