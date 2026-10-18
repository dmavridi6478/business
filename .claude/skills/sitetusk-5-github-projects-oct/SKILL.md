---
name: sitetusk-5-github-projects-oct
description: The @sitetusk "5 GitHub projects they do not want you to know about" slides (FFmpeg, audiobookshelf, Apache Superset, SiYuan, btop++) with what each does, licences read on 18 October 2026 (FFmpeg is LGPL with optional GPL parts), and practical catches. Use when picking self-hosted and media tools.
---

# Site Tusk, 5 GitHub projects (oct)

Source: five repo slides plus a "bookmark playlist" slide and a robot cover; the headline is clickbait, all five are well-known public projects. Licences read 18 October 2026.

| Repo | Slide says | Licence | Catch |
|---|---|---|---|
| FFmpeg/FFmpeg | Multimedia framework to record, convert and stream audio and video (libavcodec, ffmpeg, ffplay, ffprobe) | LGPL-2.1+ in the root file; some optional components and builds are GPL | Codec patents and build options matter for commercial use |
| advplyr/audiobookshelf | Self-hosted audiobook and podcast server with multi-user, progress sync, mobile apps (beta) | GPL-3.0 | The README warns frontend pull requests are paused while the Vue frontend moves to React |
| apache/superset | Open-source data visualisation and exploration platform for dashboards from almost any database | Apache-2.0 | Needs a database, auth and ops work; heavy for small teams |
| siyuan-note/siyuan | Self-hosted knowledge management with block-level references, Markdown WYSIWYG and AI agent collaboration | AGPL-3.0 | AGPL obligations if you modify and host it; paid sync and extras |
| aristocratos/btop | Terminal resource monitor showing CPU, memory, disk, network, processes | Apache-2.0 | Local tool; no catch beyond platform support |

Nothing was installed or followed. Related: `self-hosted-docker-stack`, `site-tusk-github-repos-5`, `dev-repos-to-clone`.
