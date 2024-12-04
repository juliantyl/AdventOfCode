import collections
import functools
import re
from collections import Counter
from itertools import cycle, combinations, accumulate, chain
from aoc.helpers import output, read_input_from_file, input_lines


filename = "input.txt"

input = read_input_from_file(filename)
lines = input_lines(input)

# 140x140
lines = lines[:140]
print(len(lines))
out = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "X":
            # LEFT
            if i >= 3:
                if lines[i - 1][j] + lines[i-2][j] + lines[i-3][j] == 'MAS':
                    out += 1
                    print('left')
                if j >= 3:
                    if lines[i - 1][j - 1] + lines[i - 2][j - 2] + lines[i - 3][j - 3] == 'MAS':
                        out += 1
                        print('left up')
                if j < len(lines[i]) - 3:
                    if lines[i - 1][j + 1] + lines[i - 2][j + 2] + lines[i - 3][j + 3] == 'MAS':
                        out += 1
                        print('left down')
            # RIGHT
            if i < len(lines) - 3:
                if lines[i + 1][j] + lines[i + 2][j] + lines[i + 3][j] == 'MAS':
                    out += 1
                    print('right')
                if j >= 3:
                    if lines[i + 1][j - 1] + lines[i + 2][j - 2] + lines[i + 3][j - 3] == 'MAS':
                        out += 1
                        print('right up')
                if j < len(lines[i]) - 3:
                    if lines[i + 1][j + 1] + lines[i + 2][j + 2] + lines[i + 3][j + 3] == 'MAS':
                        out += 1
                        print('right down')
            # UP
            if j >= 3:
                if lines[i][j - 1] + lines[i][j - 2] + lines[i][j - 3] == 'MAS':
                    out += 1
                    print('up')
            # DOWN
            if j < len(lines) - 3:
                if lines[i][j + 1] + lines[i][j + 2] + lines[i][j + 3] == 'MAS':
                    out += 1
                    print('down')


print(out)