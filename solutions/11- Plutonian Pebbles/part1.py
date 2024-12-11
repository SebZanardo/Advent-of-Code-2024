import sys


BLINKS = 25


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

stones = []
with open(path, "r") as f:
    stones = list(map(int, f.readline().strip().split()))

for _ in range(BLINKS):
    for i in range(len(stones) - 1, -1, -1):
        stone = stones[i]

        # Zero
        if stone == 0:
            stones[i] = 1
            continue

        # Even digits
        if len(str(stone)) % 2 == 0:
            middle = len(str(stone)) // 2
            left = str(stone)[:middle]
            right = str(stone)[middle:]
            stones[i] = int(left)
            stones.insert(i + 1, int(right))
            continue

        # None
        stones[i] = stone * 2024

print(f"Solution:\n{len(stones)}")
