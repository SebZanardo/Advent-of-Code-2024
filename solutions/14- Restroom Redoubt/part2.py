import sys


print("This problem requires a human to solve!")
print("Keep pressing [ENTER] until a christmas tree appears in the terminal")
print("The number above that image will be your answer")


WIDTH = 101
HEIGHT = 103


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

robots = []
with open(path, "r") as f:
    for line in f.readlines():
        parts = line.strip().split()

        px, py = map(int, parts[0][2:].split(','))
        vx, vy = map(int, parts[1][2:].split(','))

        robots.append((px, py, vx, vy))

# Simulate
counter = 0
while True:
    counter += 1
    bathroom_map = [[' ' for x in range(WIDTH)] for y in range(HEIGHT)]
    for i, robot in enumerate(robots):
        px, py, vx, vy = robot

        px += vx
        px %= WIDTH
        py += vy
        py %= HEIGHT

        bathroom_map[py][px] = '#'
        robots[i] = (px, py, vx, vy)

    print(counter)
    for row in bathroom_map:
        print(' '.join(row))

    if input():
        break

print(f"Solution:\n{counter}")
