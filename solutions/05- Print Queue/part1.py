import sys


def valid(update) -> bool:
    for i, n in enumerate(update):
        if n not in order:
            continue
        for j in range(i):
            not_before = update[j]
            if not_before in order[n]:
                return False
    return True


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
for update in updates:
    if valid(update):
        middle = len(update) // 2
        middle_total += update[middle]


print(f"Solution:\n{middle_total}")
