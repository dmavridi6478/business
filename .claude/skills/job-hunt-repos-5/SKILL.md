---
name: job-hunt-repos-5
description: The @ty.prompts.ai "5 free repos that job hunt for you" series - career-ops (scan job portals, A-F scoring, ATS CV per job, scam-posting flags), Reactive Resume (self-hosted resume builder), AIHawk (mass auto-apply bot, with risk notes), HackerRank's Hiring Agent (resume scorer) and ResumeSkills (Claude Code resume skills) - with slide stats, what each does, which job-search skills already exist here and the guardrails. Use when someone wants open-source tools for job search, resume scoring or tailoring, or asks whether auto-apply bots are a good idea.
---

# Job-hunt repos (5)

Stats are the slides' own. Nothing here was cloned or installed in the cloud session.

| # | Repo | What it does (slide) | Stats | Notes |
|---|---|---|---|---|
| 1 | `santifer/career-ops` | "Companies use AI to filter candidates; this gives you AI to filter companies." Scans Greenhouse, Ashby, Lever; scores each listing on an A-F rubric into 1.0-5.0; writes an ATS-optimised CV per job; flags scam and ghost postings; tracks applications; runs locally inside Claude Code, Codex, OpenCode or Antigravity | 64k stars, 13k forks, 268 contributors | a `career-ops` skill is also available in this environment; read what it sends where before pasting a CV in |
| 2 | `amruthpillai/reactive-resume` | resume builder that calls OpenAI, Gemini or Claude to rewrite weak bullets; self-host so your work history stays on your server; MIT | 40k stars, 4.6k forks | resume text is personal data: self-host or use a local model if the CV has client names |
| 3 | `feder-cr/Jobs_Applier_AI_Agent_AIHawk` | reads your CV, auto-applies at volume with a tailored resume and cover letter | 30k stars, 4.6k forks, 9 contributors | the slide itself says #1 argues the opposite, that filtering beats spraying: "use it on purpose, not by default". Mass auto-apply often breaks job-board terms, can get accounts banned, and sends employers unreviewed claims. **I recommend not using it unattended** |
| 4 | `interviewstreet/hiring-agent` | HackerRank's open-sourced resume ranker; their README says 50-60k intern applications a year, so it decides which get read first. Run your own resume through it | 6.9k stars, 295 issues | a signal of how screening may work, not proof of how any employer ranks you |
| 5 | `Paramchoudhary/ResumeSkills` | Claude Code skills for ATS compatibility, turning weak bullets into achievements with real metrics, scoring a job posting against your CV, interview prep | 1.7k stars, 3 contributors | small project: read the skill files before installing |

## Workflow I would run
1. Define the role, location and non-negotiables (one paragraph).
2. Use career-ops (or `/jobsearch`) to filter listings, not to apply.
3. For each shortlisted role: tailor the CV from a master CV, never inventing metrics (`/resume-gap-analysis`, `/resume-review`).
4. Score the result with Hiring Agent as a sanity check.
5. Apply manually; track in a sheet. Never let a bot submit on your behalf.
Related here: `resume-prompt-kit`, `job-search-90days`, `dream-job-10-prompts`, `linkedin-job-search-5-hacks`, `/job-search-90days`. Commands: `/job-fit-check`.
The slide CTA (7/7) pushes 1:1 calls and app builds at tyblackard.com: marketing, not part of the tools.
