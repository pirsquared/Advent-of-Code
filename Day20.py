import pandas as pd


def Day20(inp):

    s = pd.Series(inp.splitlines())
    data = s.str.extractall('(-?\d+)')[0].unstack().values

    p = data[:, 0:3].astype(int)
    v = data[:, 3:6].astype(int)
    a = data[:, 6:9].astype(int)

    # part 1
    particle = (a ** 2).sum(1).argmin()

    dfp = pd.DataFrame(p.copy())
    dfv = pd.DataFrame(v.copy())
    dfa = pd.DataFrame(a.copy())

    static_count = 0
    n = len(dfp)

    while static_count < 1000:

        dfv += dfa
        dfp += dfv
        dup = dfp.duplicated(keep=False)

        dfa = dfa[~dup]
        dfv = dfv[~dup]
        dfp = dfp[~dup]

        if len(dfp) == n:
            static_count += 1
        else:
            n = len(dfp)
            static_count = 0

    return (particle, n)

print(Day20(open('Day20.txt').read()))

# (258, 707)
