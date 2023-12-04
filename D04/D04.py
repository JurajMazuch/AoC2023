import os
import re


def part1(scratchcards_pile):
    points_sum = 0
    for scratchcard in scratchcards_pile:
        points = 0
        scratchcard = re.sub(r'Card \d+: ', '', scratchcard)
        winning_numbers = re.findall(r'\d+', scratchcard.split('|')[0])
        my_numbers = re.findall(r'\d+', scratchcard.split('|')[1])

        for number in set(winning_numbers) & set(my_numbers):
            points = max(1, points * 2)

        points_sum += points
    return points_sum


def part2(lines):
    return 0


with open(os.path.join(os.path.dirname(__file__), 'D04_Test.txt'), 'r') as file:
    input_lines = file.readlines()

print("Part 1:", part1(input_lines))
print("Part 2:", part2(input_lines))
