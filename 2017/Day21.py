from functools import reduce


class S(object):
    def __init__(self, i):
        if isinstance(i, str):
            self.s = tuple(i.split('/'))
        elif hasattr(i, '__iter__'):
            self.s = tuple(map(str, i))

    def I(self):
        return self

    def H(self):
        return S(s[::-1] for s in self.s)

    def V(self):
        return S(self.s[::-1])

    def T(self):
        return S(map(''.join, zip(*self.s)))

    def TV(self):
        return self.T().V()

    def VH(self):
        return self.V().H()

    def VT(self):
        return self.V().T()

    def HVT(self):
        return self.H().V().T()

    def variants(self):
        vars = map(self.__getattribute__, 'I H V T TV VH VT HVT'.split())
        return set(map('/'.join, map(lambda f: f().s, vars)))

    def __add__(self, o):
        return S(map(''.join, zip(self.s, o.s)))

    def __truediv__(self, o):
        return S(self.s + o.s)

    def count(self, c):
        return sum((s.count(c) for s in self.s))

    @classmethod
    def add_all(cls, others):
        return reduce(lambda a, b: a + b, others)

    @classmethod
    def div_all(cls, others):
        return reduce(lambda a, b: a / b, others)

    def __repr__(self):
        return '\n'.join(self.s)

    def __getitem__(self, items):
        return S(self.s[items])

    def vsplit(self, n):
        return list(map(S, zip(*(self[i::n] for i in range(n)))))

    def hsplit(self, n):
        return list(map(S.T, self.T().vsplit(n)))

    def split(self, n):
        return list(map(lambda s: s.hsplit(n), self.vsplit(n)))

    def enhance(self, m):
        n = len(self.s)
        if n in {2, 3}:
            return S(m['/'.join(self.s)])
        elif n % 2 == 0:
            return S.div_all([
                S.add_all([
                    e.enhance(m) for e in row
                ]) for row in self.split(2)
            ])
        elif n % 3 == 0:
            return S.div_all([
                S.add_all([
                    e.enhance(m) for e in row
                ]) for row in self.split(3)
            ])

    def rec(self, n, m):
        if n:
            return self.enhance(m).rec(n - 1, m)
        else:
            return self


inp = open('Day21.txt').read()
inp_ = """../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#"""


def parse(inp):
    idict = dict(line.split(' => ') for line in inp.splitlines())
    m = {}
    for i, v in idict.items():
        for k in S(i).variants():
            if k not in idict:
                m[k] = v
    m.update(idict)
    return m


def Day21(inp, i):
    m = parse(inp)
    start = '.#./..#/###'
    return S(start).rec(i, m).count('#')

assert Day21(inp_, 2) == 12

print(Day21(inp, 5))
print(Day21(inp, 18))

# 139
# 1857134