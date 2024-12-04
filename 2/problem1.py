import collections
import functools
import re
from collections import Counter
from itertools import cycle, combinations, accumulate, chain
from aoc.helpers import output, read_input_from_file, input_lines


filename = "input.txt"

input = read_input_from_file(filename)
lines = input_lines(input)

# print(lines)

final_in = []
out = 0

for line in lines:
    line = line.split(" ")
    print(line)
    if line == ['']: continue
    final_in.append([int(item) for item in line] )

for item in final_in:
    if item[1] == item[0]:
        continue
    decreasing = item[1] < item[0]
    if decreasing:
        allowed = {-1, -2, -3}
    else:
        allowed = {1, 2, 3}
    valid = True
    pos = 0
    while valid and pos < len(item) - 1:
        if item[pos + 1] - item[pos] not in allowed:
            valid = False
        else:
            pos = pos + 1
        if pos == len(item) -1:
            out += 1

print(out)