"""Gist is to think of hex directions as directions of 3-D"""
# http://keekerdc.com/2011/03/hexagon-grids-coordinate-systems-and-distance-calculations/

import numpy as np


dd = dict(n=0, ne=1, se=2, s=3, sw=4, nw=5)
moves = list(map(dd.get, open('Day11.txt').read().split(',')))

vectors = np.array([
    [ 1,  0, -1],
    [ 1, -1,  0],
    [ 0, -1,  1],
    [-1,  0,  1],
    [-1,  1,  0],
    [ 0,  1, -1]
])

(lambda a: (a[-1], a.max()))(np.abs(vectors[moves].cumsum(0)).max(1))
