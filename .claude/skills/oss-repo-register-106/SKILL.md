---
name: oss-repo-register-106
description: 'Verified register of 27 repos from the fourth and fifth iCloud batches (6 Oct 2026) - ten free GitHub repos for Claude users (SearXNG, Reactive Resume, changedetection.io, gallery-dl, LocalSend, Vaultwarden, ArchiveBox, LibreTranslate, cobalt, Suwayomi), the cloud-bill seven (Coolify, Ubicloud, SeaweedFS, SigNoz, Typesense, imgproxy, Trigger.dev), the replace.so six (LangWatch, Dagu, Fleetbase, Pullfrog, Orca, Multica), GitHub-trending cards (diagram-design, Substrate, OpenRig) and Awesome Claude Skills - with real licence, stars, install route and legal or licence warnings. Read before cloning or recommending any of them.'
---

# Repo register - batch 106

Checked on public GitHub pages on 6 Oct 2026 (page text; **last-push dates were not visible**, so activity is unconfirmed). Stars move daily and a few large numbers were not cross-checked (marked *). **Nothing was cloned or installed in the cloud session.** User-run steps: `scripts/batch106-install.sh`.

## A. "10 free GitHub repos for Claude" (@your.aimentor)
| Repo | What it is | Licence | Stars | Warning |
|---|---|---|---|---|
| `searxng/searxng` | Metasearch engine, no tracking | AGPL-3.0 | ~38k | AGPL: offering it as a service needs source disclosure |
| `AmruthPillai/Reactive-Resume` (now `reactive-resume/reactive-resume`) | Privacy-first resume builder | MIT | ~43.9k | Docker install; AI features need your own provider key |
| `dgtlmoon/changedetection.io` | Web page change alerts | Apache-2.0 | ~34.8k | AI features send page content to third-party LLMs; hosted tier is paid |
| `mikf/gallery-dl` | Bulk image gallery downloader CLI | GPL-2.0 | ~20k | Development moved to Codeberg (GitHub is a mirror); downloading may breach a site's terms or copyright |
| `localsend/localsend` | Open-source AirDrop alternative on the local network | Apache-2.0 | ~93.5k | None found |
| `dani-garcia/vaultwarden` | Bitwarden-compatible server in Rust | AGPL-3.0 | ~68.6k | Unofficial, not affiliated with Bitwarden Inc. Card says "premium features unlocked": that is the project's behaviour; check Bitwarden's terms before using it commercially. You own backups and security patching |
| `ArchiveBox/ArchiveBox` | Self-hosted web archiving | MIT | not shown | Archiving third-party content is your legal risk |
| `LibreTranslate/LibreTranslate` | Offline translation API | AGPL-3.0 | ~17k | Self-hosting needs no key; the hosted instance's key rules are unverified |
| `imputnet/cobalt` (card prints "inputnet") | Media downloader, no ads | AGPL-3.0 | ~44.7k | Downloads from TikTok, Instagram, X, YouTube may breach their terms; project disclaims liability |
| `Suwayomi/Suwayomi-Server` | Self-hosted Tachiyomi/Mihon manga server | MPL-2.0 (parts Apache-2.0) | ~7.8k | Content sources are unaffiliated and may infringe copyright. Not recommended for a business machine |

## B. Cloud-bill seven (@joshualevi.ai)
| Repo | Replaces | Licence | Stars | Notes |
|---|---|---|---|---|
| `coollabsio/coolify` | Heroku, Netlify, Vercel | Apache-2.0 | ~62.7k | curl-pipe installer (read it first); paid cloud option |
| `ubicloud/ubicloud` | AWS-style compute, storage, Postgres, K8s | AGPL-3.0 | ~12.3k | Paid managed service exists |
| `seaweedfs/seaweedfs` | S3 object storage | Apache-2.0 | ~35.3k | Paid Enterprise Edition exists |
| `SigNoz/signoz` | Datadog-style logs, metrics, traces | MIT core | ~32.3k | `ee/` directories carry a separate licence |
| `typesense/typesense` | Algolia, Pinecone | GPL-3.0 | ~26.6k | Paid cloud option |
| `imgproxy/imgproxy` | Per-image thumbnail services | Apache-2.0 | ~11.1k | Pro tier is paid |
| `triggerdotdev/trigger.dev` | Lambda-style job limits | Apache-2.0 | ~16.5k | Cloud or self-host |
Self-hosting moves cost from the invoice to your time, patching and backups; compare before moving a line item.

## C. replace.so six of eight
| Repo | What it is | Licence | Stars | Notes |
|---|---|---|---|---|
| `langwatch/langwatch` | LLM and agent observability, evals | Apache-2.0 (SDKs MIT) | ~4.9k | `platform/app/ee/` needs a commercial licence in production |
| `dagucloud/dagu` | YAML workflow orchestrator | GPL-3.0 | ~4.3k | Paid licence adds SSO, RBAC, audit; installer is curl-pipe |
| `fleetbase/fleetbase` | Logistics operating system | AGPL-3.0 + commercial | ~4.2k | Paid tiers |
| `pullfrog/pullfrog` | Bring-your-own-key AI agent in GitHub Actions | MIT | ~1.3k | `npx pullfrog init`; needs your own LLM key; Pro paid; it comments and edits on PRs, review its permissions |
| `stablyai/orca` | Parallel coding agents in worktrees | MIT | ~86.4k* | Uses your own agent subscriptions |
| `multica-ai/multica` | Workspace for assigning work to AI agents | Apache-2.0 + custom conditions | ~52.1k* | Conditions cover hosted services and commercial embedding; curl-pipe install |
The other two repos of the carousel were not in the upload.

## D. GitHub-trending cards (@githubnow, 6 Oct 2026)
| Repo | What it is | Licence | Stars | Notes |
|---|---|---|---|---|
| `cathrynlavery/diagram-design` | 42 editorial diagram types as HTML + SVG, installable as a skill | MIT | ~43.9k* | `/plugin marketplace add` or `npx skills add`; third-party skill, read it first. Relevant to our design templates |
| `agent-substrate/substrate` | Kubernetes runtime that multiplexes stateful agents | Apache-2.0 | ~4.4k | Needs a cluster; operator tool |
| `mvschwarz/openrig` | YAML-defined agent teams over Claude Code, Codex, Pi | Apache-2.0 | ~5.5k | `npm i -g @openrig/cli`; needs your own agent subscriptions |

## E. Lists and tools
| Item | Notes |
|---|---|
| `ComposioHQ/awesome-claude-skills` (Apache-2.0, ~76.6k) | The list in the screenshot (File Organizer, Invoice Organizer, Skill Seekers, MCP Builder...). It links third-party skills; none was installed |
| `herdrdev/herdr` (Apache-2.0, ~42.6k) | Terminal multiplexer for coding agents; matches local skill `herdr`. Ignore the 0-star fork `maxjendrall/herdr` |
| `deepseek-ai/deepseek-harness` (MIT, developer preview, 244k stars*) | Name match for the "DeepSeek harness" slide; the carousel gave no URL, so confirm |
| Claudex Loop, Looper | No matching repo confirmed; local skills `claudex-loop`, `looper` exist |
| SERPtag, AnswerThePublic, Search Console, PageSpeed Insights, AlsoAsked | SEO tools from the @entrp0 carousel; products, not repos. Search Console and PageSpeed are free; the others have free tiers with limits |

## Rules
Licence first (AGPL and GPL bind you if you embed or offer them as a service), then the account or key it needs, then the terms of any site it downloads from. Prefer reading to installing; no `curl | sh` without reading the script.

## Keywords
open source, self-hosted, GitHub repos, AGPL, Coolify, SigNoz, Vaultwarden, cobalt, diagram-design, OpenRig
