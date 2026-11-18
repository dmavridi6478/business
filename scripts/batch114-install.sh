#!/usr/bin/env bash
# Batch 114 (README Batch 110) - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: skills, commands, an agent, two templates and a theme were added to the repo; nothing was installed or run.
# Licences were read from each repo's own file on 7 November 2026.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Clone for reading (shallow; nothing is installed or run) =="
echo "   MIT: Donchitos/Claude-Code-Game-Studios, gitleaks/gitleaks"
echo "   Apache-2.0: vercel-labs/agent-desktop, aquasecurity/trivy, prowler-cloud/prowler, storytold/craft-anything (MIT OR Apache-2.0)"
echo "   BSD-3-Clause: D4Vinci/Scrapling   LGPL-2.1: semgrep/semgrep"
echo "   AGPL-3.0: trufflesecurity/trufflehog (running a modified copy as a network service requires offering its source)"
echo "   Zed (GPL-3.0-or-later) is skipped: the repository is very large. Use https://zed.dev/download or your package manager."
for r in D4Vinci/Scrapling vercel-labs/agent-desktop storytold/craft-anything gitleaks/gitleaks trufflesecurity/trufflehog semgrep/semgrep prowler-cloud/prowler aquasecurity/trivy; do
  ask "git clone $r into ~/src?" && clone "$r"
done

echo "== 2. Game studio template (clone it as its own project, not inside this repository) =="
if ask "git clone Donchitos/Claude-Code-Game-Studios into ~/my-game?"; then
  [ -d "$HOME/my-game" ] && echo "   ~/my-game exists; skipped" || git clone --depth 1 https://github.com/Donchitos/Claude-Code-Game-Studios.git "$HOME/my-game"
  echo "   Next: open Claude Code in ~/my-game and run /start (default process level: minimal)."
fi

echo "== 3. Scrapling in an isolated environment =="
if ask "create ~/venvs/scrapling and pip install 'scrapling[fetchers]'?"; then
  python3 -m venv "$HOME/venvs/scrapling" && "$HOME/venvs/scrapling/bin/pip" install "scrapling[fetchers]"
  echo "   Browser pages need 'scrapling install' (inside that venv). Check each site's terms and robots.txt first; the robots option is off unless you turn it on."
fi

echo "== 4. Read first, not automated =="
echo "   agent-desktop: 'npm install -g agent-desktop' gives an agent control of any app you grant. Keep banking, password-manager and admin windows out. Run 'agent-desktop status' first."
echo "   Scanners: scan only what you own. TruffleHog validation tests found secrets against the real service. Pin Trivy and its GitHub Actions to a verified release or full commit SHA (March 2026 compromise)."
echo "   Craft Anything is a reverse-engineering engine in alpha; recreating someone else's site, app or game can infringe copyright or terms. Clean room is a rule, not a sandbox."
echo "   Vet any repo first with the /repo-vet command in Claude Code. Plan scanning with /scanner-pick."
echo "Done. Restart Claude Code so the new commands appear."
