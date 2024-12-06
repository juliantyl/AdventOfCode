import collections
import functools
import re
from collections import Counter
from itertools import cycle, combinations, accumulate, chain
from aoc.helpers import output, read_input_from_file, input_lines


filename = "input.txt"

input = read_input_from_file(filename)
lines = input_lines(input)

visited = []

for line in lines:
    if line == '':
        lines.remove(line)
    else:
        visited.append(len(line) * [0])

print(visited)

pos = (0, 0)
dirs = {">":(0,1), "<": (0,-1), "^":(-1,0), "v":(1,0)}
direc = ""
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '>' or lines[i][j] == '<' or lines[i][j] == '^' or lines[i][j] == 'v':
            pos = (i, j)
            direc = lines[i][j]
            visited[i][j] = 1

left = False
while not left:
    next_tile = (pos[0] + dirs[direc][0], pos[1] + dirs[direc][1])
    if next_tile[0] < 0 or next_tile[0] >= len(lines) or next_tile[1] < 0 or next_tile[1] >= len(lines[0]):
        left = True
    elif lines[next_tile[0]][next_tile[1]] == '#':
        if direc == ">": direc = "v"
        elif direc == "<": direc = "^"
        elif direc == "^": direc = ">"
        elif direc == "v": direc = "<"
    else:
        pos = (next_tile[0], next_tile[1])
        visited[next_tile[0]][next_tile[1]] = 1

out = 0
for i in range(len(visited)):
    out += sum(visited[i])
print(out)