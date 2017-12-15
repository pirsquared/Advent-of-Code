import numpy as np


# Day 2, Problem 1
def day2_1(s):
    return sum(
        l[-1] - l[0] for l in
        map(sorted, (map(int, x.split()) for x in s.split('\n')))
    )


# Day 2, Problem 2
# This is crappy brute force.  I'm thinking of something better.
def day2_2(s):
    return sum(
        list(i // j for i in l for j in l if i // j == i / j and i != j)[0]
        for l in (list(map(int, x.split())) for x in s.split('\n'))
    )


# Brute force Numpy edition
def day2_2v2(s):
    a = np.array([x.split() for x in s.split('\n')], dtype=int)
    b = a[:, :, None] // a[:, None]
    c = a[:, :, None] % a[:, None] == 0
    i, j, k = np.where(c & (b != 1))
    return b[i, j, k].sum()
