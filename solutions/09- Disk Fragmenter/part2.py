import sys

print("Sorry this solution is not optimal yet and may take a while to compute")


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

right = len(filesystem) - 1
while right >= 0:
    # We have a block to possibly move
    if filesystem[right] != -1:
        # Evaluate size of block to move
        move_block_size = 0
        block_id = filesystem[right]
        while filesystem[right] == block_id:
            move_block_size += 1
            right -= 1

        # Find space for block to move to
        found = False
        temp_left = 0
        temp_right = 0
        while temp_left < right:
            if filesystem[temp_left] == -1:
                temp_right = temp_left
                while temp_right < len(filesystem) and filesystem[temp_right] == -1 and (temp_right - temp_left) < move_block_size:
                    temp_right += 1

                if temp_right - temp_left >= move_block_size:
                    found = True
                    break
                else:
                    temp_left = temp_right

            temp_left += 1

        # If space, move
        if found:
            for i in range(move_block_size):
                filesystem[temp_left + i] = filesystem[right + i + 1]
                filesystem[right + i + 1] = -1

    else:
        right -= 1

check_sum = 0
for i, id in enumerate(filesystem):
    if id == -1:
        continue
    check_sum += id * i

print(f"Solution:\n{check_sum}")
