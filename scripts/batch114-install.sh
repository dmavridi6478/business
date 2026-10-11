#!/usr/bin/env bash
# Batch 114 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing pipes a download into a shell.
# Done in the cloud session: 4 skills, 2 commands, 2 design templates, prompts. No plugin or connector was added.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }
echo "== Repos (shallow clones; read README and LICENSE first; agent tools: use a throwaway repo or VM) =="
for r in twentyhq/twenty hoppscotch/hoppscotch firecamp-io/firecamp huggingface/transformers hugohe3/ppt-master ranxianglei/billion-context TNTcraftHIM/Piik; do
  ask "git clone $r into ~/src?" && clone "$r"
done
echo "   llama.cpp: use your package manager (brew install llama.cpp / winget) or build from source. Do NOT run the 'irm ... | iex' one-liner shown on the slide."
echo "   Emdash, Jean, Rakazo: download official releases only after reading their permissions; owner/repo names were not fully legible on the slides, so find them via the project website."
echo "Done."
