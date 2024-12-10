import sys
from queue import deque


DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

start_positions = []
map_heights = []
with open(path, "r") as f:
    for y, line in enumerate(f.readlines()):
        row = []
        for x, height in enumerate(line.strip()):
            if height == '0':
                start_positions.append((x, y))
            if height == '.':
                row.append(-1)
            else:
                row.append(int(height))
        map_heights.append(row)

width = len(map_heights[0])
height = len(map_heights)

total_branches = 0
for start in start_positions:
    branches = 0
    open = deque()
    open.append(start)

    while open:
        x, y = open.pop()

        valid_dirs = 0
        for dir in DIRECTIONS:
            new_x = x + dir[0]
            new_y = y + dir[1]

            if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height:
                continue

            current_height = map_heights[y][x]
            new_height = map_heights[new_y][new_x]

            if (new_height - current_height) != 1:
                continue

            if new_height == 9:
                branches += 1
                continue

            open.append((new_x, new_y))

    total_branches += branches

print(f"Solution:\n{total_branches}")
