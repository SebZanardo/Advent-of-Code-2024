import sys
from collections import defaultdict


def is_ordered(update: list[int], ordering_rules: dict[int, set]) -> bool:
    for i, num in enumerate(update):
        # If there are no ordering rules for this number skip!
        # Never actually the case :((
        # if num not in ordering_rules:
        #     continue

        # Otherwise iterate over every number before in sequence
        # Return false if a previous page in sequence must be before current
        for j in range(i):
            previous_num = update[j]
            if previous_num in ordering_rules[num]:
                return False

    return True


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

# Parse input file into a dictionary for rules and a 2D array for page updates
# Use a set for O(1) lookup
ordering_rules = defaultdict(set)
updates = []
with open(path, "r") as f:
    rules, page_updates = f.read().split("\n\n")

    for rule in rules.split('\n'):
        x, y = map(int, rule.split('|'))
        ordering_rules[x].add(y)

    for page_update in page_updates.strip().split('\n'):
        updates.append(list(map(int, page_update.split(','))))

# If update is sorted then sum middle term
middle_total = 0
for update in updates:
    if not is_ordered(update, ordering_rules):
        continue

    middle_index = len(update) // 2
    middle_total += update[middle_index]

print(f"Solution:\n{middle_total}")
