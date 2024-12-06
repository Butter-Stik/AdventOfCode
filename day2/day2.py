from aocd import get_data
inp = get_data(day=2, year=2015).splitlines()
p1 = 0
p2 = 0
for box in inp:
    l, w, h = box.split('x')
    l = int(l)
    w = int(w)
    h = int(h)
    s1 = l * w
    s2 = l * h
    s3 = w * h
    sides = [l, w, h]
    p1 += (2 * s1) + (2 * s2) + (2 * s3) + min(s1, s2, s3)
    sides.remove(max(sides))
    p2 += (sides[0] * 2 + sides[1] * 2) + l * w * h
print(p1, p2)
