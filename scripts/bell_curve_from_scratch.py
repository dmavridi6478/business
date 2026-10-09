"""Bell curve from scratch - the 16 lines shown in @quantfinancetogo "Quant finance from scratch, part 4" (transcribed from the video).
Simulated numbers only; education, not financial advice. Needs numpy. Run: python scripts/bell_curve_from_scratch.py
"""
import numpy as np
rng = np.random.default_rng(4)  # simulated coin
coin = [1, -1]                            # right or left
steps = rng.choice(coin, (1000, 12))  # 12 rows
rights = (steps == 1).sum(axis=1)  # where it lands
print(np.bincount(rights, minlength=13))  # pile
rng3 = np.random.default_rng(3)  # part 3's walks
walks = rng3.choice(coin, (1000, 400)).cumsum(1)
print(walks[:, -1].std())  # about 20 = sqrt(400)
moves = rng.uniform(-1, 1, (100000, 100))
sums = moves.sum(axis=1)  # 100 moves added
z = abs(sums) / sums.std()  # in standard devs
print(np.mean([z < k for k in (1, 2, 3)], axis=1))
yearly = 0.01 * np.sqrt(252)  # 16 % a year
print(yearly * np.arange(1, 4))  # 16, 32, 48 %
print(1 / (z > 3).mean())  # bell: 1 in 370

# --- checks added by us (not in the video) ---
assert rights.shape == (1000,) and np.bincount(rights, minlength=13).sum() == 1000
assert 17 < walks[:, -1].std() < 23                       # about sqrt(400) = 20
p = np.mean([z < k for k in (1, 2, 3)], axis=1)
assert abs(p[0] - 0.68) < 0.02 and abs(p[1] - 0.954) < 0.01 and p[2] > 0.99  # 68-95-99.7 rule
assert abs(yearly - 0.1587) < 0.001                       # about 16 % a year
# 1 in 370 is the normal-curve answer; with only 100,000 draws the estimate is noisy, so just check order of magnitude
assert 200 < 1 / (z > 3).mean() < 800
print("bell curve checks passed")
