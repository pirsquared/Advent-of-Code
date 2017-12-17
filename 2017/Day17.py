def step_insert(step, n):
    a = [0]
    p = 0

    for value in range(1, n + 1):
        p = (p + step) % len(a) + 1
        a = a[:p] + [value] + a[p:]

    return a[a.index(n) + 1]


assert step_insert(3, 2017) == 638
print(step_insert(355, 2017))


def position(step, n):
    p = 0
    for i in range(1, n + 1):
        p = (p + step) % i + 1
        yield (i, p)


def get_position_one(step, n):
    return [i for i, p in position(step, n) if p == 1][-1]


print(get_position_one(355, 50_000_000))

# 1912
# 21066990
