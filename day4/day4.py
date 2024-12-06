from aocd import get_data
inp = get_data(day=4, year=2015)
import hashlib
found1 = False
i = 0
while True:
    val = int(hashlib.md5(str.encode(inp + str(i))).hexdigest(), 16)
    if val <= int("0xfffffffffffffffffffffffffff", 16):
        if not found1:
            print(i)
            found1 = True
        if val <= int("0xffffffffffffffffffffffffff", 16):
            print(i)
            break
    i += 1
