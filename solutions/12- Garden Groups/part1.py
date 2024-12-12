import sys
from collections import defaultdict


DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

# Parse input into 2D array
garden = []
with open(path, "r") as f:
    for y, line in enumerate(f.readlines()):
        garden.append(list(line.strip()))

# Calculate width and height
width = len(garden[0])
height = len(garden)

# Only create region with connected parts
# Floodfill
index = 0
regions = defaultdict(set)
added = set()
for y in range(height):
    for x in range(width):
        if (x, y) in added:
            continue

        char = garden[y][x]

        this_region = set()
        this_region.add((x, y))

        open = []
        open.append((x, y))

        while open:
            lx, ly = open.pop()
            for dir in DIRECTIONS:
                new_x = lx + dir[0]
                new_y = ly + dir[1]

                if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height:
                    continue

                if garden[new_y][new_x] != char:
                    continue

                new_pos = (new_x, new_y)

                if new_pos not in this_region:
                    this_region.add(new_pos)
                    open.append(new_pos)
                    added.add(new_pos)

        regions[index] = this_region
        index += 1


perimeter_map = defaultdict(set)
for key, val in regions.items():
    # Calculate perimeter
    for pos in val:
        x, y = pos

        for i, dir in enumerate(DIRECTIONS):
            new_x = x + dir[0]
            new_y = y + dir[1]

            if (new_x, new_y) in val:
                continue

            if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height:
                perimeter_map[key].add((new_x, new_y, i))
            else:
                perimeter_map[key].add((new_x, new_y, i))

total_price = 0
for key in regions.keys():
    area = len(regions[key])
    perimeter = len(perimeter_map[key])
    total_price += area * perimeter

print(f"Solution:\n{total_price}")
