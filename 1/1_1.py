import sys

with open("1_1.txt") as f:
    lines = f.read()

tests = lines.split("\n")

maxsum = -sys.maxsize-1
tempsum = 0

for curr in tests:
    if curr != '':
        t = int(curr)
        tempsum += t
    else:
        maxsum = max(tempsum, maxsum)
        tempsum = 0

maxsum = max(tempsum, maxsum)

print(maxsum)