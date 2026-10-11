"""Part 31 'Transformer: attention, layer by layer' (@machinelearningtogo), lines 1-16 as shown on screen.
The video imports `train, test, words, pets` from a module called `pets` that is not shown, so make_pets() below
builds a small stand-in with the same shape. Lines marked VIDEO are transcribed from the final frame (low-res: verify against the video).
Run: python attention_train_from_scratch.py   (needs numpy)
"""
import numpy as np

def make_pets():
    pets = ["cat", "dog", "bird", "fish", "frog", "mouse", "horse", "goat"]      # 8 pets -> y in 0..7
    objs = ["milk", "bone", "seed", "water", "fly", "cheese", "hay", "grass"]
    verbs = ["drank", "ate", "found", "took"]
    adjs = ["thirsty", "hungry", "tired", "happy"]
    words = ["the", "because", "it", "was"] + pets + objs + verbs + adjs
    rng = np.random.default_rng(0)
    data = []
    for _ in range(400):
        p = rng.integers(8); o = rng.integers(8)
        s = ["the", pets[p], verbs[rng.integers(4)], "the", objs[o], "because", "it", "was", adjs[rng.integers(4)]]
        data.append((s, int(p)))                      # y: which pet "it" means
    return data[:200], data[200:], words, pets

train, test, words, pets = make_pets()               # stands in for: from pets import train, test, words, pets

# ---- VIDEO lines 1-16 ----
r = np.random.default_rng(31)                                                      # 1  (numpy imported above)
Wq, Wk, Wv = r.normal(0, .1, (3, len(words), 8))                                   # 3
def look(s):  # how much "it" looks at each word                                    # 4
    i = [words.index(w) for w in s]                                                # 5
    q = Wq[i[s.index('it')]]  # the query of "it"                                  # 6
    a = np.exp(Wk[i] @ q); return i, q, a / a.sum()                                # 7
for s, y in train * 40:  # y: the pet "it" means                                    # 8
    i, q, a = look(s); K, V = Wk[i], Wv[i]                                         # 9
    p = np.exp(a @ V); p /= p.sum(); p[y] -= 1                                      # 10
    g = a * (V @ p - a @ V @ p)  # backpropagation                                  # 11
    np.add.at(Wv, i, -np.outer(a, p))  # values                                    # 12
    np.add.at(Wk, i, -np.outer(g, q))  # keys                                      # 13
    Wq[i[s.index('it')]] -= K.T @ g  # query                                        # 14
w = [look(s)[2][s.index(pets[y])] for s, y in test]                                 # 15
print(f'{np.mean(w):.0%} on the right word')                                        # 16
assert np.mean(w) > 0.5, "attention on the right pet should rise well above chance (about 11%)"
