from aocd import get_data
import re
inp = get_data(day=24,year=2024).split("\n\n")
init = inp[0].splitlines()
gates = inp[1].splitlines()
wires = {}
for line in gates:
    ws = re.findall(r".\d+", line)
    operation = line.split(" -> ")
    for w in ws:
        wires[w] = ""
    wires[operation[1]] = operation[0]
for i in init:
    nums = i.split(": ")
    if nums[1] == '1':
        wires[nums[0]] = True
    else:
        wires[nums[0]] = False
zs = [wire for wire in wires if wire.startswith("z")]
def evaluate_wire(wire):
    if wire == True or wire == False:
        return wire
    op = wires[wire]
    if op == True or op == False:
        return op
    parts = op.split(' ')
    gate = parts[1]
    w1 = evaluate_wire(parts[0])
    w2 = evaluate_wire(parts[2])
    if w1 != True and w2 != False:
        w1 = evaluate_wire(w1)
    if w2 != True and w2 != False:
        w2 = evaluate_wire(w2)
    if gate == 'AND':
        return w1 and w2
    if gate == 'OR':
        return w1 or w2
    if gate == 'XOR':
        return w1 ^ w2 
zs = sorted(zs)
zs.reverse()
strng = ''
for z in zs:
    if evaluate_wire(z):
        strng += '1'
    else:
        strng += '0'
xs = [x for x in init if x.split(": ")[0].startswith("x")]
ys = [y for y in init if y.split(": ")[0].startswith("y")]
xs.reverse()
xstr = ''
ys.reverse()
ystr = ''
for x in xs:
    if x.split(": ")[1] == '0':
        xstr += '0'
    else:
        xstr += '1'
for y in ys:
    if y.split(": ")[1] == '0':
        ystr += '0'
    else:
        ystr += '1'
print(strng)
print(int(strng, 2))
for i in range(len(strng)):
    
