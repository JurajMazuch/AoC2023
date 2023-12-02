import os

word_to_digit = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
}


def find_first_digit(input_string):
    digit = next((int(char) for char in input_string if char.isdigit()), None)
    return digit


def get_calibration_sum(lines):
    calibration_sum = 0

    for line in lines:
        first_digit = find_first_digit(line)
        last_digit = find_first_digit(line[::-1])

        calibration_sum += int(str(first_digit) + str(last_digit))

    return calibration_sum


def get_calibration_sum_2(lines):
    calibration_sum = 0

    for line in lines:
        first_occurrence = None
        last_occurrence = None
        first_position = len(line) + 1
        last_position = -1

        for word in word_to_digit.keys():
            index = line.find(word)
            while index != -1:
                if index < first_position:
                    first_position = index
                    first_occurrence = word
                if index > last_position:
                    last_position = index
                    last_occurrence = word
                index = line.find(word, index + 1)

        first_digit = word_to_digit.get(first_occurrence)
        last_digit = word_to_digit.get(last_occurrence)

        calibration_sum += int(first_digit + last_digit)

    return calibration_sum


with open(os.path.join(os.path.dirname(__file__), 'D01.txt'), 'r') as file:
    input_lines = file.readlines()

sum_of_calibration = get_calibration_sum(input_lines)
print("Part 1:", sum_of_calibration)

sum_of_calibration = get_calibration_sum_2(input_lines)
print("Part 2:", sum_of_calibration)
