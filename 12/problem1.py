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
for i, line in enumerate(lines):
    lines[i] = list(line)


def check_surrounding(pos):
    ls = [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]
    out = []
    for item in ls:
        if item[0] >= IMIN and item[0] < IMAX and item[1] >= JMIN and item[1] < JMAX and lines[item[0]][item[1]] == lines[pos[0]][pos[1]]:
            out.append(item)
    return out

def create_list_touching(curr, touched):
    if curr in touched:
        return None
    touched.add(curr)
    output = [curr]
    for item in check_surrounding(curr):
        if item not in touched:
            output += create_list_touching(item, touched)
    return output

IMIN = 0
IMAX = len(lines)
JMIN = 0
JMAX = len(lines[0])

unexplored = set()
area_dic = {}
peri_dic = {}

for i in range(IMAX):
    for j in range(JMAX):
        unexplored.add((i,j))

id = 0

while unexplored:
    curr = unexplored.pop()
    curr_list = create_list_touching(curr, set())
    area_dic[id] = 0
    peri_dic[id] = 0
    for item in curr_list:
        if item in unexplored:
            unexplored.remove(item)
        area_dic[id] += 1
        peri_dic[id] += 4 - len(check_surrounding(item))
    id += 1

out = 0
for i in range(id):
    out += peri_dic[i] * area_dic[i]
print(out)



