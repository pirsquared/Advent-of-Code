from functools import partial
from itertools import islice, count
from collections import deque, defaultdict
import operator as op

inp = open('Day23.txt').read()


def parse(instructions):
    return [(f, args) for f, *args in map(str.split, instructions.splitlines())]


def get(register, V):
    try:
        V = int(V)
        return V
    except ValueError:
        return register.setdefault(V, 0)


def Day23_part1(inp):
    instructions = parse(inp)
    position = 0
    register = defaultdict(int)
    num = len(instructions)
    num_mul = 0
    count = 0

    ops = dict(add=op.add, mul=op.mul, mod=op.mod, sub=op.sub)
    while 0 <= position < num:

        ins, args = instructions[position]
        num_mul += ins == 'mul'

        if ins == 'set':
            register[args[0]] = get(register, args[1])
            position += 1

        elif ins == 'jnz':
            X, Y = args
            position += get(register, Y) if get(register, X) else 1

        else:
            register[args[0]] = ops[ins](register[args[0]],
                                         get(register, args[1]))
            position += 1

        count += 1

    return num_mul


def get_prime_generator():
    D = {}
    yield 2

    for q in islice(count(3), 0, None, 2):
        p = D.pop(q, None)
        if p:
            x = q + p + p
            while x in D:
                x += p + p
            D[x] = p
        else:
            D[q * q] = q
            yield q


def h():
    base = set(range(106500, 123501, 17))
    pgen = get_prime_generator()
    prms = [next(pgen)]
    while prms[-1] < 123501:
        prms.append(next(pgen))

    return len(base - set(prms))


print(Day23_part1(inp))
print(h())
