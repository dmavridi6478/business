#!/usr/bin/env bash
# Batch 112 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing pipes a download into a shell.
# Done in the cloud session: 8 skills, 3 commands, 1 agent, 3 design templates, prompts; plugins code-simplifier, context7, frontend-design, superpowers installed at user scope.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Claude Code plugins (slides say claude-plugins-official; built-in marketplace here is anthropic-plugin-directory) =="
for p in code-simplifier context7 frontend-design superpowers; do
  ask "show install command for $p?" && echo "   /plugin install $p@anthropic-plugin-directory"
done
echo "   code-review: not published under that name in the built-in marketplace. Run /plugin, search 'code-review', read the source and publisher before installing."

echo "== 2. Repos (shallow clones; read README and LICENSE before running anything) =="
for r in trycua/cua leepokai/codync Tencent/WeKnora storytold/artcraft DietrichGebert/ponytail liquidslr/system-design-notes sw33tLie/macshot; do
  ask "git clone $r into ~/src?" && clone "$r"
done
echo "   cua and codync drive real desktops or coding agents: use a throwaway VM or container, not your logged-in machine."
echo "Done. Restart Claude Code so new commands appear."
