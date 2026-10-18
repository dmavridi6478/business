---
name: colibri-moe-laptop-inference-notes
description: Notes on the @epic8244 carousel "744B on your laptop" about JustVugg/colibri (Apache-2.0, pure C engine that runs Mixture-of-Experts models by streaming experts from disk), with the slide claims, what the README confirms, what remains unverified (speed, disk size) and cautions before running it. Use when assessing local inference of very large models. Nothing was cloned or run.
---

# colibri, "744B on your laptop" (@epic8244 carousel, 6 slides)

Source: dark terminal-style slides (cover "744B on your laptop", "up to 2.8T", "stream from disk", "clone + build", "tiny engine"). The terminal windows and decorative photos on the slides are staged graphics, not captures of real runs. Repo checked on 18 October 2026.

| Slide claim | What I could confirm |
|---|---|
| Repo JustVugg/colibri, 37.8k stars, Apache 2.0, pure C, zero dependencies | Repo exists and its LICENSE is Apache-2.0. Stars not checked |
| Runs 744B GLM-5.2 on a laptop | The README shows `colibri v2.0.0 · GLM-5.2 · 744B MoE · int4 · streaming CPU`, "ready in 32s · resident 9.9 GB" |
| "up to 2.8T" (Kimi K3), nine model families, "as little as 8 to 16GB of RAM" | The README lists more engines than the slide (ten language-model engines plus an image model and decision models); the RAM floor is the slide's claim |
| "It treats disk, RAM and VRAM as one pool and streams routed experts from disk" | This is the README's own description |
| Tokens per second | **Not stated reliably.** The slide's throughput numbers sit in a staged graphic. Streaming experts from disk is bound by SSD speed, so expect far slower than a model that fits in memory |

## Read critically
- **[Certain]** Model weights of this size still need hundreds of gigabytes (quantised) of free disk. "On your laptop" means "with a very large fast SSD", not "with 16 GB of disk".
- **[Likely]** Speed will be usable for experiments, not for production chat; measure tokens per second yourself before planning around it.
- **[Likely]** Check each model's own licence; the engine's Apache-2.0 does not cover the weights.
- Read the README and build script before running anything; nothing was cloned or built here. Compare with `claude-token-rules-22` and `free-llm-api-providers-13` for cheaper routes.
