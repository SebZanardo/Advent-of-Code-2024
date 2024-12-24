import sys


cache = {}


def solver(patterns: tuple[str], design: str, combos: int) -> int:
    if not design:
        combos += 1
        return combos

    for p in patterns:
        if design[:len(p)] == p:
            combos = is_possible(patterns, design[len(p):], combos)

    return combos


def is_possible(patterns: tuple[str], design: str, combos: int) -> int:
    if design in cache:
        combos += cache[design]
        return combos
    else:
        cache[design] = solver(patterns, design, 0)

    if not design:
        combos += 1
        return combos

    for p in patterns:
        if design[:len(p)] == p:
            combos = is_possible(patterns, design[len(p):], combos)

    return combos


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

with open(path, "r") as f:
    pattern_string, design_string = f.read().split('\n\n')
    patterns = tuple([p.strip() for p in pattern_string.split(',')])
    designs = [d.strip() for d in design_string.split()]


possible_combos = 0
for design in designs:
    combos = is_possible(patterns, design, 0)
    possible_combos += combos

print(f"Solution:\n{possible_combos}")
