from aocd import get_data
from functools import cache
inp = get_data(day=11,year=2024).split()
stones = {key: 1 for key in inp}
newstones = {}
blinks = 75
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
while blinks > 0:
    for stone in stones:
        newstone = get_newstone(stone)
        for new in newstone:
            if new not in newstones:
                newstones[new] = 0
            newstones[new] = newstones[new] + stones[stone]
    stones = newstones.copy()
    newstones = {}
    blinks -= 1
sum = 0
for stone in stones:
    sum += stones[stone]
print(sum)
