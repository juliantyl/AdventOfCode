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

blocks = []

for line in lines:
    if line == '':
        lines.remove(line)
    else:
        blocks.append(len(line) * [0])

pos = (0, 0)
dirs = {">":(0,1), "<": (0,-1), "^":(-1,0), "v":(1,0)}
direc = ""
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '>' or lines[i][j] == '<' or lines[i][j] == '^' or lines[i][j] == 'v':
            pos = (i, j)
            direc = lines[i][j]
            blocks[i][j] = 'X'
        elif lines[i][j] == '#':
            blocks[i][j] = 'X'


left = False

def get_next_dir(direction):
    if direction == ">":
        return "v"
    elif direction == "<":
        return "^"
    elif direction == "^":
        return ">"
    elif direction == "v":
        return "<"
    else:
        return ""

def check_if_blocc(position, direction, blocc_pos):
    sim_pos = position
    sim_dir = direction
    visited_positions = set()

    while True:
        next_tile = (sim_pos[0] + dirs[sim_dir][0], sim_pos[1] + dirs[sim_dir][1])
        if next_tile[0] < 0 or next_tile[0] >= len(lines) or next_tile[1] < 0 or next_tile[1] >= len(lines[0]):
            return False
        if (next_tile, sim_dir) in visited_positions:
            return True
        visited_positions.add((next_tile, sim_dir))
        if lines[next_tile[0]][next_tile[1]] == '#' or next_tile == blocc_pos:
            sim_dir = get_next_dir(sim_dir)
        else:
            sim_pos = next_tile


out = 0
while not left:
    next_tile = (pos[0] + dirs[direc][0], pos[1] + dirs[direc][1])
    if next_tile[0] < 0 or next_tile[0] >= len(lines) or next_tile[1] < 0 or next_tile[1] >= len(lines[0]):
        left = True
    elif lines[next_tile[0]][next_tile[1]] == '#':
        direc = get_next_dir(direc)

    elif blocks[next_tile[0]][next_tile[1]] == 0 and check_if_blocc(pos, get_next_dir(direc), next_tile):
        blocks[next_tile[0]][next_tile[1]] = 1
        print(f'placeable at {next_tile[0]}, {next_tile[1]}')
        out += 1
        pos = (next_tile[0], next_tile[1])
    else:
        blocks[next_tile[0]][next_tile[1]] = 1
        pos = (next_tile[0], next_tile[1])

print(out)