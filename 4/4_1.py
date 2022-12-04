with open("4_1.txt") as f:
    lines = f.read()

assignments = lines.split("\n")

counter = 0

for curr in assignments:
    split_str = curr.split("-")
    num1_1 = int(split_str[0])
    str23 = split_str[1].split(",")
    num1_2 = int(str23[0])
    num2_1 = int(str23[1])
    num2_2 = int(split_str[2])

    if (num2_1 >= num1_1 and num2_2 <= num1_2) or (num1_1 >= num2_1 and num1_2 <= num2_2):
        counter += 1

print(counter)