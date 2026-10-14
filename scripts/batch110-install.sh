#!/usr/bin/env bash
# Batch 107 (file name batch110) - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: skills, commands, agents and design templates were added to the repo; nothing was installed.
# Facts come from each repo's README and LICENSE, read on 12 October 2026.
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. SkillSpector first (Apache-2.0) - the scanner you use before every other install =="
echo "   README: uv tool install git+https://github.com/NVIDIA/skillspector.git   (it also pulls third-party packages: read their licences)"
ask "install SkillSpector with uv (requires uv)?" && uv tool install git+https://github.com/NVIDIA/skillspector.git
echo "   Then: skillspector scan ./some-skill/ --no-llm   (the LLM pass sends the skill's text to a model provider)"

echo "== 2. Clone for reading (shallow; no install, nothing is run) =="
for r in cathrynlavery/diagram-design rohitg00/ai-engineering-from-scratch microsoft/BitNet Tencent/WeKnora open-webui/open-webui amaancoderx/npxskillui usestrix/strix; do
  ask "git clone $r into ~/src?" && clone "$r"
done

echo "== 3. Claude Code add-ons (run INSIDE Claude Code, one at a time; scan first) =="
echo "   /plugin install superpowers@claude-plugins-official                         (already loaded in this workspace)"
echo "   claude plugin install mattpocock-skills@claude-plugins-official"
echo "   /plugin marketplace add forrestchang/andrej-karpathy-skills  then  /plugin install andrej-karpathy-skills@karpathy-skills   (no licence file found at the repo root)"
echo "   /plugin marketplace add anthropics/skills  then  /plugin install document-skills@anthropic-agent-skills"
echo "   /plugin marketplace add https://github.com/affaan-m/ECC  then  /plugin install ecc@ecc   (big system; do not stack a manual install)"

echo "== 4. Vibe-coding layers =="
ask "npm install -g @playwright/cli@latest ?" && npm install -g @playwright/cli@latest
ask "npm install -g skillui (reverse-engineers a site's design; use on sites you have rights to)?" && npm install -g skillui
echo "   Strix needs Docker. README installer is 'curl -sSL https://strix.ai/install | bash' - NOT run here. Read it, or use pipx: pipx install strix-agent"

echo "== 5. Self-host (Docker). Each starts a service on your machine; stop with docker stop <name> =="
ask "Open WebUI on port 3000 (custom licence: branding clause above 50 users)?" && docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
ask "MeTube on port 8081 (AGPL-3.0; download only what you may)?" && { mkdir -p "$HOME/metube-downloads" && docker run -d -p 8081:8081 -v "$HOME/metube-downloads:/downloads" --name metube ghcr.io/alexta69/metube; }
echo "   Glance (AGPL-3.0): follow its README's docker compose template; the README's step downloads and unpacks a tarball - read the template first."
echo "   Stirling-PDF, CryptPad (xwiki-labs/cryptpad, AGPL-3.0), JumpServer (GPL-3.0), WeKnora (Docker Compose): use each README; JumpServer is security infrastructure, do not run it casually."

echo "== 6. Read first, not automated =="
echo "   free-claude-code (AGPL-3.0): its install is a piped script and the proxy sees every prompt and file. Read scripts/install.sh, scan it, run it in a container."
echo "   Spotube (BSD-4-Clause) plays audio sourced from YouTube; GeminiWatermarkTool removes only the VISIBLE watermark (not SynthID): do not use it to disguise AI images."
echo "   Spacedrive, Translumo (Windows only), GitHub Store: install from their releases only after a scan."
echo "Done. Restart Claude Code so the new commands appear: /skill-scan /automation-pick /brand-map /seo-team /addon-pick /oss-pick-oct /lead-gen-map"
