---
name: oss-seeds-ten-and-eighteen-nov2026
description: Checked register of two November 2026 sources - the "seeds" board of ten small new repos (LingBot-Touch, Relax, DataCat, Dalibre, Scarlet, GiroCrab, git twig, Lobe MyGo, tinytraffic, Muelle) and the @pallidev21 / @your.aimentor / @githubnow carousels (Upscayl, Stirling PDF, EarTrumpet, ActivityWatch, Bruno, kiri, phonebox, openmotion, Univer, claude-trading-skills, astryx, nginx, claude-mem) - with licences read from 19 repos, what is new, and cautions the cards omit (finance app, AI trading skills, public share links, phone-controlled permission prompts). Use before installing any of them.
---

# Two repo boards (read 23 November 2026)

Checked: 19 repos exist (`git ls-remote`) and licences were read from repo files. Star counts, "planted Nov N" dates and "+N this week" figures are the cards' and unchecked (GitHub API blocked). Nothing was cloned, installed or run. Already registered earlier: Upscayl, Stirling PDF, claude-mem, Astryx (see `oss-finds-eight-creators-nov2026`, `repo-stirling-pdf`, `github-now-top10-nov8`). Bruno, EarTrumpet and nginx were not licence-read here (Bruno MIT and nginx BSD-2-clause by my recollection, unverified).

## Seeds board (ten repos, "discover ... at bestproductivityresources.com", an affiliate-style site)

| # | Project | Repo | Card line | Licence (read) | Caution |
|---|---|---|---|---|---|
| 1 | LingBot-Touch | `Robbyant/lingbot-touch` | Open model files teaching robot hands to feel from touch sensors | Apache-2.0 | Research code; needs hardware and GPUs |
| 2 | Relax | `makepad/relax` | Run a Rust program straight from source, no build wait | MIT | Marked experimental |
| 3 | DataCat | `replit/datacat` | Watch your own servers: charts, logs, alerts, self-hosted | Apache-2.0 (default branch `develop`) | You operate it and secure it |
| 4 | Dalibre | `djyde/dalibre` | Desktop e-book library that reads and writes Calibre libraries | GPL-3.0 | Back up your library first |
| 5 | Scarlet | `Forward-Future/scarlet` | Open video editor driven by Claude Code or Codex | MIT | Agent edits files on your machine |
| 6 | GiroCrab | `GiroCrab/GiroCrab` | Mac/iPhone online banking, data encrypted on your device | GPL-3.0 | Handles bank credentials: unaudited new project, use only after independent review |
| 7 | git twig | `leostera/git-twig` | Cheap copies of a Git project so agents work side by side; "up to 97% less disk" | MIT | The 97% is the card's claim, unmeasured |
| 8 | Lobe MyGo | `lobehub/lobe-mygo` | Ready-made buttons and panels for native Go desktop apps | MIT | Library |
| 9 | tinytraffic | `egoist/tinytraffic` | Simple website stats, one file, visitor data on your server | AGPL-3.0 | Still needs consent and privacy notice where law requires |
| 10 | Muelle | `crafter-station/Muelle` | Windows taskbar swapped for a Mac-style dock | MIT | Replaces a system component: test first |

## Carousel set

| Project | Repo | Licence (read) | Note |
|---|---|---|---|
| ActivityWatch | `ActivityWatch/activitywatch` (master) | MPL-2.0 | Tracks windows and apps locally; card says optional Pro is separate |
| Univer | `dream-num/univer` (dev) | Apache-2.0 | Spreadsheet engine library, not an app; AI-agent edit API claim unverified |
| openmotion | `nexu-io/openmotion` | Apache-2.0 | Rebuilds a reference video as HTML via HyperFrames; mind copyright of the reference video |
| kiri | `libracoder/kiri` | Apache-2.0 | Docker Desktop alternative; `kiri share` makes a public HTTPS link to a container: anyone with the link reaches it, so never share anything with data or secrets |
| phonebox | `ersinkoc/phonebox` | MIT | Old Android phone as a control panel; the card says it can Allow/Deny Claude Code permissions from the phone: that is a security boundary, keep it on your own network |
| claude-trading-skills | `tradermonty/claude-trading-skills` | MIT | 74 skills for market analysis; not financial advice, the card's "decisions stay with you" is right; verify data sources |
| Bruno, EarTrumpet, nginx | `usebruno/bruno`, `File-New-Project/EarTrumpet`, `nginx/nginx` | not read | Bruno: API client keeping collections as files; EarTrumpet: per-app volume on Windows 10/11; nginx: web server |

## Not done

No installs, clones or runs; counts and dates unverified. Use `/repo-vet owner/repo` and `/repo-licence-check` first.

## Addendum, 24 November 2026: the same five repos in a @buildwithneej carousel (13 slides, "week of Nov 20")

The zip repeats five repos already above (Univer, phonebox, openmotion, claude-trading-skills, kiri) with install lines and the creator's own tests. Nothing new was built; these details were added to the existing entries. The 5 in 13 slides, the creator's picks ("trying Claude Trading Skills first") and the closing "comment REPO and I'll DM you my notes" gate are promotion; star gains (+2,909, +3,760, +5,314, +3,385, +5,277 this week) are unchecked.

| Repo | Install line shown | Claims by the creator | Caution |
|---|---|---|---|
| phonebox | `setup.sh` (Mac, Linux) or `setup.ps1` (Windows), open 127.0.0.1:8765, pick a template | Over 100 widgets, 30 templates, Android 5+, no account, no cloud; shows Claude and Codex usage limits; app comes from the GitHub releases page | Read the setup script before running it; sideloaded Android app with USB debugging; allowing or denying Claude Code permissions from a phone is a security boundary |
| kiri | `brew install --cask libracoder/kiri/kiri`, then `kiri share web` | Public HTTPS link runs through the maker's relay server and needs a GitHub sign-in; Mac and Linux; Apache-2.0, in beta | Traffic passes a third party's relay; beta software; share only a throwaway container |
| openmotion | `npx skills add nexu-io/openmotion --skill openmotion`, then ask your agent to set up the Studio | Free open source; image, video, music and voice models bill to your own accounts; needs Chrome and FFmpeg; "rendered a 20-second template in 31 seconds" | Model costs are yours; the 31 seconds is one unrepeated test on unknown hardware |
| Univer | `pnpm add @univerjs/presets @univerjs/preset-sheets-core`, `univerAPI.createWorkbook({})` | Apache-2.0 core handles editing and formulas; charts, XLSX and live collaboration are commercial add-ons; "one edit by code, total recalculated to 117,541.6" | Check which features you need are in the paid tier; the sum is one sample |
| claude-trading-skills | `cp -r skills/market-breadth-analyzer ~/.claude/skills/` | Several skills use free public data with no key; 22 need a Financial Modeling Prep key (free plan 250 calls a day); a market-breadth run scored 34.1/100 "Weakening" in 7 seconds | Educational only, not financial advice; the score is one run on data through 19 November; a keyed data vendor's terms apply |
