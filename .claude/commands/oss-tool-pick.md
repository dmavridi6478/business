---
description: Pick a free open-source tool for a job from the 15 in the three November carousels (video editing, disk space, uninstalling, passwords, SQLite, images, shell, terminal output, media playback, private search) - plans only, installs nothing
argument-hint: [the job, e.g. "see what fills my disk" or "edit a short video"]
---

Input: "$ARGUMENTS". If empty, ask what job and which operating system.

Use `.claude/skills/oss-finds-three-carousels-nov2026/SKILL.md`.

1. Match the job to one or two tools from the skill's tables. Check the platform first (WinDirStat and BCUninstaller are Windows only).
2. Give the licence as read in the skill and the one caution the slide omits (for example Oh My Zsh's piped installer, BCUninstaller's "looking for maintainers" note, ImageMagick on untrusted files).
3. Give the install route as the README states it. For piped installers, tell the user to download and read the script first.
4. For tools that delete or modify files (WinDirStat, BCUninstaller, DB Browser for SQLite) say to back up or make a restore point first.
5. If the job is not covered, point to `/repo-vet owner/repo` and `oss-alternatives`; do not invent a tool.

Install, clone and run nothing. End with `Not verified:` for star counts and any slide claim not read from a README.
