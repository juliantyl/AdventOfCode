import collections
import copy
import functools
import re
from collections import Counter
from itertools import cycle, combinations, accumulate, chain
from aoc.helpers import output, read_input_from_file, input_lines


filename = "input.txt"

input = read_input_from_file(filename)
lines = input_lines(input)
lines = lines[:len(lines) - 1]



for i, line in enumerate(lines):
    lines[i] = [int(_) for _ in line]


IMIN = 0
IMAX = len(lines)
JMIN = 0
JMAX = len(lines[0])


trailheads = set()
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == 0:
            trailheads.add((i, j))


def parse(trailhead, lines, visited):
    pos = trailhead
    cont = True
    while cont:
        surroundings = check_surrounding(pos)
        visited.add(pos)
        if lines[pos[0]][pos[1]] == 9:
            return 1
        elif len(surroundings) == 0:
            return 0
        elif len(surroundings) == 1:
            if lines[surroundings[0][0]][surroundings[0][1]] == lines[pos[0]][pos[1]] + 1 and surroundings[0] not in visited:
                pos = surroundings[0]
        else:
            output = 0
            for position in surroundings:
                if (lines[position[0]][position[1]] == lines[pos[0]][pos[1]] + 1) and position not in visited:
                    output += parse(position, lines, visited)
            return output



def check_surrounding(pos):
    ls = [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]
    out = []
    for item in ls:
        if item[0] >= IMIN and item[0] < IMAX and item[1] >= JMIN and item[1] < JMAX:
            out.append(item)
    return out

out = 0
for trailhead in trailheads:
    visited = set()
    out += parse(trailhead, lines, visited)
print(out)