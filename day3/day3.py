from aocd import get_data
import re
inp = get_data(day=3, year=2024)
instructions = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", inp)
nums = []
numdos = []
do = True
for instruction in instructions:
    found = re.findall("\d+", instruction)
    if found != []:
        nums.append(found)
        if do == True:
            numdos.append(found)
    else:
        if instruction == "don't()":
            do = False
        else:
            do = True
print(instructions)
tot = 0
totdos = 0
for num in nums:
    tot += int(num[0]) * int(num[1])
for num in numdos:
    totdos += int(num[0]) * int(num[1])
print(tot, totdos)
