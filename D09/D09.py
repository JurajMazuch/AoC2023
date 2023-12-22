import os


def part1(data):
    sum_of_numbers = 0
    for line in data.split('\n'):
        sequence = list(map(int, line.split(' ')))
        next_number = sequence[-1]

        while any(s != 0 for s in sequence):
            sequence = [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]
            next_number += sequence[-1]

        sum_of_numbers += next_number

    return sum_of_numbers


def part2(data):
    sum_of_numbers = 0
    for line in data.split('\n'):
        sequence = list(map(int, line.split(' ')))
        first_numbers = [sequence[0]]

        while any(s != 0 for s in sequence):
            sequence = [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]
            first_numbers.append(sequence[0])

        first_numbers.reverse()
        previous_number = 0
        for first_number in first_numbers[1:]:
            previous_number = first_number - previous_number

        sum_of_numbers += previous_number

    return sum_of_numbers


with open(os.path.join(os.path.dirname(__file__), 'D09.txt'), 'r') as file:
    input_data = file.read()

print("Part 1:", part1(input_data))
print("Part 2:", part2(input_data))
