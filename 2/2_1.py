def assign_score_default(c):
    if c == 'X':
        return 1
    if c == 'Y':
        return 2
    if c == 'Z':
        return 3

def assign_score_win_lose(arr):
    opponent = arr[0]
    you = arr[2]

    if opponent == 'A':
        if you == 'X':
            return 3
        if you == 'Y':
            return 6
        else:
            return 0
    
    if opponent == 'B':
        if you == 'X':
            return 0
        if you == 'Y':
            return 3
        if you == 'Z':
            return 6
    
    else:
        if you == 'X':
            return 6
        if you == 'Y':
            return 0
        else:
            return 3

with open("2/2_1.txt") as f:
    lines = f.read()

games = lines.split("\n")

total_score = 0

for curr in games:
    total_score += assign_score_win_lose(curr) + assign_score_default(curr[2])

print(total_score)