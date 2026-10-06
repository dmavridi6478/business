"""A 4-layer tanh network that learns two interleaved spirals, in 16 lines of numpy.

Recreated from the "Machine Learning From Scratch, Part 25: What is a Deep Network?" video (@machinelearningtogo).
The network and training loop below are the video's code, typed from a screenshot; `spirals.py` is written here.
Run:  python3 scripts/ml/deep_spirals.py
"""
import numpy as np
from spirals import X, y, new, truth  # x, y, 1
rng = np.random.default_rng(25)
shapes = [(3, 16), (16, 16), (16, 3), (3, 1)]
W = [rng.normal(0, s[0]**-.5, s) for s in shapes]
def net(x):                       # input to output
    h = [x]
    for w in W: h += [np.tanh(h[-1] @ w)]
    return h
for step in range(10000):
    h = net(X)                    # forward
    g = (h[-1] - y) * (1 - h[-1]**2)  # error
    for i in (3, 2, 1, 0):        # backward
        g, W[i] = (g @ W[i].T * (1 - h[i]**2),
                   W[i] - .002 * h[i].T @ g)
print(f'{(net(new)[-1] * truth > 0).sum()} of {len(new)}')
print(f'train: {(net(X)[-1] * y > 0).sum()} of {len(X)}')
