import sys
from queue import deque


WIDTH = 71
HEIGHT = 71
SIMULATE = 1024
DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

blocks = []
with open(path, "r") as f:
    for line in f.readlines():
        blocks.append(tuple(map(int, line.split(','))))

memory_space = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]
for i in range(SIMULATE):
    block_y, block_x = blocks[i]
    memory_space[block_y][block_x] = 1

open_nodes = deque()
open_nodes.append((0, 0))
visited = set()
visited.add((0, 0))
steps = 0
while open_nodes:
    steps += 1
    for i in range(len(open_nodes)):
        x, y = open_nodes.popleft()

        for (dx, dy) in DIRECTIONS:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= WIDTH or ny < 0 or ny >= HEIGHT:
                continue

            if memory_space[ny][nx]:
                continue

            if (nx, ny) not in visited:
                open_nodes.append((nx, ny))
                visited.add((nx, ny))

    if (WIDTH - 1, HEIGHT - 1) in visited:
        break

print(f"Solution:\n{steps}")
