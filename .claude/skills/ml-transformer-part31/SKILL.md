---
name: ml-transformer-part31
description: The "Transformer: attention, layer by layer" video, Machine Learning from Scratch part 31 (@machinelearningtogo) - the 16-line numpy script that LEARNS attention (query, key and value matrices trained by hand-written backpropagation to find which pet "it" means), transcribed from the final frame, made runnable with a stand-in dataset, with a line-by-line explanation and the video's steps (tokens, 8-number embeddings, position, every word asks, information flows in, "it looks back", query/key/value). Use to learn or teach how attention is trained, or as the trained companion to ml-attention-part21 (which uses hand-set matrices).
---

# Transformer attention, trained (part 31)

Source: a 127-second video, frames only (no audio). **Confidence: medium** for the code (final frame, low resolution; line 14's trailing comment is hidden by the watermark), high for the storyline. The video's `pets` module (`train, test, words, pets`) is not shown, so `scripts/attention_train_from_scratch.py` builds a stand-in dataset of sentences like "the cat drank the milk because it was thirsty". Run: `python scripts/attention_train_from_scratch.py` (needs numpy).

Part 21 (`ml-attention-part21`) shows attention with hand-set matrices. This part shows how the matrices are **learned**.

## Video storyline (frame order)
1. All words at once: every word sees every other word. 2. Google, 2017: translation ("the cat drank the milk" to French). 3. Tokens (words split into pieces). 4. Every token becomes a list of 8 numbers (an embedding; "our keys"). 5. Real models add the position of each word. 6. Every word asks, and "it" asks which word it refers to. 7. The information flows in: "it" mixes in the information of "cat". 8. "It looks back" (a causal view: a word attends only to earlier words). 9. Query, key, value as real numbers: the query of "it" (what am I looking for?), the key of "cat" (what do I contain?), and the value of "cat" (what it hands over).

## The 16 lines
| Lines | What it does |
|---|---|
| 1 | numpy and a seeded generator |
| 2 | load sentences (`train`, `test`), vocabulary `words`, the 8 candidate `pets` |
| 3 | three random matrices Wq, Wk, Wv, one 8-number row per vocabulary word |
| 4 to 7 | `look(s)`: take the query of "it", score it against the key of every word (`Wk[i] @ q`), softmax into weights `a` that sum to 1 |
| 8 | train: 40 passes over the training sentences; `y` is which pet "it" means |
| 9 | attention weights, keys K and values V of this sentence |
| 10 | the answer is the weighted mix of values (`a @ V`) turned into probabilities `p`; subtract 1 at the right pet to get the error |
| 11 | back through the softmax to get the gradient `g` on the attention scores |
| 12 to 14 | nudge values (12), keys (13) and the query of "it" (14) downhill |
| 15 to 16 | on unseen sentences, how much attention "it" puts on the right pet word |

## Result [Certain for the stand-in data]
The stand-in task is easy (the pet is always the second word, objects never repeat pets), so the script reaches about 100% attention on the right pet; chance is about 11% (one in nine content words). The video's own number is not legible; do not quote 100% as the video's result.

## Teaching notes
- Query = what I look for, key = what I offer, value = what I hand over. Training makes the query of "it" match the keys of pets and not objects.
- Real models use many heads, hundreds of dimensions, positions and a causal mask, and train on billions of words, not 200 sentences.
- Related: `ml-attention-part21`, `ml-six-key-lines`, `quant-bell-curve-part4`, design template `quant-code-pane-dark`. Command: `/attention-demo`.
