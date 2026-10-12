---
name: ml-svm-part29
description: "Machine Learning from Scratch part 29" (@machinelearningtogo) - a support vector machine in 16 lines of numpy that finds the widest gap between two groups (made-up stock volatility vs past return), learns from 40 points, then sorts 2,000 new points (1,999 right with two features, all right with three), plus the SVR idea (a tolerance band around a line). Includes a runnable script. Use when explaining or demoing SVM, margins, support vectors, or classification versus regression.
---

# SVM from scratch (part 29)

Script: `scripts/svm_from_scratch.py` (the video's code, run and checked here: width 2.51, 99.95% right with two features, 100% with three, closest points 5, 22, 33).

## Idea
- Learn from examples with known answers (supervised: categories or numbers).
- Each stock has two numbers (volatility, past return). The SVM draws the line with the widest empty band between "rise" and "fall"; only the closest points (support vectors) decide the line.
- A new point is classified by which side of the line it falls on.
- Add a third feature and the line becomes a plane; "dimensions = features".
- SVR (support vector regression) is the same idea with a tolerance band around a fitted line: points inside the band cost nothing (21 of 30 inside in the video's example); only points outside pull the line. The video's svr.py was not legible enough to copy exactly, so it is not reproduced.

## How the 16 lines work
Start with zero weights; for 50,000 steps find points too close to the line (`y * (X @ w + b) < 1`), nudge `w` and `b` towards them with a shrinking step (`10 / t`) and a small pull of `w` towards zero (`w - w / t`). Width of the gap = `2 / |w|`.

## Cautions
The data are made up ("not advice"); 40 training points is fine for toy data and unsafe for real markets. For real work use scikit-learn's `SVC` with scaling and a held-out test set (`ml-pipeline-workflow`). Related: `ml-transformer-part31`, `ml-attention-part21`, `quant-bell-curve-part4`, `/attention-demo`.
