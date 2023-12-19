import os
import re


class Race:
    def __init__(self, time, distance):
        self.time = time
        self.distance = distance


def part1(paper):
    times = list(map(int, re.findall(r'\d+', paper.split('\n')[0])))
    distances = list(map(int, re.findall(r'\d+', paper.split('\n')[1])))
    races = [Race(time, distance) for time, distance in zip(times, distances)]

    margin_of_error = 1
    for race in races:
        options_count = 0
        for speed in range(0, race.time):
            distance = speed * (race.time - speed)
            if distance > race.distance:
                options_count += 1
        margin_of_error *= options_count

    return margin_of_error


def part2(paper):
    t = int(''.join(re.findall(r'\d+', paper.split('\n')[0])))
    d = int(''.join(re.findall(r'\d+', paper.split('\n')[1])))
    race = Race(t, d)

    margin_of_error = 1
    options_count = 0
    for speed in range(0, race.time):
        distance = speed * (race.time - speed)
        if distance > race.distance:
            options_count += 1
    margin_of_error *= options_count

    return margin_of_error


with open(os.path.join(os.path.dirname(__file__), 'D06.txt'), 'r') as file:
    input = file.read()

print("Part 1:", part1(input))
print("Part 2:", part2(input))
