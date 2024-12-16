from aocd import get_data
inp = get_data(day=16,year=2024).splitlines()
dirs = {
    0: [-1, 0],
    1: [0, 1],
    2: [1, 0],
    3: [0, -1]
}
opposite = {
    0: [1, 0],
    1: [0, -1],
    2: [-1, 0],
    3: [0, 1]
}
walls = [(r, c) for r in range(len(inp)) for c in range(len(inp[r])) if inp[r][c] == '#']
w = len(inp[0]) - 1
h = len(inp) - 1
S = (h - 1, 1)
E = (1, w - 1)
scores = []
paths_to_check = [(S, 3, 0)]
p2paths_to_check = [(E, 2, 0)]
seen = {S: 0}
seenp2 = {E: 0}
def get_next_tiles(tile, p2):
    next_tiles = []
    for dir in dirs:
        if dir == opposite[tile[1]]:
            continue
        r, c = tile[0]
        _r, _c = dirs[dir]
        rr = r + _r
        cc = c + _c
        newpos = (rr, cc)
        if newpos in walls:
            continue
        newscore = tile[2] + 1
        if dir != tile[1]:
            newscore += 1000
        if not p2:
            if newpos in seen and seen[newpos] < newscore:
                continue
        else:
            if newpos in seenp2 and seenp2[newpos] < newscore:
                continue
        next_tiles.append((newpos, dir, newscore))
        if not p2:
            seen[newpos] = newscore
        else:
            seenp2[newpos] = newscore
    return next_tiles
while len(paths_to_check) > 0:
    for tile in paths_to_check:
        for t in get_next_tiles(tile, False):
            paths_to_check.append(t)
        paths_to_check.remove(tile)
while len(p2paths_to_check) > 0:
    for tile in p2paths_to_check:
        for t in get_next_tiles(tile, True):
            p2paths_to_check.append(t)
        p2paths_to_check.remove(tile)
p1 = seen[E]
p2 = 0
for tile in seen:
    if seen[tile] + seenp2[tile] == p1 or seen[tile] + seenp2[tile] == p1 - 1000:
        p2 += 1
print("P1: " + str(p1) + "\n" + "P2: " + str(p2))
