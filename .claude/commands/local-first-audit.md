---
description: Audit which of your files live only in a cloud account, and pick the first one to move to a local open-source tool, with the backup it needs
argument-hint: [where your demo videos, notes, credentials and artwork live today]
---

Use the skill `local-first-app-stack`. Input: "$ARGUMENTS".

1. Read `.claude/skills/local-first-app-stack/SKILL.md`.
2. For demo videos, notes, credentials and artwork, mark each: only in a cloud account / local and backed up / local and not backed up. Ask at most 3 yes/no questions if the input is thin.
3. Recommend the single first move (default: credentials to KeePassXC) and name the backup that must exist before moving it. Remind the user that sync is not backup.
4. Never ask the user to paste passwords, keys or private files, and never read credential files.
