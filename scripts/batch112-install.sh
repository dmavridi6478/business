#!/usr/bin/env bash
# Batch 112 - optional installs. RUN ON YOUR OWN MACHINE. Every step asks first. Nothing here pipes a download into a shell.
# Done in the cloud session: 9 skills, 9 commands, 5 design templates, 5 themes, a workflows page and a prompts file were added to the repo; nothing was installed.
# Repo slugs, stars and licences for the Part 17 / Part 12 / finds repos were read from GitHub pages on 19 October 2026
# (see .claude/skills/oss-swap-part-17, oss-swap-part-12 and github-finds-oct-19).
set -euo pipefail
ask() { read -r -p "$1 [y/N] " a; [[ "$a" =~ ^[Yy]$ ]]; }
clone() { [ -d "$HOME/src/${1#*/}" ] && { echo "   $1 already cloned"; return; }; mkdir -p "$HOME/src" && git clone --depth 1 "https://github.com/$1.git" "$HOME/src/${1#*/}"; }

echo "== 1. Low-ops tools (read the README; most are apps or libraries, not servers) =="
for r in microsoft/playwright vuejs/vitepress garris/BackstopJS mitmproxy/mitmproxy desktop/desktop ghostty-org/ghostty; do
  ask "git clone $r into ~/src (read-only look)?" && clone "$r"
done

echo "== 2. Context-cost tool worth testing on one real session =="
ask "git clone headroomlabs-ai/headroom into ~/src (Apache-2.0)?" && clone "headroomlabs-ai/headroom"

echo "== 3. Servers you would have to run and patch =="
for r in valkey-io/valkey coder/code-server gocd/gocd jitsucom/jitsu pocketbase/pocketbase jenkinsci/jenkins VictoriaMetrics/VictoriaMetrics; do
  ask "git clone $r into ~/src (read-only look)?" && clone "$r"
done

echo "== 4. Licence reads needed first (GitHub reports 'Other') =="
for r in Graylog2/graylog2-server Arize-ai/phoenix; do
  ask "git clone $r into ~/src, then read its LICENSE file?" && clone "$r"
done

echo "== 5. Data and research (read the licence: os-taxonomy is ODbL, share-alike) =="
for r in withmarbleapp/os-taxonomy shiyu-coder/Kronos; do
  ask "git clone $r into ~/src?" && clone "$r"
done

echo "== 6. Not automated =="
echo "   Docker Agent: run 'docker agent new' yourself after reading the official docs (needs Docker Desktop 4.63+ or Homebrew and a model key)."
echo "   Connectors cannot be installed from a script: Tally and n8n exist in the claude.ai directory; authorise them in connector settings if you want them."
echo "   Never run a shell-tool agent with secrets in the environment."
echo "Done. Restart Claude Code so the new commands appear."
