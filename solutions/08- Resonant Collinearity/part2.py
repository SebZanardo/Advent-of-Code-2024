import sys
from collections import defaultdict


def inside_map(x: int, y: int, width: int, height: int) -> bool:
    return x >= 0 and x < width and y >= 0 and y < height


EMPTY = '.'


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

# Parse antenna positions into a dictionary, and find width and height of map
width = 0
height = 0
antennas = defaultdict(list)
with open(path, "r") as f:
    for y, row in enumerate(f.readlines()):
        height = y + 1
        for x, char in enumerate(row.strip()):
            width = x + 1
            if char == EMPTY:
                continue
            antennas[char].append((x, y))

# Loop through all antenna pairs in group and calculate antinode positions
antinodes = set()
for antenna, positions in antennas.items():
    for i, pos1 in enumerate(positions):
        for j in range(i + 1, len(positions)):
            pos2 = positions[j]

            # Calculate difference
            x_diff = pos1[0] - pos2[0]
            y_diff = pos1[1] - pos2[1]

            # Find offset position forward
            # Loop in direction until outside map
            offset_x = pos1[0] - x_diff
            offset_y = pos1[1] - y_diff
            while True:
                if inside_map(offset_x, offset_y, width, height):
                    antinodes.add((offset_x, offset_y))
                else:
                    break
                offset_x -= x_diff
                offset_y -= y_diff

            # Find offset position backward
            # Loop in direction until outside map
            offset_x = pos2[0] + x_diff
            offset_y = pos2[1] + y_diff
            while True:
                if inside_map(offset_x, offset_y, width, height):
                    antinodes.add((offset_x, offset_y))
                else:
                    break
                offset_x += x_diff
                offset_y += y_diff

print(f"Solution:\n{len(antinodes)}")
