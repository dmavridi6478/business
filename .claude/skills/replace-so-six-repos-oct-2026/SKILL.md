---
name: replace-so-six-repos-oct-2026
description: The @replace.so "6 GitHub repos so good they shouldn't be free" carousel (five of six repos present: Convex, LimeSurvey, Prismical, Coder, Harper) with the licence read from each repo, the Convex licence that is not open source despite the slide, what could not be verified about Prismical, and when each is worth using. Use when the user asks about any of these repos, wants an open-source survey tool, grammar checker, reactive database or cloud development environment.
---

# 6 GitHub repos "so good they shouldn't be free"

Source: @replace.so, 6 images (cover and five repo slides; the cover says six repos, so one slide is missing from the archive). Read 14 October 2026. Star counts on the slides (12,690; 3,761; 104; 16,987; 16,361) were not re-checked.

| Repo | What the slide says | Licence (read from the repo) | What to know |
|---|---|---|---|
| Convex (`get-convex/convex-backend`) | "Open-source reactive database for web apps" | **Functional Source License 1.1, Apache 2.0 Future License (FSL-1.1-Apache-2.0)**, copyright 2026 Convex, Inc. | Source-available with use restrictions, not an open-source licence, even though the README calls it open source. It converts to Apache 2.0 later. Read the licence's permitted-use and competing-use terms before building a product on it. Self-hosted builds contain a beacon (telemetry), per the README |
| LimeSurvey | Free, open-source survey platform with branching and multilingual support | GPL-2.0 or later | A hosted paid version also exists. Self-hosting survey data makes you the data controller: privacy notice, retention, access control |
| Prismical | Open-source AI note taker that transcribes meetings and voice notes | **Not verified** | The repo was not found. A directory listing says MIT, local Whisper and Parakeet transcription and about 14 stars, while the slide says 104. Treat the licence and star count as unconfirmed. Do not install before you have the real repo URL and have scanned it |
| Coder (`coder/coder`) | Self-hosted platform for Terraform-defined development environments and AI coding agents | AGPL-3.0 | The README also sells a Premium tier. AGPL applies if you modify it and offer it to others over a network. A platform team's tool, not a solo developer's |
| Harper (`Automattic/harper`) | Fast, privacy-focused English grammar checker that runs locally | Apache-2.0 | English only (README). Runs locally, so your text is not sent to a remote server |
| (sixth repo) | Not in the archive | Unknown | The cover shows five icons for six repos. Ask for the missing slide if you need it |

## When each is worth it

- **Harper:** yes, for anyone who writes English and objects to cloud grammar checkers.
- **LimeSurvey:** yes, if you must keep survey data on your own infrastructure. For a one-off survey, a hosted tool is less work.
- **Convex:** only after reading the licence. A good fit for a team that accepts FSL terms.
- **Coder:** only for a team that manages development environments in the cloud.
- **Prismical:** wait until its repo, licence and maintenance are confirmed.

## Rules

- "Free" and "open source" are different claims. The Convex slide is the clearest case in this archive.
- Nothing here was installed. Scan any repo you intend to install with `skillspector-preinstall-scan`.
