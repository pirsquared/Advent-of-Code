from collections import defaultdict
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
    for y, x in zip(*np.where(a)):
        state[y + x * 1j - (n + m * 1j)] = -1 + 0j

    return state


def infect(inp, change, max_bursts):
    state = init(parse(inp))
    position     =  0 + 0j
    direction    = -1 + 0j
    num_infected =  0
    turn_left    =  0 + 1j
    infected     = -1 + 0j

    for burst in range(max_bursts):
        direction       *= state[position] * turn_left
        state[position] *= change
        num_infected    += state[position] == infected
        position        += direction

    return num_infected


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
