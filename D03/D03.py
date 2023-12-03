import os
import re


def is_valid_symbol(symbol):
    return not (symbol.isdigit() or symbol in {'.', '\n'})


def is_valid_position(row, col, max_row, max_col):
    return 0 <= row < max_row and 0 <= col < max_col


def is_valid_part_number(schematic, row, part_number_start, part_number_end):
    for col in range(part_number_start, part_number_end):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if is_valid_position(row + i, col + j, len(schematic), len(schematic[0])):
                    if is_valid_symbol(schematic[row + i][col + j]):
                        return True
    return False


def part1(schematic):
    part_number_sum = 0

    for row in range(len(schematic)):
        for part_number_match in [(match.group(), match.start(), match.end()) for match in
                                  re.finditer(r'\d+', schematic[row])]:
            part_number = part_number_match[0]
            part_number_start = part_number_match[1]
            part_number_end = part_number_match[2]

            if is_valid_part_number(schematic, row, part_number_start, part_number_end):
                part_number_sum += int(part_number)

    return part_number_sum


def is_adjacent(part_number_start, part_number_end, gear_col):
    return part_number_start - 1 <= gear_col <= part_number_end


def part2(schematic):
    gear_ratios_sum = 0

    for row in range(len(schematic)):
        for gear_col in [index for index, value in enumerate(schematic[row]) if value == '*']:
            gear_ratio = 1
            row_top = max(row - 1, 0)
            row_bottom = min(row + 1, len(schematic))

            adjacent_part_numbers = 0
            for r in range(row_top, row_bottom + 1):
                for part_number in [(match.group(), match.start(), match.end()) for match in
                                    re.finditer(r'\d+', schematic[r])]:
                    if is_adjacent(part_number[1], part_number[2], gear_col):
                        adjacent_part_numbers += 1
                        gear_ratio *= int(part_number[0])

            if adjacent_part_numbers == 2:
                gear_ratios_sum += gear_ratio

    return gear_ratios_sum


with open(os.path.join(os.path.dirname(__file__), 'D03.txt'), 'r') as file:
    input_lines = file.readlines()

print("Part 1:", part1(input_lines))
print("Part 2:", part2(input_lines))
