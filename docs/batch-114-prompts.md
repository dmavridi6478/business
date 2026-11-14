# Batch 110 (files numbered 114) - prompts to copy and paste

The archive holds a carousel of five repo cards (@your.aimentor, with five detail slides) and one 48-second video of five security scanners (@cyberwithjohann). Neither contains a prompt, so nothing was converted from a prompt. The commands below are the new ways to use what was added; the prompts are ready to paste into Claude Code.

## Commands installed (type in Claude Code)

| Command | Use |
|---|---|
| `/scanner-pick [target]` | Pick Gitleaks, TruffleHog, Trivy, Semgrep or Prowler for a target; plans only, runs nothing |
| `/studio-plan [engine] [idea]` | Plan a game with a studio chain of command on the lightest process; writes `docs/game-plan-YYYY-MM-DD.md` |
| `/repo-vet owner/repo` | (existing) Vet any of the five repos before installing |

## Prompts (plain text)

**1. Choose scanners for a project**
```
/scanner-pick a git repository that I own, plus the container image built from it and the AWS account it runs in
```

**2. Review what a scanner sends and needs**
```
Using the security-scanners-five skill, list for each of Gitleaks, TruffleHog, Trivy, Semgrep and Prowler what it sends off the machine, what credentials it needs, and its licence. Mark anything you could not verify.
```

**3. Plan a small game**
```
/studio-plan godot a one-screen puzzle game where the player rotates tiles to connect pipes
```

**4. Decide between the five tools**
```
Using the five-repos-agent-tools-nov2026 skill, which of Claude Code Game Studios, Craft Anything, Scrapling, Zed and agent-desktop would help a two-person marketing agency in Athens, and which would be risky? Give the licence and the main warning for each.
```

**5. Check one repo before installing**
```
/repo-vet D4Vinci/Scrapling
```

**6. Scraping, the careful way**
```
I want to collect public prices from three competitor websites. Using the five-repos-agent-tools-nov2026 skill, tell me what to check first (terms, robots.txt, personal data), and compare Scrapling with the TinyFish connector that is already connected.
```
