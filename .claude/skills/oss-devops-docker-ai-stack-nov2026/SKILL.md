---
name: oss-devops-docker-ai-stack-nov2026
description: Register of 56 slides from five creators (@dotdevs DevOps and databases sets, @mapplebox.com Docker tools, @raphal3494 "startup stack on 4 GB of RAM" and "instead of" cards, @quadri_folo "10 brilliant GitHub projects") - Portainer, Dockge, Komodo, Arcane, Dozzle, K3s, Caddy, Argo CD, OpenTofu, Traefik, Qdrant, DuckDB, ClickHouse, libSQL, Valkey, Postgres, Plausible, GlitchTip, LobbyStack, Bigcapital, Twenty, Zero, Dokploy, Bun, SvelteKit, Better Auth, Craft Apps, EmDash, AnythingLLM, Jan, Khoj, LobeChat, GPT4All, and ten quadri_folo finds (Gyotaku, Lastbook, TeleDrive, kiri, Concat, Blender skills, Muse4AI, TapFeed, App Store compliance, Gamer) - with what is new versus covered, licences where the slide prints them, and the cautions the slides omit. Use before choosing a self-hosted stack or installing any of them.
---

# DevOps, Docker and AI stack slides (read 24 November 2026)

Checked: where noted, repos exist (`git ls-remote`). Licences are **as printed on the slide** unless marked "not read"; no repo licence file was read for this batch, and star counts (K3s 34,427, Caddy 79,165, Qdrant 35,624, DuckDB 43,138, Argo CD 24,636, OpenTofu 30,908, libSQL 17,335, Traefik 65,583, Valkey 27,735, ClickHouse 50,986, AnythingLLM 67,938, LobeChat 83,870, GPT4All 77,343, Khoj 37,978, Jan 45,438) are the slides' own, unchecked. Nothing was cloned, installed or run.

## Already covered earlier (not duplicated)

kiri, Twenty, Traefik, AnythingLLM, Jan, Dockge (see `self-hosted-docker-stack`), Craft Apps, Bun, Postgres-as-base, Springback, ClickHouse and Qdrant (patterns only), OpenTofu (multi-cloud skill).

## Docker management (@mapplebox.com, five tools)

| Tool | Line | Note |
|---|---|---|
| Portainer | The classic: containers, images, stacks in one web UI | Exposes the Docker socket: protect the UI like root access |
| Dockge | Compose files in a clean UI, by the maker of Uptime Kuma (`louislam/dockge`, exists) | Manages compose stacks by files |
| Komodo | Deploy stacks to all your servers, watch CPU, RAM, disk (`moghtech/komodo`, exists) | Agents on every server widen the attack surface |
| Arcane | Modern Docker dashboard that scans images for vulnerabilities | Repo not reachable anonymously from here; verify the real source first |
| Dozzle | Live logs and stats from every container in the browser | Logs can contain secrets |
Bonus: What's Up Docker (WUD) update alerts to your phone. Auto-updating containers without testing is a risk; alert, then update deliberately.

## DevOps (@dotdevs, slide licences)

K3s (Apache-2.0, lightweight Kubernetes), Caddy (Apache-2.0, automatic HTTPS), Argo CD (Apache-2.0, deploy to Kubernetes from Git), OpenTofu (MPL-2.0, Terraform fork), Traefik (MIT, reverse proxy). Kubernetes tools need real operations skill; for one server, Docker Compose plus Caddy is usually enough.

## Databases (@dotdevs)

Qdrant (Apache-2.0, vector search), DuckDB (MIT, analytics on files), ClickHouse (Apache-2.0, real-time analytics), libSQL (MIT, SQLite fork), Valkey (BSD-3-Clause, Linux Foundation Redis fork). Postgres from @raphal3494: "one copy is plenty" at about 100 MB under a busy test (the creator's own test).

## @raphal3494 "startup stack on 4 GB RAM"

Dokploy (instead of Vercel, `Dokploy/dokploy` exists), Plausible (instead of Google Analytics; its ClickHouse database is why 4 GB is needed), GlitchTip (Sentry-compatible), LobbyStack (AI receptionist, Twilio and OpenAI keys, you pay phone and AI), Bigcapital (instead of QuickBooks, `bigcapitalhq/bigcapital` exists), Zero (email client, instead of Superhuman, `Mail-0/Zero` exists), SvelteKit, Better Auth, EmDash (Cloudflare's WordPress successor), Valkey. The memory figures ("under 100 MB", "about 30 MB") are one author's test, not guarantees.
- AI receptionist: callers must be told a recording or AI is used where law requires it.
- Self-hosted bookkeeping and email: you own backups, security and, for accounts, compliance. Do not replace accounting software without your accountant.

## @quadri_folo "10 brilliant GitHub projects" (as the slides describe)

| # | Project | Slide line | Exists | Caution |
|---|---|---|---|---|
| 1 | Gyotaku | Screenshots into a searchable library with local OCR | yes | OCR of screenshots can capture passwords |
| 2 | Lastbook | Offline knowledge library (encyclopedias, maps, optional local AI) | yes | Large downloads |
| 3 | TeleDrive | Telegram as personal cloud storage | yes (master) | Against or near Telegram's terms for storage; do not keep the only copy there |
| 4 | kiri | Docker alternative with share link | covered | Public link |
| 5 | Concat | Open-source video editor with MCP | not checked | |
| 6 | Blender Agent Skills | Skills for Blender in coding agents | yes | |
| 7 | Muse4AI | Connects agents to Meta Muse via unofficial MCP/REST | yes | "Unofficial": may break or breach terms |
| 8 | TapFeed | View TP-Link Tapo cameras on a Windows desktop | not checked | Camera access: use strong passwords, local network only |
| 9 | App Store Compliance | Checks apps against App Store and Play requirements | yes | A checklist, not approval |
| 10 | Gamer | Experimental agent that plays games from the screen | yes | Research code; do not point at online games (cheating bans) |

## Not done

No licence files read, nothing installed, no star counts checked. Use `/repo-vet owner/repo` and `/repo-licence-check` first.
