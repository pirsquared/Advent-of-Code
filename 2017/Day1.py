# Day 1, Problem 1
def day1_1(s):
    return sum(
        map(int, (s[i] for i in range(len(s)) if
                  s[i] == s[(i + 1) % len(s)]))
    )


# Day 1, Problem 2
def day1_2(s):
    return sum(
        map(int, (s[i] for i in range(len(s)) if
                  s[i] == s[(i + len(s) // 2) % len(s)]))
    )
