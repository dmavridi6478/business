---
name: oss-finds-three-carousels-nov2026
description: Checked register of the 15 GitHub projects in three November 2026 carousels - @palidev21 "5 GitHub tools you'll wish you found sooner" (Shotcut, WinDirStat, BCUninstaller, KeePassXC, DB Browser for SQLite), @dotdevs "5 GitHub projects worth exploring" (Whitebophir, DeepDiagram, OpenFlowKit, Nanobot, Lorien; already registered, new star snapshot only) and @sitetusk "5 GitHub projects they don't want you to know about" (ImageMagick, Oh My Zsh, rich, mpv, SearXNG) - with each licence read from the repo, platform, install route and the warnings the slides omit. Use before installing any of them, when choosing a free tool for a job, or when asked what is new versus already covered.
---

# 15 open-source projects from three carousels

Checked 7 November 2026: every repo exists (`git ls-remote`), licences read from each repo's own file, platforms and install lines read from each README. Star counts are as printed on the slides and could not be checked (the GitHub API is blocked from the cloud container). The "â˜…" characters on the @dotdevs slides are a star icon mis-encoded in the source.

## @palidev21 - five desktop tools (cover, five cards, closing slide)

| Tool | Repo | Licence (read) | Platform | Install route (README) | Caution the slide omits |
|---|---|---|---|---|---|
| Shotcut (video editor) | `mltframework/shotcut` | GPL-3.0 (`COPYING`) | Windows, macOS, Linux (build badges) | Binaries at shotcut.org/download | The card's "edit in portrait" claim was not checked |
| WinDirStat (disk space) | `windirstat/windirstat` | GPL-3.0 (`LICENSE.md`) | Windows only | `winget install -e --id WinDirStat.WinDirStat`, or `scoop install extras/windirstat` | README says it can also open, move and delete files, run cleanup tools and recover deleted files, so treat it as more than a viewer; "inspect before removing" is the card's own advice |
| BCUninstaller (bulk uninstall) | `Klocman/Bulk-Crap-Uninstaller` (card URL `BCUninstaller/...` resolves) | Apache-2.0 (README and `Licence.txt`) | Windows only | Releases page | README opens with "Looking for maintainers". Bulk removal can break software you still need: make a restore point and read the leftover list first (my advice) |
| KeePassXC (password vault) | `keepassxreboot/keepassxc` | GPL-2.0 or GPL-3.0 | Windows, macOS, Linux | keepassxc.org/download | Already in `open-source-apps-penny-4` and `local-first-app-stack`. Back up the database and protect the master password |
| DB Browser for SQLite | `sqlitebrowser/sqlitebrowser` | Bi-licensed MPL-2.0 and GPL-3.0 or later | Windows, macOS, Linux | Releases per README | Edit a copy, not your only file; the card says back up before editing |

The cover and closing slide only list the five names; a "playlist" slide in the next carousel is a self-promotion screenshot.

## @dotdevs - five repos, already registered

All five are in `replace-so-agent-repos` (checked 4 October 2026). Licences were re-read on 7 November and are unchanged. New snapshot as printed on the slides (5 November), against the earlier slide values in that register:

| Repo | Licence | Stars now | Stars in register |
|---|---|---|---|
| `lovasoa/whitebophir` (shared whiteboard) | AGPL-3.0 | 2,679 | 2,645 |
| `LingyiChen-AI/DeepDiagram` (text to diagrams; needs an LLM key) | AGPL-3.0 | 992 | 923 |
| `openflowkit/openflowkit` (diagram studio with an MCP server; earlier register used `Vrun-design/openflowkit`, both URLs resolve) | MIT | 931 | 770 |
| `HKUDS/nanobot` (personal agent platform) | MIT | 49,854 | 48,288 |
| `mbrlabs/Lorien` (infinite canvas; quiet since 2025) | MIT | 6,875 | 6,796 |

The carousel also advertises "Springback", the creator's own iOS habit app. It is a promotion, not a tool, and was not assessed.

## @sitetusk - five repos, headline "they don't want you to know"

That framing is clickbait: all five are long-established, widely used projects.

| Tool | Repo | Licence (read) | Install route (README) | Notes |
|---|---|---|---|---|
| ImageMagick | `ImageMagick/ImageMagick` | ImageMagick License (its own permissive licence; read it before redistributing) | See imagemagick.org | Slide says "200+ formats"; the README only says a "wide range", so the number is unverified. Keep it updated and restrict it when it processes untrusted files (general security practice, not read from a source here) |
| Oh My Zsh | `ohmyzsh/ohmyzsh` | MIT | README's basic install is `sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`, a piped installer; the README itself recommends downloading and reading it first. It renames your existing `.zshrc` | Needs zsh, curl or wget, and git |
| rich | `Textualize/rich` | MIT | `python -m pip install rich` | README text says Python 3.8 or later; the slide badge shows 3.9 to 3.14, so the versions differ by date |
| mpv | `mpv-player/mpv` | GPLv2 or later by default; LGPLv2.1 or later with `-Dgpl=false` | See mpv.io/installation | Command-line player; no GUI as such |
| SearXNG | `searxng/searxng` | AGPL-3.0 | Installation guide at docs.searxng.org | Already in `oss-ai-alternatives` and `dev-repos-to-clone`. README: "Users are neither tracked nor profiled" describes the engine, not any public instance you pick |

## New to this repository

Shotcut, WinDirStat, BCUninstaller, DB Browser for SQLite, ImageMagick (named only inside other skills), Oh My Zsh, rich, mpv. Use `/oss-tool-pick [job]` to choose among them and `/repo-vet owner/repo` for any other.

## Licence flags

AGPL-3.0 (Whitebophir, DeepDiagram, SearXNG): offer source if you run a modified copy as a network service. GPL-2.0/3.0 (Shotcut, WinDirStat, KeePassXC, DB4S, mpv by default): fine to use; copyleft applies if you distribute changes or link them into your own software.

## Not done

Nothing was cloned, installed or run. No claim on a slide about speed, file counts or screenshots was reproduced.
