---
name: gemini-faceless-youtube-five-prompts
description: The @martiendejong_dev carousel "Gemini can now build you a faceless YouTube channel and monetize it in 60 days - copy these prompts" - five prompts (find a niche, build the channel, viral video ideas, script with AI-tool recommendations, grow to 50,000 subscribers) transcribed with their slots, how they differ from the earlier faceless-YouTube prompt sets in this repo, and the checks the carousel omits (the 60-day monetisation claim, YouTube's eligibility thresholds and reused or mass-produced content rules, unverified demand data, a typo in the script prompt). Use when planning a faceless YouTube channel with any chat model, or when comparing prompt sets.
---

# "Faceless YouTube channel in 60 days" - five prompts

Source: five black prompt slides from @martiendejong_dev under a green cover reading "Gemini can now build you a faceless YouTube channel and monetize it in 60 days. Copy these prompts." The prompt texts are transcribed below; slots in [BRACKETS] are the slides'. Notes, checks and the plan are my additions. Nothing was run, and no claim on the cover was tested.

## The five prompts

| # | Title | Prompt (verbatim) |
|---|---|---|
| 1 | Find a profitable niche | "Act as a YouTube growth strategist. Find 10 profitable faceless YouTube niches I can start with zero subscribers, no budget, no camera, and no voice recording. Analyze demand, competition, viral potential, and monetization opportunities. Rank the top 3 niches and recommend the best one for my first 60 days." |
| 2 | Build my channel from scratch | "Act as a YouTube branding expert. Help me build a professional faceless YouTube channel in the [NICHE] niche. Generate channel names, an SEO-friendly description, branding ideas, channel keywords, and a complete setup checklist to stand out from competitors." |
| 3 | Generate viral video ideas | "Act as a YouTube content strategist. Generate 30 high-potential video ideas for my [NICHE] channel targeting [AUDIENCE]. For each idea, provide a clickable title, a strong opening hook, the video concept, and a thumbnail idea. Focus on trending topics, audience demand, and shareability." |
| 4 | Create videos with AI | "Act as an expert faceless YouTube scriptwriter. Write a complete [VIDEO LENGTH]-minute script about [TOPIC]. Include a powerful 5-second hook, engaging storytelling, scene-by-scene visual direcjtions, on-screen text, editing instructions, and a compelling ending. Recommend free or affordable AI tools to create the video without showing my face or recording my voice." (the slide misspells "directions") |
| 5 | Grow to 50,000 subscribers | "Act as my YouTube growth coach. Create a detailed 60-day growth plan for my [NICHE] channel, starting from zero subscribers. Tell me what to post daily, how to optimize titles and thumbnails, how to improve audience retention, and how to use Shorts and long-form videos strategically. Include weekly performance targets and explain how to adjust the strategy based on analytics." |

## How this differs from what the repo already has

The earlier set is in `/faceless-youtube-prompts-5` (niche list with RPM above $7, 20 viral ideas, script modelled on a competitor, Sora 2 content, a calendar) and the five structured `/yt-niche`, `/yt-calendar`, `/yt-seo`, `/yt-script`, `/yt-monetize` commands. This set adds a branding and setup prompt (2) and a 60-day growth-coach prompt (5), and asks for the AI-tool recommendation inside the script prompt. Use the `yt-*` commands for a guided build and this set for quick one-shot prompts.

## Checks the carousel omits

- **"Monetize in 60 days" is a promise, not a result.** The slides show no channel, revenue or timeline. YouTube Partner Programme eligibility has subscriber and watch-time (or Shorts view) thresholds and a review; confirm the current numbers and rules on YouTube's own help pages before planning around a date.
- **Demand data is not in the chat model.** Prompts 1 and 3 ask for "demand", "competition" and "trending topics". A chat model without live search will give plausible guesses. Feed it real data first: YouTube search suggestions, your own competitor channel stats, Google Trends, or a research tool such as the NexLev connector where authorised.
- **Faceless is allowed, mass-produced is risky.** YouTube's policies on repetitive, reused or inauthentic content and on disclosing realistic synthetic media apply. Original commentary, real editing and your own scripting protect a channel; template videos in bulk do not. Check the current policy text.
- **Rights.** AI footage, stock clips, music and voices each carry licence terms; keep a note of where every asset came from.
- **"50,000 subscribers" targets.** A 60-day plan to 50,000 from zero is not a normal outcome; treat prompt 5's weekly targets as hypotheses and replace them with your own measured baseline after four weeks.
- **Slots.** Fill [NICHE], [AUDIENCE], [VIDEO LENGTH] and [TOPIC] with specifics, or the answers will be generic.

## Order that works (my addition)

1. Gather real data on three candidate niches (search results, competitor view counts, upload frequency).
2. Run prompt 1 with that data pasted in; choose one niche on evidence.
3. Prompt 2 for naming and setup; check names for trademark and availability yourself.
4. Prompt 3 for ideas; test five titles and thumbnails against competitor videos before producing.
5. Prompt 4 for one script; read it aloud, cut filler, add your own facts and sources.
6. Prompt 5 after the first four weeks of real analytics, not before.

Related: `yt-faceless-channel`, `/faceless-youtube-prompts-5`, `/yt-niche`, `/yt-script`, `/yt-calendar`, `youtube-niche-finder`, `youtube-seo-optimizer`, `ai-video-prompts-viral`. Nothing is published or uploaded by this skill.
