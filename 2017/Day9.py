import re

s = open('day9input.txt').read()
remove_cleanup = re.sub('!.', '', s)
remove_garbage = re.sub('<[^>]*>', '<>', remove_cleanup)

total, level = 0, 0

for c in remove_garbage:
    if c == '{':
        level += 1
        total += level
    elif c == '}':
        level -= 1

print(b, len(remove_cleanup) - len(remove_garbage))

# 9662 4903
