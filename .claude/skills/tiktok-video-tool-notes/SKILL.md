---
name: tiktok-video-tool-notes
description: What could be read from four short TikTok videos (frames only, no audio transcript) - Codync (@GithubSignals), "Top Claude MCPs to make it 100x more powerful" (@samdespo: scraping MCP, social posting MCP, Perplexity, Context7, Higgsfield, GPT image generation), a @sadie.ontech agent-skills montage (browser agent tasks, Claude Scientific Skills, a cybersecurity skills repo mapped to MITRE ATT&CK/NIST), and Microsoft's open-source SkillOpt (@min.json: improves a skill from your Claude Code sessions and corrections). Use as leads to verify, not as a source of facts.
---

Limits: audio was not transcribed; only on-screen captions and frames were read. Confidence is low on anything not written on screen.
- **Codync** (leepokai/codync, Apache-2.0): see `github-trending-oct8-repos`.
- **samdespo MCP list** (7 items, names partly read from frames): a web-scraping MCP (LLM-ready markdown/JSON/screenshots), a social-posting/automation MCP covering Instagram, Facebook, YouTube, LinkedIn, TikTok, Perplexity, Context7, Higgsfield, GPT Images. Mapped here: scraping -> `exa`/TinyFish/Bright Data connectors; social posting -> Blotato (`blotato-nine-platform-posting`), Typefully, Taplio; Perplexity -> not connected; Context7 -> installed; Higgsfield and image generation -> Higgsfield connector.
- **sadie.ontech**: shows a browser agent exporting X followers to a CSV and filling a job application; "Claude Scientific Skills" and a cybersecurity skills repo mapping skills to MITRE ATT&CK, NIST CSF, ATLAS, D3FEND, AI RMF. Repo names were not legible: do not guess; ask for the link.
- **SkillOpt** (microsoft/SkillOpt, already in README at 15.6k stars): the video says it reads your Claude Code sessions, e.g. report drafting plus your corrections, and rewrites the report-writing skill's instructions. Related here: `skill-comply`, `improve-system`, `learn-eval`, `skill-health`. Review every proposed diff before applying.
