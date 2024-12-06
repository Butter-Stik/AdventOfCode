from aocd import get_data
inp = get_data(day=6 ,year=2024).splitlines()
guard = {
    "^": [[-1, 0], ">"], 
    ">": [[0, 1], "v"], 
    "v": [[1, 0], "<"], 
    "<": [[0, -1], "^"]}
p1 = []
p1solved = False
def escape(block):
    visits = []
    cellvisits = []
    map = []
    cell = [0, 0]
    size = [0, 0]
    for i in range(len(inp)):
        row = []
        for j in range(len(inp[i])):
            row.append(inp[i][j])
            if inp[i][j] == '#':
                continue
            if inp[i][j] in guard:
                cell = [i, j]
                p1.append([i, j])
                visits.append([[i, j], inp[i][j]])
            if [i, j] == block:
                print(block)
                row[j] = "#"
            if p1solved and block not in p1:
                return True
        map.append(row)
        size[1] = len(row)
    size[0] = len(map)
    repeats = 0
    numturns = 0
    while True:
        _y, _x = cell
        guard_ = map[_y][_x]
        newcell = [[_y + guard[guard_][0][0], _x + guard[guard_][0][1]], guard_]
        y = newcell[0][0]
        x = newcell[0][1]
        if y < 0 or y > size[0] - 1:
            return True
        if x < 0 or x > size[1] -1:
            return True
        
        while map[y][x] == "#":
            numturns += 1
            map[_y][_x] = guard[guard_][1]
            guard_ = map[cell[0]][cell[1]] 
            newcell = [[_y + guard[guard_][0][0], _x + guard[guard_][0][1]], guard_]
            y = newcell[0][0]
            x = newcell[0][1]
            
            if y < 0 or y > size[0] - 1:
                return True
            if x < 0 or x > size[1] - 1:
                return True

        if newcell[0] not in p1 and not p1solved:
            p1.append(newcell[0])
        if newcell not in visits:
            visits.append(newcell)
        else:
            return False
        if newcell[0] in cellvisits:
            repeats += 1
            if repeats > numturns:
                return False
        map[newcell[0][0]][newcell[0][1]] = guard_
        map[cell[0]][cell[1]] = "."
        cell = newcell[0]

escape([10000, 10000])
print(len(p1))
p1solved = True
p2 = 0
for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j] in guard or inp[i][j] == "#":
            continue
        if not escape([i, j]):
            p2 += 1
            print(p2)
        else:
            print("no loop")
print(p2)
