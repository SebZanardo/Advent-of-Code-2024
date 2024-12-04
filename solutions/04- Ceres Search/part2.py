import sys


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

# Read word_search in as a 2D array of characters
word_search = []
with open(path, "r") as f:
    for line in f.readlines():
        word_search.append(list(line.strip()))

pattern_forward = 'MAS'
pattern_backward = 'SAM'
total = 0

# Word search is a square, so n can be treated as width and height
n = len(word_search)

# Diagonal forwards '\' and backwards '/'
for y in range(n-2):
    row_forwards = []
    row_backwards = []

    for x in range(n-2):
        forwards = ""
        backwards = ""

        for i in range(3):
            forwards += word_search[i+y][x+i]
            backwards += word_search[i+y][n-x-i-1]

        row_forwards.append(forwards)
        row_backwards.append(backwards)

    row_backwards.reverse()

    # Check if forward and backward diagonals match in X shape
    for s1, s2 in zip(row_forwards, row_backwards):
        if s1 != pattern_forward and s1 != pattern_backward:
            continue

        if s2 != pattern_forward and s2 != pattern_backward:
            continue

        total += 1

print(f"Solution:\n{total}")
