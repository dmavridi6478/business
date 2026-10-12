#!/usr/bin/env bash
# Batch 118 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing pipes a download into a shell.
# Done in the cloud session: 3 skills, 4 commands, 1 design template, prompts. No plugin, connector or clone was added.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }
echo "== Repos (shallow clones; read README and LICENSE first; run unknown tools in a container or VM) =="
for r in excalidraw/excalidraw getmaxun/maxun heyform/heyform wavetermdev/waveterm eugeny/tabby; do
  ask "git clone $r into ~/src?" && clone "$r"
done
echo "   Owner/repo names for these were not shown on the slides and need checking on GitHub first: storytold/photocraft, morluto/rea, lexmount/moli, Niko1221/Strata, MXterm, Vesta, Calyx, OpenChatCut, Macshot."
echo "   Moli's install line pipes curl into sh: download the script, read it, verify the checksum, or build from source."
echo "   AnyPS5 is deliberately NOT included: console executables are protected, so modifying or porting them can be unlawful."
echo "Done."
