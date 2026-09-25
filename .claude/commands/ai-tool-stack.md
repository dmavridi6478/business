# /ai-tool-stack

Get a recommended AI tool stack for any use case, role, or workflow — with integration map and implementation order.

## Usage
```
/ai-tool-stack [use case or workflow] [optional: team size, budget, constraints]
```

## Examples
```
/ai-tool-stack content creation pipeline for a solo creator
/ai-tool-stack B2B lead generation and outreach, team of 5, budget $500/mo
/ai-tool-stack internal knowledge base and Q&A bot, small law firm
/ai-tool-stack YouTube channel automation, faceless content, no-code only
/ai-tool-stack customer support automation, e-commerce, Shopify store
```

## What You Get
- Recommended stack across 4 layers (Plan / Build / Execute / Scale)
- Integration map showing how tools connect
- Monthly cost estimate with free tier options
- Implementation sequence (what to set up first)
- One-line rationale per tool
- The single most important tool to start with

$ARGUMENTS

---

## Prompt (executed internally)

Act as an AI productivity systems architect. The user's use case: **$ARGUMENTS**

Design the optimal AI tool stack for this use case. Apply the AI Tool Stacking framework:

```
PLAN layer   → Ideas, projects, tasks, knowledge management
BUILD layer  → Automation platform connecting the tools
EXECUTE layer → AI assistants handling day-to-day work
SCALE layer  → Analytics, monitoring, performance measurement
```

Reference the 12 AI Skills tool universe when selecting:
- Prompt Engineering: ChatGPT, Claude, Gemini, Grok, Perplexity
- Workflow Automation: Zapier, Make, n8n, Bardeen, Notion AI
- AI Agents: CrewAI, LangGraph, AutoGen, LangChain, Claude Agent SDK
- RAG: LlamaIndex, Haystack, Vectara, LangChain
- Staying Updated: Feedly, The Verge, TechCrunch, VentureBeat
- Multimodal AI: Claude, Gemini, Grok, ChatGPT
- Fine-Tuning: OpenAI GPT Builder, HuggingFace, Cohere, Flowise
- Voice AI: ElevenLabs, HeyGen, Synthesia, VAPI
- Tool Stacking: Notion, ClickUp, Asana, Zapier
- AI Video: Runway, VEED, Opus Clip, Sora
- SaaS Dev: Lovable, Cursor, Windsurf, Bubble
- LLM Management: PromptLayer, Helicone, TruLens, Arize AI

**DELIVER:**

### Use Case Summary
One sentence: what this stack is designed to do and for whom.

### Recommended Stack

**PLAN Layer**
| Tool | Role in stack | Free tier? | Paid cost |
|------|--------------|------------|-----------|
| ...  | ...          | ...        | ...       |

**BUILD Layer** (same table format)

**EXECUTE Layer** (same table format)

**SCALE Layer** (same table format)

### Integration Map
Plain-text diagram showing how data flows between tools:
```
[Tool A] → triggers → [Tool B] → feeds → [Tool C] → reports to → [Tool D]
```

### Monthly Cost Estimate
- Minimum (free tiers only): $X/mo
- Recommended setup: $X/mo
- Full stack: $X/mo

### Implementation Sequence
Number the steps from 0 to ready:
1. Start here — the single tool that unlocks everything else
2. Add this next — explain why
3–N. Continue building...

### The One Tool to Start With
Name the single highest-leverage tool for this use case and explain why in 2 sentences. Include the exact URL.

### What to Avoid
List 2–3 common tool choices that look right but add friction for this use case specifically.

Format as a clean, scannable recommendation. Be concrete — name real tools, real costs, real integrations.
