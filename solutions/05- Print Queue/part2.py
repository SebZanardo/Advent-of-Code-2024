import sys
# I may have quickly tried to random.shuffle() until valid :))
# import random

print("Sorry this solution is not optimal yet and may take a while to compute")


def valid(update) -> int:
    for i, n in enumerate(update):
        if n not in order:
            continue
        for j in range(i):
            not_before = update[j]
            if not_before in order[n]:
                return i
    return -1


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

order: dict[int, list[int]] = {}
updates = []
with open(path, "r") as f:
    line = f.readline().strip()

    while line:
        x, y = map(int, line.split('|'))
        if x in order:
            order[x].append(y)
        else:
            order[x] = [y]
        line = f.readline().strip()

    line = f.readline().strip()
    while line:
        updates.append(list(map(int, line.strip().split(','))))
        line = f.readline().strip()

middle_total = 0
for i, update in enumerate(updates):
    return_code = valid(update)

    if return_code == -1:
        continue

    while return_code != -1:
        # Re-order
        value = update.pop(return_code)

        last_return_code = return_code
        for j in range(len(update)+1):
            update.insert(j, value)

            if valid(update) != last_return_code:
                break

            value = update.pop(j)

        return_code = valid(update)

    middle = len(update) // 2
    middle_total += update[middle]


print(f"Solution:\n{middle_total}")
