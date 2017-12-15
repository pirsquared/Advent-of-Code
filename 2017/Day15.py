from itertools import islice

inputA = 277
inputB = 349
testA = 65
testB = 8921


def gA(value, k=None):
    while True:
        if (k is None) or (value % k == 0):
            yield value
        value = (16807 * value) % 2147483647


def gB(value, k=None):
    while True:
        if (k is None) or (value % k == 0):
            yield value
        value = (48271 * value) % 2147483647


def judge(t):
    a, b = t
    c = 0xFFFF
    return (c & a) == (c & b)


def test(A, B, n, kA=None, kB=None):
    return sum(map(judge, islice(zip(gA(A, kA), gB(B, kB)), n)))


assert test(A=testA, B=testB, n=40000000) == 588
assert test(A=testA, B=testB, n=5000000, kA=4, kB=8) == 309

print(
    test(A=inputA, B=inputB, n=40000000),
    test(A=inputA, B=inputB, n=5000000, kA=4, kB=8)
)


# 592 320
