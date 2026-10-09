"""Attention from scratch - the 16 lines shown in @machinelearningtogo "Machine Learning from Scratch, part 21: Attention" (transcribed from the video).
Made-up features (thing, alive, place, pronoun); Wq/Wk are hand-set so that "it" looks for a living thing. Needs numpy.
Run: python scripts/attention_from_scratch.py
"""
import numpy as np
w = ("the animal didn't cross the street"
     " because it was tired").split()
f = {"animal": [1, 1, 0, 0],    # made-up features:
     "street": [1, 0, 1, 0],    # thing, alive,
     "it":     [0, 0, 0, 1]}    # place, pronoun
X = np.array([f.get(t, [0] * 4) for t in w])
Wq = np.array([[0, 0], [0, 0], [0, 0], [2, 4]])
Wk = np.array([[1, 0], [0, 1], [0, 0], [0, 0]])
Wv = np.eye(4)
Q, K, V = X @ Wq, X @ Wk, X @ Wv
S = Q @ K.T / np.sqrt(2)  # scaled dot products
A = np.exp(S) / np.exp(S).sum(1, keepdims=True)
new = A @ V               # weighted sum
for t, a in zip(w, A[7]): print(t, a.round(2))
print("it now:", new[7].round(2))

# --- checks added by us (not in the video) ---
assert len(w) == 10 and w[7] == "it"
assert np.allclose(A.sum(1), 1)                      # every row of weights adds up to one
top = dict(zip(w, A[7]))
assert top["animal"] > 0.8 and top["street"] < 0.1   # video: animal ~85 %, street ~5 %
assert new[7].shape == (4,)
print("attention checks passed")
