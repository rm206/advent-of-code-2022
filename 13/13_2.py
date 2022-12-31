import ast
from collections import defaultdict
from functools import cmp_to_key

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

master_dict = defaultdict(list)
for i, curr in enumerate(input.split("\n")):
    if not curr:
        continue
    master_dict[i] = ast.literal_eval(curr)

master_dict[i+1] = [[2]]
master_dict[i+2] = [[6]]

sorted_master_dict = sorted(master_dict.values(), key=cmp_to_key(is_in_correct_order))

index_1 = sorted_master_dict.index([[2]]) + 1
index_2 = sorted_master_dict.index([[6]]) + 1
print(index_1 * index_2)