from aocd import get_data
inp = get_data(day=8 ,year=2024).splitlines()
antennas = [(inp[r][c], r, c) for r in range(len(inp)) for c in range(len(inp[r])) if inp[r][c] != "."]
size = [len(inp) - 1, len(inp[0]) - 1]
groups = {}
for antenna in antennas:
    key = antenna[0]
    if key not in groups:
        groups[key] = []
    groups[key].append((antenna[1], antenna[2]))

antinodes = []
for key, group in groups.items():
    pairs = [(a, b) for idx, a in enumerate(group) for b in group[idx + 1:]]
    pairdiffs = [(r2 - r1, c2 - c1) for (r1, c1), (r2, c2) in pairs]
    for i in range(len(pairs)):
        dr, dc = pairdiffs[i]
        p1, p2 = pairs[i]
        for i in range(max(size)):
            a1 = (p1[0] - dr * i, p1[1] - dc * i)
            a2 = (p2[0] + dr * i, p2[1] + dc * i)
            for antinode in (a1, a2):
                if all(0 <= antinode[i] <= size[i] for i in range(len(antinode))) and antinode not in antinodes:   
                    antinodes.append(antinode)
print(len(antinodes))
