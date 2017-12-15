import operator as op


def parse(line):
    r, i, q, _, c = line.split(' ', 4)
    c_, op, v = c.split()
    return r, i, q, c_, op, v


ops = {'==': op.eq, '<': op.lt, '<=': op.le, '>': op.gt, '>=': op.ge,
       '!=': op.ne}

m = 0
data = {}
for line in s.splitlines():
    r, i, q, c, o, v = parse(line)
    q = int(q)
    v = int(v)
    q *= -1 if i == 'dec' else 1
    if ops[o](data.get(c, 0), v):
        if r in data:
            data[r] += q
        else:
            data[r] = q

        m = max(m, max(data.values()))

print(m, max(data.values()))