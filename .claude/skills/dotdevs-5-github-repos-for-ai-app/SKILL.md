---
name: dotdevs-5-github-repos-for-ai-app
description: The @dotdevs "5 GitHub repos for your next AI app" carousel (Vercel AI SDK, Mastra, Browser Use, Open WebUI, Unsloth) with each repo one-line promise, licences read from LICENSE files on 18 October 2026 (Open WebUI is a custom licence with a branding clause), and cautions. Use when choosing a stack for an AI app.
---

# 5 GitHub repos for your next AI app (@dotdevs)

Source: 7 slides (cover, five repo cards, a save slide). Stars on the cards are the author's and unverified. Licences read from each repo's root LICENSE file on 18 October 2026.

| # | Repo | Slide promise | Licence | Note |
|---|---|---|---|---|
| 1 | vercel/ai (Vercel AI SDK) | "stream AI answers into any UI" (card: 27k stars) | Apache-2.0 | TypeScript toolkit; works with many model providers |
| 2 | mastra-ai/mastra | "build AI agents in TypeScript" (29k stars) | Apache-2.0 (LICENSE.md) | Agent framework; check which parts sit outside the core licence |
| 3 | browser-use/browser-use | "let an agent click through websites" | MIT | Browser agents act on real sites; they can submit forms and spend money. See `browser-use-to-stagehand` |
| 4 | open-webui/open-webui | "a chat interface for any model" (154k stars) | **Custom "Open WebUI License"**, a BSD-3-style text; read the branding clause before rebranding or reselling | Not OSI-standard; do not assume it is MIT |
| 5 | unslothai/unsloth | "fine-tune models on smaller GPUs" (78k stars) | Apache-2.0 | Fine-tuning needs a GPU and a clean dataset; see `finetuning-method-selection` |

## Read critically
- **[Certain]** Browser Use is the only one that can take real-world actions; give it a sandboxed account and a spending limit.
- **[Certain]** Open WebUI's licence is not plain MIT; read the file.
- **[Likely]** Mastra and the AI SDK overlap (both TypeScript agent tooling); pick one rather than stacking them.
- Nothing was cloned or installed. Related here: `ai-app-stack-2026`, `lean-software-stack`.
