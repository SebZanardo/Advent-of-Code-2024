import sys


def is_possible(patterns: list[str], design: str) -> bool:
    if not design:
        return True

    for p in patterns:
        if design[:len(p)] == p:
            if is_possible(patterns, design[len(p):]):
                return True
    return False


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

patterns = []
designs = []
with open(path, "r") as f:
    pattern_string, design_string = f.read().split('\n\n')
    patterns = [p.strip() for p in pattern_string.split(',')]
    designs = [d.strip() for d in design_string.split()]


possible = 0
for design in designs:
    if is_possible(patterns, design):
        possible += 1

print(f"Solution:\n{possible}")
