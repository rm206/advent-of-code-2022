import ast

with open("13_1.txt") as f:
    input = f.read()

def is_in_correct_order(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left < right
    if isinstance(left, list) and isinstance(right, list):
        i = 0
        while i < len(left) and i < len(right):
            if left[i] == right[i]:
                i += 1
                continue
            else:
                return is_in_correct_order(left[i], right[i])
        if i == len(right):
            return True
        else:
            return False
    if isinstance(left, int) != isinstance(right, int):
        if isinstance(left, int):
            left_list = [left]
            return is_in_correct_order(left_list, right)
        if isinstance(right, int):
            right_list = [right]
            return is_in_correct_order(left, right_list)

master_list = []

for curr in input.split("\n\n"):
    sub_list = [ast.literal_eval(curr.split("\n")[0]), ast.literal_eval(curr.split("\n")[1])]
    master_list.append(sub_list)

counter = 0
for i, v in enumerate(master_list):
    if is_in_correct_order(v[0], v[1]):
        counter += (i+1)

print(counter)