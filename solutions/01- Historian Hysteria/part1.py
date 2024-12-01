import sys


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

with open(path, "r") as f:
    left = []
    right = []
    for line in f.readlines():
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)
    left.sort()
    right.sort()

    total_difference = 0
    for i in range(len(left)):
        total_difference += abs(left.pop() - right.pop())

print(f"Solution:\n{total_difference}")
