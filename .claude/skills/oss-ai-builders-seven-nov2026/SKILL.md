---
name: oss-ai-builders-seven-nov2026
description: Checked register of the seven-card "AI for builders" carousel (@martiendejong_dev, cover "7 GitHub repos that should honestly cost money") - VoiceStudio, HyperFrames, Hallmark, colibri, claude-mem, Paperclip, gstack - with what is new (VoiceStudio, colibri), what is already registered, licences read from the repos, hardware and consent cautions, and which claims were not verified. Use before installing any of them, when choosing a local voice tool or a local large-model runner, or when asked what is new versus already covered.
---

# "AI for builders" - seven repos (carousel read 15 November 2026)

Checked 15 November 2026: every repo exists (`git ls-remote`), licences read from the repo files, claims compared with the READMEs. Star counts, "trending +8.7k this week" and "Works with ... + 12 more" are as printed on the cards and were not checked (the GitHub API is blocked from the cloud container). The cover title "should honestly cost money" is a hook, not a finding.

| # | Project | Repo | Card says | Licence (read) | Status here |
|---|---|---|---|---|---|
| 01 | VoiceStudio | `debpalash/VoiceStudio` | Free ElevenLabs alternative on your laptop; clone voices, dub into 646 languages, dictate offline, books to audiobooks; 102.8k stars | AGPL-3.0 (`LICENSE`) | New |
| 02 | HyperFrames | `heygen-com/hyperframes` | Write HTML, render an MP4; 450 titles, transitions, charts; 80.2k stars | Apache-2.0 (card) | Already registered: skill `hyperframes` |
| 03 | Hallmark | `Nutlope/hallmark` | 50 themes, flags AI design tells in a real browser; 49.8k stars; made by Together AI | MIT (card) | Already registered: skill `hallmark` |
| 04 | colibri | `JustVugg/colibri` | Frontier open models on your own laptop, from 8 GB RAM, no GPU, streams from the SSD, OpenAI-compatible API; 48.5k stars | Apache-2.0 (`LICENSE`) | New |
| 05 | claude-mem | `thedotmack/claude-mem` | A second agent takes notes; every new session starts with what matters; 114.1k stars | Apache-2.0 (card) | Already registered |
| 06 | Paperclip | `paperclipai/paperclip` | Run a company of AI agents with an org chart and a budget; one line `npx paperclipai@latest onboard --yes`; 109.7k stars | MIT (card) | Already registered |
| 07 | gstack | `garrytan/gstack` | YC CEO's Claude Code setup; 23 tools; 140k stars | MIT (card) | Already registered: skill `gstack` |

## The two new ones

**VoiceStudio.** README: "Clone, design, dub, dictate, transcribe and narrate in 646 languages." Local engines run on Apple Silicon (Metal), Windows with NVIDIA CUDA, experimental AMD ROCm, or CPU. The README also sells a commercial licence for client work and a hosted API "coming soon", so "free" applies to the AGPL open-source build, not to the commercial tiers.
- Voice cloning needs the speaker's consent; the card's own footer says "Only clone voices you have permission to use." Do not clone a client, colleague or public figure without written permission, and label dubbed or synthetic audio where a platform or law requires it.
- AGPL-3.0: if you run a modified copy as a network service you must offer its source.
- The "646 languages" figure is the README's headline; quality per language was not tested.

**colibri.** A pure-C runner for very large mixture-of-experts models: it keeps the small active part in RAM and reads the experts from disk. README minimums: 8 GB RAM at the very least (16 GB or more is better), 22 GB free disk for the smallest model, and an internet connection for the download. Supported families listed include GLM-5.2, Kimi K3, DeepSeek V4 and Qwen3.6.
- The card's footer is the honest line: "The biggest models run slowly on a laptop." Disk use grows with the model, and speed depends on the SSD.
- It downloads very large model files and offers GPU builds; read the setup script before running it.
- Related earlier register: `oss-finds-regularbasis-nov2026` (the Kimi K3 in C claim).

## Cautions on the already-registered five

- Paperclip and gstack hand real permissions to coding agents (shell, git, deploys). Start in a throwaway repository, set the budget limits first, and keep approval on.
- claude-mem stores what happens in your sessions; check what it records before using it on client or confidential work.
- HyperFrames is a free engine; HeyGen sells an optional Pro tier (card footer).

## Not done

Nothing cloned, installed or run. Star counts, weekly gains, "23 tools", "450 titles", "12 more" integrations and the 646-language quality were not reproduced. Use `/free-app-pick`, `/repo-vet owner/repo` and `/repo-licence-check` before installing.
