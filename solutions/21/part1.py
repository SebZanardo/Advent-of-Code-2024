import sys


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

with open(path, "r") as f:
    for line in f.readlines():
        pass

print(f"Solution:\n{None}")
