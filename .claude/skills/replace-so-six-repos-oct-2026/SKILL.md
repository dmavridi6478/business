---
name: replace-so-six-repos-oct-2026
description: The @replace.so "6 GitHub repos so good they shouldn't be free" carousel (five of six repos present: Convex, LimeSurvey, Prismical, Coder, Harper) with the licence read from each repo, the Convex licence that is not open source despite the slide, the Prismical repo found and checked, and when each is worth using. Use when the user asks about any of these repos, wants an open-source survey tool, grammar checker, reactive database or cloud development environment.
---

# 6 GitHub repos "so good they shouldn't be free"

Source: @replace.so, 6 images (cover and five repo slides; the cover says six repos, so one slide is missing from the archive). Read 14 October 2026. Star counts on the slides (12,690; 3,761; 104; 16,987; 16,361) were not re-checked.

| Repo | What the slide says | Licence (read from the repo) | What to know |
|---|---|---|---|
| Convex (`get-convex/convex-backend`) | "Open-source reactive database for web apps" | **Functional Source License 1.1, Apache 2.0 Future License (FSL-1.1-Apache-2.0)**, copyright 2026 Convex, Inc. | Source-available with use restrictions, not an open-source licence, even though the README calls it open source. It converts to Apache 2.0 later. Read the licence's permitted-use and competing-use terms before building a product on it. Self-hosted builds contain a beacon (telemetry), per the README |
| LimeSurvey | Free, open-source survey platform with branching and multilingual support | GPL-2.0 or later | A hosted paid version also exists. Self-hosting survey data makes you the data controller: privacy notice, retention, access control |
| Prismical (`amicalhq/prismical`) | Open-source AI note taker that transcribes meetings and voice notes | MIT (LICENSE read; copyright 2025 Naomi Chopra, Haritabh Singh; third-party components and model weights are listed in its NOTICE file) | Found through a directory listing (the slide shows no URL), then checked against the repo: macOS (Apple silicon and Intel) and Windows desktop app; local transcription with whisper.cpp; bring your own model (OpenAI, Anthropic, OpenRouter, any OpenAI-compatible endpoint, or Ollama); an optional Prismical cloud for sync, sharing, calendar and speaker diarization. The README says it captures system audio with no bot joining the call: **recording other people needs their consent in many places, and meeting data is personal data**. The slide's 104 stars matches the directory page, which labels it "last 30 days", so the true total is unconfirmed |
| Coder (`coder/coder`) | Self-hosted platform for Terraform-defined development environments and AI coding agents | AGPL-3.0 | The README also sells a Premium tier. AGPL applies if you modify it and offer it to others over a network. A platform team's tool, not a solo developer's |
| Harper (`Automattic/harper`) | Fast, privacy-focused English grammar checker that runs locally | Apache-2.0 | English only (README). Runs locally, so your text is not sent to a remote server |
| (sixth repo) | Not in the archive | Unknown | The cover shows five icons for six repos. Ask for the missing slide if you need it |

## When each is worth it

- **Harper:** yes, for anyone who writes English and objects to cloud grammar checkers.
- **LimeSurvey:** yes, if you must keep survey data on your own infrastructure. For a one-off survey, a hosted tool is less work.
- **Convex:** only after reading the licence. A good fit for a team that accepts FSL terms.
- **Coder:** only for a team that manages development environments in the cloud.
- **Prismical:** reasonable to try on your own machine for your own notes, after a scan of the build you install. Do not record calls without telling the participants.

## Rules

- "Free" and "open source" are different claims. The Convex slide is the clearest case in this archive.
- Nothing here was installed. Scan any repo you intend to install with `skillspector-preinstall-scan`.
