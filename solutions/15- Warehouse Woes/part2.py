import sys


CHAR_WALL = '#'
CHAR_BOX = 'O'
CHAR_EMPTY = '.'
CHAR_ROBOT = '@'
CHAR_NORTH = '^'
CHAR_EAST = '>'
CHAR_SOUTH = 'v'
CHAR_WEST = '<'
CHAR_LEFT_BOX = '['
CHAR_RIGHT_BOX = ']'

# North, East, South, West
DIRECTIONS = ((0, -1), (1, 0), (0, 1), (-1, 0))


# Not needed as there is a wall surrounding warehouse on all sides
# def inside_bounds(x: int, y: int, width: int, height: int) -> bool:
#     return x >= 0 and x < width and y >= 0 and y < height


def push_boxes_horizontally(
    warehouse: list[list[str]],
    bx: int,
    by: int,
    dx: int
) -> bool:
    valid = False
    bnx = bx

    # If pushing boxes right will be pushing [ side, left is pushing ] side
    while True:
        bnx += dx * 2

        tile = warehouse[by][bnx]

        if tile == CHAR_EMPTY:
            valid = True
            break

        if tile == CHAR_WALL:
            break

    # Perform box/boxes move
    if valid:
        while bnx != bx:
            warehouse[by][bnx] = warehouse[by][bnx - dx]
            bnx -= dx
        warehouse[by][bx] = CHAR_EMPTY

    return valid


def push_boxes_vertically(
    warehouse: list[list[str]],
    bx: int,
    by: int,
    dy: int
) -> bool:
    valid = True

    # bx, by = left side of box
    if warehouse[by][bx] == CHAR_RIGHT_BOX:
        bx -= 1

    boxes_to_move = []
    stack = [(bx, by)]
    seen = set()
    seen.add((bx, by))
    while stack:
        x, y = stack.pop()

        ny = y + dy

        left = warehouse[ny][x]
        right = warehouse[ny][x + 1]

        if left == CHAR_WALL or right == CHAR_WALL:
            valid = False
            break

        # []
        # []
        if left == CHAR_LEFT_BOX and (x, ny) not in seen:
            stack.append((x, ny))
            seen.add((x, ny))

        # []    @
        #  []  []
        #   @ []
        elif left == CHAR_RIGHT_BOX and (x - 1, ny) not in seen:
            stack.append((x - 1, ny))
            seen.add((x - 1, ny))

        #  [] @
        # []  []
        # @    []
        if right == CHAR_LEFT_BOX and (x + 1, ny) not in seen:
            stack.append((x + 1, ny))
            seen.add((x + 1, ny))

        boxes_to_move.append((x, y))

    if valid:
        boxes_to_move.sort(key=lambda x: x[1])
        if dy == 1:
            boxes_to_move.reverse()
        for (x, y) in boxes_to_move:
            warehouse[y + dy][x] = CHAR_LEFT_BOX
            warehouse[y + dy][x + 1] = CHAR_RIGHT_BOX
            warehouse[y][x] = CHAR_EMPTY
            warehouse[y][x + 1] = CHAR_EMPTY

    return valid


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
                robot_x = x * 2
                robot_y = y
                row.append(CHAR_EMPTY)
                row.append(CHAR_EMPTY)
            elif char == CHAR_BOX:
                row.append(CHAR_LEFT_BOX)
                row.append(CHAR_RIGHT_BOX)
            else:
                row.append(char)
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

    tile = warehouse[ny][nx]

    # Cannot move into a wall
    if tile == CHAR_WALL:
        continue

    # If empty move player
    if tile == CHAR_EMPTY:
        x = nx
        y = ny

    # Try to push box or boxes
    elif tile == CHAR_LEFT_BOX or tile == CHAR_RIGHT_BOX:
        valid = False

        # Pushing vertically vs horizontally is different logic
        if direction_index == 0 or direction_index == 2:
            valid = push_boxes_vertically(warehouse, nx, ny, dy)
        elif direction_index == 1 or direction_index == 3:
            valid = push_boxes_horizontally(warehouse, nx, ny, dx)

        # Move player
        if valid:
            x = nx
            y = ny

    # warehouse[y][x] = CHAR_ROBOT
    # for row in warehouse:
    #     print(''.join(row))
    # print()
    # warehouse[y][x] = CHAR_EMPTY

# Calculate GPS coordinate sum
gps_coordinate_sum = 0
for y in range(height):
    for x in range(width):
        if warehouse[y][x] != CHAR_LEFT_BOX:
            continue
        gps_coordinate_sum += y * 100 + x

print(f"Solution:\n{gps_coordinate_sum}")
