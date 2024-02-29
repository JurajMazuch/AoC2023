import os
import re


def find_substring(main_string, substring, start_position):
    for i in range(start_position, len(main_string) - len(substring) + 1):
        match = True
        for j in range(len(substring)):
            if main_string[i + j] != substring[j] and main_string[i + j] != '?':
                match = False
                break
        if match:
            return i
    return -1


def get_arrangement_count(condition, damaged_groups, pos, pattern):
    damaged_group_str = '.' + '#' * damaged_groups[0] + '.'
    arrangement_count = 0
    group_pattern = '(?=' + damaged_group_str.replace('.', '[\\.\\?]').replace('#', '[#\\?]') + ')'
    for pos in [int(match.start()) for match in re.finditer(group_pattern, condition)]:
        arrangement = condition[:pos] + damaged_group_str + condition[pos + len(damaged_group_str):]

        if len(damaged_groups) == 1:
            if pattern.match(arrangement.replace("?", ".")):
                arrangement_count += 1
        else:
            arrangement_count += get_arrangement_count(arrangement, damaged_groups[1:], pos + 1, pattern)

    return arrangement_count


def generate_check_pattern(damaged_groups):
    return r"^\.*" + r''.join(r"#{" + str(g) + r"}\.+" for g in damaged_groups) + r"$"


def part1(data):
    total_arrangement_count = 0

    for row in data.split('\n'):
        parts = row.split()
        condition = f".{parts[0]}."
        damaged_groups = list(map(int, parts[1].split(',')))

        pattern = re.compile(generate_check_pattern(damaged_groups))

        total_arrangement_count += get_arrangement_count(condition, damaged_groups, 0, pattern)

    return total_arrangement_count


def part2(data):
    total_arrangement_count = 0

    for row in data.split('\n'):
        parts = row.split()
        condition = f".{'?'.join([parts[0]] * 5)}."
        damaged_groups = list(map(int, parts[1].split(','))) * 5

        pattern = re.compile(generate_check_pattern(damaged_groups))

        total_arrangement_count += get_arrangement_count(condition, damaged_groups, 0, pattern)

    return total_arrangement_count


with open(os.path.join(os.path.dirname(__file__), 'D12_Test.txt'), 'r') as file:
    input_data = file.read()

print("Part 1:", part1(input_data))
print("Part 2:", part2(input_data))
