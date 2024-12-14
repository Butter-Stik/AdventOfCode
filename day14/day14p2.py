from aocd import get_data
import re
inp = get_data(day=14,year=2024).splitlines()
inp = [[int(val) for val in re.findall("-?\d+", line)] for line in inp]
size = [103, 101]
q1 = q2 = q3 = q4 = 0
seen = set()
iter = 0
while len(seen) != len(inp):
    seen = set()
    for i in range(len(inp)):
        robot = inp[i]
        middle = False
        qr = 0
        qc = 0
        c, r, vc, vr = robot
        r = (r + (vr)) % size[0]
        c = (c + (vc)) % size[1]
        inp[i] = c, r, vc, vr
        seen.add((c, r))
    iter += 1
print(iter)
board = ""
for i in range(size[1]):
    row = ""
    for j in range(size[0]):
        if (j, i) in seen:
            row += "#"
        else:
            row += "."
    row += "\n"
    board += row
print(board)
