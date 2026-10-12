#!/usr/bin/env bash
# Batch 113 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing pipes a download into a shell.
# Done in the cloud session: 7 skills + 2 updated, 4 commands, 1 agent, 3 design templates, prompts. No plugin or connector was added.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Self-hostable replacements (shallow clones; read README and LICENSE before running anything) =="
for r in Stirling-Tools/Stirling-PDF syncthing/syncthing toeverything/AFFiNE usebruno/bruno keepassxreboot/keepassxc docusealco/docuseal Automattic/harper edenfunf/reelmimic; do
  ask "git clone $r into ~/src?" && clone "$r"
done
echo "   Prefer each project's official release/installer over building from a clone. Test password-vault and signing tools with non-critical data first."

echo "== 2. Glasser connector (paid, pay-per-call, vendor unverified) =="
if ask "show the connector command for Glasser (does not run it)?"; then
  echo "   Read the vendor's terms and privacy page, set a small balance cap, then:"
  echo "   claude mcp add --transport http Glasser https://api.glasser.ai/mcp   # then /mcp -> Glasser -> Authenticate"
fi
echo "Done. Restart Claude Code so new commands appear."
