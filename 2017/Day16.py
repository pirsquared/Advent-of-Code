from collections import deque
from functools import partial


def maybe_int(i):
    try:
        return int(i)
    except ValueError:
        return i


def move(m, moves):
    moves[m[0]](*map(maybe_int, m[1:].split('/')))


def exchange(dancers, i, j):
    dancers[i], dancers[j] = dancers[j], dancers[i]


def partner(dancers, a, b):
    exchange(dancers, dancers.index(a), dancers.index(b))


def perform(dancers, dance):
    moves = dict(
        s=dancers.rotate,
        x=partial(exchange, dancers),
        p=partial(partner, dancers)
    )

    for m in dance.split(','):
        move(m, moves)

    return dancers


def repeat_dance(dancers, dance, n):
    initial_state = ''.join(dancers)
    i = 0

    while n:

        dancers = perform(dancers, dance)
        n -= 1
        i += 1
        state = ''.join(dancers)

        if state == initial_state:
            n = n % i

    return dancers


assert ''.join(repeat_dance(deque('abcde'), 's1,x3/4,pe/b', 1)) == 'baedc'
assert ''.join(repeat_dance(deque('abcde'), 's1,x3/4,pe/b', 2)) == 'ceadb'

inp = open('Day16.txt').read()

print(''.join(repeat_dance(deque('abcdefghijklmnop'), inp, 1)))
print(''.join(repeat_dance(deque('abcdefghijklmnop'), inp, 1_000_000_000)))

# giadhmkpcnbfjelo
# njfgilbkcoemhpad
