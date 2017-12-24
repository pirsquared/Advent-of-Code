inp = open('Day24.txt').read()
tnp = """\
0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10"""

def parse(inp):
    *components, = map(
        tuple,
        (map(int, l.split('/'))
         for l in inp.splitlines())
    )
    return components


def m(c, n, p=0):
    k = lambda n: lambda x: x != n[1]
    a = range(len(c))
    d = [m(c[:i] + c[i+1:], sorted(c[i], key=k(n)), p) for i in a if n[1] in c[i]]
    return [n] + max(d, key=lambda x: [len(x) * p, sum(map(sum, x))]) if d else [n]

def wrap(inp, p=0):
    return sum(map(sum, m(parse(inp), [0, 0], p)))

assert wrap(tnp) == 31
assert wrap(tnp, True) == 19

print(wrap(inp))
print(wrap(inp, 1))

