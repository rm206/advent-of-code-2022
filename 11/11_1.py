from collections import defaultdict

with open("11_1.txt") as f:
    input = f.read()

def populate() -> None:
    global monkey_items
    global monkey_op
    global monkey_test
    global monkey_if_true
    global monkey_if_false
    global monkey_inspect_counter

    split1 = input.split("\n\n")
    for index, curr in enumerate(split1):
        monkey_items[index] = [int(i) for i in curr.split("\n")[1][curr.split("\n")[1].find(": ")+2:].split(",")]
        monkey_op[index] = curr.split("\n")[2][curr.split("\n")[2].find("old"):]
        monkey_test[index] = int(curr.split("\n")[3][-2:])
        monkey_if_true[index] = int(curr.split("\n")[4][-1])
        monkey_if_false[index] = int(curr.split("\n")[5][-1])
        monkey_inspect_counter[index] = 0

def start_round() -> None:
    global monkey_items
    global monkey_op
    global monkey_test
    global monkey_if_true
    global monkey_if_false
    global monkey_inspect_counter

    for curr_monkey in range(len(monkey_items)):
        if len(monkey_items[curr_monkey]) == 0:
            continue
        while len(monkey_items[curr_monkey]) != 0:
            monkey_inspect_counter[curr_monkey] += 1
            old = monkey_items[curr_monkey].pop(0)
            worry_level = eval(monkey_op[curr_monkey])
            worry_level = worry_level // 3
            if worry_level % monkey_test[curr_monkey] == 0:
                monkey_items[monkey_if_true[curr_monkey]].append(worry_level)
            else:
                monkey_items[monkey_if_false[curr_monkey]].append(worry_level)


monkey_items = defaultdict(list)
monkey_op = {}
monkey_test = {}
monkey_if_true = {}
monkey_if_false = {}
monkey_inspect_counter = {}

populate()

for i in range(20):
    start_round()

print(sorted(monkey_inspect_counter.values(), reverse=True)[0] * sorted(monkey_inspect_counter.values(), reverse=True)[1])