from aocd import get_data
import re
from math import floor
inp = get_data(day=13 ,year=2024).split("\n\n")
allnums = [re.findall("\d+", prize) for prize in inp]
def get_tokens(p2):
    tokens = 0
    for numset in allnums:
        numset = [int(num) for num in numset]
        a_x, a_y, b_x, b_y, X, Y = numset
        if p2:
            X += 10000000000000
            Y += 10000000000000
        B = ((Y * a_x) - (X * a_y)) / ((b_y * a_x) - (b_x * a_y))
        A = (X - (B * b_x)) / a_x
        if A != floor(A) or B != floor(B):
            continue
        tokens += (3 * A) + B
    return int(tokens)
print(get_tokens(False), get_tokens(True))
