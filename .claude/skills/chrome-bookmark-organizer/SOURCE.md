# Source

- Repo: https://github.com/ye4wzp/chrome-bookmark-organizer (`skill/` directory, plus `docs/chrome-sync.md`)
- Commit: 4ec3c044a36305e3357891f7c40ddec9f4a84e50
- License: MIT (see LICENSE.txt)
- Reviewed: scripts are local-only (no network calls, no subprocess or eval). They read and rewrite a Chromium `Bookmarks` JSON file.
- Not installed: the planned Chrome extension (`extension/`), which is a README only.
- Limitation: needs a local Chrome profile, so it does not work in the cloud sandbox. Use it on the owner's own machine, with Chrome closed and Chrome Sync switched off first (see `docs/chrome-sync.md`).
