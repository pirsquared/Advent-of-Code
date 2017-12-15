# Unedited

instructions = list(map(int, open('day5_1.txt')))

a = instructions

i = 0
c = 1
while i < len(a):
    jump = a[i]
    if jump >= 3:
        a[i] -= 1
    else:
        a[i] += 1
    i += jump
    c += 1

c - 1