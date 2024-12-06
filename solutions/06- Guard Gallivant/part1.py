import sys


# For debugging a parsing issue I had
# def print_map(map: list[list[str]], visited: set[tuple[int, int]]) -> None:
#     for y in range(len(map)):
#         print(f"{y}\t", end="")
#         for x in range(len(map[0])):
#             if (x, y) in visited:
#                 print("*", end="")
#             else:
#                 print(map[y][x], end="")
#         print()
#     print()


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

    # Mark current square as seen
    visited.add((x, y))

distinct = len(visited)

print(f"Solution:\n{distinct}")
