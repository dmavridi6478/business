---
name: github-finds-oct-19
description: Verified notes on repos from the 19 Oct 2026 batch of GitHub finds - headroom (context compression for LLM calls), Kronos (financial K-line foundation model), os-taxonomy (open curriculum prerequisite graph, ODbL) from @githubnow; ShareX, ActivityWatch, Krokiet, HandBrake, FreeTube from @palidev21; Umami, public-apis, lobe-chat, Alacritty, Home Assistant, freeCodeCamp, Klipper, Jellyfin, OBS Studio, TheAlgorithms/Python from @sitetusk. Use when asked what a repo is, whether it is worth starring, or which licence applies. Run via /github-finds.
---

# GitHub finds - 19 Oct 2026 batch

## Verified on GitHub, 19 Oct 2026

| Repo | What it is | Stars | Licence | Note |
|---|---|---|---|---|
| `headroomlabs-ai/headroom` | Compresses tool outputs, logs, files and RAG chunks before they reach the LLM; library, proxy and MCP server; runs locally | 76,032 (card: +317 today) | Apache-2.0 | Claims "20% fewer tokens for coding agents, 60-95% for JSON"; the claim is the repo's own, test on your workload |
| `shiyu-coder/Kronos` | Foundation model pre-trained on candlestick (OHLCV) tokens from 45 exchanges; open weights 4.1M-102M params on Hugging Face; fine-tuning scripts | 41,309 (card: +355 today) | MIT | Research model; **not financial advice**; backtest is not a forecast |
| `withmarbleapp/os-taxonomy` | 1,590 micro-topics, 3,221 prerequisite edges, 8 subjects, aligned to NGSS, Common Core, UK NC | 5,444 (card: +427 today) | **ODbL v1.0** (data licence, share-alike) | Attribution and share-alike apply to derived databases; read before reuse |

Overlap: `ecc-tools-cost-audit` covers token-cost auditing; headroom is a candidate tool for it, not tested on a real run here.

## From @palidev21 (desktop apps; stats not verified)

| App | Job |
|---|---|
| ShareX (Windows) | Capture and record, annotate, OCR and QR, hotkey workflows; review upload destinations before sharing |
| ActivityWatch | App time tracking, AFK detection, browser insights, local dashboard (data stored locally) |
| Krokiet (czkawka family) | Find duplicate, similar, big and empty files; review results before deleting |
| HandBrake | Convert videos to MP4/MKV/WebM, device presets, queue, audio and subtitles |
| FreeTube | Subscriptions without a Google sign-in, playlists, mini player; independent client, not a Google product |

## From @sitetusk "5 GitHub projects" (descriptions only; stats not verified)

Umami (privacy-first web analytics, MIT per card badge, needs Node 18.18+ and PostgreSQL 12.14+), public-apis (curated list of public APIs), lobe-chat (multi-agent chat platform), Alacritty (GPU terminal), Home Assistant (local home automation), freeCodeCamp (curriculum), Klipper (3D-printer firmware), Jellyfin (media server, GPL-2.0 per badge), OBS Studio (recording and streaming, GPL-2.0-or-later per the README), TheAlgorithms/Python (educational algorithms; "may be less efficient than the standard library").

Rules: star counts change daily; re-check before quoting. Never install from a carousel: read the README and licence first (see `scripts/batch111-install.sh`).
