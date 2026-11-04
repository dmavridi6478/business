---
name: unsloth-local-guide
description: Beginner path for running, fine-tuning and exporting open LLMs locally with Unsloth (setup, LoRA fine-tune, local inference, GRPO reasoning training, GGUF export for desktop apps, the Studio web UI), with the errors in the source cards corrected against the Unsloth docs. Use when asked how to run or fine-tune a model on your own machine. Defers to the deeper finetuning skills for method choice.
---

# Unsloth local guide (beginner path)

Source: a six-card carousel by @aigenesis.official (Batch 118: setup, how it works, inference, GRPO, export, Studio). The card code was checked against Unsloth's documentation on 25 October 2026; **one card is wrong** (see "Corrections"). Repo `unslothai/unsloth`: Apache-2.0, 78,530 stars on 25 October 2026 (the card showed 66.8k); its description is now "Local UI to run and train LLMs and diffusion models", so the product has grown past the library the cards describe.

## Path

1. **Set up.** Python 3.9 or higher (check `python --version`), create a virtual environment (`python -m venv unsloth-env`, activate it), `pip install unsloth`, verify with `import unsloth`, optionally `pip install xformers trl accelerate`. Check the current install page for your GPU and OS; install steps and supported Python versions change.
2. **Load a model.** `FastLanguageModel.from_pretrained(model_name=..., max_seq_length=..., load_in_4bit=True)`. Card examples: Llama 3 8B, Mistral 7B, Gemma 7B.
3. **Add LoRA adapters.** `FastLanguageModel.get_peft_model(model, r=16, lora_alpha=16, lora_dropout=0, target_modules=[...])`. LoRA trains a small set of extra parameters, so it needs far less memory than full fine-tuning.
4. **Prepare data** as instruction, input, output pairs (or chat messages) with the model's own chat template.
5. **Train** with `trl`'s `SFTTrainer`. Start with a small subset and a held-out set; look at the loss and at real outputs.
6. **Run inference locally.** `FastLanguageModel.for_inference(model)` enables the faster inference path, then tokenise, `model.generate(**inputs, max_new_tokens=...)`, `tokenizer.decode(..., skip_special_tokens=True)`.
7. **Export for desktop apps.** `model.save_pretrained_gguf("dir", tokenizer, quantization_method="q4_k_m")` (also `q8_0`, `f16`). Load the GGUF in llama.cpp, Ollama or Unsloth Studio.
8. **Optional, reasoning:** GRPO (Group Relative Policy Optimization) samples several answers per prompt, scores them with reward functions you define, and updates the model toward higher-reward answers. It needs verifiable reward functions (correctness, format) to work; "you design the reward" is the hard part.
9. **Optional, no code:** Unsloth Studio, a web UI to chat with, fine-tune and manage open models.

## Corrections to the cards

- The export card shows `from unsloth import export_to_gguf`. [Certain] The documented call is `model.save_pretrained_gguf(directory, tokenizer, quantization_method=...)` (and `push_to_hub_gguf`); the tokenizer is required.
- The cards show tiny placeholder datasets and `trainer.train()` with no hyperparameters. Treat them as shape, not a recipe; use a maintained notebook from the Unsloth docs for your model.
- The card says fine-tuned models run "without paid APIs". True for inference; training still needs a suitable GPU (or a rented one), and base-model licences (Llama, Gemma and others) carry use terms you must read.

## Gotchas from the docs

- A model that works inside Unsloth but gives gibberish, endless or repeated output after export to Ollama or llama.cpp is most often a **chat template or end-of-sequence token mismatch**. Use the same template for training and serving, and check whether the runtime adds an extra start-of-sequence token.
- GGUF export can run out of GPU memory; lower `maximum_memory_usage` (default 0.75 in `save_pretrained`).

## Before you fine-tune (added advice)

- Try prompting, then retrieval, before fine-tuning; fine-tuning teaches style and format, not new facts reliably.
- Build the evaluation set first (see `finetuning-method-selection` and the `llm-finetuning` agents). Without a baseline you cannot tell if training helped.
- Check dataset licences and personal data before training; a fine-tuned model can reproduce training text.
- Save the adapter, the base model name and version, the chat template and the data hash with every run.

## Related

`finetuning-method-selection`, `lora-qlora-recipes`, `grpo-rlvr-training`, `dataset-curation`, `quantized-export`, `vision-sft`, `spark-environment-setup` (DGX Spark). Prompts in `docs/batch-118-prompts.md`.
