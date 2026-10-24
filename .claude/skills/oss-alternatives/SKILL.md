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


## Batch 116: 30 repos from six card series (verified on GitHub, 23 October 2026)

Stars and licences were read from each repo page. Card star counts are often far older (for example andrej-karpathy-skills 52K on the card, 222,852 now), so recheck before quoting.

**@blank9485 "5 GitHub projects worth your weekend"**

| Repo | Does | Stars | Licence | Care |
|---|---|---|---|---|
| `open-webui/open-webui` | Chat interface for Ollama and OpenAI-compatible APIs | 156,576 | Other | Custom licence with branding terms; read it before commercial use |
| `karakeep-app/karakeep` | Bookmark-everything with AI tags | 29,885 | AGPL-3.0 | See Batch 114 |
| `louislam/uptime-kuma` | Self-hosted uptime monitor | 92,805 | MIT | Run on an always-on host |
| `CorentinTh/it-tools` | Handy developer tools (JSON, UUID, hashes) | 40,947 | GPL-3.0 | Use sample data in any public instance |
| `docling-project/docling` | Convert PDFs and office files to Markdown or JSON | 69,453 | MIT | Verify extraction on a sample first |

**Site Tusk "5 GitHub projects they don't want you to know about"**

| Repo | Does | Stars | Licence |
|---|---|---|---|
| `vinta/awesome-python` | Curated list of Python frameworks and tools | 329,597 | Other |
| `duckdb/duckdb` | In-process analytical SQL database | 42,451 | MIT |
| `esphome/esphome` | Configure ESP32/ESP8266 devices for home automation | 11,946 | Other |
| `jesseduffield/lazygit` | Terminal UI for git | 83,390 | MIT |
| `dandavison/delta` | Syntax-highlighting pager for git diffs | 32,551 | MIT |

**@palidev21 "5 free tools hiding on GitHub" (Windows upgrades)**

| Repo | Does | Stars | Licence | Care |
|---|---|---|---|---|
| `microsoft/PowerToys` | Window layouts, bulk rename, color picker | 139,612 | MIT | Windows only |
| `obsproject/obs-studio` | Screen recording and live streaming | 77,985 | GPL-2.0 | - |
| `audacity/audacity` | Audio editor | 18,815 | Other | Optional plugins and services may cost extra |
| `kovidgoyal/calibre` | Ebook library manager | 26,221 | GPL-3.0 | Format conversion needs DRM-free files |
| `bleachbit/bleachbit` | System cleaner | 7,222 | GPL-3.0 | Deletes files: preview and review every selection first |

**@replace.so "6 repos" (five named)**

| Repo | Does | Stars | Licence | Card says it replaces |
|---|---|---|---|---|
| `Kilo-Org/kilocode` | Open coding agent for VS Code, JetBrains, CLI | 27,699 | MIT | Paid coding assistants |
| `ubicloud/ubicloud` | Open cloud on bare metal (compute, Postgres, K8s) | 12,331 | AGPL-3.0 | AWS |
| `omnara-ai/omnara` | Self-hostable managed-agent platform | 3,193 | Apache-2.0 | Claude Managed Agents |
| `statamic/cms` | Flat-file Laravel CMS (core package) | 4,911 | Other | Hosted CMS; the Pro edition is paid |
| `ansvisor/ansvisor` | AI search visibility tracking | 159 | MIT | Paid AEO tools; very young, 159 stars |

**@martiendejong_dev "learn" cards: three do not match their repo**

| Repo | Stars | Licence | What the card says | What the repo says |
|---|---|---|---|---|
| `debpalash/VoiceStudio` | 82,715 | AGPL-3.0 | Local voice cloning, dubbing, transcription | Matches (offline ElevenLabs alternative). Clone only voices you have consent for |
| `thedotmack/claude-mem` | 102,396 | Apache-2.0 | A better memory for Claude | Matches (captures sessions, compresses, injects context). Overlaps the Cognee memory already used here |
| `bilawalsidhu/gods-eye-view` | 59,321 | Other | 3D globe of planes, ships, cameras | Matches in spirit; check each data source's terms |
| `paperclipai/paperclip` | 106,518 | MIT | "Turn any document into insights" (chat with documents) | **Mismatch:** "the open-source app to manage agents at work" |
| `multica-ai/andrej-karpathy-skills` | 222,852 | none shown | A learning path of Karpathy's articles, videos and projects | **Mismatch:** a single CLAUDE.md of coding guidelines derived from his LLM-pitfall observations |
| `affaan-m/ECC` | see `github-trending-top10-oct5` | MIT | "Complete computer science curriculum" | **Mismatch:** an agent harness (skills, memory, security), verified in Batch 113 |

The mock screenshots on these cards show features the repos do not describe. [Certain] for the three mismatches above. Always open the repo page and read the README before trusting a card.


## Batch 117 additions: desktop and utility apps (@martiendejong_dev cards)

Stars and licences were read from each repo page in Batch 117 where reachable (exa rate limits hit; unreachable items are marked). [Certain] on what each repo says about itself; [Guessing] on how well each works for you.

| Repo / app | Does | Licence | Care |
|---|---|---|---|
| `LizardByte/Sunshine` | Self-hosted game streaming host for Moonlight clients, 42,575 stars | GPL-3.0 | Opens network ports and handles input from a remote client: use on a trusted LAN or behind a VPN, set a strong PIN |
| `hluk/CopyQ` | Clipboard history manager with scripting, 12,513 stars | GPL-3.0 | A clipboard manager stores everything you copy, including passwords: exclude password managers, encrypt or limit history |
| `ShareX/ShareX` | Screen capture, recording, upload automation (Windows), 40,367 stars | GPL-3.0 | Windows only; check where automatic uploads go |
| `kando-menu/kando` | Circular gesture (pie) launcher menu, 6,511 stars | Other (README is CC-BY-4.0; read the repo licence) | Macros can run arbitrary commands: review any shared menu before importing |
| `imputnet/cobalt` | No-signup media downloader web service, 45,396 stars | AGPL-3.0 | Downloading from platforms can breach their terms of service and copyright; use only for content you may download. AGPL: publishing a modified self-hosted copy carries source obligations |
| `GyulyVGC/sniffnet` | Real-time network traffic monitor, 41,680 stars | Apache-2.0 | Packet capture may need elevated rights; monitor only networks you own or administer |
| `localsend/localsend` | Offline file sharing on the same Wi-Fi, cross-platform, 95,434 stars | Apache-2.0 | Only on trusted networks; confirm the receiving device name before accepting |
| `mifi/lossless-cut` | Lossless video and audio trimming | GPL-2.0 (verified earlier) | Cuts only at keyframes unless you re-encode |
| `rustdesk/rustdesk` | Remote desktop, self-hostable | AGPL-3.0 (verified earlier) | Exposes a remote-control surface: strong permanent password, 2FA where offered, restrict the relay server |
| Steg Cloak | Hides an encrypted message in text with invisible Unicode characters | **Unverified** (repo not located) | Dual-use. Fine for privacy experiments; do not rely on it for secrecy without reading the code, and do not use it to hide data in ways that break an employer's or a platform's rules |

All eight verified repos are alternatives to paid tools only loosely: the cards frame them as "too good to be free". Open licences still carry obligations (GPL and AGPL attribution and source rules if you distribute changes).
