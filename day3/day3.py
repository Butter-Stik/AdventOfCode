from aocd import get_data
inp = get_data(day=3, year=2015)
dirs = {
    "^": [0, -1],
    ">": [1, 0],
    "<": [-1, 0],
    "v": [0, 1]
}
visits = [[0, 0]]
robovisits = [[0, 0]]
cell = [0,0]
robocell = [[0, 0], [0, 0]]
n = 0
for dir in inp:
    dir = dirs[dir]
    newcell = [cell[0]+dir[0], cell[1]+dir[1]]
    if newcell not in visits:
        visits.append(newcell)
    cell = newcell
    if n % 2 == 0:
        newcell = [robocell[0][0] + dir[0], robocell[0][1] + dir[1]]
        if newcell not in robovisits:
            robovisits.append(newcell)
        robocell[0] = newcell
    else:
        newcell = [robocell[1][0] + dir[0], robocell[1][1] + dir[1]]
        if newcell not in robovisits:
            robovisits.append(newcell)
        robocell[1] = newcell
    n += 1
print(len(visits), len(robovisits))
