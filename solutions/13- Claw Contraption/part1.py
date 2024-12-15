import sys
import re


A_COST = 3
B_COST = 1


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

pattern = '[0-9]+'
prizes = []
with open(path, "r") as f:
    for prize in f.read().split('\n\n'):
        matches = re.findall(pattern, prize)
        prizes.append(list(map(int, matches)))

# Key observation: there is only one solution
# Use the subsitution method to solve for both unknown values a and b
total_tokens = 0
for prize in prizes:
    ax, ay, bx, by, tx, ty = prize

    # Substitution method
    spent_b = ((ty * ax) - (ay * tx)) / (by * ax - bx * ay)

    # No solution, skip
    if int(spent_b) != spent_b:
        continue

    spent_a = (tx - bx * spent_b) / ax

    total_tokens += int(spent_a * A_COST + spent_b * B_COST)

print(f"Solution:\n{total_tokens}")
