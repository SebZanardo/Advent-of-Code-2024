import sys


WALL = '#'
EMPTY = '.'
START = 'S'
END = 'E'

MOVE_SCORE = 1
TURN_SCORE = 1000
DIRECTIONS = ((0, -1), (1, 0), (0, 1), (-1, 0))


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

reindeer_maze = []
start_x = -1
start_y = -1
end_x = -1
end_y = -1
with open(path, "r") as f:
    for y, line in enumerate(f.readlines()):
        row = []
        for x, char in enumerate(line.strip()):
            if char == START:
                start_x = x
                start_y = y
                row.append(EMPTY)
            elif char == END:
                end_x = x
                end_y = y
                row.append(EMPTY)
            else:
                row.append(char)
        reindeer_maze.append(row)

width = len(reindeer_maze[0])
height = len(reindeer_maze)

best_scores = [[-1 for x in range(width)] for y in range(height)]
open = [(start_x, start_y, 1, 0)]

while open:
    x, y, current_dir_index, score = open.pop()

    for dir_index, dir in enumerate(DIRECTIONS):
        if (dir_index + 2) % 4 == current_dir_index:
            continue

        nx = x + dir[0]
        ny = y + dir[1]

        if nx < 0 or nx >= width or ny < 0 or ny >= height:
            continue

        if reindeer_maze[ny][nx] == WALL:
            continue

        new_score = score + MOVE_SCORE

        if current_dir_index != dir_index:
            new_score += TURN_SCORE

        if best_scores[ny][nx] == -1 or new_score < best_scores[ny][nx]:
            best_scores[ny][nx] = new_score
            open.append((nx, ny, dir_index, new_score))

print(f"Solution:\n{best_scores[end_y][end_x]}")
