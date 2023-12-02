import os


def part1(lines):
    return 0


def part2(lines):
    return 0


with open(os.path.join(os.path.dirname(__file__), 'D03_Test.txt'), 'r') as file:
    input_lines = file.readlines()

sum_of_calibration = part1(input_lines)
print("Part 1:", sum_of_calibration)

sum_of_calibration = part2(input_lines)
print("Part 2:", sum_of_calibration)
