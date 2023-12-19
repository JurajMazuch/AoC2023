import os
import re


def part1(scratchcards_pile):
    points_sum = 0
    for scratchcard in scratchcards_pile:
        winning_numbers = set(re.findall(r'\d+', scratchcard.replace(':', '|').split('|')[1]))
        my_numbers = set(re.findall(r'\d+', scratchcard.replace(':', '|').split('|')[2]))

        my_winning_numbers_count = len(winning_numbers & my_numbers)

        if my_winning_numbers_count > 0:
            points_sum += pow(2, my_winning_numbers_count - 1)

    return points_sum


def part2(scratchcards_pile, i):
    scratchcard = scratchcards_pile[i - 1]
    winning_numbers = set(re.findall(r'\d+', scratchcard.replace(':', '|').split('|')[1]))
    my_numbers = set(re.findall(r'\d+', scratchcard.replace(':', '|').split('|')[2]))

    scratchcards_count = len(winning_numbers & my_numbers)

    for j in range(1, scratchcards_count + 1):
        scratchcards_count += part2(scratchcards_pile, i + j)

    return scratchcards_count


with open(os.path.join(os.path.dirname(__file__), 'D04.txt'), 'r') as file:
    input_lines = file.readlines()

print("Part 1:", part1(input_lines))

scratchcards_count = len(input_lines)
for i in range(1, scratchcards_count + 1):
    scratchcards_count += part2(input_lines, i)
print("Part 2:", scratchcards_count)
