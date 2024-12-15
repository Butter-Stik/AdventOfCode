from aocd import get_data
inp = get_data(day=15,year=2024).split("\n\n")
grid = inp[0].splitlines()
dirs = {
    "^": [-1, 0],
    ">": [0, 1],
    "v": [1, 0],
    "<": [0, -1]
}
walls = [(r, c * 2) for r in range(len(grid)) for c in range(len(grid[r])) if grid[r][c] == "#"]
boxes = [[r, c * 2] for r in range(len(grid)) for c in range(len(grid[r])) if grid[r][c] == "O"]
robot = [[r, c * 2] for r in range(len(grid)) for c in range(len(grid[r])) if grid[r][c] == "@"][0]
moves = [dirs[inp[1][i]] for i in range(len(inp[1])) if inp[1][i] != "\n"]
def can_move(obj, dir, isbox):
    boxes_touching = []
    r, c = obj
    rr = r + dir[0]
    cc = c + dir[1]
    if (rr, cc) in walls or (rr, cc - 1) in walls:
        return False
    if isbox:
        if (rr, cc + 1) in walls:
            return False
    if [rr, cc] in boxes:
        boxes_touching.append([rr, cc])
    if [rr, cc - 1] in boxes and [rr, cc - 1] != obj:
        boxes_touching.append([rr, cc - 1])
    if isbox:
        if [rr, cc + 1] in boxes and [rr, cc + 1] != obj:
            boxes_touching.append([rr, cc + 1])
    for box in boxes_touching:
        if not can_move(box, dir, True):
            return False
    return True, [rr, cc]
def move_boxes(box, dir):
    boxes_touching = []
    r, c = box
    rr = r + dir[0]
    cc = c + dir[1]
    if [rr, cc] in boxes:
        boxes_touching.append([rr, cc])
    if [rr, cc - 1] in boxes and [rr, cc - 1] != box:
        boxes_touching.append([rr, cc - 1])
    if [rr, cc + 1] in boxes and [rr, cc + 1] != box:
        boxes_touching.append([rr, cc + 1])
    for touching in boxes_touching:
        move_boxes(touching, dir)
    for i in range(len(boxes)):
        if boxes[i] == box:
            boxes[i] = [rr, cc]
inp[1] = ''.join(inp[1].splitlines())
def print_board(move):
    board = ""
    for r in range(len(grid)):
        row = ""
        for c in range(len(grid[0]) * 2):
            if (r, c) in walls or (r, c - 1) in walls:
                row += "#"
            elif [r, c] in boxes:
                row += "["
            elif [r, c - 1] in boxes:
                row += "]"
            elif [r, c] == robot:
                row += "@"
            else:
                row += "."
        board += row + '\n'
    print(board + "\n\n" + inp[1][step], step)
    wait = input()
step = 0
for move in moves:
    canmove = can_move(robot, move, False)
    if canmove:
        robot = [robot[0] + move[0], robot[1] + move[1]]
        if robot in boxes:
            move_boxes(robot, move)
        elif [robot[0], robot[1] - 1] in boxes:
            move_boxes([robot[0], robot[1] - 1], move)
    step += 1
p2 = 0
for box in boxes:
    p2 += box[0] * 100 + box[1]
print(p2)
