import sys
from collections import Counter


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

# Initialise a counting hashmap for left and right lists
left = Counter()
right = Counter()

# Parse input file adding integers to left and right hashmaps
with open(path, "r") as f:
    for line in f.readlines():
        l, r = map(int, line.split())
        left[l] += 1
        right[r] += 1

# Calculate similarity score
similarity_score = 0
for num, occurences in left.items():
    similarity_score += num * right[num] * occurences

print(f"Solution:\n{similarity_score}")
