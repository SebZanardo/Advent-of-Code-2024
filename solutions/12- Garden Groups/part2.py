import sys
from collections import defaultdict


DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

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

straight_map = defaultdict(int)
for key, val in perimeter_map.items():
    while val:
        straight_map[key] += 1
        open = [val.pop()]
        while open:
            x, y, d = open.pop()

            # If left or right check up and down
            if d == 0 or d == 1:
                for y_change in (1, -1):
                    ny = y + y_change
                    new_pos = (x, ny, d)

                    if new_pos in val:
                        val.remove(new_pos)
                        open.append(new_pos)

            # If down or up check left and right
            elif d == 2 or d == 3:
                for x_change in (1, -1):
                    nx = x + x_change
                    new_pos = (nx, y, d)

                    if new_pos in val:
                        val.remove(new_pos)
                        open.append(new_pos)

total_price = 0
for key in regions.keys():
    area = len(regions[key])
    straight = straight_map[key]
    total_price += area * straight

print(f"Solution:\n{total_price}")
