import sys


WIDTH = 101
HEIGHT = 103
SECONDS = 100


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

q1 = 0
q2 = 0
q3 = 0
q4 = 0
for robot in robots:
    px, py, vx, vy = robot

    # Simulate
    for _ in range(SECONDS):
        px += vx
        px %= WIDTH
        py += vy
        py %= HEIGHT

    # Calculate which quadrant the robot is in and increment counter
    if px == WIDTH // 2:
        continue

    if py == HEIGHT // 2:
        continue

    if px <= WIDTH / 2 and py <= HEIGHT / 2:
        q1 += 1

    elif px >= WIDTH / 2 and py <= HEIGHT / 2:
        q2 += 1

    elif px <= WIDTH / 2 and py >= HEIGHT / 2:
        q3 += 1

    elif px >= WIDTH / 2 and py >= HEIGHT / 2:
        q4 += 1

print(f"Solution:\n{q1 * q2 * q3 * q4}")
