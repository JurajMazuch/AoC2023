import os
import re


def map_source(source, category):
    for line in category.split('\n')[1:]:
        rng = list(map(int, line.split()))
        destination_range_start, source_range_start, range_length = rng

        if source_range_start <= source <= source_range_start + range_length:
            return destination_range_start - source_range_start + source

    return source


def part1(almanac):
    source_category = [int(seed) for seed in re.findall(r'\d+', almanac.split('\n')[0])]

    for category in almanac.split('\n\n')[1:]:
        source_category = [map_source(source, category) for source in source_category]

    return min(source_category)


def map_source_2(sources, category):
    sources_new = []
    for source in sources:
        residue = [source]
        for line in sorted(category.split('\n')[1:], key=lambda x: int(x.split()[1])):
            rng = list(map(int, line.split()))
            destination_range_start, source_range_start, range_length = rng
            source_range = range(source_range_start, source_range_start + range_length)
            destination_range = range(destination_range_start, destination_range_start + range_length)

            intersection = range(max(source.start, source_range.start), min(source.stop, source_range.stop))
            residue_left = range(source.start, min(source.stop, source_range.start))
            residue_right = range(max(source.start, source_range.stop), source.stop)

            if intersection.start < intersection.stop:
                sources_new.append(range(intersection.start - source_range.start + destination_range.start, intersection.start - source_range.start + destination_range.start + len(intersection)))
                if source in residue:
                    residue.remove(source)

                if residue_right.start < residue_right.stop:
                    sources.append(residue_right)
                if residue_left.start < residue_left.stop:
                    sources_new.append(residue_left)

        sources_new.extend(residue)

    return sources_new


def part2(almanac):
    seeds = [int(seed) for seed in re.findall(r'\d+', almanac.split('\n')[0])]
    source = []
    for i in range(0, len(seeds) - 1, 2):
        source_start = seeds[i]
        source_length = seeds[i + 1]
        source.append(range(source_start, source_start + source_length))

    for category in almanac.split('\n\n')[1:]:
        source = map_source_2(source, category)

    return min(source, key=lambda x: x.start).start


with open(os.path.join(os.path.dirname(__file__), 'D05.txt'), 'r') as file:
    input = file.read()

print("Part 1:", part1(input))
print("Part 2:", part2(input))
