import sys


print("Sorry this solution is not optimal yet and may take a while to compute")


WALL = '#'
EMPTY = '.'
START = 'S'
END = 'E'

MOVE_SCORE = 1
TURN_SCORE = 1000
DIRECTIONS = ((0, -1), (1, 0), (0, 1), (-1, 0))


def find_best(best_scores: dict[tuple, int], x: int, y: int) -> int:
    lowest = -1

    for i in range(4):
        triple = (x, y, i)
        if triple in best_scores:
            if best_scores[triple] < lowest or lowest == -1:
                lowest = best_scores[triple]

    return lowest


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


# Create a directional flowfield using a DFS
best_scores = {}
best_scores[(start_x, start_y, 1)] = 0
open_nodes = [(start_x, start_y, 1)]

while open_nodes:
    x, y, current_dir_index = open_nodes.pop()

    for dir_index, dir in enumerate(DIRECTIONS):
        # Don't need to check for a 180 turn
        if (dir_index + 2) % 4 == current_dir_index:
            continue

        nx = x + dir[0]
        ny = y + dir[1]

        if nx < 0 or nx >= width or ny < 0 or ny >= height:
            continue

        if reindeer_maze[ny][nx] == WALL:
            continue

        new_score = best_scores[(x, y, current_dir_index)] + MOVE_SCORE

        if current_dir_index != dir_index:
            new_score += TURN_SCORE

        if ((nx, ny, dir_index) not in best_scores or
                new_score < best_scores[(nx, ny, dir_index)]):
            best_scores[(nx, ny, dir_index)] = new_score
            open_nodes.append((nx, ny, dir_index))

# Go from end to start traversing flowfield with a DFS
open_nodes = [(end_x, end_y, find_best(best_scores, end_x, end_y))]
unique = set()
unique.add((end_x, end_y))

while open_nodes:
    x, y, score = open_nodes.pop()

    for dir in DIRECTIONS:
        nx = x + dir[0]
        ny = y + dir[1]

        if nx < 0 or nx >= width or ny < 0 or ny >= height:
            continue

        if reindeer_maze[ny][nx] == WALL:
            continue

        if (nx, ny) in unique:
            continue

        for i in range(4):
            if (nx, ny, i) in best_scores:
                best = best_scores[(nx, ny, i)]
                if (best == (score - MOVE_SCORE) or
                        best <= (score - TURN_SCORE - MOVE_SCORE)):
                    open_nodes.append((nx, ny, best))
                    unique.add((nx, ny))

print(f"Solution:\n{len(unique)}")
