---
description: Pick which Claude Code add-ons or vibe-coding plugins to install for a job, without stacking overlaps
argument-hint: [what you are building]
---

Use the skills `claude-code-addons-top5` and `vibe-coding-plugin-layers-5`. Input: "$ARGUMENTS".

1. Read both skill files.
2. Say which one or two add-ons fit the job, which are already present in this repo, and which overlap.
3. Give the exact install command for each from the skill, flag any piped installer, and recommend `/skill-scan` before installing anything not already vendored.
4. Do not install anything.
