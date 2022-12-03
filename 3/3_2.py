with open("3_1.txt") as f:
    lines = f.read()

rucksacks = lines.split("\n")

i = 0
total_score = 0

while i < len(rucksacks):
    curr = rucksacks[i : i + 3]
    set1 = set(curr[0])
    set2 = set(curr[1])
    set3 = set(curr[2])

    common_elt = list(set1 & set2 & set3)[0]

    if common_elt.islower():
        total_score += ord(common_elt) - 96
    else:
        total_score += ord(common_elt) - 38
    
    i += 3

print(total_score)