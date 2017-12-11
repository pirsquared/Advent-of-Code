import numpy as np


dd = dict(n=0, ne=1, se=2, s=3, sw=4, nw=5)
moves = list(map(dd.get, open('Day11.txt').read().split(',')))

def cycle2(p):
    p = p.reshape(-1, 3)
    return (p - p.min(0)).ravel()

def cycle3(p):
    p = p.reshape(-1, 2)
    return (p - p.min(0)).ravel()

def mean_dir(p):
    p = p.copy()
    for i in range(6):
        j = (i + 2) % 6
        k = p[[i, j]].min()
        p[[i, j]] -= k
        p[(i + 1) % 6] += k
    return p

def proc(p):
    return mean_dir(cycle2(cycle3(p))).sum()

print(proc(np.bincount(moves)))

print(max(map(proc, np.eye(6, dtype=int)[moves].cumsum(0))))

# 670
# 1426
