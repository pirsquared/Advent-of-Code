from collections import defaultdict
from itertools import islice, count
import numpy as np


def parse(inp):
    return np.array([
        [int(x) for x in line]
        for line in inp.replace('#', '1')
            .replace('.', '0')
            .splitlines()
    ])


def init(a):
    n, m = map(lambda x: x // 2, a.shape)
    state = defaultdict(lambda: 1 + 0j)
    for i, j in zip(*np.where(a)):
        state[i + j * 1j - (n + m * 1j)] = -1 + 0j

    return state


def infect(inp, c, limit):
    s = init(parse(inp))
    p, d, i = 0j, -1 + 0j, 0

    for b in range(limit):
        d *= s[p] * 1j
        s[p] *= c
        i += s[p] == -1 + 0j
        p += d

    return i


inp = open('Day22.txt').read()
tnp = '..#\n#..\n...'

assert infect(tnp, -1, 7) == 5
assert infect(tnp, -1, 70) == 41
assert infect(tnp, -1, 10_000) == 5587
assert infect(tnp, -1j, 100) == 26
assert infect(tnp, -1j, 10_000_000) == 2511944

print(infect(inp, -1, 10_000))
print(infect(inp, -1j, 10_000_000))

# 5411
# 2511416
