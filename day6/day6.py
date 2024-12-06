from aocd import get_data
import re
inp = get_data(day=6 ,year=2015).splitlines()
instructions = []
map = []
brightmap = []
toggle = lambda light : not light
on = lambda light : True
off = lambda light : False
togglebright = lambda light : light + 2
onbright = lambda light : light + 1
offbright = lambda light : max(light - 1, 0)
nametofunc = {
    "turn on": on,
    "turn off": off,
    "toggle": toggle
}
nametobrightfunc = {
    "turn on": onbright,
    "turn off": offbright,
    "toggle": togglebright
}
for i in range(1000):
    row = []
    brightrow = []
    for j in range(1000):
        row.append(False)
        brightrow.append(0)
    map.append(row)
    brightmap.append(brightrow)
for line in inp:
    instruction = re.findall("(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)", line)[0]
    instructions.append(instruction)
    func = nametofunc[instruction[0]]
    brightfunc = nametobrightfunc[instruction[0]]
    for i in range(int(instruction[1]), int(instruction[3]) + 1):
        for j in range(int(instruction[2]), int(instruction[4]) + 1):
            map[i][j] = func(map[i][j])
            brightmap[i][j] = brightfunc(int(brightmap[i][j]))
p2 = 0
p1 = 0
for row in map:
    p1 += row.count(True)
for row in brightmap:
    for light in row:
        p2 += light
print(p1, p2)
