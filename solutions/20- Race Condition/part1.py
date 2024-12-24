import sys
from queue import deque
from collections import Counter


EMPTY = '.'
WALL = '#'
START = 'S'
END = 'E'
DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))
MIN_SAVED = 100


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

racetrack = []
sx = 0
sy = 0
ex = 0
ey = 0
with open(path, "r") as f:
    for y, line in enumerate(f.readlines()):
        row = []
        for x, char in enumerate(line.strip()):
            if char == START:
                row.append(EMPTY)
                sx = x
                sy = y
            elif char == END:
                row.append(EMPTY)
                ex = x
                ey = y
            else:
                row.append(char)
        racetrack.append(row)

width = len(racetrack[0])
height = len(racetrack)

# Create map of shortest path to each cell
steps = 0
open_cells = deque()
open_cells.appendleft((sx, sy))
visited = set()
visited.add((sx, sy))
shortest_path = [[-1 for x in range(width)] for y in range(height)]
shortest_path[sy][sx] = 0

while open_cells:
    steps += 1
    for i in range(len(open_cells)):
        x, y = open_cells.pop()

        for dx, dy in DIRECTIONS:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= width or ny < 0 or ny >= height:
                continue

            if racetrack[ny][nx] == WALL:
                continue

            if (nx, ny) not in visited:
                open_cells.appendleft((nx, ny))
                visited.add((nx, ny))
                shortest_path[ny][nx] = steps

cheats = Counter()
# cheat_details = []
for x, y in visited:
    score = shortest_path[y][x]
    for dx, dy in DIRECTIONS:
        nx = x + dx * 2
        ny = y + dy * 2

        if nx < 0 or nx >= width or ny < 0 or ny >= height:
            continue

        if racetrack[ny][nx] == WALL:
            continue

        saved = score - shortest_path[ny][nx] - 2
        if saved >= MIN_SAVED:
            # cheat_details.append((x, y, nx, ny, saved))
            cheats[saved] += 1

# print(cheats)
#
# for row in shortest_path:
#     print('\t'.join(map(str, row)))


print(f"Solution:\n{sum(cheats.values())}")
