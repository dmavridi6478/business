---
name: trending-three-nov23
description: Three trending GitHub repos from a @githubnow carousel dated 23 November 2026 (yetone/magpie agent model gateway, Jakeschincariol/instagram-agent-skill, cursor/plugins spec) with what each does as printed, what each can touch, what was not verified, and trial rules. Use before installing any of the three, or when you want one gateway for several coding agents, Instagram Reel planning skills, or a plugin-manifest pattern.
---

# Three trending repos (23 November 2026)

Source: 3-card @githubnow carousel plus an outro card (a repeat of the "Tomorrow's drop" outro, skipped). Star figures are the card's; repo pages could not be read this session (GitHub access to other repos not enabled), so licences and counts are not independently verified.

| Repo | Card says | Card figure | Care |
|---|---|---|---|
| `yetone/magpie` | Agent model gateway: edits the one model key in each agent's own config and routes every agent through a single local gateway; next account or routing group takes over when a quota runs out; prompt masking is opt-in and runs locally. Headline: "Codex on DeepSeek. Claude Code on Kimi." MIT licensed | +20,728 stars this month | See below |
| `Jakeschincariol/instagram-agent-skill` | 13 Claude skills for Reels, carousels, captions, planning. Reels scored against 26 hook formulas; `beats.py` times each line and flags dead air; caption preview at about 125 characters. Python tools run locally with no API key | +5,309 stars this month | Local scripts: read them before running; the skills write, you post |
| `cursor/plugins` | Spec for Cursor plugins: each plugin is a standalone directory with a `.cursor-plugin/plugin.json` manifest. Official plugins for Google Workspace, GitHub, Salesforce, Playwright, plus agent workflows (orchestrate, pstack, advisor, thermos) | +196 stars today | A spec, not an app; compare with Claude Code plugins before copying the pattern |

## magpie: the real risks
- **It rewrites each agent's config** to point at a local gateway and holds your provider keys. Back up the configs first and run it in a spare project.
- **Quota failover across accounts** can breach a provider's terms if it rotates shared or multiple accounts to dodge limits. Check each provider's terms; use your own paid keys.
- **Model swapping changes behaviour and data flow.** A prompt written for one model goes to another vendor (DeepSeek, Kimi): confirm what data may leave your company and where it is processed.
- **"The agent never sees the error"** hides failures: log failovers so you can see cost and quality shifts.
- **Masking is opt-in.** Off by default means keys and emails travel unmasked.
- An earlier batch noted Magpie with only a 3.7k card figure and no owner (`dev-repos-to-clone`); the owner here is `yetone`. [Likely] it is the same project, now far larger. Verify on GitHub.

## Trial protocol
Use `trial-repo`: age and stars, licence file, read the install and config-edit code, run in a throwaway project with a spend cap, know how to restore the configs.

## instagram-agent-skill: how to use
Idea, then hook scoring, then beat timing, then you post. Keep the scoring as a prompt aid, not a guarantee of reach. For Greek-language content check hook formulas and the 125-character preview rule on your own account.

Run with `/trending-pick` or `/trial-repo <owner/repo>`. Related: `trending-repos-week-oct23`, `github-trending-three-nov2`, `social-publishing`, `claude-code-tooling`, `prompt-injection-defense`.
