import sys

with open("1_1.txt") as f:
    lines = f.read()

tests = lines.split("\n")

tempsum = 0
sums = set({})

for curr in tests:
    if curr != '':
        t = int(curr)
        tempsum += t
    else:
        sums.add(tempsum)
        tempsum = 0

sums.add(tempsum)

top3sum = 0

for i in range(3):
    tempmax = max(sums)
    top3sum += tempmax
    sums.remove(tempmax)

print(top3sum)