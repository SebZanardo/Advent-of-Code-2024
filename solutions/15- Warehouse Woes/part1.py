import sys


CHAR_WALL = '#'
CHAR_BOX = 'O'
CHAR_EMPTY = '.'
CHAR_ROBOT = '@'
CHAR_NORTH = '^'
CHAR_EAST = '>'
CHAR_SOUTH = 'v'
CHAR_WEST = '<'

# North, East, South, West
DIRECTIONS = ((0, -1), (1, 0), (0, 1), (-1, 0))


def inside_bounds(x: int, y: int, width: int, height: int) -> bool:
    return x >= 0 and x < width and y >= 0 and y < height


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"


robot_x = -1
robot_y = -1
warehouse = []
moves = []
with open(path, "r") as f:
    warehouse_string, moves_string = f.read().split('\n\n')

    # Parse warehouse
    for y, line in enumerate(warehouse_string.split()):
        row = []
        for x, char in enumerate(line):
            if char == CHAR_ROBOT:
                robot_x = x
                robot_y = y
                row.append(CHAR_EMPTY)
            else:
                row.append(char)
        warehouse.append(row)

    # Parse instructions as index into DIRECTIONS array
    for char in moves_string:
        if char == CHAR_NORTH:
            moves.append(0)
        elif char == CHAR_EAST:
            moves.append(1)
        elif char == CHAR_SOUTH:
            moves.append(2)
        elif char == CHAR_WEST:
            moves.append(3)

width = len(warehouse[0])
height = len(warehouse)

# Simulate
x = robot_x
y = robot_y
for direction_index in moves:
    dx, dy = DIRECTIONS[direction_index]

    nx = x + dx
    ny = y + dy

    # Do not move if moving outside map bounds
    if not inside_bounds(nx, ny, width, height):
        continue

    tile = warehouse[ny][nx]

    # Cannot move into a wall
    if tile == CHAR_WALL:
        continue

    if tile == CHAR_EMPTY:
        x = nx
        y = ny

    # Try to push the box or boxes
    elif tile == CHAR_BOX:
        bx = nx
        by = ny

        valid = False
        while True:
            if not inside_bounds(bx, by, width, height):
                break

            tile = warehouse[by][bx]

            if tile == CHAR_EMPTY:
                valid = True
                break

            # Cannot move into a wall
            if tile == CHAR_WALL:
                break

            # If tile is a box then try push it
            bx += dx
            by += dy

        # Move the box/boxes
        if valid:
            while bx != nx or by != ny:
                bnx = bx - dx
                bny = by - dy
                warehouse[by][bx] = warehouse[bny][bnx]
                bx = bnx
                by = bny
            warehouse[by][bx] = CHAR_EMPTY

            x = nx
            y = ny

    # for row in warehouse:
    #     print(''.join(row))
    # print()

# Calculate GPS coordinate sum
gps_coordinate_sum = 0
for y in range(height):
    for x in range(width):
        if warehouse[y][x] != CHAR_BOX:
            continue
        gps_coordinate_sum += y * 100 + x

print(f"Solution:\n{gps_coordinate_sum}")
