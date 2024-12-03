import sys
import re


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

# Parse input file into a single string removing newline characters
corrupted_memory = ""
with open(path, "r") as f:
    for line in f.readlines():
        corrupted_memory += line.strip()

# Regex pattern match all non-overlapping instances
pattern_operation = r'mul\(([0-9]+),([0-9]+)\)'
matches = re.findall(pattern_operation, corrupted_memory)

# Calculate total of all multiply instructions
total = 0
for r in matches:
    mul_instruction = list(map(int, r))
    total += mul_instruction[0] * mul_instruction[1]

print(f"Solution:\n{total}")
