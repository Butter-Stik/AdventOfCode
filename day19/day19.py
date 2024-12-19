from aocd import get_data
from functools import cache
inp = get_data(day=19,year=2024).split("\n\n")
towels = inp[0].split(", ")
patterns = inp[1].splitlines()
@cache
def can_make_pattern(pattern):
    num = 0
    if not pattern:
        return 1
    for i in range(len(pattern)):
        substring = pattern[:i+1]
        nextnum = can_make_pattern(pattern[i+1:])
        if substring in towels and nextnum > 0:
            num += nextnum
    return num
p1 = 0
p2 = 0
for pattern in patterns:
    num = can_make_pattern(pattern)
    p2 += num
    if num > 0:
        p1 += 1
print(p1, p2)
