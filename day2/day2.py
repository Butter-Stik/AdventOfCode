passed_lines, second_passed_lines = [], []
with open("input.txt", "r") as file:
    inp = file.read().splitlines()

def test(split): 
    for i in range(len(split)):
        split[i] = int(split[i])
    prev = split[0]
    
    inc = True
    passed = True
    if prev > split[1]:
        inc = False
        
    for i in range (1, len(split)):
        n = split[i]
        
        if ((n > prev) and (inc == False)):
            passed = False
        if ((n < prev) and (inc == True)):
            passed = False    
        if (abs(prev - n) == 0):
            passed = False
        if (abs(prev - n) > 3):
            passed = False
        prev = split[i]
    return passed
for line in inp:     
    if test(line.split()):
        passed_lines.append(line.split())
    else:
        passed = False
        for i in range(len(line.split())):
            l = line.split()
            l.pop(i)
            if test(l):
                passed = True
        if passed:
            second_passed_lines.append(line.split())
print(len(passed_lines), len(passed_lines) + len(second_passed_lines))
