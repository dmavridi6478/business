---
name: free-tools-feel-illegal-5
description: The "5 tools that feel illegal to be free" carousel from @will.ai.m (Whisper, Upscayl, LocalSend, Immich, Stirling-PDF) with each tool's replaced product, repo, licence read on 15 October 2026 and the catch the slide omits (Whisper is command-line only, Immich is not a backup by itself, AGPL on two of the five).
---

# 5 tools that feel illegal to be free

Source: a 7-slide @will.ai.m carousel ("Premium software you would normally pay hundreds for. All free, and it all runs on your own machine."): cover, five tool slides, a follow slide. Stars and "last updated" on the slides are unverified; licences below were read from each repo's LICENSE file.

| Tool | Slide says | Replaces | Repo | Licence | Catch |
|---|---|---|---|---|---|
| Whisper | OpenAI's speech model turns any recording into accurate text on your own machine | Otter.ai | openai/whisper | MIT | The slide footnote admits "command line only, interface shown is illustrative". README: `pip install -U openai-whisper`, needs `ffmpeg`; models from tiny to turbo (about 6 GB VRAM for turbo). No meeting bot, no speaker labels, no live notes: not a like-for-like Otter replacement |
| Upscayl | AI enlarges and cleans up low-res images up to 16x on your own GPU | Topaz Gigapixel ($99 per the slide) | upscayl/upscayl | AGPL-3.0 | Needs a capable GPU; AI upscaling invents detail, so do not use it on evidence or documents where accuracy matters |
| LocalSend | Sends files between phone, laptop and any OS over your own wifi, works offline | AirDrop | localsend/localsend | Apache-2.0 | Both devices on the same network; guest or segmented wifi can block discovery |
| Immich | Auto-backs up every photo and video off your phone, with search and face recognition on your hardware | Google Photos | immich-app/immich | AGPL-3.0 | You run a server (Docker) and own the storage. Its README says to always follow a 3-2-1 backup plan: it is not a backup by itself. Face recognition handles biometric data about other people |
| Stirling-PDF | Merge, split, sign, edit and convert PDFs with 50+ tools on your own machine | Adobe Acrobat | Stirling-Tools/Stirling-PDF | MIT | Check which features are in the free build; the company also sells a hosted and enterprise product. Existing skill: `repo-stirling-pdf` |

## Notes
- **"Feels illegal" is a headline, not a risk.** All five are normal open-source projects; none needs a licence workaround.
- **AGPL (Upscayl, Immich)** is fine for personal use; if you modify and offer it to others over a network you must offer the source.
- **Hosting costs time:** Immich and Stirling-PDF server mode need updates, backups and security; Whisper, Upscayl and LocalSend are desktop apps with little upkeep.
- **Greek audio:** Whisper is multilingual, but accuracy on Greek varies by model size; test on your own recordings before trusting a transcript.
- Already covered elsewhere in the repo: LocalSend (`lean-software-stack`), Stirling-PDF (`repo-stirling-pdf`). Use `/self-host-swap` and `/repo-licence-check` before relying on any of them; see also `modelsignal-free-swaps-22`.
