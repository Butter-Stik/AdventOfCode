from aocd import get_data
inp = get_data(day=20,year=2024).splitlines()
inp = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############""".splitlines()

dirs = {
    0: [-1, 0],
    1: [0, 1],
    2: [1, 0],
    3: [0, -1]
}
walls = [(r, c) for r in range(len(inp)) for c in range(len(inp[r])) if inp[r][c] == "#"]
S = [(r, c) for r in range(len(inp)) for c in range(len(inp[r])) if inp[r][c] == "S"][0]
E = [(r, c) for r in range(len(inp)) for c in range(len(inp[r])) if inp[r][c] == "E"][0]

def floodfill(start, end):
    map = {(r, c): 99999999999999 for r in range(len(inp)) for c in range(len(inp[r]))}
    allbytes = []
    tiles_to_check = [(start, 0)]
    map[start] = 0
    while len(tiles_to_check) > 0:
        for tile in tiles_to_check:
            r, c = tile[0]
            for dir in dirs:
                dr, dc = dirs[dir]
                rr = r + dr
                cc = c + dc
                if (rr, cc) in walls:
                    continue
                if (rr, cc) not in map:
                    continue
                if map[(rr, cc)] <= tile[1] + 1:
                    continue
                tiles_to_check.append(((rr, cc), tile[1] + 1))
                map[(rr, cc)] = tile[1] + 1
            tiles_to_check.remove(tile)
    return map
s_to_e = floodfill(S, E)
e_to_s = floodfill(E, S)
base = s_to_e[E]
cheats = []
p2 = 0
tiles_on_path = [(r, c) for r in range(len(inp)) for c in range(len(inp[r])) if s_to_e[(r, c)] + e_to_s[(r, c)] == s_to_e[E]]
for tile in tiles_on_path:
    for dr in range(-20, 21):
        for dc in range(-20, 21):
            if abs(dr) + abs(dc) > 20:
                continue
            r, c = tile
            rr = r + dr
            cc = c + dc
            if (rr, cc) not in tiles_on_path:
                continue
            if (rr, cc) in walls or (rr, cc) not in s_to_e:
                continue
            steps_to_cheat = s_to_e[(r, c)]
            steps_from_cheat = e_to_s[(rr, cc)]
            steps_in_cheat = abs(dr) + abs(dc)
            total_steps = steps_to_cheat + steps_from_cheat + steps_in_cheat
            #print(base - total_steps)
            if total_steps + 50 <= base:
                #print(base - total_steps)
                cheats.append(base - total_steps)
                #print(p2)
print(len(cheats))
