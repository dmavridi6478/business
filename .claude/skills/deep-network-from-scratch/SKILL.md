---
name: deep-network-from-scratch
description: 'A 16-line numpy deep neural network (4 tanh layers, hand-written backpropagation) that separates two interleaved spirals, with a line-by-line explanation and a runnable script verified in this repo (200/200 unseen points, 400/400 training). Use when teaching or learning what a deep network does, why depth bends a space, or what backprop is, without a framework. Source - "Machine Learning From Scratch, Part 25: What Is a Deep Network?" video by @machinelearningtogo.'
---

# What is a deep network? - 16 lines of numpy

**Run it:** `python3 scripts/ml/deep_spirals.py` (needs numpy). Result on this repo's dataset: `200 of 200` on new points, `400 of 400` on training points, ~1.5 s. The video's `spirals` module was not shown, so `scripts/ml/spirals.py` is written here; the network and loop are the video's.

## The idea (as the video builds it)
Two spirals cannot be separated by one straight line (the best line gets about two-thirds right). Stack layers: layer 1 draws straight lines, layer 2 bends them into curves, layer 3 pulls the spirals apart, and the output makes one flat cut. Each layer is `tanh(inputs @ weights)`.

## The code, line by line
| Line | Meaning |
|---|---|
| `X, y, new, truth` | Inputs are `(x, y, 1)` - the constant 1 is a bias; labels are +1 / -1; `new` are unseen test points |
| `shapes = [(3,16),(16,16),(16,3),(3,1)]` | Layer sizes: 3 -> 16 -> 16 -> 3 -> 1 (three hidden layers) |
| `rng.normal(0, s[0]**-.5, s)` | Random start; scale 1/sqrt(fan-in) keeps tanh from saturating |
| `net(x)` | Forward pass; keeps every layer's output `h` because backprop needs them |
| `g = (h[-1]-y) * (1-h[-1]**2)` | Output error times tanh's slope (derivative of tanh is `1 - tanh^2`) |
| `for i in (3,2,1,0)` | Walk backward; `g @ W[i].T * (1-h[i]**2)` sends the error to the previous layer; `W[i] - .002 * h[i].T @ g` updates this layer (learning rate 0.002). The tuple on the right is evaluated first, so the old `W[i]` is used for the error you pass back |
| `print(...)` | Counts new points where prediction and truth have the same sign |

## Caveats
- Full-batch gradient descent, 10,000 steps, no regularisation: fine for a toy, not a recipe. `h[0]` is the raw input, so `(1-h[0]**2)` at `i=0` is meaningless but harmless (that gradient is discarded).
- "200 of 200" depends on the dataset's noise and spacing; with noisier spirals expect fewer. Change the seed in `spirals.py` to see the variance.

## Keywords
deep learning, backpropagation, numpy, tanh, two spirals, machine learning from scratch
