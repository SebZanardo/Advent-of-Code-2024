import sys
from heapq import heapify, heappop


# Try to read a path to an input file from command line arguments
path = sys.argv[1] if len(sys.argv) > 1 else "input.in"

# Initialise an array for left and right lists
left = []
right = []

# Parse input file appending integers to left and right lists
with open(path, "r") as f:
    for line in f.readlines():
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)

# Transform left and right lists into min heaps
# heapq.heapify is an O(n) time, O(1) space operation
# heapify is faster than an iterative heappush which is 0(n*log(n)) time
heapify(left)
heapify(right)

# Pop off the smallest value on each heap and calculate difference
total_difference = 0
for _ in range(len(left)):
    total_difference += abs(heappop(left) - heappop(right))

print(f"Solution:\n{total_difference}")
