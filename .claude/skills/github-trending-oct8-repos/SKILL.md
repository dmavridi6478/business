---
name: github-trending-oct8-repos
description: Repos from @githubnow (8 Oct 2026 briefings), @replace.so and a @GithubSignals video, with the slide numbers and what to do with each - affaan-m/ECC (agent harness), trycua/cua (computer-use agents), DietrichGebert/ponytail (lazy code generator), liquidslr/system-design-notes, storytold/artcraft (AI creative IDE), Tencent/WeKnora (document RAG and agents), leepokai/codync (coding agents as teammates), macshot, Openscreen, Frappe Builder, Figranium, Openwhispr. Use when scouting open-source tools or deciding what to clone.
---

# Seen on the slides (stars are the slides' own numbers, unverified)
| Repo | Claim on the slide | Notes / existing coverage |
|---|---|---|
| affaan-m/ECC | Agent Harness OS, +1,139 stars today; skills, memory, security; Claude Code, Cursor, Codex, Opencode; npm `ecc-universal`, `ecc-agentshield` | repo already has `ecc-guide`, `configure-ecc`, `ecc-recipes` |
| trycua/cua | open-source computer-use infra, +383 stars; Driver (inspect/operate native apps via screenshots+actions), Spaces (full desktops), Bench (evaluation); macOS/Windows/Linux | new; run in a sandbox VM, never on your daily desktop with logged-in accounts |
| DietrichGebert/ponytail | Ponytail 5: -53% code, -41% time, -26% cost, -45% tokens; 98% of risky logic ships with a test (68% without); 5,700+ Claude Code sessions, Opus 5.5, 39 tasks (the author's benchmark) | repo already has `ponytail`, `ponytail-audit`, `-debt`, `-gain`, `-help`, `-review` |
| liquidslr/system-design-notes | +910 stars; 28 chapters (problem -> high-level -> deep dives -> trade-offs); Discord, Uber, Google, AWS, Netflix | already listed in `dev-repos-to-clone`; "README runs in ten minutes" is the slide's claim |
| storytold/artcraft | AI Creative IDE in Rust, +1,465 stars; 2D/3D scene staging, character posing, image-to-3D, per-project models | new; creative tooling, needs model/API keys |
| Tencent/WeKnora | +815 stars this week; RAG + agentic reasoning + wiki; 10+ document formats; sync Confluence/Feishu/GitLab/Notion; skills run in Docker or E2B | new; relevant to `rag-pipeline-architecture` |
| leepokai/codync | "open-source Grok Bot alternative": coding agents (Claude Code, Codex, Cursor, Pi, OpenCode, Grok Build, Gemini, Copilot) as teammates you message; Apache-2.0; macOS/Windows/Linux + iOS app (@GithubSignals video, AI-generated, ~181 stars) | new; low star count, vet before use |
| sw33tLie/macshot | macOS screenshot/recording, OCR, redaction, scroll capture, MP4/GIF (3,419 stars) | macOS only |
| getopenscreen/openscreen | screen recorder + editor, cursor effects, local AI (2,846 stars) | in README already |
| frappe/builder | low-code visual website builder (2,351 stars) | in README already |
| figranium/figranium | self-hosted visual browser automation, API-triggered scraping (725 stars) | see `replace-so-agent-repos` |
| OpenWhispr/openwhispr | voice-to-text, local or cloud (8,147 stars) | skill `openwhispr` exists |
Rule: clone and read the README and licence first (`scripts/batch112-install.sh` offers shallow clones, asks per repo). Do not run install scripts or give an agent your real desktop without reading them.
