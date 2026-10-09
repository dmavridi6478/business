#!/usr/bin/env python3
"""Six key lines from "Machine Learning from Scratch" (part 23), made runnable.

The video shows six one-line fragments. They use names the video never defines
(grow, rng, d, C, X, t, f, i, sig), so this file supplies the smallest honest
context for each line and checks that it learns something. The line from the
video is marked "VIDEO LINE" in each section. Requires only numpy.

Run: python3 scripts/ml_six_key_lines.py
"""
import numpy as np

rng = np.random.default_rng(7)


def sig(z):
    return 1 / (1 + np.exp(-z))


def gini(y):
    p = y.mean() if len(y) else 0.0
    return 2 * p * (1 - p)


# Shared toy data: 400 applicants, 2 features (income, missed payments), label 1 = repays.
X = rng.normal(size=(400, 2))
y = (X[:, 0] - X[:, 1] + rng.normal(scale=0.5, size=400) > 0).astype(float)


def best_split(Xs, ys, thresholds=24):
    """Part 18: try cuts on every feature; keep the lowest weighted gini."""
    best = (np.inf, 0, 0.0)
    for f in range(Xs.shape[1]):
        for t in np.quantile(Xs[:, f], np.linspace(0.05, 0.95, thresholds)):
            L = Xs[:, f] > t  # VIDEO LINE 4 (L = X[i, f] > t): "answer is yes"
            score = (L.sum() * gini(ys[L]) + (~L).sum() * gini(ys[~L])) / len(ys)
            if score < best[0]:
                best = (score, f, t)
    return best


# --- Part 1: linear regression -------------------------------------------------
x1 = rng.uniform(0, 10, 100)
t1 = 2.5 * x1 + 1 + rng.normal(scale=0.5, size=100)
w, b = 0.0, 0.0
for _ in range(1000):  # the video's "guess, error, nudge, repeat" loop
    pred = w * x1 + b  # VIDEO LINE 2
    err = pred - t1
    w -= 0.01 * (err * x1).mean()
    b -= 0.01 * err.mean()
print(f"1 linear regression : w={w:.2f} b={b:.2f} (true 2.5 and 1.0)")
assert abs(w - 2.5) < 0.2 and abs(b - 1.0) < 0.8

# --- Part 18: decision tree (a single yes/no question, i.e. a stump) -------------
score, f, t = best_split(X, y)
L = X[:, f] > t
yes_label, no_label = y[L].mean() >= 0.5, y[~L].mean() >= 0.5  # each side votes its majority class
acc_tree = (np.where(L, yes_label, no_label) == (y == 1)).mean()
print(f"2 decision tree     : ask 'feature {f} > {t:.2f}' -> accuracy {acc_tree:.2f}")
assert acc_tree > 0.6


# --- Part 20: random forest -------------------------------------------------------
def grow(idx):
    """Grow one stump on the bootstrap sample idx; return a row -> vote function."""
    _, f_, t_ = best_split(X[idx], y[idx])
    sides = [y[idx][X[idx][:, f_] > t_].mean(), y[idx][X[idx][:, f_] <= t_].mean()]
    hi, lo = sides[0] >= 0.5, sides[1] >= 0.5
    return lambda row: float(hi if row[f_] > t_ else lo)


# VIDEO LINE 6-7: 100 trees, each trained on rng.choice(400, 400) (sampling with replacement)
V = np.sum([[*map(grow(rng.choice(400, 400)), X)] for _ in range(100)], 0)
acc_forest = ((V >= 50) == (y == 1)).mean()
print(f"3 random forest     : 100 stumps, majority vote -> accuracy {acc_forest:.2f}")
assert acc_forest > 0.6

# --- Part 22: gradient boosting ---------------------------------------------------
p = np.full(400, y.mean())
for k in range(200):
    r = y - p  # what the ensemble still gets wrong
    _, f_, t_ = best_split(X, r, thresholds=12)  # a stump fitted to the residuals
    L = X[:, f_] > t_
    step = np.where(L, r[L].mean() if L.any() else 0, r[~L].mean() if (~L).any() else 0)
    p += 0.01 * step  # VIDEO LINE 9 (p += .01 * grow()): grow() = the fitted stump's output
acc_boost = ((p > 0.5) == (y == 1)).mean()
print(f"4 gradient boosting : 200 rounds at 0.01 -> accuracy {acc_boost:.2f}")
assert acc_boost > 0.6

# --- Part 17: k-means -------------------------------------------------------------
blobs = np.vstack([rng.normal(c, 0.4, size=(100, 2)) for c in ([0, 0], [4, 4], [0, 5])])
k = 3
best_inertia, C = np.inf, None
for _ in range(10):  # one run can land in a local minimum (two centres in one blob), so restart
    Ck = blobs[rng.choice(len(blobs), k, replace=False)]
    for _ in range(9):
        d = np.linalg.norm(blobs[:, None] - Ck[None], axis=2)
        g = d.argmin(1)  # VIDEO LINE 11: nearest centre
        for j in range(k):
            if (g == j).any():
                Ck[j] = blobs[g == j].mean(0)  # VIDEO LINE 12: move centre to its group's mean
    inertia = (np.linalg.norm(blobs[:, None] - Ck[None], axis=2).min(1) ** 2).sum()
    if inertia < best_inertia:
        best_inertia, C = inertia, Ck.copy()
print(f"5 k-means           : centres {np.round(C[np.argsort(C[:, 0])], 1).tolist()}")
assert all(min(np.linalg.norm(C - c, axis=1)) < 0.5 for c in ([0, 0], [4, 4], [0, 5]))

# --- Part 3: neural network (2 inputs, 2 hidden neurons, 1 output = 9 weights) ----
X4 = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], float)
t4 = np.array([0, 1, 1, 0.0])  # XOR: not solvable without the hidden layer
x0, x1_ = X4[:, 0], X4[:, 1]
w = rng.normal(size=9)
for _ in range(20000):
    a = sig(w[0] * x0 + w[1] * x1_ + w[2])  # VIDEO LINE 14
    bb = sig(w[3] * x0 + w[4] * x1_ + w[5])  # VIDEO LINE 15
    pp = sig(w[6] * a + w[7] * bb + w[8])  # VIDEO LINE 16
    dp = (pp - t4) * pp * (1 - pp)
    da, db = dp * w[6] * a * (1 - a), dp * w[7] * bb * (1 - bb)
    w -= 2.0 * np.array([(da * x0).sum(), (da * x1_).sum(), da.sum(),
                         (db * x0).sum(), (db * x1_).sum(), db.sum(),
                         (dp * a).sum(), (dp * bb).sum(), dp.sum()])
print(f"6 neural network    : XOR outputs {np.round(pp, 2).tolist()} (target 0 1 1 0)")
assert ((pp > 0.5) == (t4 == 1)).all(), "stuck in a local minimum; change the seed"
print("all six checks passed")
