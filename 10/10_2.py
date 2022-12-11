with open("10_1.txt") as f:
    input = f.read()

instructions = input.split("\n")
for curr in range(len(instructions)):
    if instructions[curr].split()[0] == "addx":
        instructions[curr] = [instructions[curr].split()[0], int(instructions[curr].split()[1])]

def update_with_noop():
    global register_X
    global cycle_number
    global required_values
    global sprite

    cycle_number += 1
    if (cycle_number - 1) % 40 in sprite:
        required_values.add(cycle_number - 1)

def update_with_addx(addend):
    global register_X
    global cycle_number
    global required_values
    global sprite

    cycle_number += 1
    if (cycle_number - 1) % 40 in sprite:
        required_values.add(cycle_number - 1)
    cycle_number += 1
    if (cycle_number - 1) % 40 in sprite:
        required_values.add(cycle_number - 1)
    register_X += addend
    sprite = [register_X - 1, register_X, register_X + 1]

register_X = 1
cycle_number = 0
required_values = set({})
sprite = [register_X - 1, register_X, register_X + 1]

for curr in instructions:
    if curr == "noop":
        update_with_noop()
    else:
        update_with_addx(curr[1])

for c in range(cycle_number):
    if c in required_values:
        print("#", end = "")
        if c%40 + 1 in {40, 80, 120, 160, 200}:
            print()
    else:
        print(" ", end = "")
        if c%40 + 1 in {40, 80, 120, 160, 200}:
            print()