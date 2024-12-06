from aocd import get_data
inp = get_data(day=1, year=2015)
p1 = 0
for i in range(len(inp)):
    if inp[i] == "(":
        p1 += 1
    else:
        p1 -= 1
    if p1 == -1:
        print(i + 1)
print(p1)
