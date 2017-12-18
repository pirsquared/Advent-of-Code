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


def logic_part1(instructions, register, stk):
    position = 0

    num = len(instructions)

    while 0 <= position < num:
        ins, args = instructions[position]

        if ins == 'set':
            register[args[0]] = get(register, args[1])
            position += 1

        elif ins == 'rcv':
            if get(register, args[0]) and stk:
                return stk.pop()
            else:
                position += 1

        elif ins == 'snd':
            stk.append(get(register, args[0]))
            position += 1

        elif ins == 'jgz':
            X, Y = args
            position += get(register, Y) if get(register, X) > 0 else 1

        else:
            register[args[0]] = ops[ins](register[args[0]],
                                         get(register, args[1]))
            position += 1

    return stk.pop()


test_ = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""

parse(test_)

assert logic_part1(parse(test_), defaultdict(int), deque()) == 4

print(logic_part1(instructions, defaultdict(int), deque()))


def logic(instructions, register, stk_i, stk_o):
    position = 0
    total_sends = 0

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
                yield total_sends
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

    yield total_sends


def logic_part2():
    stk0, stk1 = deque(), deque()

    prog1 = logic(instructions, defaultdict(int, {'p': 1}), stk0, stk1)
    prog0 = logic(instructions, defaultdict(int, {'p': 0}), stk1, stk0)

    for t in prog1:
        try:
            next(prog0)
        except:
            break

    return t


print(logic_part2())
