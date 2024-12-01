import sys


# Try to read path to an input file from command line argument
# i.e. python3 main.py _filepath_
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

with open(path, "r") as f:
    for line in f.readlines():
        pass

print(f"Part 1 Solution:\n{None}")
print(f"Part 2 Solution:\n{None}")
