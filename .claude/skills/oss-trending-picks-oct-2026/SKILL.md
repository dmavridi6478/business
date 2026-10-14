---
name: oss-trending-picks-oct-2026
description: Sixteen open-source repos from the @githubnow and @githubvault carousels of 12 October 2026 (Open WebUI, BitNet, free-claude-code, AI Engineering from Scratch, WeKnora, diagram-design, SkillSpector, Spotube, MeTube, Stirling-PDF, Spacedrive, Translumo, Glance, JumpServer, CryptPad, GeminiWatermarkTool, GitHub Store) with each repo's real licence, what it needs to run, the slide claim that was and was not confirmed, and a use / skip / careful verdict. Use when the user asks which of these to install, what a licence allows, how to self-host one, or whether a trending repo is safe for business use.
---

# Open-source picks, 12 October 2026 - verified

Sources: @githubnow "GitHub Trending" slides (open-webui, BitNet, ai-engineering-from-scratch, WeKnora, free-claude-code, diagram-design) and @githubvault slides (Spotube, MeTube, Stirling-PDF, Spacedrive, Translumo, Glance, JumpServer, CryptPad, GeminiWatermarkTool, GitHub Store). Each repo's README and LICENSE file were read on 12 October 2026. Star counts and "stars today" figures on the slides were **not** re-checked.

## Licence and risk table

| Repo | Licence (from the repo's LICENSE) | What it is | Slide claim check | Verdict |
|---|---|---|---|---|
| open-webui/open-webui | **Open WebUI License** (BSD-style, plus a clause forbidding removal of Open WebUI branding unless <=50 end users in 12 months or a licence is bought) - not OSI open source | Self-hosted chat UI for Ollama and OpenAI-compatible APIs | Description matches; the slide does not mention the branding clause | **Use, with care** for internal use under 50 users; read clause 4 before any client deployment |
| microsoft/BitNet | MIT | bitnet.cpp, inference for 1-bit LLMs on CPU and GPU | Matches: 1.37x-5.07x on ARM, 2.37x-6.17x on x86, up to 82.2% less energy on x86, 100B model at 5-7 tokens/s on one CPU (vendor figures, not measured here). Slide says "lossless", README text read says "lossless" for inference of its own models | **Use** to experiment; models are limited to those released for the format |
| Alishahryar1/free-claude-code | **AGPL-3.0** | Local proxy so coding agents can use 60+ providers | README: 61 providers, 11 agents, fallback. "Not affiliated with Anthropic". Install shown is a **piped script** (`curl ... | sh`) | **Careful.** Read `scripts/install.sh` first, scan it, run in a container. A proxy sees every prompt and file your agent sends, so a bad one is a data leak. AGPL applies if you offer it as a service |
| rohitg00/ai-engineering-from-scratch | MIT | Curriculum with labs | "528 lessons across 20 phases" could **not** be confirmed in the README text read | **Use** for self-study; treat the lesson count as unverified |
| Tencent/WeKnora | MIT with third-party exceptions (listed in its LICENSE) | Documents to RAG, agent and wiki | README matches: hybrid search, Docker/E2B/Cube sandboxes, swappable models. Sandboxed skills and a browser extension that drives your own Chrome are powerful: scope them | **Use** in a private deployment after reading the exception list |
| cathrynlavery/diagram-design | MIT | Agent skill that writes diagrams as one HTML file | **Matches**: "44 diagram types" in the README | **Use**; also see the `artifact-diagramming` skill |
| NVIDIA/SkillSpector | Apache-2.0 | Security scanner for agent skills | See `skillspector-preinstall-scan` | **Use** before every skill install |
| KRTirtho/spotube | BSD-4-Clause (advertising clause) | Music player that takes metadata from Spotify and audio from YouTube and others via plugins | Matches. It plays audio sourced from YouTube, which may breach YouTube's terms and rights holders' rights | **Skip for business.** Personal use is your own legal risk |
| alexta69/metube | AGPL-3.0 | Web UI for yt-dlp downloads | Matches (Docker `docker run -d -p 8081:8081 ...`) | **Careful.** Download only what you own or have permission for |
| Stirling-Tools/Stirling-PDF | MIT for the open parts; README calls it **open-core** | Self-hosted PDF tools | Matches; some features sit in paid tiers | **Use** for private PDFs; repo already has `repo-stirling-pdf` |
| spacedriveapp/spacedrive | Apache-2.0 | Cross-platform file manager (Rust), p2p sync | Matches the slide; the slide's mock UI shows Gmail and Chrome sources, which are product concepts - check what the release build actually supports | **Try** on a test folder |
| ramjke/Translumo | Apache-2.0 | Windows real-time screen translator (OCR then translate) | Matches; Windows only | **Use** on Windows if needed; text on screen goes to the translator you pick |
| glanceapp/glance | AGPL-3.0 | Self-hosted feed dashboard | Matches | **Use** for a private dashboard; AGPL only matters if you serve it to others |
| jumpserver/jumpserver | GPL-3.0 | Open-source PAM / bastion host | Matches | **Use** only if you run servers for a team; it is security infrastructure, not a toy |
| xwiki-labs/cryptpad (slide: cryptpad/cryptpad) | AGPL-3.0 | End-to-end encrypted collaborative office | Slide's repo path returned 404 when raw files were fetched; the upstream is `xwiki-labs/cryptpad`. "Not even the admin can read the contents" holds only if you trust the code the server sends to your browser | **Use** for sensitive collaboration; self-host or use a trusted instance |
| allenk/GeminiWatermarkTool | MIT | Removes the **visible** Gemini watermark by reverse alpha blending | Matches; the README states it does **not** remove SynthID (the invisible mark) | **Do not use to pass off AI images as human-made.** Fine for your own images where the label is not needed |
| OpenHub-Store/GitHub-Store | Apache-2.0 | Installs open-source apps from GitHub releases | Matches | **Careful.** It installs binaries from releases: scan, check the publisher |

## Order to try (business-useful first)

1. SkillSpector (safety gate), diagram-design, Stirling-PDF.
2. Open WebUI + a local model (BitNet only if you have the hardware and want to experiment).
3. WeKnora for a private knowledge base.
4. Glance, CryptPad, Translumo as needed.
5. Last: free-claude-code (proxy risk), JumpServer (only if you manage servers).

## Rules

- Self-host only what you can update and back up. A server you forget is a risk.
- AGPL and GPL: check the obligations before offering the software to clients.
- Do not run installers copied from a README without reading them; scan the repo first.
- The install helper is `scripts/batch110-install.sh`. It asks before every step and installs nothing on its own.

## Command

`/oss-pick-oct <your need>` returns the one or two repos that fit, the licence consequence and the first command.
