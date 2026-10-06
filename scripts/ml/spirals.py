"""Two-spirals dataset for deep_spirals.py. Written for this repo; the video's own `spirals` module was not shown.

X has 3 columns (x, y, 1) - the constant 1 is a bias input. y is +1 / -1. `new`/`truth` are fresh points not used in training.
"""
import numpy as np


def _spiral(rng, n, noise):
    t = np.sqrt(rng.uniform(0.05, 1.0, n)) * 3 * np.pi          # radius grows with angle
    pts = []
    for sign in (1, -1):                                        # second arm is the first rotated by pi
        a = t + (0 if sign == 1 else np.pi)
        r = t / (3 * np.pi)
        pts.append(np.c_[r * np.cos(a), r * np.sin(a)] + rng.normal(0, noise, (n, 2)))
    X = np.vstack(pts)
    y = np.r_[np.ones(n), -np.ones(n)]
    return X, y


_rng = np.random.default_rng(7)
_X, y = _spiral(_rng, 200, 0.02)
X = np.c_[_X, np.ones(len(_X))]
y = y.reshape(-1, 1)
_Xn, _yn = _spiral(_rng, 100, 0.02)
new = np.c_[_Xn, np.ones(len(_Xn))]
truth = _yn.reshape(-1, 1)
