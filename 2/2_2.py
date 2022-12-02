to_return_mapping = {('A', 0) : 'sci',
                     ('A', 3) : 'rock',
                     ('A', 6) : 'paper',

                     ('B', 0) : 'rock',
                     ('B', 3) : 'paper',
                     ('B', 6) : 'sci',

                     ('C', 0) : 'paper',
                     ('C', 3) : 'sci',
                     ('C', 6) : 'rock'}

def assign_score_win_lose(c):
    if c == 'X':
        return 0
    if c == 'Y':
        return 3
    else:
        return 6

def assign_score_default(c):
    if c == 'rock':
        return 1
    if c == 'paper':
        return 2
    else:
        return 3

def assign_score(c):
    win_draw_lose_score = assign_score_win_lose(c[2])
    return (win_draw_lose_score + assign_score_default(to_return_mapping[(c[0], win_draw_lose_score)]))


with open("2/2_1.txt") as f:
    lines = f.read()

games = lines.split("\n")

total_score = 0

for curr in games:
    total_score += assign_score(curr) 

print(total_score)