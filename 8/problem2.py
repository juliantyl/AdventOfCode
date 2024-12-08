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
            pos = [loc[0], loc[1]]
            pos_diff = (comparator[0] - loc[0], comparator[1] - loc[1])


            while pos[0] >= 0 and pos[0] < x_bound and pos[1] >= 0 and pos[1] < y_bound:
                antinode_locations.add(tuple(pos))
                pos[0] += pos_diff[0]
                pos[1] += pos_diff[1]

            pos = [loc[0], loc[1]]
            while pos[0] >= 0 and pos[0] < x_bound and pos[1] >= 0 and pos[1] < y_bound:
                antinode_locations.add(tuple(pos))
                pos[0] -= pos_diff[0]
                pos[1] -= pos_diff[1]


for antinode_location in antinode_locations:
    line = list(lines[antinode_location[0]])
    line[antinode_location[1]] = "#"
    lines[antinode_location[0]] = "".join(line)

for line in lines:
    print(line)

print(len(antinode_locations))
