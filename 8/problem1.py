import collections
import functools
import re
from collections import Counter
from itertools import cycle, combinations, accumulate, chain
from aoc.helpers import output, read_input_from_file, input_lines


filename = "input.txt"

input = read_input_from_file(filename)
lines = input_lines(input)
lines = lines[:len(lines) - 1]

antinode_locations = set()
banned_locations = set()
locations = {}
x_bound = len(lines[0])
y_bound = len(lines)


for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == ".":
            continue
        elif c not in locations:
            locations[c] = [(i, j)]
            banned_locations.add((i, j))
        else:
            locations[c].append((i, j))
            banned_locations.add((i, j))

print(banned_locations)

for key in locations:
    for i, loc in enumerate(locations[key]):
        for comparator in locations[key][i + 1:]:
            pos1 = (2*loc[0] - comparator[0], 2*loc[1] - comparator[1])
            pos2 = (2*comparator[0] - loc[0], 2*comparator[1] - loc[1])
            if pos1[0] >= 0 and pos1[0] < x_bound and pos1[1] >= 0 and pos1[1] < y_bound:
                antinode_locations.add(pos1)
            if pos2[0] >= 0 and pos2[0] < x_bound and pos2[1] >= 0 and pos2[1] < y_bound:
                antinode_locations.add(pos2)

for antinode_location in antinode_locations:
    line = list(lines[antinode_location[0]])
    line[antinode_location[1]] = "#"
    lines[antinode_location[0]] = "".join(line)

for line in lines:
    print(line)

print(len(antinode_locations))
