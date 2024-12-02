import sys


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

# Parse input into 2D array of integers
reports = []
with open(path, "r") as f:
    for line in f.readlines():
        reports.append(list(map(int, line.split())))

# Walk through each report with two pointers and check direction and difference
# Two pointers move along pointing to consecutive elements in the report
safe = 0
for report in reports:
    # Find first pair direction to determine report direction
    # direction = 0: decreasing, 1: increasing
    report_direction = (report[1] - report[0]) > 0

    for i in range(len(report) - 1):
        # Check difference between last two levels is between 1 and 3
        difference = abs(report[i] - report[i + 1])
        if (difference < 1 or difference > 3):
            break

        # Check direction matches the direction of the first two levels
        direction = (report[i + 1] - report[i]) > 0
        if direction != report_direction:
            break
    else:
        # If the loop wasn't broken then the report is safe
        safe += 1

print(f"Solution:\n{safe}")
