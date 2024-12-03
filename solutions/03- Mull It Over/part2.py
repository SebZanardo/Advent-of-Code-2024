import sys
import re


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

pattern_remove = r'(don\'t\(\)(.*?)do\(\))'
pattern_remove_end = r'don\'t\(\).*'
pattern = r'mul\(([0-9]+),([0-9]+)\)'

long_line = ''
with open(path, "r") as f:
    for line in f.readlines():
        long_line += line.strip()

# Enable disable
snippet = re.search(pattern_remove, long_line)
while snippet:
    long_line = long_line[:snippet.start()] + long_line[snippet.end():]
    snippet = re.search(pattern_remove, long_line)

# Remove trail
trailing = re.search(pattern_remove_end, long_line)
if trailing:
    long_line = long_line[:trailing.start()] + long_line[trailing.end():]

# Find mul operations
operations = []
results = re.findall(pattern, long_line)
for r in results:
    operations.append(list(map(int, r)))

total = 0
for multiply in operations:
    total += multiply[0] * multiply[1]

print(f"Solution:\n{total}")
