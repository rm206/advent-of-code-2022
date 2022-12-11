with open("10_1.txt") as f:
    input = f.read()

instructions = input.split("\n")
for curr in range(len(instructions)):
    if instructions[curr].split()[0] == "addx":
        instructions[curr] = [instructions[curr].split()[0], int(instructions[curr].split()[1])]

def update_with_noop():
    global register_X
    global cycle_number
    global to_measure_cycles
    global required_values

    cycle_number += 1
    if cycle_number in to_measure_cycles:
        required_values.add(register_X * cycle_number)

def update_with_addx(addend):
    global register_X
    global cycle_number
    global to_measure_cycles
    global required_values

    cycle_number += 1
    if cycle_number in to_measure_cycles:
        required_values.add(register_X * cycle_number)
    cycle_number += 1
    if cycle_number in to_measure_cycles:
        required_values.add(register_X * cycle_number)
    register_X += addend


register_X = 1
cycle_number = 0
to_measure_cycles = {20, 60, 100, 140, 180, 220}
required_values = set({})

for curr in instructions:
    if curr == "noop":
        update_with_noop()
    else:
        update_with_addx(curr[1])

print(sum(required_values))