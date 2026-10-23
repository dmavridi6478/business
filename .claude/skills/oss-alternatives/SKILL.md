# OSS Alternatives Guide

Open-source replacements for paid AI SaaS tools — run locally, no subscription.

## Quick Reference

| Paid Tool | OSS Alternative | Install | What It Does |
|-----------|----------------|---------|--------------|
| remove.bg | **rembg** | `pip install rembg` | AI background removal from images |
| Moises.ai | **spleeter** | `pip install spleeter` | Vocal/instrument stem separation |
| Adobe Scan | **ocrmypdf** | `pip install ocrmypdf` | OCR + searchable PDF creation |
| Rask.ai | **pyvideotrans** | `pip install pyvideotrans` | Video translation + dubbing |
| Audible | **audiblez** | `pip install audiblez` | Text-to-audiobook conversion |
| Docx/PDF→MD | **markitdown** | `pip install markitdown[all]` | Convert any doc format to Markdown |

## Usage Examples

### rembg — Remove Background
```bash
rembg i input.png output.png
# Or batch:
rembg p input_folder/ output_folder/
```

### spleeter — Split Audio Stems
```bash
spleeter separate -p spleeter:2stems -o output/ audio.mp3
# 2stems = vocals + accompaniment
# 4stems = vocals + drums + bass + other
# 5stems = vocals + drums + bass + piano + other
```

### ocrmypdf — OCR PDF
```bash
ocrmypdf input.pdf output_searchable.pdf
ocrmypdf -l eng+fra input.pdf output.pdf  # multi-language
```

### pyvideotrans — Translate & Dub Video
```bash
pyvideotrans --source_language en --target_language es input.mp4 output.mp4
```

### audiblez — Text to Audiobook
```bash
audiblez book.epub -l en-us -v af_sky
# Voices: af_sky, af_bella, am_adam, am_michael, etc.
```

### markitdown — Convert Docs to Markdown
```python
from markitdown import MarkItDown
md = MarkItDown()
result = md.convert("presentation.pptx")
print(result.text_content)
```
```bash
markitdown input.pdf > output.md
markitdown input.docx > output.md
markitdown https://example.com > output.md
```

## 25 free replacements for paid subscriptions (@will.ai.m, Batch 112)

Star counts are the card's figures (not verified; the card has no date). 25 icons, 24 list entries: entry 16 pairs Open WebUI with Ollama.

| # | Group | Free tool | Replaces | Card stars | Job |
|---|---|---|---|---|---|
| 01 | Creative | ComfyUI | Midjourney | 132k | Make images on your own graphics card |
| 02 | Creative | OpenVoice | ElevenLabs | 37k | Clone a voice from a short clip |
| 03 | Creative | Kdenlive | Premiere Pro | 5.6k | Cut and export video, no watermark |
| 04 | Creative | GIMP | Photoshop | 6.4k | Retouch photos and edit layers |
| 05 | Creative | Penpot | Canva Pro | cut off on card | Design interfaces in your browser |
| 06 | Office | ONLYOFFICE | Microsoft 365 | 5.3k | Opens Word, Excel and PowerPoint files |
| 07 | Office | AppFlowy | Notion | 76k | Notes and databases on your own machine |
| 08 | Office | NocoDB | Airtable | 65k | Turn a database into a usable spreadsheet |
| 09 | Office | Joplin | Evernote | 56k | Write notes that sync to storage you own |
| 10 | Office | Stirling-PDF | Adobe Acrobat | cut off on card | Merge, split and sign PDFs in your browser |
| 11 | Cloud | Nextcloud | Google Drive | 37k | Your own file drive on your own server |
| 12 | Cloud | Immich | Google Photos | 113k | Back up every photo from your phone |
| 13 | Cloud | Vaultwarden | 1Password | 67k | Host your own password vault |
| 14 | Cloud | Pi-hole | Ad-block subscriptions | 61k | Block ads for every device on your wifi |
| 15 | Cloud | Syncthing | Dropbox sync | cut off on card | Sync folders straight between devices |
| 16 | AI | Open WebUI + Ollama | ChatGPT Plus | 151k | Run a chatbot on your own computer |
| 17 | AI | n8n | Zapier | 203k | Wire apps together without writing code |
| 18 | AI | Cline | Copilot | 68k | An AI coding agent inside your editor |
| 19 | AI | Whisper | Otter | 109k | Turn any recording into text, offline |
| 20 | Comms | cal.com | Calendly | 48k | Let people book time in your calendar |
| 21 | Comms | listmonk | Mailchimp | 23k | Send newsletters from your own server |
| 22 | Comms | Home Assistant | Smart-home hubs | 90k | Run your smart home without the cloud |
| 23 | Comms | SearXNG | Private search | 37k | Search the web without being tracked |
| 24 | Comms | Mailspring | Outlook | cut off on card | Every email account in one inbox |

### Hidden costs (the card's "no trials, no credits, no per-seat pricing" omits these)

Hosting and bandwidth, backups, security patching, your hours, and for password managers and file drives the risk of being the only person responsible for the data. Rule: self-host only what you can restore from backup in an hour; otherwise use the paid or managed option. Vaultwarden, Nextcloud and Immich hold the most sensitive data on this list.

Overlap: `oss-alternatives`, `opensource-desktop-app-alternatives`, `oss-ai-alternatives` already cover subsets; this skill is the one-card index.

## When to Use This Skill

Invoke `/oss-alternatives` when:
- A user asks how to do background removal, audio separation, OCR, video dubbing, or audiobook creation
- Looking to cut SaaS costs
- Need offline/local processing for privacy


## Batch 114 finds (verified on GitHub, 22 October 2026)

Ten "free alternatives" cards (@martiendejong_dev) plus tool cards (@palidev21). Stars, forks and licences below were read from each repo page; **the cards' price comparisons ($14/month YouTube Premium, Zapier Pro $600/month, Figma $45 per editor, Calendly Teams $16 per user, Google Analytics 360 $150,000/year, Notion $20 per user) were not verified** and depend on plan and date.

| Tool | Does | Stars | Licence | Card pairs it with | Licence care |
|---|---|---|---|---|---|
| `yt-dlp/yt-dlp` | Command-line audio/video downloader | 200,336 | Unlicense | YouTube Premium downloads | Check the site's terms and copyright before downloading |
| `ollama/ollama` | Run open models locally | 184,295 | MIT | Hosted chat subscriptions | Model licences differ from the runner's |
| `immich-app/immich` | Self-hosted photo and video library | 116,930 | AGPL-3.0 | Cloud photo storage | Network-use copyleft; photos are sensitive, test restore |
| `openai/whisper` | Speech-to-text, runs offline | 111,079 | MIT | Transcription services | - |
| `plausible/analytics` | Cookie-free web analytics | 29,602 | AGPL-3.0 | Google Analytics 360 | Self-host needs ClickHouse and Postgres; hosted plan is the default route |
| `AppFlowy-IO/AppFlowy` | Notion-style workspace | 77,620 | AGPL-3.0 | Notion | - |
| `penpot/penpot` | Design and prototyping | 61,491 | MPL-2.0 | Figma | - |
| `n8n-io/n8n` | Workflow automation | 208,337 | **Other (fair-code, not OSI open source)** | Zapier Pro | Read the Sustainable Use licence before offering it as a service |
| `calcom/cal.com` | Scheduling (repo now shows as cal.diy) | 49,134 | MIT | Calendly Teams | Repo name and homepage changed; recheck the install path |
| `bitwarden/server` | Password manager backend | 20,443 | **Other** (server licence is not plain open source) | Paid password managers | Self-hosting a vault makes you responsible for backups |

Desktop and browser tools (@palidev21):

| Tool | Does | Stars | Licence |
|---|---|---|---|
| `mifi/lossless-cut` | Lossless video/audio trimming (FFmpeg GUI) | 44,925 | GPL-2.0 |
| `alyssaxuu/screenity` | Screen recorder with annotation, no watermark | 18,798 | GPL-3.0 |
| `pdfarranger/pdfarranger` | Merge, split, rotate and reorder PDF pages (Linux GTK) | 5,989 | GPL-3.0 |
| `koodo-reader/koodo-reader` | Ebook reader and library with sync | 28,605 | AGPL-3.0 |
| `karakeep-app/karakeep` | Bookmark-everything app with AI tagging | 29,885 | AGPL-3.0 |

For more PDF work see `repo-stirling-pdf` (94,653 stars, licence shown as Other: open-core). The "10 GitHub repos that feel illegal to use" cover's "$50 billion in corporate revenue" line is not sourced.

Rule: a "free" tool costs hosting, time and risk. AGPL means that offering a modified version over a network obliges you to publish your changes; for internal use, read the licence rather than assuming.


## Batch 115: seven "illegal tools" (@martiendejong_dev-style cards, verified on GitHub, 23 October 2026)

Card stars are older than these figures. "Replaces" is the card's claim; price claims were not verified.

| Repo | Does | Stars | Licence | Card says it replaces | Care |
|---|---|---|---|---|---|
| `D4Vinci/Scrapling` | Adaptive web-scraping framework | 89,078 | BSD-3-Clause | ScrapingBee | Respect site terms, robots and data-protection law; "walks past bot blocks" is a legal and ethical risk, not a feature |
| `OpenBB-finance/OpenBB` (now under `openbq-org`) | Open data platform for analysts, quants and AI agents | 74,567 | Other | A Bloomberg terminal | Data licences of the underlying providers apply |
| `coollabsio/coolify` | Self-hosted PaaS for sites, databases, apps | 63,501 | Apache-2.0 | Vercel, Heroku | You own uptime, security patches and backups |
| `twentyhq/twenty` | Open CRM designed for AI | 59,538 | Other | Salesforce | Read the licence for the enterprise features |
| `myshell-ai/OpenVoice` | Instant voice cloning | 38,037 | MIT | ElevenLabs | Clone only voices you have consent for; check local law on synthetic voice |
| `Fosowl/agenticSeek` | Fully local autonomous agent (browse, code, multi-step) | 27,531 | GPL-3.0 | Manus | Local does not mean safe: an agent that browses and runs code needs a sandbox |
| `documenso/documenso` | Open-source e-signature | 15,516 | AGPL-3.0 | DocuSign | Legal validity of e-signatures depends on the country and document type; keep the audit trail |

Re-check before quoting: star counts change daily. "$50 billion in corporate revenue" style claims on the cover are unsourced.
