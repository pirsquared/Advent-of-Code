def find_group(n, g, d):
    g_ = set(d[n])
    new = g_ - g
    g |= g_
    for k in new:
        g |= find_group(k, g, d)
    return g


s = open('Day12_input.txt').read()

d = {k: v.split(', ') for k, v in [line.split(' <-> ') for line in s.splitlines()]}

len(find_group('0', set(), d))

nodes = set(d.keys())

count = 0
while nodes:
    node = next(iter(nodes))
    group = find_group(node, set(), d)
    nodes -= group
    count += 1

count
