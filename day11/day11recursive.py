from aocd import get_data
from functools import cache
inp = get_data(day=11,year=2024).split()
stones = {key: 1 for key in inp}
newstones = {}
blinks = 75
sum = 0
@cache
def get_newstone(stone):
    newstone = []
    if stone == '0':
        newstone = ['1']
    elif len(stone) % 2 == 0:
        midpoint = len(stone) // 2
        newstone = [str(int(stone[:midpoint])), str(int(stone[midpoint:]))]
    else:
        newstone = [str(int(stone) * 2024)]
    return newstone
@cache
def get_count(stone, b):
    count = 0
    if b == 0:
        return 1
    for stone in get_newstone(stone):
        count += get_count(stone, b - 1)
    return count
for stone in stones:
    sum += get_count(stone, blinks)
print(sum)
