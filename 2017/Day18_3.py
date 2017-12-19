from functools import partial
import asyncio
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


async def logic(instructions, register, stk_i, stk_o):
    pflg = register['p'] == 1

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
                # This is a hack job in my opinion.  I need a way
                # to wait for other parallel job.  Work in progress!
                await asyncio.sleep(.1)
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

    if pflg:
        print(f'{total_sends}')


stacks = [deque(), deque()]

loop = asyncio.get_event_loop()
# Blocking call which returns when the display_date() coroutine is done
loop.run_until_complete(asyncio.gather(
    logic(instructions, defaultdict(int, {'p': 0}), *stacks),
    logic(instructions, defaultdict(int, {'p': 1}), *stacks[::-1])
))
loop.close()
