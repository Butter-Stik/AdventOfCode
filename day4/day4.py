from aocd import get_data
inp = get_data(day=4, year=2024).splitlines()
lettertonum = {
    'X': 3,
    'M': 2,
    'A': 1,
    'S': 0
}
size = []
def search(x, y, dir):
    curr = 3
    xx, yy = dir
    while curr > 0:
        _x = x + xx
        _y = y + yy
        if (_x == -1) or (_x == size + 1) or (_y == -1) or (_y == size + 1):
            return 0
        if inp[_y][_x] == curr - 1:
            curr -= 1
            x += xx
            y += yy
            if curr == 0:
                return 1
        else:
            return 0
def xsearch(x, y):
    if (x == 0) or (x == size) or (y ==  0) or (y == size):
        return 0
    tl = inp[y - 1][x - 1]
    tr = inp[y - 1][x + 1]
    bl = inp[y + 1][x - 1]
    br = inp[y + 1][x + 1]
    if tl == 1 or tl == 3:
        return 0
    if tr == 1 or tr == 3:
        return 0
    if bl == 1 or bl == 3:
        return 0
    if br == 1 or br == 3:
        return 0

    if tl == br or tr == bl:
        return 0
    return 1
    
def get_dirs(x, y):
    dirs = []
    left = 0
    right = 0
    top = 0
    bot = 0
    if x >= 3:
        left = -1
    if x <= size - 3:
        right = 1
    if y >= 3:
        top = -1
    if y <= size - 3:
        bot = 1
    for i in range(top, bot + 1):
        for j in range(left, right + 1):
            dirs.append([j, i])
    return dirs

def find_matches(x, y):
    dirs = get_dirs(x, y)
    found = 0
    for dir in dirs:
        found += search(x, y, dir)
    return found

matches = 0
xmas = 0
for i in range(len(inp)):
    inp[i] = list(inp[i])
    for j in range(len(inp[i])):
        inp[i][j] = lettertonum[inp[i][j]]
size = len(inp[i]) - 1
for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j] == 3:
            matches += find_matches(j, i)
        elif inp[i][j] == 1:
            xmas += xsearch(j, i)
print(matches, xmas)
