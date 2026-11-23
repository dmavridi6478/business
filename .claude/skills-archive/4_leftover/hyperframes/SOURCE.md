Vendored from https://github.com/heygen-com/hyperframes (skills/hyperframes/SKILL.md), MIT License.
Cloned at commit:
67edb01bf4aa2f5931e838e46e14e0f51a5809ee

HyperFrames (HeyGen) is "write HTML, render video" — compositions are plain
HTML with data attributes, rendered to real video, built for agent-driven
workflows (no React/proprietary DSL). This vendors the mandatory entry-point
skill; the full repo ships 19 skills (hyperframes-cli, hyperframes-animation,
motion-graphics, captions-overlay, etc.) plus the CLI/renderer itself, which
this vendoring does not include. Install the rest with:
npx skills add heygen-com/hyperframes -g -a claude-code -s '*' -y
