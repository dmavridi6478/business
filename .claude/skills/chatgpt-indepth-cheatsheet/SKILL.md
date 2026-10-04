---
name: chatgpt-indepth-cheatsheet
description: Text version of a one-page "ChatGPT In-Depth Cheatsheet" image (extensions, GPT Store, role playing, writing styles, prompting techniques, temperature control, terminology, an AI overview, best tool categories, alternatives) with errata - where the sheet is loose or misleading, such as temperature values that are API settings rather than ChatGPT app controls. Use when someone wants a quick prompt-technique reference, role and writing-style lists, or a plain definition of terms such as token, training and prompt engineering. Different from chatgpt-astra-cheatsheet.
---

# ChatGPT In-Depth Cheatsheet (transcribed, with corrections)

Source: one infographic image (file `IMG_6505`), labelled "Power User Reference". It reads like generated artwork: a stray colour code (`#F4C430`) is printed over the Jailbreaks box. Treat it as a memory aid, not documentation. No specific product version is claimed.

| Section | Contents on the sheet |
|---|---|
| Extensions | Browsing and web retrieval; summarisation; prompt management and libraries; document interaction (PDF, docs, notes); workflow automation and integrations; data extraction and structured outputs. Tip: use extensions to reduce context overhead |
| GPT Store | Task-specific assistants; research and productivity GPTs; file and PDF GPTs; writing and editing specialists; coding and debugging helpers. "Specialisation over general use" |
| Role playing | Ethical hacker, negotiation coach, startup mentor, productivity strategist, academic tutor, marketing advisor, software assistant, creative writer. "Role = perspective + constraints, so better outputs" |
| Writing styles | Analytical, Executive, Technical, Instructional, Conversational, Storytelling, Peer-to-peer; plus a tone/formality slider |
| Prompting techniques | Goal-oriented prompting (marked "Pro"), constraint framing, scenario comparison, guided brainstorming, step-by-step reasoning, reverse prompting, success-criteria definition |
| Temperature control | High 1.1 (exploratory, idea generation), Medium 0.7 (balanced), Low 0.2 (deterministic, factual, concise) |
| Terminology | Input, Output, Large Language Model, Generative AI, Training, Tokens (chunks of text that affect limits and cost), Prompt Engineering |
| AI overview | Nested circles: AI, machine learning, neural networks, deep learning; around them natural language processing, computer vision, reinforcement learning, decision systems, generative models; "Future / AGI" |
| Jailbreaks (conceptual awareness) | Role-based overrides, persona simulation, narrative framing, instruction-hierarchy awareness. Footer: "Educational context, not instructions" |
| Best AI tools | Search and research, presentation creation, content generation, image and media tools |
| Alternatives | Open-source models (Llama, Falcon, Mistral); research-focused models (Claude, Gemini); lightweight inference models (TinyLlama, Phi) |

## Errata and cautions

- **Temperature values are API parameters.** The ChatGPT app does not expose a temperature slider to ordinary users, as far as I know; the 1.1 / 0.7 / 0.2 figures apply where an API or playground lets you set them. Ranges and defaults differ by model. [Likely]
- **The "Alternatives" row mixes categories.** Naming Claude and Gemini "research-focused" is a loose label, not a defined class.
- **The Jailbreaks box is awareness only.** It lists concept names, not methods. Defensive reading: anything in a prompt that tries to override instructions, adopt a persona to bypass rules, or hide a request inside a story should be treated as untrusted input by applications. This skill gives no bypass techniques. [Certain]
- **"Role = perspective + constraints" is sound; "ethical hacker" is a role label, not an authorisation.** Security testing needs permission regardless of persona.
- Extensions and the GPT Store change often; check the current product before relying on a named feature.

## How to use the technique list

Pick one technique per prompt: state the goal and the success criteria first, add constraints (length, format, audience), then ask for step-by-step reasoning only where the task needs it.
