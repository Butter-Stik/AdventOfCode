from aocd import get_data
import re
print(sum([int(num[0]) * int(num[1]) for num in re.findall("mul\((\d+),(\d+)\)", get_data(day=3, year=2024))]))
