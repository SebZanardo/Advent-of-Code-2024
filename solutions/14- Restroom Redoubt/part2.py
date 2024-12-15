import sys


WIDTH = 101
HEIGHT = 103
EMPTY = ' '
ROBOT = '#'
PATTERN = ROBOT * 31


def create_bathroom_map_and_move(
    robots: list[tuple[int, int, int, int]]
) -> list[list[str]]:
    # Create 2D array and draw robots on their cells
    bathroom_map = [[EMPTY for x in range(WIDTH)] for y in range(HEIGHT)]

    for i, robot in enumerate(robots):
        px, py, vx, vy = robot
        bathroom_map[py][px] = ROBOT

        # Move robot and constrain within bounds of map
        px += vx
        px %= WIDTH
        py += vy
        py %= HEIGHT

        robots[i] = (px, py, vx, vy)

    return bathroom_map


def easter_egg(bathroom_map: list[list[str]]) -> bool:
    # Check for the pattern in each row of the map
    for row in bathroom_map:
        if PATTERN in ''.join(row):
            return True

    return False


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

# Parse robots into an array as (x, y, vx, vy)
robots = []
with open(path, "r") as f:
    for line in f.readlines():
        parts = line.strip().split()

        px, py = map(int, parts[0][2:].split(','))
        vx, vy = map(int, parts[1][2:].split(','))

        robots.append((px, py, vx, vy))

# Simulate movement until easter egg detected
seconds_counter = 0
bathroom_map = create_bathroom_map_and_move(robots)
while not easter_egg(bathroom_map):
    bathroom_map = create_bathroom_map_and_move(robots)
    seconds_counter += 1

# Uncomment to see easter egg
# for row in bathroom_map:
#     print(' '.join(row))

print(f"Solution:\n{seconds_counter}")
