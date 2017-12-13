def severity(firewall, delay=0):
    return sum(
        ((k + delay) % (2 * v - 2) == 0) * k * v
        for k, v in firewall.items()
    )


print(severity(firewall))

delay = 0
x = severity(firewall, delay)
while (x != 0) or (delay % (firewall[0] * 2 - 2) == 0):
    delay += 1
    x = severity(firewall, delay)

print(delay)
