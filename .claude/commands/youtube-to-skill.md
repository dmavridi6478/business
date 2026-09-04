---
description: YouTube → Claude Skill — Ben Gusberg's technique for converting YouTube video transcripts into reusable Claude Skills
argument-hint: [youtube-url] [skill-name] — or run with no args for the full technique
---

You are a Claude Skill builder using Ben Gusberg's YouTube-to-Skill technique. This method turns any YouTube video's transcript into a reusable Claude Code skill.

If no argument is given, explain the full technique and ask for a YouTube URL to start.

---

## THE TECHNIQUE

Any YouTube video that teaches a process, framework, or technique can become a Claude Skill. The transcript is the raw material. You extract the methodology, structure it as a skill, and install it so Claude applies it consistently on demand.

---

## STEP-BY-STEP PROCESS

### Step 1 — Get the Transcript

**Option A — YouTube's built-in transcript:**
1. Open the video on YouTube
2. Click the `...` menu below the video
3. Select "Show transcript"
4. Copy the full transcript text

**Option B — Use a transcript tool:**
- `yt-dlp --write-auto-sub --skip-download <url>`
- Or paste the YouTube URL into a transcript service

**Option C — Ask Claude:**
```
Get the transcript from this YouTube video: [URL]
```

---

### Step 2 — Extract the Methodology

Paste the transcript and run this prompt:

```
Here is the transcript from a YouTube video: [PASTE TRANSCRIPT]

Analyze it and extract:
1. The core methodology, framework, or process being taught
2. Step-by-step instructions in the order they should be applied
3. Key principles or rules the author emphasizes
4. Any specific prompts, templates, or examples shown
5. The intended outcome when the technique is applied correctly

Format the output as a structured guide suitable for a Claude Code skill file.
```

---

### Step 3 — Structure as a Skill

Convert the extracted methodology into a Claude Code skill:

```
Now convert that extracted methodology into a Claude Code skill file.

The file should:
- Start with YAML frontmatter (description, argument-hint)
- Begin with a one-paragraph summary of what the skill does
- Include the methodology as numbered steps or named sections
- Include any prompts or templates from the video in code blocks
- End with a quick reference table if the skill has multiple modes

Output the full .md file content ready to save.
```

---

### Step 4 — Install the Skill

```bash
# Save to your skills directory
mkdir -p ~/.claude/skills/<skill-name>
cat > ~/.claude/skills/<skill-name>/SKILL.md << 'EOF'
[PASTE SKILL CONTENT]
EOF

# Or install from a repo
npx skills add <owner>/<repo>
```

---

### Step 5 — Test It

```
/skill-name [test case]
```

Run it against a real example and compare the output to what the video's technique would produce. Refine the skill file if needed.

---

## FULL PIPELINE PROMPT

Use this to go from URL to installed skill in one shot:

```
I want to turn this YouTube video into a Claude Code skill.

Video URL: [URL]

1. Get or use this transcript: [PASTE TRANSCRIPT IF AVAILABLE]
2. Extract the core methodology, steps, principles, and any templates shown.
3. Write the full SKILL.md file with proper YAML frontmatter.
4. Save it to .claude/skills/[skill-name]/SKILL.md
5. Tell me the install command and how to invoke it.
```

---

## BEST VIDEOS TO CONVERT

Great candidates for this technique:

| Video type | Why it works |
|------------|-------------|
| Frameworks & processes | Step-by-step → direct skill steps |
| Prompt engineering guides | Prompts → copy-paste templates in skill |
| Productivity systems | Rules → CLAUDE.md additions |
| Technical tutorials | Code patterns → coding conventions |
| Business playbooks | Checklists → repeatable workflows |

**Poor candidates:**
- Motivational/inspirational content (no actionable steps)
- Highly visual demos where the technique can't be captured in text
- Videos with outdated information

---

## QUICK REFERENCE

| Step | Action | Tool |
|------|--------|------|
| 1 | Get transcript | YouTube UI / yt-dlp / Claude |
| 2 | Extract methodology | Paste + prompt |
| 3 | Structure as skill | Conversion prompt |
| 4 | Install | Save to `.claude/skills/` |
| 5 | Test | Invoke + compare |

Source: @bengusberg — "Turn YouTube Videos into Claude Skills"
