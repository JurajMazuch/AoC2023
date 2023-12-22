import os


def find_galaxies(image):
    galaxies = []
    for x, row in enumerate(image):
        for y, char in enumerate(row):
            if char == '#':
                galaxies.append((x, y))
    return galaxies


def find_empty_rows_and_columns(galaxies, image_size):
    rows_with_galaxy, cols_with_galaxy = zip(*galaxies)

    empty_rows = set(range(image_size[0])) - set(rows_with_galaxy)
    empty_cols = set(range(image_size[1])) - set(cols_with_galaxy)

    return empty_rows, empty_cols


def insert_rows(coordinates, x_inserted, count):
    return [(x + count - 1, y) if x >= x_inserted else (x, y) for x, y in coordinates]


def insert_columns(coordinates, y_inserted, count):
    return [(x, y + count - 1) if y >= y_inserted else (x, y) for x, y in coordinates]


def manhattan_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


def get_distance_sum(data, void_size):
    image = [list(line) for line in data.split('\n')]
    galaxies = find_galaxies(image)
    empty_rows, empty_columns = find_empty_rows_and_columns(galaxies, (len(image), len(image[0])))

    for row in sorted(empty_rows, reverse=True):
        galaxies = insert_rows(galaxies, row, void_size)

    for col in sorted(empty_columns, reverse=True):
        galaxies = insert_columns(galaxies, col, void_size)

    distance_sum = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            distance_sum += manhattan_distance(galaxies[i], galaxies[j])

    return distance_sum


with open(os.path.join(os.path.dirname(__file__), 'D11.txt'), 'r') as file:
    input_data = file.read()

print("Part 1:", get_distance_sum(input_data, 2))
print("Part 2:", get_distance_sum(input_data, 1000000))
