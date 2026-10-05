---
name: ai-tool-links-index
description: Router for the ~400 AI tools, websites and repos saved in Dimitrios's iCloud note "Links and sites" (https://www.icloud.com/notes/0034G1gqR4ra1BTR13sd25fdw). Use first whenever a user asks "is there a tool/site/repo for X" (video, images, websites/apps, voice, PDFs, slides/infographics, writing/research, business/automation, free utilities); it names the category skill to load and lists what was intentionally excluded.
---

# Links and Sites - Router

The note is a flat list of ~400 site names (many duplicated), 9 identifiable open-source projects and 67 TikTok short links. It contains **no written procedures or workflows**, so none were built. Everything below is a directory built from the saved names plus general knowledge; capability claims were not re-verified on the live sites.

## Which skill to load
| User need | Skill |
|---|---|
| Video generation, avatars, dubbing, clipping | `ai-video-generators` |
| Image generation, cleanup, logos, mockups, UI design | `ai-image-design-tools` |
| Build a site, app, chatbot, UI components | `ai-website-app-builders` |
| TTS, voice cloning, music, transcription | `ai-voice-audio-tools` (open-source voice repos: `ai-voice-tools`) |
| PDFs, conversion, translation, spreadsheets | `pdf-document-conversion-tools` |
| Slides, infographics, diagrams, charts | `presentations-infographics-diagrams` |
| Writing, summarising, research, study, chat models | `ai-writing-research-tools` |
| Sales, marketing, competitor research, automation | `business-growth-automation-tools` |
| Free utilities, learning, catalogues, maps | `free-utility-learning-resources` |
| The 67 saved TikToks | `tiktok-saved-links` |

## Repo skills (cloned shallow, read-only)
| Note entry | Repo | Skill | Licence note |
|---|---|---|---|
| Wan2.1 | Wan-Video/Wan2.1 | `repo-wan21` | Apache-2.0 |
| Hunyuan | Tencent-Hunyuan/HunyuanVideo | `repo-hunyuanvideo` | **Excludes EU/UK/South Korea** |
| Cogvideo | zai-org/CogVideo | `repo-cogvideo` | Apache-2.0 code; separate model licence |
| ominicontrol | Yuanshi9815/OminiControl | `repo-ominicontrol` | Apache-2.0 |
| stirlingpdf.io | Stirling-Tools/Stirling-PDF | `repo-stirling-pdf` | Open-core |
| reactbits.dev | DavidHDev/react-bits | `repo-react-bits` | MIT + Commons Clause |
| roadmap.sh | kamranahmedse/developer-roadmap | `repo-developer-roadmap` | see repo `license` |
| pinokio.computer | pinokiocomputer/pinokio | `repo-pinokio` | MIT-style |
| azgaar.github.io/fantasy-map-generator | Azgaar/Fantasy-Map-Generator | `repo-fantasy-map-generator` | MIT |

Not cloned: n8n (already in `setup-repos.sh`; see the existing `n8n-*` skills). Other entries (webcrumbs, uiverse, opensourcealternative.to, ninite, agent.ai, etc.) were saved as sites; their repos were not confirmed, so none were guessed.

## Intentionally excluded from the skills
- A free movie/series streaming site (copyright-infringement risk).
- A service described in the note as bypassing card checks on free trials (terms-of-service violation).
- AI-detector "bypass" tools are listed in `ai-writing-research-tools` only with a policy restricting help to disclosed, permitted use.

## Maintenance
When the note changes, re-fetch it (CloudKit public share resolves the text), add new names to the matching category skill, re-verify any site before recommending it, and delete dead links.
