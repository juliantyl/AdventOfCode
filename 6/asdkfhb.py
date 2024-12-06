import collections
import copy
import functools
import re
from collections import Counter
from itertools import cycle, combinations, accumulate, chain
from aoc.helpers import output, read_input_from_file, input_lines


filename = "test.txt"

input = read_input_from_file(filename)
lines = input_lines(input)

visited = []
blocks = []

for line in lines:
    if line == '':
        lines.remove(line)
    else:
        visited.append([list() for i in range(len(line))])
        blocks.append(len(line) * [0])

pos = (0, 0)
dirs = {">":(0,1), "<": (0,-1), "^":(-1,0), "v":(1,0)}
direc = ""
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '>' or lines[i][j] == '<' or lines[i][j] == '^' or lines[i][j] == 'v':
            pos = (i, j)
            direc = lines[i][j]
            visited[i][j].append(direc)
            blocks[i][j] = -1
        elif lines[i][j] == '#':
            blocks[i][j] = -1


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
    visited_positions = set()  # Track visited (position, direction) pairs

    while True:
        next_tile = (sim_pos[0] + dirs[sim_dir][0], sim_pos[1] + dirs[sim_dir][1])
        if next_tile[0] < 0 or next_tile[0] >= len(lines) or next_tile[1] < 0 or next_tile[1] >= len(lines[0]):
            return False  # Exited the grid
        if (next_tile, sim_dir) in visited_positions:
            return True  # Loop detected
        visited_positions.add((next_tile, sim_dir))
        if lines[next_tile[0]][next_tile[1]] == '#' or next_tile == blocc_pos:
            sim_dir = get_next_dir(sim_dir)  # Turn right
        else:
            sim_pos = next_tile  # Move forward


out = 0
while not left:

    next_tile = (pos[0] + dirs[direc][0], pos[1] + dirs[direc][1])
    # print(f'NEXT TILE: {next_tile}')
    if next_tile[0] < 0 or next_tile[0] >= len(lines) or next_tile[1] < 0 or next_tile[1] >= len(lines[0]):
        # print(f"DONE")
        left = True
    elif lines[next_tile[0]][next_tile[1]] == '#':
        # print("HIT A WALL, TURNING")
        direc = get_next_dir(direc)
        visited[pos[0]][pos[1]].append(direc)

    elif check_if_blocc(pos, get_next_dir(direc), next_tile):
        if blocks[next_tile[0]][next_tile[1]] == 0:
            blocks[next_tile[0]][next_tile[1]] = 1
            print(f'placeable at {next_tile[0]}, {next_tile[1]}')
            out += 1
        pos = (next_tile[0], next_tile[1])
        # print(visited[next_tile[0]][next_tile[1]])
        visited[next_tile[0]][next_tile[1]].append(direc)
        # print(visited[next_tile[0]][next_tile[1]])
    else:
        # print("CONTINUING B")
        pos = (next_tile[0], next_tile[1])
        # print(visited[next_tile[0]][next_tile[1]])
        visited[next_tile[0]][next_tile[1]].append(direc)
        # print(visited[next_tile[0]][next_tile[1]])

print(out)