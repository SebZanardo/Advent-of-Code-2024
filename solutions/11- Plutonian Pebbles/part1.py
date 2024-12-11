import sys
from collections import Counter


# Number of blinks to perform
BLINKS = 25


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

# Parse input file into hashmap
stones_map = Counter()
with open(path, "r") as f:
    for stone in f.readline().strip().split():
        stones_map[int(stone)] += 1

# Simulate blinks, simulating same sized stones in one step
for i in range(BLINKS):
    new_stone_map = Counter()

    for stone, count in stones_map.items():
        # Zero
        if stone == 0:
            new_stone_map[1] += count

        # Even digits
        elif len(str(stone)) % 2 == 0:
            middle = len(str(stone)) // 2
            left = str(stone)[:middle]
            right = str(stone)[middle:]
            new_stone_map[int(left)] += count
            new_stone_map[int(right)] += count
            continue

        # None of the above
        else:
            new_stone_map[stone * 2024] += count

    stones_map = new_stone_map

print(f"Solution:\n{sum(stones_map.values())}")
