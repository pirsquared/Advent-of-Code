"""A slightly different take.  I used the send method."""
from functools import partial
from collections import deque, defaultdict
import operator as op

inp = open('Day18.txt').read()


def parse(instructions):
    return [(f, args) for f, *args in map(str.split, instructions.splitlines())]


instructions = parse(inp)

ops = dict(add=op.add, mul=op.mul, mod=op.mod)


def get(register, V):
    try:
        V = int(V)
        return V
    except ValueError:
        return register.setdefault(V, 0)


def coroutine(instructions, register):
    position = 0
    total_sends = 0

    stk_i = yield None, None
    stk_o = deque()

    num = len(instructions)

    while 0 <= position < num:
        ins, args = instructions[position]

        if ins == 'set':
            register[args[0]] = get(register, args[1])
            position += 1

        elif ins == 'rcv':
            if stk_i:
                register[args[0]] = stk_i.popleft()
                position += 1
            else:
                stk_i = yield stk_o, total_sends
                stk_o = deque()
                if not stk_i:
                    break

        elif ins == 'snd':
            stk_o.append(get(register, args[0]))
            total_sends += 1
            position += 1

        elif ins == 'jgz':
            X, Y = args
            position += get(register, Y) if get(register, X) > 0 else 1

        else:
            register[args[0]] = ops[ins](register[args[0]],
                                         get(register, args[1]))
            position += 1

    yield stk_o, total_sends


def day18part2(instructions):
    progs = [
        coroutine(instructions, defaultdict(int, dict(p=0))),
        coroutine(instructions, defaultdict(int, dict(p=1)))
    ]

    [next(p) for p in progs]

    stk, tot0 = progs[0].send(deque())

    tots = [0, 0]

    i = 1
    while True:
        stk, temp = progs[i].send(stk)
        if temp == tots[i]:
            break
        else:
            tots[i] = temp
            i ^= 1

    return tots[1]


print(day18part2(instructions))
