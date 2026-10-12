"""Support vector machine in numpy, as shown in @machinelearningtogo "Machine Learning from Scratch, part 29".
Lines 1-16 are the video's code (read from video frames; the video says 2 features, then 3).
Run: python3 svm_from_scratch.py
The made-up stock data is from the video ("made-up example, not advice")."""
import numpy as np; r = np.random.default_rng(29)
def svm(X, y):  # the widest possible gap
    w, b = 0 * X[0], 0.0
    for t in range(1, 50001):
        s = y * (X @ w + b) < 1  # too close
        g = 10 * y[s] / t
        w, b = w - w / t + g @ X[s], b + g.sum()
    return w, b
y = np.tile([-1, 1], 1020)  # 40 to learn, 2000 new
X = r.normal(np.outer(y, [1.6, 1.1, 1]), .6)
for A in X[:, :2], X:  # two features, then three
    w, b = svm(A[:40], y[:40])  # learn from 40
    m = y * (A @ w + b)  # side and distance
    print(2 / (w @ w)**.5)  # width of the gap
    print(np.where(m[:40] < 1.01)[0])  # closest
    print(np.mean(m[40:] > 0))  # new points right
