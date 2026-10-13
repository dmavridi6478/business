#!/usr/bin/env bash
# Batch 109 (file name batch112) - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: skills, commands and design templates were added to the repo; nothing was installed.
# Facts come from each repo's README and LICENSE, read on 13 October 2026.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }
scan() {
  # Standing rule: scan before install. Static mode only. Read the findings; whole-repo scores of software repos are noisy.
  if command -v skillspector >/dev/null 2>&1; then
    echo "   SkillSpector (static) on $1:"; skillspector scan "$1" --no-llm 2>&1 | sed -n '1,25p' || true
  else
    echo "   SkillSpector not found. Install it first: uv tool install git+https://github.com/NVIDIA/skillspector.git"
    ask "   continue WITHOUT a scan?" || return 1
  fi
}

echo "== 1. Clone for reading (shallow; nothing is run) =="
for r in alibaba/open-code-review xtool-org/xtool vercel-labs/skills Aider-AI/aider; do
  ask "git clone $r into ~/src?" && clone "$r"
done

echo "== 2. Aider (Apache-2.0). README install, copied exactly: =="
echo "     python -m pip install aider-install"
echo "     aider-install"
if ask "scan ~/src/aider, then run the two commands above?"; then scan "$HOME/src/aider" && python -m pip install aider-install && aider-install; fi
echo "   The slide's 'aider --model a,b,c' line is not documented in the README. Check: aider --help"

echo "== 3. open-code-review (Apache-2.0; needs a model endpoint and key you configure) =="
if ask "scan ~/src/open-code-review, then npm install -g @alibaba-group/open-code-review?"; then scan "$HOME/src/open-code-review" && npm install -g @alibaba-group/open-code-review; fi

echo "== 4. vercel-labs/skills (MIT). Lists only; installs nothing =="
echo "     npx skills add <owner/repo> --list"
echo "   Never use --all on a source you have not read. Scan the skill folder first, then: npx skills add <owner/repo> --skill <name> -a claude-code"
ask "run 'npx skills add vercel-labs/agent-skills --list' (downloads the CLI package, installs no skill)?" && npx skills add vercel-labs/agent-skills --list

echo "== 5. xtool (MIT). Not automated =="
echo "   Follow the installation page for your system (https://xtool.sh/documentation/xtooldocs/installation-linux or -macos)."
echo "   It asks for Apple Developer Services credentials: use an account you can rotate, and read its auth documentation first."

echo "Done. Restart Claude Code so the new commands appear: /coding-tool-pick /briefing-oct13-pick /linkedin-landing-page"
