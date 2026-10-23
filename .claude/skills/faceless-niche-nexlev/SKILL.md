---
name: faceless-niche-nexlev
description: A gated workflow for finding and vetting a faceless YouTube niche with the NexLev connector - discover outlier channels, filter by faceless, monetised and size, separate AI-generated and dramatised channels, pull each channel's breakout videos, check saturation and revenue estimates, then decide against platform-policy, licence and originality gates. Use when someone wants a faceless channel niche, asks which niches are growing, or wants to validate a niche idea with data instead of a one-off scan. Built from the Claude YouTube scan story (Batch 116) and tested live against NexLev on 23 October 2026. Read-only until you save to the swipe file.
---

# Faceless niche workflow with NexLev

NexLev is connected in this environment (tools `mcp__NexLev__*`). Every research tool below is read-only. `save_to_swipefile` and the folder tools **write to the user's NexLev account**, so ask first. All revenue, RPM and "outlier score" numbers are NexLev estimates, not channel statements. Outlier score is a video or channel's views divided by its own average: 2 is strong, 3 is exceptional, and a small sample inflates it.

## Steps

| # | Step | Tool | Gate |
|---|---|---|---|
| 1 | Inspiration | `latest_discovered_faceless_niches` (limit 20, outlierScore 2) | none |
| 2 | Topic search | `search_niche_finder_channels` with `query` = your niche, `isFaceless` true, `isMonetizationEnabled` true, `minOutlierScore` 2, `maxSubscribers` 50000 | pick at most 3 niches |
| 3 | Triage by how it is made | Read `isAiChannel`, `editingStyle`, `editingVoice`, description | **Flag AI-generated, "dramatized" or fabricated-story channels** (see below) |
| 4 | Breakout videos | `youtube_channel_outliers` on the top 3 channels, and `faceless_outliers_videos` with a semantic `query` | note topics and title patterns, not copy |
| 5 | Saturation | `get_similar_channels` (async, level 1) or count results at step 2 | if many near-identical channels, the niche is crowded |
| 6 | Revenue sanity | `check_channel_monetization`, `get_video_rpm` on 2-3 videos | use the lower of NexLev and your own estimate |
| 7 | Originality plan | You, not a tool | **Gate:** what is your own angle, script, footage and voice? |
| 8 | Policy and licence check | You | **Gate:** YouTube monetisation and synthetic-content rules, footage and music licences, voice consent |
| 9 | Decide, then save | `save_to_swipefile` only after approval | **Human approval** |

## Red flags found in a live test (23 October 2026)

Query: "wildlife and nature documentary", faceless, outlier score 2 or higher. Five results:

| Channel | Subs | Est. monthly revenue | Outlier | AI flag | Est. RPM | Note |
|---|---|---|---|---|---|---|
| Wild Worldnario | 9,030 | $895 | 8.82 | no | $2.46 | 14 videos, first video July 2026 |
| Wildlife Untamed | 18,100 | $1,691 | 7.65 | yes | $1.84 | 26 videos, first video June 2026 |
| Animal Earth Documentary | 8,000 | $201 | 3.18 | no | $1.47 | States royalty-free footage licence |
| Savage Nature | 240,000 | $11,696 | 4.77 | yes | $2.37 | Description says "dramatized, digitally created" |
| W-Wildlife Documentary | 28,000 | $277 | 8.50 | yes | $4.10 | Named "final moments" orca-trainer stories; no uploads since January 2026 |

What this shows:
- **Three of five are flagged AI-generated**, and one openly dramatises. A high outlier score does not mean a sound model; it can mean a fabricated story that went viral. [Likely] The named orca-trainer stories are fabricated (the "Jessica Radcliffe" story circulated in 2025 as an AI-made hoax); verify before relying on that channel as a model. Do not copy fabricated-news formats: it risks demonetisation and harm.
- **Revenue estimates are modest.** RPM per NexLev is about $1.5-4.1 in this sample, and most channels earn a few hundred dollars a month. Only one channel clears $10,000 a month.
- **Newness hides risk.** Several channels began in mid-2026, so the sample says nothing about durability.
- In the latest-discovered list, one channel showed a 14.85x outlier with 5,000 subscribers and 14 days of history: tiny samples inflate the score.

## Use it
`/faceless-niche-scan <niche or "inspire me">`. After step 8, go on with `/yt-niche`, `/yt-script`, `/yt-calendar`, `/yt-seo`, `/yt-monetize`. Background and caveats: `yt-faceless-channel/references/claude-youtube-scan.md`.
