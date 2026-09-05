# Build n8n Workflows with Claude
*Source: @epic8244 on TikTok — "How to Build AI Agents with Claude"*

Use this command to generate a production-ready n8n workflow JSON using Claude as your workflow architect.

---

## Setup (one-time, do this first)

### Step 1 — Open Claude
Open Claude desktop app or claude.ai.

### Step 2 — Open Projects
Click the **Projects** section in the left sidebar.

### Step 3 — Create a new Project
Name it: **"n8n Workflows"**

### Step 4 — Paste these grounding rules into Project Instructions
```
// Grounding rules
Always reference the "n8n-io/n8n" Github repo before building anything.
Never invent nodes or features that don't exist.
```

### Step 5 — Upload sample n8n workflow JSON files
Upload 2–3 real n8n workflow JSON files so Claude learns the exact node format.
- Use existing workflows from your n8n instance (export → JSON)
- Or use examples from https://n8n.io/workflows/
- Recommended: ~250–500 line JSON files (Gmail labeller, Telegram bot, RAG starter)
- Switch model to **Claude Sonnet 4.6** for this project

---

## Usage (per workflow)

Once the project is set up, describe the workflow you want:

### Prompt template:
```
Build me a workflow that [describe what it does].
Requirements:
- Trigger: [webhook / schedule / Gmail / etc.]
- Steps: [list the main steps]
- Output: [where the result goes]
Make it match the JSON format of the example files I uploaded.
```

### Example prompt:
```
Build me a Short Video Automation workflow that:
- Triggers on a schedule (daily)
- Generates a 60-second house-building video concept using an AI image/video node
- Posts the result to YouTube, Facebook, TikTok, and Instagram
Match the exact JSON structure of the example workflows.
```

Claude will return a complete n8n workflow JSON. Copy it → paste it into n8n → Import → Done.

---

## Tips
- Always upload real workflow JSON files — Claude needs them to stay grounded
- If a node doesn't exist in n8n, Claude will tell you (that's the grounding rule working)
- Use Sonnet 4.6 for workflow generation, Haiku 4.5 for quick edits
- Keep the Project loaded so Claude remembers your workflow style across sessions
