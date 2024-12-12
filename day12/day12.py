from aocd import get_data
inp = get_data(day=12,year=2024).splitlines()
dirs = {
    0: [-1, 0],
    1: [0, 1],
    2: [1, 0],
    3: [0, -1]
}
def get_corners(tile, gooddirs):
    r, c, p = tile
    if len(gooddirs) == 4:
        corners = 4
        if inp[r - 1][c - 1] == p:
            corners -= 1
        if inp[r - 1][c + 1] == p:
            corners -= 1
        if inp[r + 1][c - 1] == p:
            corners -= 1
        if inp[r + 1][c + 1] == p:
            corners -= 1
    elif len(gooddirs) == 3:
        corners = 2
        d1, d2, d3 = gooddirs
        leg = d1
        if d1[0] == d2[0] or d1[1] == d2[1]:
            leg = d3
        if d1[0] == d3[0] or d1[1] == d3[1]:
            leg = d2
        if leg[0] != 0:
            if inp[r + leg[0]][c - 1] == p:
                corners -= 1
            if inp[r + leg[0]][c + 1] == p:
                corners -= 1
        else:
            if inp[r - 1][c + leg[1]] == p:
                corners -= 1
            if inp[r + 1][c + leg[1]] == p:
                corners -= 1
    elif len(gooddirs) == 2:
        corners = 2
        d1, d2 = gooddirs
        if d1[0] == d2[0] or d1[1] == d2[1]:
            corners = 0
        else:
            cornerr = d1[0]
            cornerc = d2[1]
            if d1[0] == 0:
                cornerr = d2[0]
                cornerc = d1[1]
            if inp[r + cornerr][c + cornerc] == p:
                corners = 1
        
    elif len(gooddirs) == 1:
        corners = 2
    else:
        corners = 4
    return corners
p1 = 0
p2 = 0
tileschecked = []
map = {(r, c) for r in range(len(inp)) for c in range(len(inp[r]))}
tiles = [(r, c, inp[r][c]) for r in range(len(inp)) for c in range(len(inp[r]))]
for tile in tiles:
    if tile in tileschecked:
        continue
    tileschecked.append(tile)
    group = [tile]
    corners = 0
    perimeter = 0
    for t in group:
        gooddirs = []
        matches = []
        for dir in dirs:
            _r = t[0] + dirs[dir][0]
            _c = t[1] + dirs[dir][1]
            if (_r, _c) not in map:
                perimeter += 1
                continue
            _p = inp[_r][_c]
            if _p != t[2]:
                perimeter += 1
                continue
            if (_r, _c, _p) not in group:
                matches.append((_r, _c, _p))
                tileschecked.append((_r, _c, _p))
            gooddirs.append(dirs[dir])
        for match in matches:
            group.append(match)
        corners += get_corners(t, gooddirs)
    p1 += len(group) * perimeter
    p2 += len(group) * corners
print(p1, p2)
