import sys
from copy import deepcopy


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

reports = []
with open(path, "r") as f:
    for line in f.readlines():
        reports.append(list(map(int, line.split())))


def test_if_safe(report) -> bool:
    last_level = report[0]
    for i in range(1, len(report)):
        level = report[i]
        difference = abs(last_level - level)
        if difference > 3 or difference < 1:
            return False
        last_level = level

    direction = (report[0] - report[1]) > 0

    last_level = report[0]
    for i in range(1, len(report)):
        level = report[i]
        if (last_level - level > 0) != direction:
            return False
        last_level = level

    return True


safe = 0
for report in reports:
    # Safe already
    if test_if_safe(report):
        safe += 1
        continue

    # Need to remove one
    for i in range(len(report)):
        report_mod = deepcopy(report)
        report_mod.pop(i)
        if test_if_safe(report_mod):
            safe += 1
            break

print(f"Solution:\n{safe}")
