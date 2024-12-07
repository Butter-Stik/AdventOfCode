from aocd import get_data
import re
inp = get_data(day=7, year=2024).splitlines()
ops = []
for line in inp:
    ops.append(re.findall("\d+", line))

def countDigit(n):
    if (n / 10 == 0):
        return 1
    return 1 + countDigit(n / 10)

def int_to_ternary(n):
  """Converts an integer to its ternary representation."""

  if n == 0:
    return "0"

  ternary = ""
  while n > 0:
    n, remainder = divmod(n, 3)
    ternary = str(remainder) + ternary

  return ternary

def operation(op, number):
    ternary = int_to_ternary(number)[::-1]
    signs = []
    for i in range(len(op)):
        signs.append("+")
    for i in range(len(ternary)):
        if ternary[i] == "1":
            signs[i] = "*"
        if ternary[i] == "2":
            signs[i] = "||"
    return signs

p1 = 0
for op in ops:
    found = False
    target = int(op[0])
    op.pop(0)
    signs = []
    for i in range(int(pow(3, len(op) - 1))):
        _op = operation(op, i)
        num = int(op[0])
        for n in range(len(op) - 1):
            if _op[n] == "+":
                num += int(op[n + 1])
            elif _op[n] == "*":
                num *= int(op[n + 1])
            else:
                num = int(str(num) + str(op[n + 1]))
        if num == target and not found:
            found = True
            p1 += target
print(p1)
