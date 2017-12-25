from collections import defaultdict


def parse(inp):
    init, *states_raw = inp.split('\n\n')
    begin, steps = init.split('\n')
    begin = begin[-2]
    steps = int(steps.rsplit(' ', 2)[1])

    states = {}
    for state in states_raw:
        s, s0, w0, m0, c0, s1, w1, m1, c1 = map(
            lambda x: dict(left=-1, right=1).get(x, x),
            map(
                lambda s: s.strip('.:').strip().rsplit(' ', 1)[1],
                state.splitlines()
            )
        )
        states[s] = {}
        states[s][int(s0)] = dict(write=int(w0), move=int(m0), then=c0)
        states[s][int(s1)] = dict(write=int(w1), move=int(m1), then=c1)

    return begin, steps, states


def Day25(inp):
    state, steps, states = parse(inp)

    tape = defaultdict(int)
    cursor = 0
    for i in range(steps):
        s = states[state][tape[cursor]]
        tape[cursor] = s['write']
        cursor += s['move']
        state = s['then']

    return sum(tape.values())


inp = open('Day25.txt').read()

tnp = """\
Begin in state A.
Perform a diagnostic checksum after 6 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A."""

assert Day25(tnp) == 3
print(Day25(inp))