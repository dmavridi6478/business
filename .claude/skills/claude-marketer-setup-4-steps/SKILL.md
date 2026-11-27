---
name: claude-marketer-setup-4-steps
description: Four-step setup of Claude for a marketer (identity through custom instructions and a banned-words list, persistent context through one Project per function, reusable playbooks saved as prompt templates, and connectors to Drive, Gmail and a CRM) with what to put in each, a least-privilege connector checklist, and the claims in the source graphic that are unproven. Use when setting up Claude for a marketing role or team.
---

# How to set up Claude for marketers: 4 steps

Source: an infographic by Louis Cho (Batch 121). The header claims: cost $20/month, setup time 4 hours, 4 steps, "12 roles replaced", 100+ MCP apps. [Guessing] "12 roles replaced" and "4 hours" are marketing; no basis is given. Treat the steps as a sensible order of work and measure the time you actually save. Product names and menus change; check Claude's current settings screens.

| Step | Name | What the graphic says | What to do |
|---|---|---|---|
| 1 | Identity (universal instructions) | Set brand, voice and rules once so every conversation inherits them | In Claude's settings, paste custom instructions: who you are, who you serve, tone rules, and a banned-words list |
| 2 | Projects (persistent context) | One Project per function with your real documents | Content, Email and Research Projects, each with only its own files |
| 3 | Skills (reusable playbooks) | Prompt templates that run the same task the same way every time | Save the prompt that produced your best output; reuse it weekly |
| 4 | MCP (connected infrastructure) | Connect Claude to your actual tools | Google Drive, Gmail and Calendar, then your CRM |

## Step 1: Identity
- **Custom instructions** (graphic 1.01): paste brand voice, tone rules and a banned-words list.
- **Brand voice rules** (1.02): who you are, who you serve, what you never say. Claude reads this before every response.
- **Banned words list** (1.03): the example is "Never say: leverage, tapestry, groundbreaking." Keep the list short (ten to twenty words); a long list makes text stilted, and you should also give positive examples of how you do sound.
- Do not paste confidential strategy or personal data into instructions that apply to every chat.

## Step 2: Projects
- **Content project** (2.01): best posts, campaign briefs, copy examples, so Claude writes in your style.
- **Email project** (2.02): sequences, templates and conversion data. One project, one function: never mix contexts.
- **Research project** (2.03): ICP profiles, competitor notes, market data. Output quality follows input quality.
- Upload only documents you are allowed to share with the service, remove personal data, and date each file so outdated material does not steer the output. Projects and some features depend on your plan; check yours.

## Step 3: Reusable playbooks
The graphic calls these "skills" and saves them as project instructions or templates. [Certain] This is not the same as Claude's Skills feature (a SKILL.md package); either works, but a saved prompt is the lightweight version.
- **LinkedIn post skill** (3.01): the prompt that produces your best posts, run weekly.
- **Campaign brief skill** (3.02): input an objective, output a full brief.
- **CX analysis skill** (3.03): feed customer feedback, get journey gaps and recommendations each quarter.
- Version each template, note what it needs as input, and review the first five outputs by hand.

## Step 4: Connectors (MCP)
- **Google Drive** (4.01): point at campaign folders; analyse results; draft the next brief.
- **Gmail and Calendar** (4.02): read threads, draft replies, flag what needs attention. Drafts only; you send.
- **CRM** (4.03): the graphic says 100+ connectors exist (Slack, Notion, HubSpot, Salesforce) and "the connections are the moat."
- **Least privilege:** connect read-only first, scope to one folder or one inbox label, review what each connector can write or send, and remove connectors you do not use. Every connector gives an AI service access to company data; get your security or legal team's approval for customer data.

## Build order (added)
1. Write the instruction block and test it on five tasks. 2. Create one Project (the function you use most) and measure for two weeks. 3. Turn the three most repeated prompts into templates. 4. Add one connector, read-only.

Run with `/claude-marketer-setup <your role, brand voice, tools>`. Related: `claude-18-setup`, `claude-cowork-setup`, `brand-voice`, `claude-marketing-50-verbs`, `claude-code-marketing-team`, `connector-starter-stacks`, `protect-mcp-setup`, `claude-5-official-skills`.
