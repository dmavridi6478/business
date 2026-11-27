---
description: Run the safe-trial protocol on a GitHub repo before installing it (age, licence, install path, permissions, sandbox, rollback, scam signals)
argument-hint: [owner/repo or GitHub URL]
---

Use the `trending-repos-week-oct23` skill and `repo-scan`.

Input: $ARGUMENTS

1. Read the repo page: created date, stars, forks, open issues, licence, contributors. Quote the numbers with today's date; do not use numbers from a post or screenshot.
2. Read the licence file and say in one line what it allows and what it requires.
3. Read the install instructions and any prompt file, setup script or plugin manifest end to end. List every command and what it does. Flag anything that pipes a download into a shell.
4. List what it can read, write, send, delete or execute, and what credentials or personal data it touches.
5. Look for scam signals: tokens, look-alike domains, unexplained paid programmes, and a README that asks for secrets.
6. Give a verdict: skip, read-only look, or sandbox trial. For a trial, give the sandbox, the backup to make first and the exact rollback.
7. Do not clone, install or run anything. Show the commands I would run and wait for me.
