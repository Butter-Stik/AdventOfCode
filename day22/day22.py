from aocd import get_data
inp = get_data(day=22,year=2024).splitlines()
MOD = 16777216
p1 = 0
allprices = {}
for n in inp:
    initvalue = int(n)
    n = int(n)
    allprices[initvalue] = [n % 10]
    for i in range(2000):
        n = (n ^ (n << 6)) % MOD
        n = (n ^ (n >> 5)) % MOD
        n = (n ^ (n << 11)) % MOD
        allprices[initvalue].append(n % 10)
    p1 += n
print(p1)
alldiffs = {}
for m in allprices:
    nums = allprices[m]
    alldiffs[m] = []
    for i in range(1, 2001):
        alldiffs[m].append(nums[i] - nums[i - 1])
sequences = {}
sums = {}
for m in alldiffs:
    diffs = alldiffs[m]
    sequences[m] = {}
    for i in range(3, 2000):
        sequence = (diffs[i - 3], diffs[i - 2], diffs[i - 1], diffs[i])
        if sequence not in sequences[m]:
            sequences[m][sequence] = allprices[m][i + 1]
            if sequence in sums:
                sums[sequence] += allprices[m][i + 1]
            else:
                sums[sequence] = allprices[m][i + 1]
p2 = [sums[x] for x in sums]
print(max(p2))
