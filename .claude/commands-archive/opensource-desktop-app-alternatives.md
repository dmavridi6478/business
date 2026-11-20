# Open-Source Alternatives to Paid Desktop Software

Source: @epic8244 (TikTok), "I deleted all Paid Softwares for these
opensource alternatives." Five apps, all confirmed live on GitHub.

None of these overlap the repos already listed in this repo's
`self-hosted-docker-stack` skill or the "Open-Source App Alternatives"
entry (Batch 74) — those cover photo backup, team chat, analytics, and
release pipelines; these five are desktop creative/productivity tools.

| # | App | Alternative to | What it does | Repo |
|---|---|---|---|---|
| 1 | **OpenCut** | CapCut, Adobe Premiere Pro, DaVinci Resolve, Filmora, Final Cut Pro | Browser-based, open-source video editor. No installs, no account, any platform. | [`OpenCut-app/OpenCut`](https://github.com/OpenCut-app/OpenCut) |
| 2 | **AnythingLLM** | Claude, ChatGPT, Grok, Perplexity, Gemini, and other chat UIs | Desktop app + self-hostable platform: chat with your documents, run AI agents, work with LLMs entirely on your own machine. No account required. | [`Mintplex-Labs/anything-llm`](https://github.com/Mintplex-Labs/anything-llm) |
| 3 | **Nuclear** | Spotify, YouTube Music, SoundCloud, Apple Music, Deezer, Tidal | Desktop music player that pulls audio from multiple online sources. No ads, no tracking, no subscription; fully auditable source. | [`nukeop/nuclear`](https://github.com/nukeop/nuclear) |
| 4 | **Cap** | Loom, Screen Studio, CleanShot, Bandicam, ScreenFlow, Kite, Shotbase, Camtasia | Cross-platform screen recorder (macOS/Windows/Linux) covering instant/studio/screenshot modes in one app. | [`CapSoftware/Cap`](https://github.com/CapSoftware/Cap) — already referenced in this repo's `self-hosted-docker-stack` skill (Batch 79) |
| 5 | **Handy** | Wispr Flow, Superwhisper, Typeless, Aqua Voice, Willow, Voibe, Monologue, AudioPen | Desktop speech-to-text: press a shortcut, speak, release, text appears in any field. No cloud, no subscription, no copy-paste step. | [`cjpais/Handy`](https://github.com/cjpais/Handy) |

## Clone all (run on your own machine — these are desktop apps, not services to run in this sandbox)

```bash
mkdir -p ~/repos/oss-desktop-alternatives && cd ~/repos/oss-desktop-alternatives
git clone --depth=1 https://github.com/OpenCut-app/OpenCut
git clone --depth=1 https://github.com/Mintplex-Labs/anything-llm
git clone --depth=1 https://github.com/nukeop/nuclear
git clone --depth=1 https://github.com/CapSoftware/Cap
git clone --depth=1 https://github.com/cjpais/Handy
```

Each is a desktop or local-first application — follow its own README for
build/install (`AnythingLLM` also ships prebuilt desktop installers; `Cap`
and `Handy` are Tauri/Rust apps that need a local toolchain to build from
source). None of these run meaningfully inside a headless Claude Code
container — install them on your own laptop.
