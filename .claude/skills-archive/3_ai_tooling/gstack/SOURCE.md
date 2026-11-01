Vendored from https://github.com/garrytan/gstack (root SKILL.md router), MIT License.
Cloned at commit:
1cab5e11083a37ea0bc62117e9a9c5d05d68785e

gstack is Garry Tan's Claude Code setup: 23+ specialized skills/agents acting
as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA across
the product lifecycle. This vendors only the top-level router SKILL.md.

Full functionality (the browse binary, the other ~70 subskill directories,
multi-host support for Codex/Kiro/Factory/OpenCode) requires the real
installer, which needs the 'bun' runtime and was NOT run here (it symlinks
into multiple tool configs across the machine — install deliberately, not
as a side effect of cloning this repo):

  git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack
  cd ~/.claude/skills/gstack && ./setup
