from aocd import get_data
inp = get_data(day=18,year=2024).splitlines()
dirs = {
    0: [-1, 0],
    1: [0, 1],
    2: [1, 0],
    3: [0, -1]
}
w = h = 70
allbytes = []
iteration = len(inp)
def test_iteration(iter, p1):
    map = {(r, c): 99999999999999 for r in range(h + 1) for c in range(w + 1)}
    allbytes = []
    for i in range(iter):
        c, r = inp[i].split(',')
        allbytes.append((int(r), int(c)))
    tiles_to_check = [((0, 0), 0)]
    map[(0, 0)] = 0
    while len(tiles_to_check) > 0:
        for tile in tiles_to_check:
            r, c = tile[0]
            for dir in dirs:
                dr, dc = dirs[dir]
                rr = r + dr
                cc = c + dc
                if (rr, cc) in allbytes:
                    continue
                if (rr, cc) not in map:
                    continue
                if map[(rr, cc)] <= tile[1] + 1:
                    continue
                tiles_to_check.append(((rr, cc), tile[1] + 1))
                map[(rr, cc)] = tile[1] + 1
            tiles_to_check.remove(tile)
    if p1:
        print(map[(h, w)])
    elif map[(h, w)] != 99999999999999:
        print(inp[iter])
        return True
while True:
    if test_iteration(iteration, False):
        break
    iteration -= 1
test_iteration(1024, True)
