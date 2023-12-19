import os
import re
from collections import defaultdict
import math


def get_nodes(data):
    nodes = defaultdict(dict)

    for node in data.split('\n')[2:]:
        m = re.findall(r'\w+', node)
        nodes[m[0]] = {'L': m[1], 'R': m[2]}
    return nodes


def part1(data):
    instructions = [*data.split('\n')[0]]
    nodes = get_nodes(data)

    key = 'AAA'
    steps = 0
    while key != 'ZZZ':
        key = nodes[key][instructions[steps % len(instructions)]]
        steps += 1

    return steps


def part2(data):
    instructions = [*data.split('\n')[0]]
    nodes = get_nodes(data)

    keys = [key for key in nodes if key.endswith('A')]
    steps = [0] * len(keys)

    for i in range(0, len(keys)):
        while not keys[i].endswith('Z'):
            instruction = instructions[steps[i] % len(instructions)]
            keys[i] = nodes[keys[i]][instruction]
            steps[i] += 1

    return math.lcm(*steps)


with open(os.path.join(os.path.dirname(__file__), 'D08.txt'), 'r') as file:
    input_data = file.read()

print("Part 1:", part1(input_data))
print("Part 2:", part2(input_data))
