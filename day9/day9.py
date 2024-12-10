from aocd import get_data
import math
inp = get_data(day=9 ,year=2024)
fileblock = []
for n in range(0, len(inp), 2):
    for i in range(int(inp[n])):
        fileblock.append(n // 2)
    if n + 1 < len(inp):
        for i in range(int(inp[n + 1])):
            fileblock.append(".")
reverse = fileblock[:]
reverse.reverse()
reverse[:] = (value for value in reverse if value != ".")
length = len(reverse)
for i in range(len(fileblock)):
    if fileblock[i] == ".":
        if len(reverse) != 0:
            fileblock[i] = reverse.pop(0)
p1 = 0
for j in range(length):
    p1 += fileblock[j] * j
print(fileblock, p1)
