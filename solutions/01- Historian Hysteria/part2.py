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

    total = 0
    for num in left:
        total += num * right.count(num)

print(f"Solution:\n{total}")
