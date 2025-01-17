from aocd import get_data
import re
inp = get_data(day=7, year=2024).splitlines()
ops = []
for line in inp:
    ops.append(re.findall("\d+", line))

def operation(op, number):
    binary = bin(number)[2:][::-1]
    signs = []
    for i in range(len(op)):
        signs.append("+")
    for i in range(len(binary)):
        if binary[i] == "1":
            signs[i] = "*"
    return signs

p1 = 0
for op in ops:
    found = False
    target = int(op[0])
    op.pop(0)
    signs = []
    for i in range(int(pow(2, len(op) - 1))):
        _op = operation(op, i)
        num = int(op[0])
        for n in range(len(op) - 1):
            if _op[n] == "+":
                num += int(op[n + 1])
            else:
                num *= int(op[n + 1])
        if num == target and not found:
            found = True
            p1 += target
print(p1)
