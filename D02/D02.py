import os
import re


def get_cube_count(game_set, color):
    match = re.search(rf'(\d+) {color}', game_set)
    return int(match.group(1)) if match else 0


def part1(lines, red=12, green=13, blue=14):
    game_sum = 0

    for line in lines:
        game_id = re.search(r'Game (\d+):', line).group(1)
        game_sum += int(game_id)

        for game_set in line.split(';'):
            r = get_cube_count(game_set, 'red')
            g = get_cube_count(game_set, 'green')
            b = get_cube_count(game_set, 'blue')

            if r > red or g > green or b > blue:
                game_sum -= int(game_id)
                break

    return game_sum


def part2(lines):
    power_sum = 0

    for line in lines:
        red = max(int(match.group(1)) if match else 0 for match in re.finditer(r'(\d+) red', line))
        green = max(int(match.group(1)) if match else 0 for match in re.finditer(r'(\d+) green', line))
        blue = max(int(match.group(1)) if match else 0 for match in re.finditer(r'(\d+) blue', line))

        set_power = red * green * blue
        power_sum += set_power

    return power_sum


with open(os.path.join(os.path.dirname(__file__), 'D02.txt'), 'r') as file:
    input_lines = file.readlines()

sum_of_calibration = part1(input_lines)
print("Part 1:", sum_of_calibration)

sum_of_calibration = part2(input_lines)
print("Part 2:", sum_of_calibration)
