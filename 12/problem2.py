import collections
import functools
import re
from collections import Counter
from itertools import cycle, combinations, accumulate, chain
from aoc.helpers import output, read_input_from_file, input_lines


filename = "test.txt"

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
    total_sides = 4
    leftmost = curr
    # print(curr_list)
    for item in curr_list:
        if item in unexplored:
            unexplored.remove(item)
        if item[1] < leftmost[1]:
            leftmost = item
        area_dic[id] += 1
    # find the leftmost point

    current_tl = leftmost
    sides = 0
    dir = "up"
    # print('start')
    visited = set()
    while True:
        # first check up
        if dir == "up":
            if up(current_tl) in curr_list:
                if left(up(current_tl)) in curr_list:
                    dir = "left"
                    current_tl = left(up(current_tl))
                    sides += 1
                else:
                    current_tl = up(current_tl)
            else:
                dir = "right"
                sides += 1
        elif dir == "right":
            if right(current_tl) in curr_list:
                if up(right(current_tl)) in curr_list:
                    dir = "up"
                    current_tl = up(right(current_tl))
                    sides += 1
                else:
                    current_tl = right(current_tl)
            else:
                dir = "down"
                sides += 1
        elif dir == "down":
            if down(current_tl) in curr_list:
                if right(down(current_tl)) in curr_list:
                    dir = "right"
                    current_tl = right(down(current_tl))
                    sides += 1
                else:
                    current_tl = down(current_tl)
            else:
                dir = "left"
                sides += 1
        elif dir == "left":
            if left(current_tl) in curr_list:
                if down(left(current_tl)) in curr_list:
                    dir = "down"
                    current_tl = down(left(current_tl))
                    sides += 1
                else:
                    current_tl = left(current_tl)
            else:
                dir = "up"
                sides += 1
        # print(dir, current_tl, leftmost, lines[current_tl[0]][current_tl[1]])
        if dir == "up" and current_tl == leftmost:
            # print('broke')
            break

    peri_dic[id] = sides
    id += 1

out = 0
print(peri_dic)
print(area_dic)
for i in range(id):
    out += peri_dic[i] * area_dic[i]
print(out)



