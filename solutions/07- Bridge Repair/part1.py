import sys


def possible(result: int, values: list[int]) -> bool:
    # Iterative backtracking algorithm
    stack = []
    stack.append((values[0], '+', 1))
    stack.append((values[0], '*', 1))

    # While there are more combinations to test
    while stack:
        current_total, operation, i = stack.pop()

        # Perform operation
        if operation == '+':
            current_total += values[i]

        elif operation == '*':
            current_total *= values[i]

        # If the answer is already too large, it cannot get smaller
        # Note: There are no negative numbers in the input
        if current_total > result:
            continue

        # If there are more values to compute
        if i + 1 < len(values):
            stack.append((current_total, '+', i + 1))
            stack.append((current_total, '*', i + 1))

        # If all values in total then compare to result
        elif current_total == result:
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

# Test all possible equation combinations and sum total if possible
total_calibration_result = 0
for equation in equations:
    result, values = equation
    if possible(result, values):
        total_calibration_result += result

print(f"Solution:\n{total_calibration_result}")
