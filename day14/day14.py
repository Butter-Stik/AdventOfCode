from aocd import get_data
import re
inp = get_data(day=14,year=2024).splitlines()
inp = [[int(val) for val in re.findall("-?\d+", line)] for line in inp]
size = [103, 101]
seconds = 2024
q1 = q2 = q3 = q4 = 0
for robot in inp:
    middle = False
    qr = 0
    qc = 0
    c, r, vc, vr = robot
    r = (r + (vr * 100)) % size[0]
    c = (c + (vc * 100)) % size[1]
    if r < (size[0]) // 2 and c < (size[1]) // 2:
        q1 += 1
    elif r < (size[0]) // 2 and c > (size[1]) // 2:
        q2 += 1
    elif r > (size[0]) // 2 and c < (size[1]) // 2:
        q3 += 1
    elif r > (size[0]) // 2 and c > (size[1]) // 2:
        q4 += 1
print(q1*q2*q3*q4)
