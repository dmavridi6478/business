---
name: own-your-apps-joshualevi-7
description: "7 apps you rent that you could own by tonight" (@joshualevi.ai) - open-source, self-hostable replacements with the slide numbers - Stirling-PDF, syncthing, AFFiNE, bruno, KeePassXC, DocuSeal, harper - plus a switching-cost checklist (backups, exports, who maintains it). Use when someone wants to replace a paid SaaS (PDF tools, file sync, Notion/Miro, Postman, password manager, DocuSign, Grammarly) with an open-source one. Star counts are the slides' own.
---

| # | Repo | Replaces | What it is (slide) | Stats on slide |
|---|---|---|---|---|
| 1 | Stirling-Tools/Stirling-PDF | online PDF tools | 50+ tools: edit, merge, split, sign, redact, OCR, convert; desktop or own server, the document never leaves | 94k stars, 321 contributors, 11k forks |
| 2 | syncthing/syncthing | Dropbox-style sync | continuous file sync between your own machines, no account, nothing in the middle | 89k stars, 358 contributors, 6k forks |
| 3 | toeverything/AFFiNE | Notion + Miro | docs, whiteboard, tables on one canvas; local-first; self-host the sync | 73k stars, 274 contributors, 5k forks |
| 4 | usebruno/bruno | Postman / Insomnia | API collections as plain files in a folder; Git does the collaboration; offline only, no cloud sync ever | 47k stars, 482 contributors, 3k forks |
| 5 | keepassxreboot/keepassxc | 1Password / Bitwarden / Proton Pass | one encrypted file you keep anywhere; browser integration, passkeys, TOTP; imports from the three | 29k stars, 459 contributors, 2k forks |
| 6 | docusealco/docuseal | DocuSign | 12 field types on a PDF, verifiable signature, 14 languages; open-source DocuSign alternative | 19k stars, 6 contributors shown, 2k forks |
| 7 | Automattic/harper | Grammarly | offline grammar checker in Rust; checks in milliseconds without sending text to a server | 16k stars, 151 contributors, 704 forks |
Slide framing: "seven things you currently rent by the month, and the repo that does the same job on hardware you already paid for."

# Before you switch (not on the slides)
1. Free is not zero cost: you own updates, backups and security patches; self-hosted signing (DocuSeal) and password vaults (KeePassXC) are high-stakes, so test with non-critical data first.
2. Export from the old tool first and keep it for one billing cycle.
3. Check the licence (AGPL and similar terms matter if you host it for others) and who maintains it; DocuSeal shows only 6 contributors.
4. Back up the encrypted vault and sync folders separately; syncthing is sync, not backup.
Related: `repo-stirling-pdf`, `oss-alternatives`, `open-source-swap-stack-8`, `self-host-swap` (command), `repo-licence-check` (command).
