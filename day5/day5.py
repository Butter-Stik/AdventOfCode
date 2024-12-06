from aocd import get_data
import re
inp = get_data(day=5, year=2015).splitlines()
p1 = 0
p2 = 0
for line in inp:
    if "ab" in line or "cd" in line or "pq" in line or "xy" in line:
        continue
    if len(re.findall("[aeiou]", line)) < 3:
        continue
    double = False
    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            double = True
    if double == False:
        continue
    p1 += 1
for line in inp:
    double = False
    for i in range(len(line) - 1):
        if line.count(str(line[i]) + str(line[i + 1])) > 1:
            double = True
    gap = False
    for i in range(len(line) - 2):
        if line[i] == line[i + 2]:
            gap = True
    if gap and double:
        p2 += 1
print(p1, p2)
