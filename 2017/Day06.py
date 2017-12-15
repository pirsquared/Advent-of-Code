# Unedited
def reallocate(banks):
    n = len(banks)
    i = banks.argmax()
    k = banks[i]
    banks[i] = 0
    for j in range(1, k + 1):
        banks[(i + j) % n] += 1
        k -= 1


counter = 0
while True:
    reallocate(banks)
    counter += 1
    tup = tuple(banks)
    if tup in tracker:
        print(counter, tracker[tup], counter - tracker[tup])
        break
    else:
        tracker[tup] = counter

