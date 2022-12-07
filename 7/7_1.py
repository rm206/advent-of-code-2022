from collections import defaultdict

with open("7_1sample.txt") as f:
    input = f.read()

commands = input.split("\n")

dir_subdir = defaultdict(list)
dir_size = {}
curr_stack = []

for curr in commands:
    if curr[0:4] == "$ cd" and curr[-2:] != "..":
        curr_stack.append(curr.split()[2])
        dir_subdir[curr.split()[2]] = []
        dir_size[curr.split()[2]] = 0
        continue
    
    if curr == "$ ls":
        continue

    if curr.split()[0] == "dir":
        dir_subdir[curr_stack[-1]].append(curr.split()[1])
        continue

    if curr == "$ cd ..":
        curr_stack.pop()
        continue
    
    else:
        curr_size = int(curr.split()[0])
        dir_size[curr_stack[-1]] = dir_size.get(curr_stack[-1], 0) + curr_size

def calculate_sizes(dirname):
    if dirname == "/":
        for subdir in dir_subdir["/"]:
            calculate_sizes(subdir)
    else:
        for subdir in dir_subdir[dirname]:
            calculate_sizes(subdir)
            dir_size[dirname] += dir_size[subdir]

calculate_sizes("/")

res = 0

for dir, size in dir_size.items():
    if size < 100000:
        res += size

print(res)