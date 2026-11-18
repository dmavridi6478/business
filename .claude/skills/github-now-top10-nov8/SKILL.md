---
name: github-now-top10-nov8
description: Register of the "Top 10 GitHub Repos Trending Today" short video by @githubnow (8 November 2026 snapshot) - cloudflare/security-audit-skill, milind-soni/OpenMausBot, sherlock-project/sherlock, zed-industries/zed, mattpocock/skills, google/skills, anthropics/skills, astral-sh/ruff, prometheus/prometheus, meta/astryx - with the on-screen star gains, what was verified (five repos' existence and licences), and the cautions (Sherlock searches usernames across sites, a "security audit skill" is not an audit). Use when comparing what is trending, choosing a skill repo to read, or checking what is new versus already covered.
---

# GitHub trending top 10 (video, @githubnow)

One 26-second video; the ranked list is on screen for about two seconds. Figures are the video's own, read from frames; none were checked against GitHub (the API is blocked from the cloud container). The video has auto captions that read "OPEN-SOURCE GROK", "SOCIAL NETWORKS" and "MACHINE-READABLE" but I did not check them against the repos.

| Rank | Repo (as shown) | Gain shown | Total shown | Notes |
|---|---|---|---|---|
| 1 | `cloudflare/security-audit-skill` | +2,088 | 65.5k | MIT (read). A skill that guides an agent through a security review; it is not an audit and does not prove an app is secure. Read its SKILL.md before installing |
| 2 | `milind-soni/OpenMausBot` | +1,986 | 16.8k | Apache-2.0; already in `oss-finds-eight-creators-nov2026`. Runs your Claude, Codex and Grok CLIs |
| 3 | `sherlock-project/sherlock` | +1,819 | 100.3k | MIT (read). Hunts a username across social networks: use only on yourself or with consent, as it can be used to profile people |
| 4 | `zed-industries/zed` | +1,119 | - | Already registered |
| 5 | `mattpocock/skills` | +1,111 | - | Exists; skills collection; not read |
| 6 | `google/skills` | +449 | - | Exists; not read |
| 7 | `anthropics/skills` | +386 | - | Exists; the official skills repo; not read |
| 8 | `astral-sh/ruff` | +350 | - | Python linter; not read |
| 9 | `prometheus/prometheus` | +325 | - | Monitoring; not read |
| 10 | `meta/astryx` | +185 | - | Not checked; could not confirm the path |

Verified: existence and default branch for `cloudflare/security-audit-skill`, `sherlock-project/sherlock`, `mattpocock/skills`, `google/skills`, `anthropics/skills`; licences for the first and the third. Not checked: the other repos' licences and `meta/astryx`.

## How to use a trending list

A one-day star gain shows attention, not quality or safety. Skill repos in particular run with your agent's permissions: read the files, pin a commit, and use `/repo-vet`.
