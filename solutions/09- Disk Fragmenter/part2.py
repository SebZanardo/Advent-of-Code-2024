import sys


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

# Parse input into a hashmap for blocks, and a 2D list for free space
# blocks -> {id : (index, size)}
# free_space -> [(index, size), ...]
blocks: dict[int: tuple[int, int]] = {}
free_space: list[tuple[int, int]] = []
with open(path, "r") as f:
    files = list(map(int, list(f.readline().strip())))
    index = 0
    is_block = True
    for i in range(len(files)):
        size = files[i]

        if is_block:
            blocks[i//2] = (index, size)
            is_block = False

        else:
            if size != 0:
                free_space.append((index, size))
            is_block = True

        index += size

# Iterate over blocks backwards
for id, (index, size) in reversed(blocks.items()):
    # Find first free space for block of adequate size
    found = False
    for i, (space_index, space_size) in enumerate(free_space):
        # Do not try to move the block further to the right
        if space_index > index:
            break

        # Found a spot to move the block!
        if space_size >= size:
            found = True
            break

    # Perform move
    # No need to resolve fragmentation left behind as it is not searched again
    if found:
        blocks[id] = (space_index, size)
        space_remaining = space_size - size

        # Remove free space if size is zero
        if space_remaining <= 0:
            free_space.pop(i)
        # Otherwise modify to correct size
        else:
            free_space[i] = (space_index + size, space_remaining)

# Calculate total
check_sum = 0
for id, (index, size) in blocks.items():
    for i in range(size):
        check_sum += id * (index + i)

print(f"Solution:\n{check_sum}")
