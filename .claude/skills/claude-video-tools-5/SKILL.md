---
name: claude-video-tools-5
description: Five open tools for making videos with Claude without a video-generation model (HyperFrames, OneTake, Collage B-Roll, Claude Animation Base, Lemo-Opuscar) from a short TikTok walkthrough, each checked on GitHub for repo, licence, cost and requirements, with a chooser by job, the licence trap in OneTake, and the lead-magnet and cost caveats. Use when choosing a way to make launch videos, explainers, B-roll or animated shorts with Claude Code.
---

# Five tools for making videos with Claude

Source: a one-minute TikTok by george.automates (Batch 126): "5 tools to make Claude produce videos". The audio was not transcribed (no speech-to-text here), so this skill uses the on-screen captions and names and the repos checked on GitHub on 1 November 2026. The video ends with "comment VIDEO and I'll send you the links", a lead-magnet hook; every link below comes from GitHub, not from that offer.

| # | Tool | Repo | What it makes | Checked facts |
|---|---|---|---|---|
| 1 | HyperFrames (HeyGen) | `heygen-com/hyperframes` | Write HTML, render video, built for agents; overlays, transitions, captions, promos | Already in this library as the `hyperframes` skill (default video framework). Very active repo (6,570 commits; release v0.8.225 on 31 Oct 2026). Stars not read |
| 2 | OneTake | `feitangyuan/onetake` | Product launch films, teasers and feature demos as one continuous take: each beat grows out of the previous one, with a slideshow-detecting "oracle" | 3,444 stars, created 26 Sep 2026, one contributor. **Licence shown on GitHub as "Other"; a third-party listing says PolyForm-Noncommercial-1.0.0 (free for noncommercial use). Read the LICENSE file before any client or company use.** Needs Python 3, Playwright with Chromium, ffmpeg, Node; narration adds faster-whisper and Kokoro TTS. Its own page says it does not need HyperFrames or Remotion |
| 3 | Collage B-Roll | `pyang5166/gbro-collage-broll` | A 5-second halftone paper-collage B-roll clip from one line of voiceover (9:16, 720x1280, 24 fps, silent MP4) | MIT. Chinese and English README, created July 2026, three approval gates. **It generates video with Google's Gemini Omni Flash first and last frames, so it needs your own Gemini API access and costs money per clip.** Stars not read (the video showed 1.5k) |
| 4 | Claude Animation Base | `JohnHeibel/ClaudeAnimationBase` | Hand-painted cartoons in p5.js and p5.brush with the "Clawd" character and 31 emotions, plus a guide for the model | 2,217 stars (the video showed 1.6k), 195 forks, MIT, created 23 Sep 2026. Author's tests used Claude Opus 5.5 at xhigh reasoning in Claude Code; higher reasoning gives more elaborate scenes |
| 5 | Lemo-Opuscar | `lemomo-ai/lemo-opuscar` | A toolbox of film styles made in code, each with a style prompt and a demo film, no video model | The video said 51 styles; the repo README says 59 and its site says 66 and 98 in different places, so the count is not stable. Code and docs MIT; demo films CC BY 4.0 (credit required); **three demo narration tracks are excluded from that licence**. Install as a plugin or clone. Needs Node 20+, ffmpeg, Python 3.11+. The author says a film takes an agent 30 to 60 minutes and a fair amount of tokens. Tuned for Claude Opus 5.5; other models may not reproduce the styles |

## Choosing
| Job | Start with | Why | Watch for |
|---|---|---|---|
| Product launch or feature-demo film from screenshots | OneTake or HyperFrames | Rebuilds UI in HTML; continuous camera (OneTake) or broad HTML-to-video toolkit (HyperFrames) | OneTake licence; render time |
| 5-second B-roll under a voiceover | Collage B-Roll | One idea per clip, collage look | Paid Gemini calls; check each clip |
| Short animated cartoon with a character | Claude Animation Base | Starter kit and guide | Reasoning cost; Clawd is Anthropic's mascot character: check brand rules before commercial use |
| A film in a named visual style (watercolour, newsreel, LiDAR) | Lemo-Opuscar | Style prompts plus working demos | Token cost; demo-film credit; excluded voice tracks |
| One repeatable house format | HyperFrames | Same toolkit every time | Learning curve |

## Cautions
- **Licences differ and one is a trap.** MIT (Collage B-Roll, Claude Animation Base, Lemo-Opuscar code) is permissive; OneTake may be noncommercial. Films you make are yours under Lemo-Opuscar, but you must credit its demo films if you reuse them.
- **Cost and time are real.** Lemo-Opuscar quotes 30 to 60 minutes and many tokens per film; Collage B-Roll bills the Gemini API. Run one draft at low resolution first and set a budget.
- **You run third-party code.** These skills execute scripts, install Python and Node packages and drive a browser. Read the install steps, use a throwaway folder or container, and never put API keys in a shared repository.
- **Claims are one person's.** "Your AI video generator is not a traditional AI video generator" (on screen) is a framing; check the output yourself. Model-dependent results (Opus 5.5) may not reproduce on other models.
- **AI disclosure and rights.** Platform rules on AI-generated or altered video apply; and do not imitate real films or people: Lemo-Opuscar's "Opuscar" demo redraws well-known films, which is not licence to reuse their titles, characters or music.
- **Stars move.** Quote the repo page the day you use it.

Related: `hyperframes`, `remotion-video-creation`, `manim-video`, `video-editing`, `fal-ai-media`, `ai-video-generators`, `kesha-voice-kit`, `claude-design-skills-top5`. Run with `/claude-video-pick <video idea, length, platform, commercial or not>`.
