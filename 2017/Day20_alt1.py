import pandas as pd
import numpy as np


def Day20(inp):
    """this alternate approach evaluates pairwise acceleration.
    once pairwise acceleration is positive relative to all others,
    we can consider particle clear from any future collisions.
    """
    s = pd.Series(inp.splitlines())
    data = s.str.extractall('(-?\d+)')[0].unstack().values

    d = data.astype(int).reshape(-1, 3, 3)[:, ::-1]
    particle = np.abs(d[:, 0]).sum(1).argmin()

    static_count = 0
    n = len(dfp)

    distance_matrix = lambda p: np.abs(p - p[:, None]).sum(2)
    accelation_matrix = lambda p: np.diff(p, n=2, axis=0)
    non_dups = lambda p: (lambda u, i, c: i[c == 1])(
        *np.unique(p, return_index=True, return_counts=True, axis=0)
    )

    dis = np.abs(distance_matrix(d[:, 2]))
    p = np.stack([dis, dis, dis])

    counter = 0
    n = 0

    while d.size:
        keep = non_dups(d[:, 2])
        p = p[:, keep][..., keep]

        d = d[keep].cumsum(1)

        p = np.stack([p[1], p[2], distance_matrix(d[:, 2])])

        a = accelation_matrix(p)[0]

        if counter > 0:
            pos_acc = (a >= 0).all(1)
            n += np.count_nonzero(pos_acc)
            p = p[:, ~pos_acc][..., ~pos_acc]
            d = d[~pos_acc]

        counter += 1

    return (particle, n)


print(Day20(open('Day20.txt').read()))
