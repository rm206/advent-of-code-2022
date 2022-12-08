with open("8_1.txt") as f:
    input = f.read()

trees = [[int(c) for c in row] for row in input.split()]

total_rows = len(trees)
total_cols = len(trees[0])

def getViewUp(row_num : int, col_num : int) -> int:
    column = [i[col_num] for i in trees]
    
    if column[row_num - 1] >= column[row_num]:
        return 1
    
    to_ret = 0
    curr_index = row_num - 1
    while curr_index >= 0:
        if column[curr_index] >= column[row_num]:
            to_ret += 1
            break
        to_ret += 1
        curr_index -= 1 
    
    return to_ret

def getViewDown(row_num : int, col_num : int) -> int:
    column = [i[col_num] for i in trees]

    if column[row_num + 1] >= column[row_num]:
        return 1
    
    to_ret = 0
    curr_index = row_num + 1
    while curr_index < len(column):
        if column[curr_index] >= column[row_num]:
            to_ret += 1
            break
        to_ret += 1
        curr_index += 1 
    
    return to_ret

def getViewLeft(row_num : int, col_num : int) -> int:
    row = trees[row_num]

    if row[col_num - 1] >= row[col_num]:
        return 1
    
    to_ret = 0
    curr_index = col_num - 1
    while curr_index >= 0:
        if row[curr_index] >= row[col_num]:
            to_ret += 1
            break
        to_ret += 1
        curr_index -= 1 
    
    return to_ret

def getViewRight(row_num : int, col_num : int) -> int:
    row = trees[row_num]

    if row[col_num + 1] >= row[col_num]:
        return 1
    
    to_ret = 0
    curr_index = col_num + 1
    while curr_index < len(row):
        if row[curr_index] >= row[col_num]:
            to_ret += 1
            break
        to_ret += 1
        curr_index += 1 
    
    return to_ret

scenic_scores = [[0 for i in row] for row in trees]

for i in range(1, len(trees)-1):
    for j in range(1, len(trees[0])-1):
        scenic_scores[i][j] = getViewUp(i, j) * getViewDown(i, j) * getViewLeft(i, j) * getViewRight(i, j)

print(max([max(i) for i in scenic_scores]))