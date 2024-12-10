from aocd import get_data
import math
inp = get_data(day=9 ,year=2024)
blocks = []
for n in range(0, len(inp), 2):
    blocks.append([int(inp[n]), n // 2, False])
    if n + 1 < len(inp):
        if int(inp[n + 1]) > 0:
            blocks.append([int(inp[n + 1]), "."])
blocks.reverse()
for i in range(len(blocks)):
    block = blocks[i]
    if block[1] == ".":
        continue
    if block[2] == True:
        continue
    size = block[0]
    val = block[1]
    print(block)
    for j, blank in reversed(list(enumerate(blocks))):
        if blank[1] != "." or j < i:
            continue
        if blank[0] >= size:
            leftover = blank[0] - size
            blocks[j] = [size, val, True]
            if leftover > 0:
                blocks.insert(j, [leftover, "."])
            blocks[i] = [size, "."]
            break
p2 = 0
blocks.reverse()
n = 0
for i in range(len(blocks)):
    for j in range(blocks[i][0]):
        if blocks[i][1] != ".":
            p2 += n * int(blocks[i][1])
        n += 1
print(p2)
