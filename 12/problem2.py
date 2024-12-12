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

def creat_list_adjacent(pos, otherls):
    ls = [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1),
          (pos[0] + 1, pos[1] - 1), (pos[0] - 1, pos[1] + 1), (pos[0] + 1, pos[1] + 1), (pos[0] - 1, pos[1] - 1)]
    out = []
    for item in ls:
        if item[0] >= IMIN and item[0] < IMAX and item[1] >= JMIN and item[1] < JMAX and lines[item[0]][item[1]] == \
                lines[pos[0]][pos[1]] and item in otherls:
            out.append(item)
    return out

def up(pos):
    if pos is None: return None
    item = (pos[0] - 1, pos[1])
    if item[0] >= IMIN and item[0] < IMAX:
        return item
    return None

def down(pos):
    if pos is None: return None
    item = (pos[0] + 1, pos[1])
    if item[0] >= IMIN and item[0] < IMAX:
        return item
    return None

def left(pos):
    if pos is None: return None
    item = (pos[0], pos[1] - 1)
    if item[1] >= JMIN and item[1] < JMAX:
        return item
    return None

def right(pos):
    if pos is None: return None
    item = (pos[0], pos[1] + 1)
    if item[1] >= JMIN and item[1] < JMAX:
        return item
    return None

def check_corners(pos, otherls):
    corners = 0
    adj = creat_list_adjacent(pos, otherls)
    # TL corner
    if up(pos) in adj and left(pos) in adj:
        if up(left(pos)) not in adj:
            corners += 1
    # TR
    if up(pos) in adj and right(pos) in adj:
        if up(right(pos)) not in adj:
            corners += 1
    # BR
    if down(pos) in adj and right(pos) in adj:
        if down(right(pos)) not in adj:
            corners += 1
    # BL
    if down(pos) in adj and left(pos) in adj:
        if down(left(pos)) not in adj:
            corners += 1
    # TL in
    if up(pos) not in adj and left(pos) not in adj:
        corners += 1
    # TR in
    if up(pos) not in adj and right(pos) not in adj:
        corners += 1
    # BR in
    if down(pos) not in adj and right(pos) not in adj:
        corners += 1
    # BL in
    if down(pos) not in adj and left(pos) not in adj:
        corners += 1
    return corners

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
    print(len(unexplored))
    curr = unexplored.pop()
    curr_list = create_list_touching(curr, set())
    area_dic[id] = 0
    peri_dic[id] = 0
    corners = 0
    for item in curr_list:
        if item in unexplored:
            unexplored.remove(item)
        area_dic[id] += 1
        corners += check_corners(item, curr_list)
    # find the leftmost point
    peri_dic[id] = corners
    id += 1

out = 0
print(peri_dic)
print(area_dic)
for i in range(id):
    out += peri_dic[i] * area_dic[i]
print(out)



