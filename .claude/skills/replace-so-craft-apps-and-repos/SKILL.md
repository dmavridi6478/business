---
name: replace-so-craft-apps-and-repos
description: Five @replace.so repo cards (Pdfcraft, Photocraft, Artcraft, Rea, VoiceStudio) with the slide star counts, the repos and licences found on 16 October 2026, why the star counts do not reproduce, and the cautions on REA reverse engineering and the VoiceStudio one-line installer.
---

# @replace.so "GitHub repos so good they shouldn't be free"

Source: a card set with cover "6 GitHub repos so good they shouldn't be free"; five repo cards were in the upload (the sixth was not). Each card shows a star count, a website screenshot and one sentence.

| Card | Slide stars | Repo found | Licence | What it is |
|---|---|---|---|---|
| Pdfcraft | 14,330 | storytold/pdfcraft | Apache-2.0 | Open-source PDF reader and editor in Rust: read, organise, combine, split, search, secure; "no account, no telemetry, no cloud" |
| Photocraft | 62,967 | storytold/photocraft | Apache-2.0 | Pure Rust open-source image editor: layers, masks, adjustments, type, vectors, brushes, filters, PSD files offline |
| Artcraft | 29,078 | storytold/artcraft | MIT or Apache-2.0 (dual, per its README) | Open-source IDE for interactive AI image and video creation with 2D and 3D scene tools |
| Rea | 266,353 | morluto/rea | MIT | "Find out how software works": a CLI and MCP server that lets a coding agent inspect an app, website or binary and return evidence |
| VoiceStudio | 68,646 | debpalash/VoiceStudio | AGPL-3.0 | Local voice cloning, voice design, dubbing, dictation, transcription and audiobooks in 646 languages (see `github-trending-oct-14-2026-week`) |

## The numbers do not reproduce
- Web searches on 16 October 2026 gave different snapshots: PhotoCraft about 27,900 stars; REA between roughly 145,000 and 234,477 depending on date and source. The slide figures are higher. Treat every star count here as unverified; stars measure hype, not quality or safety.
- Secondary write-ups note that the Craft apps are early software, not yet a replacement for professional tools, and raise questions about AI-generated code quality and security [Likely].

## Cautions
- **REA:** setup is `npx rea-agents@latest setup`, which edits your coding agent's configuration (it asks first). Native analysis also needs a decompiler such as Hopper, Ghidra or IDA. Reverse engineering software can breach its licence or local law; use it on software you own or are authorised to analyse.
- **VoiceStudio:** the card shows a PowerShell one-liner that downloads and runs a script with the execution policy bypassed. Read the script first, or install from a release. Clone a voice only with the speaker's written permission.
- **Craft apps:** download from the repo's releases and check the NOTICE file for third-party terms (Artcraft's README says some bundled material is not covered by its licence).

Not installed. The user-run script lists these for cloning and reading only.
