import sys
import re


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

pattern = r'mul\(([0-9]+),([0-9]+)\)'
operations = []
with open(path, "r") as f:
    for line in f.readlines():
        results = re.findall(pattern, line)
        for r in results:
            operations.append(list(map(int, r)))

total = 0
for multiply in operations:
    total += multiply[0] * multiply[1]


print(f"Solution:\n{total}")
