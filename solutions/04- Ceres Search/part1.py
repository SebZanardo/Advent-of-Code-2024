import sys


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

# Read word_search in as a 2D array of characters
word_search = []
with open(path, "r") as f:
    for line in f.readlines():
        word_search.append(list(line.strip()))

pattern_forward = 'XMAS'
pattern_backward = 'SAMX'
total = 0

# Word search is a square, so n can be treated as width and height
n = len(word_search)

# Diagonal forwards '\' and backwards '/'
for y in range(n-3):
    for x in range(n-3):
        forwards = ""
        backwards = ""

        for i in range(4):
            forwards += word_search[i+y][x+i]
            backwards += word_search[i+y][n-x-i-1]

        if forwards == pattern_forward or forwards == pattern_backward:
            total += 1
        if backwards == pattern_forward or backwards == pattern_backward:
            total += 1

# Horizontal and vertical
for y in range(n):
    for x in range(n-3):
        horizontal = ""
        vertical = ""

        for i in range(4):
            horizontal += word_search[y][x+i]
            vertical += word_search[x+i][y]

        if horizontal == pattern_forward or horizontal == pattern_backward:
            total += 1
        if vertical == pattern_forward or vertical == pattern_backward:
            total += 1

print(f"Solution:\n{total}")
