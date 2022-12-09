with open("9_1.txt") as f:
    input = f.read()

moves = []
for curr in input.split("\n"):
    moves.append([curr.split()[0], int(curr.split()[1])])

move_dict = {'R' : [0, 1], 'L' : [0, -1], 'U' : [1, 0], 'D' : [-1, 0]}
visited = set({(0,0)})

def touching(t : int, h : int):
    return (abs(t_pos[t][0] - t_pos[h][0]) <= 1
            and abs(t_pos[t][1] - t_pos[h][1]) <= 1)

def update_tail(t, h):
    global t_pos

    diff_x = t_pos[h][0] - t_pos[t][0]
    diff_y = t_pos[h][1] - t_pos[t][1]

    if diff_x == 0:
        if diff_y > 0:
            t_pos[t][1] += 1
        else:
            t_pos[t][1] -= 1
        return
    
    if diff_y == 0:
        if diff_x > 0:
            t_pos[t][0] += 1
        else:
            t_pos[t][0] -= 1
        return
    
    if diff_x == 1 or diff_x == 2:
        if diff_y < 0:
            t_pos[t][0] += 1
            t_pos[t][1] -= 1
        else:
            t_pos[t][0] += 1
            t_pos[t][1] += 1
        return
    
    if diff_x == -1 or diff_x == -2:
        if diff_y > 0:
            t_pos[t][0] -= 1
            t_pos[t][1] += 1
        else:
            t_pos[t][0] -= 1
            t_pos[t][1] -= 1
        return


def update_head(move_dir, move_freq):
    global t_pos
    move_x, move_y = move_dict[move_dir]
    for _ in range(move_freq):
        t_pos[0][0] += move_x
        t_pos[0][1] += move_y
        for tail_id in range(1, 10):
            if not touching(tail_id, tail_id-1):
                update_tail(tail_id, tail_id-1)
            visited.add(tuple(t_pos[9]))

def execute_moves():
    for move in moves:
        update_head(move[0], move[1])

t_pos = [[0, 0] for _ in range(10)]
execute_moves()
print(len(visited))