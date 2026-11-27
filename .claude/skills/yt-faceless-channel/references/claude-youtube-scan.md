# Scan YouTube with Claude, find faceless niches, make one video

Source: @siddhantt.ai 13-slide story ("Claude scanned 1,283 YouTube videos in 4 minutes. It found 11 channels with no humans. 14 million views in 10 days. Then it made one.") (Batch 116). The scan method is reproducible; the income figures are estimates, not results. The "comment SCAN for the files" gate means the scanner script, channel list and motion files were not provided; only the slide text was captured.

## The recipe (as shown)

| # | Step | Detail |
|---|---|---|
| 1 | Connect Claude to YouTube | One free API key from Google (YouTube Data API v3), enable the API in Google Cloud, paste it into Claude Code (the slide names Opus 5.5). About 2 minutes |
| 2 | Scan | "Scan the last 10 days, rank by views divided by channel average." 16 searches, 1,283 videos, each channel's last 10 uploads, ranked by how far each video beat its own channel's average. About 3 min 51 s |
| 3 | Read the pattern | 11 faceless channels, 263 to 85,000 subscribers; 14.2 million views in 10 days (the listed rows sum to about 14.26 million, so the headline is rounded down) |
| 4 | Six traits all 11 share | No presenter (AI narration over footage); dramatic titles; 2-3 uploads a week; 20-60 minute videos; stock plus AI footage; tiny channels with millions of views |
| 5 | Toolbox (8 names, 7 free) | yt-dlp (transcripts), Whisper large-v3 (timestamps), Kokoro-82M (narrator voice on a laptop), Dia-1.6B (two-voice dialogue), ClearerVoice-Studio (cleans audio), WanGP / Wan 2.2 (AI video on your own PC), ElevenLabs v3 (free tier), Nano Banana (thumbnails). Monthly cost shown: 0 rupees |
| 6 | Footage models | Veo 3, Seedance 2.5, Wan 2.2, Nano Banana; 0 to about 35 rupees a clip |
| 7 | Script | One Claude command writes a 60-second documentary narration: a hook, short sentences, about 140 words, written in about 40 seconds |
| 8 | Voice | ElevenLabs v3 (free tier about 10 minutes a month) or Kokoro-82M locally |
| 9 | Assemble | Footage, captions, a cut, edited in After Effects; the sample clip credits CC BY 4.0 NOAA footage |

## The money slide, checked
The card says long videos pay 10-40 times more per view than Shorts. Its example: a 21-minute video with 4.0M views at an estimated $2-4 per 1,000 views is $8,000-16,000; the same views on Shorts at $0.10-0.20 per 1,000 is $400-800. The arithmetic is right (4.0M views x $2-4 per 1,000 = $8,000-16,000), but the rates are **estimates from public ranges, not these channels' statements**. Real revenue depends on audience country, topic, monetisation eligibility and ad demand. Treat it as an upper-ish scenario, not a plan.

## What the story leaves out (check before copying)
- **Platform policy:** YouTube restricts "inauthentic" mass-produced or repetitive content for monetisation and expects disclosure of realistic synthetic content. A channel that is only AI narration over stock footage is exactly where reviews look. Read the current Partner Programme and altered-or-synthetic-content rules first.
- **Licences:** each footage clip, music track and voice has its own licence. CC BY needs attribution; stock needs the right plan; cloning a real person's voice needs consent.
- **Survivorship:** 11 channels that worked tell you nothing about the hundreds that did not. Seeing "views in 10 days" says nothing about retention, takedowns or whether the channel is monetised.
- **Competition:** a niche that a scan exposes is a niche everyone else's scan exposes.

## Use it with what is here
- Niche research: `/yt-niche`, `youtube-niche-finder`. The NexLev connector (connected in this environment) exposes faceless-channel checks, outliers and RPM data, which is a sturdier source than a one-off scan.
- Script, calendar, SEO, monetisation: `/yt-script`, `/yt-calendar`, `/yt-seo`, `/yt-monetize`.
- Local voice and dubbing tools: see `oss-alternatives` (VoiceStudio, VoxCPM, Whisper, yt-dlp, Batch 114 and 116).

## NexLev route (added after the live test)
For a sturdier method than a one-off scan, use `/faceless-niche-scan` and the `faceless-niche-nexlev` skill. A live test on 23 October 2026 found three of five top wildlife outliers flagged AI-generated and one openly dramatised, and estimated RPM near $1.5-4.1, lower than the story's $2-4 range for most.
