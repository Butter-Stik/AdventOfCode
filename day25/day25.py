from aocd import get_data
inp = get_data(day=25,year=2024).split('\n\n')
keys = [schematic.splitlines() for schematic in inp if schematic[0] == "."]
locks = [schematic.splitlines() for schematic in inp if schematic[0] == "#"]
keyheights = []
lockheights = []
for key in keys:
    heights = []
    for c in range(len(key[0])):
        r = len(key)
        while key[r - 1][c] == "#":
            r -= 1
        heights.append(len(key) - 1 - r)
    keyheights.append(heights)
for lock in locks:
    heights = []
    for c in range(len(lock[0])):
        r = 0
        while lock[r + 1][c] == "#":
            r += 1
        heights.append(r)
    lockheights.append(heights)
p1 = 0
for lock in lockheights:
    for key in keyheights:
        passed = True
        for r in range(len(lock)):
            if lock[r] + key[r] > 5:
                passed = False
        if passed:
            p1 += 1
print(p1)
