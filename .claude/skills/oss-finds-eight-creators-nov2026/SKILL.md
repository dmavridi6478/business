---
name: oss-finds-eight-creators-nov2026
description: Checked register of the open-source projects in 60 carousel slides from eight creators (@inikolov.ai "anatomy" skill, @emmanuelnyatefe KOOEMMA "10 free apps", @capacityso "6 GitHub repos blowing up this week", @raphal3494 "6 Rust repos", @dotdevs "5 GitHub projects", plus @dagier_official and @vibe.worker) - what is new (anatomy, DeepTutor, OpenMausBot, Upscayl, Ventoy, Czkawka, Espanso, KDE Connect, RustDesk), what is already registered, licences read from each repo, install routes and the warnings the slides omit. Use before installing any of them, when choosing a free desktop app or repo for a job, or when asked what is new versus already covered.
---

# Open-source finds from eight creators (7 November 2026)

Checked 7 November 2026: every repo exists (`git ls-remote`), licences read from the repo's own file, platforms and install lines from the READMEs. Star counts and "this week" gains are as printed on slides and could not be checked (GitHub API blocked from the cloud container). The "Ã¢Ëœâ€¦" on @dotdevs slides is a star icon mis-encoded in the source.

## New to this repository

| Project | Repo | Licence (read) | Install route (README) | Caution the slide omits |
|---|---|---|---|---|
| anatomy (Claude skill that builds interactive isometric illustrations of machines) | `wheresryan22/anatomy` | MIT (`LICENSE`) | `npx skills add wheresryan22/anatomy -g` (add `-a claude-code`); then `/anatomy explain ...`. Node 20.10 or later; README says no API key and nothing to `npm install` | Slides say it is 30 days old with 25.6k stars (created 8 Oct 2026) - not checked. Its own limits slide: no charts, no people or exact maps, weak on ideas with no moving parts; a run took 7 minutes, the largest size 2 to 4 hours. `npx` fetches and installs files into your skills folder: read the skill first |
| DeepTutor (AI tutor: learning paths, quizzes, video lessons) | `HKUDS/DeepTutor` | Apache-2.0 | See README (Docker or Python 3.11+) | Needs model access you configure; README release notes show fast, breaking changes |
| OpenMausBot (team of AI bots; each is a real Claude, Codex or Grok CLI agent) | `milind-soni/OpenMausBot` | Apache-2.0 | Release installers (macOS, Windows, Ubuntu 24.04 beta) | Runs the `claude`, `codex` and `grok` CLIs on your machine under your login; it can act with those agents' permissions |
| Upscayl (AI image upscaler) | `upscayl/upscayl` | AGPL-3.0 | Releases page | AGPL: offer source if you run a modified copy as a service |
| Ventoy (many installers on one USB stick) | `ventoy/Ventoy` | GPL-3.0 (`COPYING`) | Releases page | Writes to the USB device: pick the right disk |
| Czkawka (duplicate and similar-file finder) | `qarmin/czkawka` | MIT (GTK GUI and CLI); GPL-3.0-only for Krokiet and Cedinia (README) | Releases page | It can delete files: review the list and keep a backup before removing |
| Espanso (text expander, type a short code get full text) | `espanso/espanso` | GPL-3.0 | Installers on espanso.org | Default branch is `dev`. A text expander sees what you type: do not expand passwords |
| KDE Connect (phone and computer working as one) | `KDE/kdeconnect-kde` | GPL-2.0 file in `LICENSES/` (KDE projects mix licences; check the file you use) | Per platform | Pairs devices over your network: pair only devices you own |
| RustDesk (open-source remote desktop) | `rustdesk/rustdesk` | AGPL-3.0 (`LICENCE`) | Releases; optional self-hosted server | Remote access is a high-value target: use a strong permanent password, and do not expose a self-hosted server without hardening |

## Already registered, not duplicated

Looked up in the repository and found in `dev-repos-to-clone`, `open-source-apps-penny-4`, `oss-tools-part3-checked`, `repo-stirling-pdf`, `github-trending-top10-oct5`, `self-hosted-docker-stack`, `designer-resource-directory`, `open-source-devtools-2026` and others:

- @capacityso: t3code (`pingdotgg/t3code`, MIT badge on the slide), claude-mem (`thedotmack/claude-mem`), superpowers (`obra/superpowers`), Karpathy skills (`multica-ai/andrej-karpathy-skills`). Slide figures: +14.6k, +8.8k, +7.5k, +5.8k, +5.6k, +3.8k stars this week; unchecked.
- @raphal3494: Zed, uv, Tauri, Polars, Goose (`block/goose`), RustDesk (new, above). Slide: "6 Rust repos"; the Zed licence and install caution are in `five-repos-agent-tools-nov2026`. Goose is shown as part of the Linux Foundation: unchecked.
- @dotdevs: AFFiNE (74,240), Traefik (65,475), Keila (2,260), Instatic (9,066), Automa (21,710), all 5 Nov snapshots; the carousel's own line is "Check current licenses and running costs". "I built Slothy" is a self-promotion app, not assessed.
- @emmanuelnyatefe KOOEMMA: Excalidraw (08), Penpot (09), Syncthing (05), Stirling PDF (10), HandBrake (07). The ten are Upscayl 01, Ventoy 02, Czkawka 03, Espanso 04, Syncthing 05, KDE Connect 06, HandBrake 07, Excalidraw 08, Penpot 09, Stirling PDF 10. "All 10 free, open source, work on Windows, Mac, Linux" is the slide's line: KDE Connect and Ventoy are not equal on every OS, so check each README.

## Not tools

@dagier_official (Recraft, Hedra, Lovable; "your first client could be one message away") and "5 Websites that 10x'd my website traffic" are covered in `freelance-and-traffic-sites-nov2026`. Capacity (app builder) and Omniscio (agent workspace) appear as promotions inside @capacityso and @vibe.worker slides and were not assessed.

## Licence flags

AGPL-3.0 (Upscayl, RustDesk): offer source if you run a modified copy as a network service. GPL (Ventoy, Espanso, KDE Connect, Czkawka's Krokiet): copyleft applies if you distribute changes.

## Not done

Nothing cloned, installed or run. Speed, star and file-count claims on slides were not reproduced as facts. Use `/free-app-pick [job]` to choose and `/repo-vet owner/repo` for anything else.
