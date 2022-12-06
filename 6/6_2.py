with open("6_1.txt") as f:
    input = f.read()

p1 = 0
p2 = 13

while p2 < len(input):
    temp = set(input[p1:p2+1])
    if len(temp) == 14:
        res = p2+1
        break

    p1 += 1
    p2 += 1

print(res)