import sys


# Character constants
GUARD = '^'
EMPTY = '.'
WALL = '#'

# Order is important for turning 90 degrees clockwise (x, y) offset
DIRECTIONS = ((0, -1), (1, 0), (0, 1), (-1, 0))


def get_path(
    map: list[list[str]],
    start_x: int,
    start_y: int,
    start_dir: int
) -> list[tuple[int, int, int]]:
    x = start_x
    y = start_y
    dir = start_dir
    path = []
    path.append((x, y, dir))

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
        path.append((x, y, dir))

    return path


def is_loop(
    map: list[list[str]],
    start_x: int,
    start_y: int,
    start_dir: int
) -> bool:
    x = start_x
    y = start_y
    dir = start_dir

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

# Parse the input into a 2D array of characters and find start position
map = []
start_x = -1
start_y = -1
start_dir = 0
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

# Find bounds of map
width = len(map[0])
height = len(map)

# Only need to try place a blocker on every square that we walk over
path = get_path(map, start_x, start_y, start_dir)

# Count number of positions that cause a loop
x, y, dir = path[0]
already_tried = set()
already_tried.add((x, y))

loop_placements = 0
for square in path:
    # Assign last position
    last_x, last_y, last_dir = x, y, dir
    x, y, dir = square

    # Do not place block in position that has already been tried previously!
    if (x, y) in already_tried:
        continue

    map[y][x] = WALL

    # Don't need to traverse from start position and rotation to test for loop
    # Can just setup player at last step before the new obstacle
    if is_loop(map, last_x, last_y, last_dir):
        loop_placements += 1

    map[y][x] = EMPTY

    already_tried.add((x, y))

print(f"Solution:\n{loop_placements}")
