from aocd import get_data
inp = get_data(day=15,year=2024).split("\n\n")
grid = inp[0].splitlines()
dirs = {
    "^": [-1, 0],
    ">": [0, 1],
    "v": [1, 0],
    "<": [0, -1]
}
walls = [(r, c) for r in range(len(grid)) for c in range(len(grid[r])) if grid[r][c] == "#"]
boxes = [[r, c] for r in range(len(grid)) for c in range(len(grid[r])) if grid[r][c] == "O"]
robot = [[r, c] for r in range(len(grid)) for c in range(len(grid[r])) if grid[r][c] == "@"][0]
moves = [dirs[inp[1][i]] for i in range(len(inp[1])) if inp[1][i] != "\n"]
def can_move(obj, dir):
    r, c = obj
    rr = r + dir[0]
    cc = c + dir[1]
    if (rr, cc) in walls:
        return False, [r, c]
    if [rr, cc] in boxes:
        return can_move([rr, cc], dir)
    else:
        return True, [rr, cc]
for move in moves:
    canmove, pos = can_move(robot, move)
    if canmove:
        robot = [robot[0] + move[0], robot[1] + move[1]]
    for i in range(len(boxes)):
        if boxes[i] == robot:
            boxes[i] = pos
p1 = 0
for box in boxes:
    p1 += box[0] * 100 + box[1]
print(p1)
