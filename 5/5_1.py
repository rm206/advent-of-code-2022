with open("5_1.txt") as f:
    lines = f.read()

input_split = lines.split("\n\n")
stack_strings = input_split[0].split("\n")
moves = input_split[1].split("\n")

num_cols = int(stack_strings[-1][-2])
cols = []
start_col_index = 0
end_col_index = 4

for curr_col in range(num_cols):
    temp = ""
    for curr in stack_strings:
        temp += curr[start_col_index:end_col_index]

    temp = "".join(c for c in temp if c.isalpha())
    cols.append(temp)
    start_col_index += 4
    end_col_index += 4

for i in range(num_cols):
    cols[i] = cols[i][::-1]
    cols[i] = [c for c in cols[i]]

for i in range(len(moves)):
    temp = moves[i].split()
    moves[i] = [int(temp[1]), int(temp[3]), int(temp[5])]

for curr in moves:
    num1 = int(curr[0])
    num2 = int(curr[1]) - 1
    num3 = int(curr[2]) - 1
    for i in range(num1):
        if len(cols[num2]) != 0:
            cols[num3].append(cols[num2].pop(-1))

result = ""

for curr in cols:
    if len(curr)!=0:
        result += curr[-1]

print(result)