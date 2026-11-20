---
description: Run the secret and dependency scanners on what an agent changed (gitleaks, osv-scanner, optional semgrep) and summarise with values masked
argument-hint: [path, default: the repo root]   (add "full" to scan the whole git history)
allowed-tools: Read, Grep, Glob, Bash(gitleaks:*), Bash(osv-scanner:*), Bash(semgrep:*), Bash(git status:*), Bash(git diff:*), Bash(git log:*), Bash(command -v:*)
---

Use the skill `agent-output-scanners` on "$ARGUMENTS" (default: the repo root). Never print a secret value: always pass `--redact` to gitleaks and mask anything you quote.

1. Check which tools exist with `command -v gitleaks osv-scanner semgrep`. If gitleaks or osv-scanner is missing, say how to install it from the skill (note the gitleaks module path gotcha) and continue with what is available. Do not install anything yourself.
2. **Secrets:** run `gitleaks detect --source <path> --redact --no-banner` (add `--no-git` for a plain directory; scan history only if the arguments include `full`). The repo has a reviewed `.gitleaksignore`; anything reported is NEW.
3. **Dependencies:** run `osv-scanner scan source -r <path>`. Group the result by lockfile and say whether the lockfile is first-party or inside a vendored `.claude/skills/*` folder.
4. **Code patterns (optional):** if semgrep is installed, run `semgrep scan --config auto <path>` only if the user asked for it (it can send metrics; add `--metrics=off`).
5. Report: findings by severity, which are new versus already-reviewed, and the one next action for each new finding. A leaked secret means rotate it first, then remove it from history.
6. Do not run trufflehog, snyk agent-scan or garak from here: they contact outside services. Tell the user when one of them would be the right next step.
