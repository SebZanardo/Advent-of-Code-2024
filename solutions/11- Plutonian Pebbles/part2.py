import sys
from collections import Counter


BLINKS = 75


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

stones = []
with open(path, "r") as f:
    stones = list(map(int, f.readline().strip().split()))
    stones_map = Counter()
    for stone in stones:
        stones_map[stone] += 1

for _ in range(BLINKS):
    new_stone_map = Counter()

    for stone, count in stones_map.items():
        # Zero
        if stone == 0:
            new_stone_map[1] += count
            continue

        # Even digits
        if len(str(stone)) % 2 == 0:
            middle = len(str(stone)) // 2
            left = str(stone)[:middle]
            right = str(stone)[middle:]
            new_stone_map[int(left)] += count
            new_stone_map[int(right)] += count
            continue

        # None
        new_stone_map[stone * 2024] += count

    stones_map = new_stone_map

print(f"Solution:\n{sum(stones_map.values())}")
