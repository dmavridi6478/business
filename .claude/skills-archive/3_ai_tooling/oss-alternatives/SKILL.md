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

## When to Use This Skill

Invoke `/oss-alternatives` when:
- A user asks how to do background removal, audio separation, OCR, video dubbing, or audiobook creation
- Looking to cut SaaS costs
- Need offline/local processing for privacy
