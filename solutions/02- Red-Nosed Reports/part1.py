import sys


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

reports = []
with open(path, "r") as f:
    for line in f.readlines():
        reports.append(list(map(int, line.split())))

safe = 0
for report in reports:
    unsafe = False

    last_level = report[0]
    for i in range(1, len(report)):
        level = report[i]
        difference = abs(last_level - level)
        if difference > 3 or difference < 1:
            unsafe = True
            break
        last_level = level

    if unsafe:
        continue

    direction = (report[0] - report[1]) > 0

    last_level = report[0]
    for i in range(1, len(report)):
        level = report[i]
        if (last_level - level > 0) != direction:
            unsafe = True
            break
        last_level = level

    if unsafe:
        continue

    safe += 1

print(f"Solution:\n{safe}")
