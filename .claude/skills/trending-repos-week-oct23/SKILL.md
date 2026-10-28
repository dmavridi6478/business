---
name: trending-repos-week-oct23
description: Five fast-growing GitHub repos from the week of 23 October 2026 (cleanyourtv, Filee, ai-job-search, MacNativeGames, ruflo) with figures read from GitHub, licences, what each can touch, and a safe-trial protocol for any trending repo. Use before installing a repo you saw in a "went wild this week" post.
---

# Five repos that "went wild" (week of 23 October 2026)

Source: a 13-slide carousel by @buildwithneej. Numbers on the slides were a snapshot; the figures below were read from each GitHub page on 28 October 2026. Several repos gained thousands of stars in days, so check again before you quote them.

| # | Repo | What it does | Stars now (slide) | Licence | What it can touch | Care |
|---|---|---|---|---|---|---|
| 1 | `Gathin23/cleanyourtv` | A coding agent debloats an Android or Google TV over Wi-Fi (ADB) and installs a clean launcher | 41,347 (27,491) | "Other": read it | Your TV's installed apps, settings, launcher | An AI agent holds ADB control of a device. Read the prompt file before pasting it, and keep the restore script. Android TV and Google TV only; Fire TV gets the cleanup only; Samsung, LG and Roku are not supported. The repo says other domains using the name are not the project |
| 2 | `KnifeLemon/Filee` | Drag a file, a ring of formats opens at the cursor; offline conversion, 263 to 267 formats | 14,711 (10,947) | MIT | Files you drag in | Created 29 September 2026: young. Slide says 255 formats; the repo now says 263 and 267 in different places. Word and PowerPoint to PDF without Office is the claim to test on a copy. The slide says the Mac build is a preview |
| 3 | `ai-job-search-dev/ai-job-search` | Job search framework on Claude Code: evaluate postings, tailor CVs, cover letters, interview prep; a second agent reviews drafts | 66,618 (64,035) | MIT | Your CV and profile files | Personal data: keep the fork private. It states it has no affiliated token or paid programme; treat any claim otherwise as a scam. The slide's test shows it removing a hidden "ignore previous instructions" line from a posting: job posts are untrusted input |
| 4 | `ly05010419/MacNativeGames` | Runs your own dumped copy of two Zelda games natively on Apple silicon | 5,393 (4,843) | MIT | Game files and console keys you supply | Legal: you must own the game, and dumping keys and files is your responsibility and may breach law or terms in your country. The repo ships no game. Needs an Apple silicon Mac; first play stutters while shaders compile. 149 open issues |
| 5 | `ruvnet/ruflo` | Agent teams, shared memory and a live console on top of Claude Code and Codex | 79,407 (78,730) | MIT | Your Claude Code settings, memory, tool use | Setup changes Claude Code settings: try in a spare project. 988 open issues, a very large surface (16 languages) and 8,500+ commits by one author; read what a plugin does before you grant it tools. The "4 ms memory recall" figure is the author's own test |

The slide's "which ones I would use" column is one person's opinion (cleanyourtv and Filee first; ai-job-search if you are job hunting; MacNativeGames if you own the game; ruflo if you run agents). Use the safe-trial protocol rather than the order.

## Safe-trial protocol for any trending repo

1. **Age and stars.** Created date, stars gained this week, number of contributors. Under 30 days old: treat as a prototype.
2. **Licence.** MIT, Apache-2.0 and BSD are permissive; GPL and AGPL carry obligations; "Other" means read the file.
3. **Read the install path.** Never pipe a download into a shell. Read any `PROMPT.md`, `setup` command or plugin manifest end to end.
4. **Permissions.** List what it can read, write, send, delete or execute. Anything touching a device, credentials, mail or money needs a sandbox first.
5. **Sandbox.** Spare project, throwaway account, virtual machine or a second device. Back up before the first run.
6. **Rollback.** Know the undo (cleanyourtv's restore script; `claude plugin uninstall` for plugins) before you start.
7. **Scam signals.** Tokens, "airdrops", look-alike domains and DMs offering "the full article" for a comment keyword. The carousel's "comment REPO" is an engagement hook; the repos are public, so you do not need a DM.
8. **Stale numbers.** Do not repeat a star count or a speed claim from a slide; re-read the page.

Run with `/trial-repo <owner/repo>`. Related: `oss-alternatives`, `claude-install-list-40`, `repo-scan`, `repo-licence-check` (command), `claude-code-tooling`, `npm-supply-chain-security`, `prompt-injection-defense`.
