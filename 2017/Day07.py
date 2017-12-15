import pandas as pd
import numpy as np
from functools import reduce


def parse_line(t):
    name, weight, *children = t.split()
    children = [x.strip(',') for x in children[1:]]
    return dict(n=name, w=int(weight[1:-1]), c=children)


data = {d['n']: d for d in map(parse_line, s.splitlines())}

all_children = reduce(set.union, map(set, (data[d]['c'] for d in data)))
all_nodes = set(data)

root = next(iter(all_nodes - all_children))


def build_tree(node, parent, data):
    this = dict(name=node, parent=parent, w=data[node]['w'])

    this['children'] = [
        build_tree(child, this, data)
        for child in data[node]['c']
        ]

    this['weight'] = this['w']
    this['weight'] += sum(d['weight'] for d in this['children'])
    return this


tree = build_tree(root, None, data)


def check(node):
    weights, raw, isdiff, mode, pos = get_weights(node)
    if isdiff.any():
        child = node['children'][pos]
        return check(child)
    else:
        return node['parent']


def get_weights(node):
    wt, ch = 'weight', 'children'
    weights = np.array([c[wt] for c in node[ch]])
    raw = np.array([c['w'] for c in node[ch]])
    isdiff = (np.diff(weights) != 0)
    mode = pd.Series(weights).mode().iat[0]
    pos = (weights != mode).argmax()
    return weights, raw, isdiff, mode, pos


def find_imbalance(node):
    weights, raw, isdiff, mode, pos = get_weights(node)
    return raw[pos] + (mode - weights[pos])


find_imbalance(check(tree))