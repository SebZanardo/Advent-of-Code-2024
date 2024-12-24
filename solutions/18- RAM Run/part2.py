import sys
from queue import deque


WIDTH = 71
HEIGHT = 71
SIMULATE = 1024
DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))


def can_find_end(memory_space: list[list[int]]) -> bool:
    open_nodes = deque()
    open_nodes.append((0, 0))
    visited = set()
    visited.add((0, 0))
    while open_nodes:
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
            return True

    return False


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

blocks = []
with open(path, "r") as f:
    for line in f.readlines():
        blocks.append(tuple(map(int, line.split(','))))

# Simulate the first 1024 steps as we already know it doesn't block
memory_space = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]
for i in range(SIMULATE):
    block_x, block_y = blocks[i]
    memory_space[block_y][block_x] = 1

for i in range(SIMULATE, len(blocks)):
    block_x, block_y = blocks[i]
    memory_space[block_y][block_x] = 1

    if not can_find_end(memory_space):
        break

print(f"Solution:\n{block_x},{block_y}")
