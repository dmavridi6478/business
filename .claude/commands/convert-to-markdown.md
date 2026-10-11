---
description: Convert a document or link to clean Markdown (markitdown or the pdf-to-markdown skill) and check headings and tables
argument-hint: <file path or URL>
---

Use skill `your-aimentor-5-repos-week`. For "$ARGUMENTS": if it is a PDF use skill `pdf-to-markdown`; otherwise run `markitdown <file> -o <name>.md` if installed (`pip install 'markitdown[all]'`, Python 3.10-3.13; scanned images need markitdown-ocr). Work on a copy. Report what converted, check headings and tables, and list anything lost (images, formulas, scans). Do not upload private files to online converters.
