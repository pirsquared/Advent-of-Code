import numpy as np
from itertools import islice, count


def alt_dirs(d):
    s = d.sum()
    return [d - s, s - d]


def in_bounds(a, p):
    i, j = p
    return (0 <= i < a.shape[0]) and (0 <= j < a.shape[1])


def new_p(p, d):
    return tuple(d + p)


def dcond(d):
    b = np.array(list('|-'), object)
    return np.abs(d).dot(b)


def move(inp):
    a = np.array([list(line) for line in inp.splitlines()])

    p = (0, (a[0] == '|').argmax())
    d = np.array([1, 0])

    seen = []

    for k in islice(count(), 0, None):

        v = a[p]
        if v in ascii_uppercase:
            seen.append(v)

        elif v == '+':
            for d_ in alt_dirs(d):
                p_ = new_p(p, d_)

                if in_bounds(a, p_):
                    v_ = a[p_]
                    c_ = dcond(d_)
                    if (v_ == c_) or (v_ in ascii_uppercase):
                        d = d_

        elif v not in (ascii_uppercase + '|-'):
            return ''.join(seen), k

        p = new_p(p, d)


test = """     |          
     |  +--+    
     A  |  C    
 F---|--|-E---+ 
     |  |  |  D 
     +B-+  +--+ 
"""

assert move(test) == ('ABCDEF', 38)

print(*move(open('Day19.txt').read()), sep='\n')

# RUEDAHWKSM
# 17264
