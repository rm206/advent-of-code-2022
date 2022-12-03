with open("3_1.txt") as f:
    lines = f.read()

rucksacks = lines.split("\n")

totalscore = 0

for curr in rucksacks:
    splitcurrlen = len(curr)//2
    set1 = set(curr[ : splitcurrlen])
    set2 = set(curr[splitcurrlen : ])
    
    common_elt_list = list(set1 & set2)
    print(common_elt_list)

    if len(common_elt_list) > 0:
        common_elt = common_elt_list[0]
        if common_elt.islower():
            totalscore += ord(common_elt) - 96
        else:
            totalscore += ord(common_elt) - 38

print(totalscore)