import os
from matplotlib.path import Path
import numpy as np


def find_start(grid):
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == 'S':
                return x, y
    return -1, -1


def in_grid(x, y, grid):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def move(x, y, direction):
    direction_offsets = {
        "N": (0, -1),
        "S": (0, 1),
        "W": (-1, 0),
        "E": (1, 0)
    }
    dx, dy = direction_offsets[direction]
    return x + dx, y + dy


def get_path(grid, x_start, y_start, direction):
    pipes = {
        '|': 'NS',
        '-': 'EW',
        'L': 'NE',
        'J': 'NW',
        '7': 'SW',
        'F': 'SE'
    }

    opposite_directions = {
        'W': 'E',
        'E': 'W',
        'N': 'S',
        'S': 'N'
    }

    path = [(x_start, y_start)]
    direction_from = opposite_directions[direction]
    x, y = move(x_start, y_start, direction)

    while (x, y) != (x_start, y_start):
        if not in_grid(x, y, grid):
            return None

        pipe = pipes.get(grid[y][x])
        if direction_from not in pipe:
            return None

        path.append((x, y))

        direction = pipe.replace(direction_from, '')
        direction_from = opposite_directions[direction]
        x, y = move(x, y, direction)
    return path


def part1(grid, x_start, y_start):
    for direction in ['E', 'W', 'S', 'N']:
        path = get_path(grid, x_start, y_start, direction)
        if path is not None:
            return int(len(path) / 2)
    return 0


def part2(grid, x_start, y_start):
    enclosed = 0
    p = []

    for direction in ['E', 'W', 'S', 'N']:
        path = get_path(grid, x_start, y_start, direction)
        if path is not None:
            p = Path(np.array(path))
            break

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if (x, y) in path:
                continue
            if p.contains_point((x, y)):
                enclosed += 1

    return enclosed


with open(os.path.join(os.path.dirname(__file__), 'D10.txt'), 'r') as file:
    data = file.read()

g = [list(line) for line in data.split('\n')]
x0, y0 = find_start(g)
print("Part 1:", part1(g, x0, y0))
print("Part 2:", part2(g, x0, y0))
