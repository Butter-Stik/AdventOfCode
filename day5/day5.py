from aocd import get_data
import re
from collections import Counter
inp = get_data(day=5, year=2024).split("\n\n")
allrules = inp[0].splitlines()
updates = inp[1].splitlines()
for i in range(len(allrules)):
    allrules[i] = allrules[i].split("|")
part1 = 0
part2 = 0
for i in range(len(updates)):
    update = updates[i].split(",")
    order = []
    for rule in allrules:
        if rule[0] in update and rule[1] in update:
            order.append(rule[0])
    counter = Counter(order)
    order = list(dict.fromkeys(sorted(order, key=lambda x: counter[x], reverse=True)))
    lastval = update.pop()
    if not lastval in order and update == order:
        part1 += int(update[len(update) // 2])
        continue
    update.append(lastval)
    part2 += int(order[len(order) // 2])
print(part1, part2)
