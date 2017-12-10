def twist(a, n):
    return a[:n][::-1] + a[n:]

def skip(a, k):
    return a[k:] + a[:k]

def knot(a, x):
    p = k = 0
    for i in x:
        a = skip(twist(skip(a, p), i), -p)
        p = (p + i + k) % len(a)
        k += 1
    return a


a, b, *_ = knot(
    list(range(256)),
    list(map(int, '130,126,1,11,140,2,255,207,18,254,246,164,29,104,0,224'.split(',')))
)

print(a * b)

def densehash(a):
    return list(map(
        lambda x: reduce(int.__xor__, x),
        zip(*(a[i::16] for i in range(16)))
    ))

def knothash(a, x):
    suffix = [17, 31, 73, 47, 23]
    y = list(map(ord, x)) + suffix
    dh = densehash(knot(a, y * 64))
    return ''.join('{:02x}'.format(n) for n in dh)

print(knothash(list(range(256)), '130,126,1,11,140,2,255,207,18,254,246,164,29,104,0,224'))

assert(knothash(list(range(256)), '') == 'a2582a3a0e66e6e86e3812dcb672a272')
assert(knothash(list(range(256)), 'AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd')
assert(knothash(list(range(256)), '1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d')
assert(knothash(list(range(256)), '1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e')

# 38628
# e1462100a34221a7f0906da15c1c979a
