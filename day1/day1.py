with open("input.txt", "r") as file:
    inp = file.read().splitlines()
list1, list2, diff, simscore = [], [], 0, 0
for line in inp:
    split_line = line.split()
    list1.append(split_line[0]), list2.append(split_line[1])
list1.sort(), list2.sort()
for i in range(len(list1)): diff += abs(int(list1[i]) - int(list2[i]))
for n in list1: simscore += list2.count(n) * int(n)
print(diff, simscore)
