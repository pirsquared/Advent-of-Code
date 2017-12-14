s = open('Day14.txt').read()


def twist(a, n):
    return a[:n][::-1] + a[n:]


def skip(a, k):
    return a[k:] + a[:k]


def knot(a, x):
    p = k = 0
    for i in x:
        a = skip(twist(skip(a, p), i), -p)
        p = (p + i + k) % len(a)
        k += 1
    return a


def densehash(a):
    return list(map(
        lambda x: reduce(int.__xor__, x),
        zip(*(a[i::16] for i in range(16)))
    ))


def knothash(x):
    a = list(range(256))
    suffix = [17, 31, 73, 47, 23]
    y = list(map(ord, x)) + suffix
    dh = densehash(knot(a, y * 64))
    return ''.join('{:02x}'.format(n) for n in dh)


def kh(x):
    i = lambda h: int(h, 16)
    b = '{:04b}'.format
    f = lambda h: b(i(h))
    return ''.join(map(f, knothash(x)))


def view(x):
    return kh(x)[:8].replace('1', '#').replace('0', '.')


arr = np.array(list(map(int, ''.join(map(kh, (s + '-' + i for i in map(str, range(128))))))))

print(arr.sum())

a = arr.reshape(128, -1)

seen = set()
available = set((i, j) for i in range(128) for j in range(128))
groups = defaultdict(set)


def path(i, j, g):
    if (i >= 0) and (j >= 0):
        seen.add((i, j))
        available.difference_update([(i, j)])
        if a[i, j] == 1:
            groups[g].add((i, j))
            moves = set([
                (i - 1, j), (i + 1, j),
                (i, j - 1), (i, j + 1)
            ])
            for i, j in (moves & available):
                path(i, j, g)


g = 0
while available:
    i, j = next(iter(available))
    path(i, j, g)
    g += 1

print(len(groups.keys()))

print(
    '\n'.join(map(view, (t + '-{}'.format(i) for i in range(8))))
)