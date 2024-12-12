import sys


DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

# Parse input file into 2D integer array and an array of starting positions
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

# Find width and height of map bounds
width = len(map_heights[0])
height = len(map_heights)

# Traverse all trails and count total branches
total_branches = 0
for start in start_positions:
    branches = 0
    open = []
    open.append(start)

    while open:
        x, y = open.pop()

        valid_dirs = 0
        for dir in DIRECTIONS:
            new_x = x + dir[0]
            new_y = y + dir[1]

            # If we are outside of the map bounds, skip
            if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height:
                continue

            current_height = map_heights[y][x]
            new_height = map_heights[new_y][new_x]

            # If we are not stepping up by one in height, skip
            if (new_height - current_height) != 1:
                continue

            # If are at the final height add to branches counter
            if new_height == 9:
                branches += 1
                continue

            open.append((new_x, new_y))

    # Add branches from this starting position to total_branches
    total_branches += branches

print(f"Solution:\n{total_branches}")
