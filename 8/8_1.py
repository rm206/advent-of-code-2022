with open("8_1.txt") as f:
    input = f.read()

trees = [[int(c) for c in row] for row in input.split()]

max_lefts = [[0 for i in row] for row in trees]
max_rights = [[0 for i in row] for row in trees]
max_ups = [[0 for i in row] for row in trees]
max_downs = [[0 for i in row] for row in trees]

for i, row in enumerate(trees):
    max_encountered = max_lefts[i][0]
    for tree_num, tree_len in enumerate(row):
        max_lefts[i][tree_num] = max_encountered
        if tree_len > max_encountered:
            max_encountered = tree_len

for i, row in enumerate(trees):
    max_encountered = max_rights[i][-1]
    for j in range(len(row)-1, -1, -1):
        max_rights[i][j] = max_encountered
        if trees[i][j] > max_encountered:
            max_encountered = trees[i][j]

for col_num in range(len(trees[0])):
    max_encountered = max_ups[0][col_num]
    for row_num, tree_len in enumerate([i[col_num] for i in trees]):
        max_ups[row_num][col_num] = max_encountered
        if tree_len > max_encountered:
            max_encountered = tree_len

for col_num in range(len(trees[0])):
    max_encountered = max_downs[-1][col_num]
    column = [i[col_num] for i in trees]
    for row_num in range(len(column)-1, -1, -1):
        max_downs[row_num][col_num] = max_encountered
        if trees[row_num][col_num] > max_encountered:
            max_encountered = trees[row_num][col_num]

res = 0
for i in range(1, len(trees)-1):
    for j in range(1, len(trees[0])-1):
        if (trees[i][j] > max_ups[i][j] or
            trees[i][j] > max_downs[i][j] or
            trees[i][j] > max_lefts[i][j] or
            trees[i][j] > max_rights[i][j]):
           
           res += 1

numRows = len(trees)
numCols = len(trees[0])
for i in range(len(trees)):
    for j in range(len(trees[0])):
        if (i == 0 or j == 0 or i == numRows - 1  or j == numCols - 1):
            res += 1

print(res)