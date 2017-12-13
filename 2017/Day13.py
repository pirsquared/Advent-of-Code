print(
    sum(
        (k % (2 * v - 2) == 0) * k * v
        for k, v in firewall.items()
    )
)


def caught(firewall, delay=0):
    return any((k + delay) % (2 * v - 2) == 0 for k, v in firewall.items())


delay = 0
while caught(firewall, delay):
    delay += 1

print(delay)
