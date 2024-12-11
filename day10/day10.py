from aocd import get_data
inp = get_data(day=10, year=2024).splitlines()
inp = [list(line) for line in inp]
dirs = {
    0: [-1, 0],
    1: [0, 1],
    2: [1, 0],
    3: [0, -1]
}
size = (len(inp) - 1, len(inp[0]) - 1)
p1 = 0
p2 = 0
for i in range(len(inp)):
    for j in range(len(inp[i])):
        n = int(inp[i][j])
        if n != 0: # not trailhead
            continue
        reachable = []
        neighbors = [(i, j)]
        for neighbor in neighbors:
            r, c = neighbor
            for dir in dirs:
                num = int(inp[r][c])
                dir = dirs[dir]
                _r = r + dir[0]
                _c = c + dir[1]
                if _r < 0 or _r > size[0] or _c < 0 or _c > size[1]:
                    continue
                if int(inp[_r][_c]) == num + 1:
                    neighbors.append((_r, _c))
                    if int(inp[_r][_c]) == 9: # path found
                        if (_r, _c) not in reachable:
                            reachable.append((_r, _c))
                        p2 += 1
        p1 += len(reachable)
print(p1, p2)
