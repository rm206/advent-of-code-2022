with open("9_1.txt") as f:
    input = f.read()

moves = []
for curr in input.split("\n"):
    moves.append([curr.split()[0], int(curr.split()[1])])

move_dict = {'R' : [0, 1], 'L' : [0, -1], 'U' : [1, 0], 'D' : [-1, 0]}
visited = set({(0,0)})

def touching():
    return (abs(h_pos[0] - t_pos[0]) <= 1
            and abs(h_pos[1] - t_pos[1]) <= 1)

def update_tail():
    global h_pos
    global t_pos

    diff_x = h_pos[0] - t_pos[0]
    diff_y = h_pos[1] - t_pos[1]

    if diff_x == 0:
        if diff_y > 0:
            t_pos[1] += 1
        else:
            t_pos[1] -= 1
        return
    
    if diff_y == 0:
        if diff_x > 0:
            t_pos[0] += 1
        else:
            t_pos[0] -= 1
        return
    
    if diff_x == 1 or diff_x == 2:
        if diff_y < 0:
            t_pos[0] += 1
            t_pos[1] -= 1
        else:
            t_pos[0] += 1
            t_pos[1] += 1
        return
    
    if diff_x == -1 or diff_x == -2:
        if diff_y > 0:
            t_pos[0] -= 1
            t_pos[1] += 1
        else:
            t_pos[0] -= 1
            t_pos[1] -= 1
        return


def update_head(move_dir, move_freq):
    global counter
    global h_pos
    global t_pos
    move_x, move_y = move_dict[move_dir]
    for _ in range(move_freq):
        h_pos[0] += move_x
        h_pos[1] += move_y
        if not touching():
            update_tail()
        visited.add(tuple(t_pos))

def execute_moves():
    for move in moves:
        update_head(move[0], move[1])

counter = 1
h_pos = [0, 0]
t_pos = [0, 0]
execute_moves()
print(len(visited))