import sys


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

filesystem = []
with open(path, "r") as f:
    files = list(map(int, list(f.readline().strip())))
    is_block = True
    for i in range(len(files)):
        if is_block:
            block_size = files[i]
            filesystem += [i//2] * block_size
            is_block = False
        else:
            free_space = files[i]
            filesystem += [-1] * free_space
            is_block = True

left = 0
right = len(filesystem) - 1
while left < right:
    # We have a space to fill
    if filesystem[left] == -1:
        # If right pointer is not free space move down
        while right > left and filesystem[right] == -1:
            right -= 1

        if right <= left:
            break

        filesystem[left] = filesystem[right]
        filesystem[right] = -1

    left += 1

check_sum = 0
for i, id in enumerate(filesystem):
    if id == -1:
        break
    check_sum += id * i

print(f"Solution:\n{check_sum}")
