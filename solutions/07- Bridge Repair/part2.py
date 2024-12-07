import sys
from itertools import product


def possible(result: int, values: list[int]) -> bool:
    combos = list(product([0, 1, 2], repeat=len(values) - 1))

    for combo in combos:
        total = values[0]

        # Perform combo of operations
        for i, operator in enumerate(combo):
            val = values[i + 1]
            if operator == 0:
                total += val
            elif operator == 1:
                total *= val
            elif operator == 2:
                total = int(str(total) + str(val))

        # Check if operator combination gives correct result
        if total == result:
            return True

    return False


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

# Parse input as pair (int, list[int]) into array
equations = []
with open(path, "r") as f:
    for line in f.readlines():
        result, values = line.strip().split(':')
        equations.append((int(result), list(map(int, values.split()))))

total_calibration_result = 0
for equation in equations:
    result, values = equation
    if possible(result, values):
        total_calibration_result += result

print(f"Solution:\n{total_calibration_result}")
