import sys
from collections import defaultdict


def is_ordered(update: list[int], ordering_rules: dict[int, list]) -> bool:
    for i, num in enumerate(update):
        # If there are no ordering rules for this number skip!
        if num not in ordering_rules:
            continue

        # Otherwise iterate over every number before in sequence
        # Return false if a previous page in sequence must be before current
        for j in range(i):
            previous_num = update[j]
            if previous_num in ordering_rules[num]:
                return False

    return True


def order(update: list[int], ordering_rules: dict[int, list]) -> None:
    ordered = False

    # If not ordered have another attempt
    while not ordered:
        for i in range(len(update)):
            num = update[i]

            # If there are no ordering rules for this number skip!
            if num not in ordering_rules:
                continue

            # Otherwise iterate over every number before in sequence
            # If found number that current number is supposed to be before
            #   and insert number before it
            for j in range(i):
                previous_num = update[j]
                if previous_num in ordering_rules[num]:
                    update.pop(i)
                    update.insert(j, num)
                    break

        ordered = is_ordered(update, ordering_rules)


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

# Parse input file into a dictionary for rules and a 2D array for page updates
ordering_rules = defaultdict(list)
updates = []
with open(path, "r") as f:
    rules, page_updates = f.read().split("\n\n")

    for rule in rules.split('\n'):
        x, y = map(int, rule.split('|'))
        ordering_rules[x].append(y)

    for page_update in page_updates.strip().split('\n'):
        updates.append(list(map(int, page_update.split(','))))

# If update is not sorted then sort and sum middle term
middle_total = 0
for update in updates:
    # Skip if already sorted
    if is_ordered(update, ordering_rules):
        continue

    # Order pages in update
    order(update, ordering_rules)

    middle_index = len(update) // 2
    middle_total += update[middle_index]

print(f"Solution:\n{middle_total}")
