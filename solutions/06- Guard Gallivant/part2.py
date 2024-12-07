import sys


def get_visited(
    map: list[list[str]],
    start_x: int,
    start_y: int
) -> set[tuple[int, int]]:
    x = start_x
    y = start_y
    dir = 0  # Up
    visited = set()
    visited.add((x, y))

    # Simulate
    while True:
        new_x = x + DIRECTIONS[dir][0]
        new_y = y + DIRECTIONS[dir][1]

        if not inside_map(new_x, new_y, width, height):
            break

        # Change direction
        if map[new_y][new_x] == WALL:
            dir += 1
            dir %= len(DIRECTIONS)
            continue

        x = new_x
        y = new_y
        visited.add((x, y))

    return visited


def is_loop(map: list[list[str]], start_x: int, start_y: int) -> bool:
    x = start_x
    y = start_y
    dir = 0  # Up

    # Record x, y and direction in set
    visited = set()
    visited.add((x, y, dir))

    # Simulate
    while True:
        new_x = x + DIRECTIONS[dir][0]
        new_y = y + DIRECTIONS[dir][1]

        if not inside_map(new_x, new_y, width, height):
            break

        # Change direction
        if map[new_y][new_x] == WALL:
            dir += 1
            dir %= len(DIRECTIONS)
            continue

        x = new_x
        y = new_y

        # We have looped if in the same position facing the same direction
        if (x, y, dir) in visited:
            return True

        visited.add((x, y, dir))

    return False


def inside_map(x, y, max_x, max_y) -> bool:
    return x >= 0 and x < max_x and y >= 0 and y < max_y


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

# Character constants
GUARD = '^'
EMPTY = '.'
WALL = '#'

# Order is important
DIRECTIONS = ((0, -1), (1, 0), (0, 1), (-1, 0))


# Parse the input into a 2D array of characters and find start position
map = []
start_x = -1
start_y = -1
with open(path, "r") as f:
    for y, line in enumerate(f.readlines()):
        row = []
        for x, char in enumerate(line.strip()):
            if char == GUARD:
                start_x = x
                start_y = y
                row.append(EMPTY)
                continue
            row.append(char)
        map.append(row)

width = len(map[0])
height = len(map)

# Only need to try place a blocker on every square that we walk over
squares_to_try = get_visited(map, start_x, start_y)

# Count number of positions that cause a loop
loop_placements = 0
for square in squares_to_try:
    x, y = square

    # Don't try start position
    if y == start_y and x == start_x:
        continue

    map[y][x] = WALL

    if is_loop(map, start_x, start_y):
        loop_placements += 1

    map[y][x] = EMPTY

print(f"Solution:\n{loop_placements}")
