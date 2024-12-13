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

input_ls = []

for i, line in enumerate(lines):
    if i % 4 == 0:
        inner = []
        inner.append((int(line.split("+")[1].strip(", Y")), int(line.split("+")[2])))
        inner.append((int(lines[i+1].split("+")[1].strip(", Y")), int(lines[i+1].split("+")[2])))
        inner.append((int(lines[i+2].split("=")[1].strip(", Y")), int(lines[i+2].split("=")[2])))
        input_ls.append(inner)


def test(a, b, target):
    ax, ay = a
    bx, by = b
    tx, ty = target
    mini = 500
    for i in range(100):
        for j in range(100):
            if ax * i + bx * j == tx and ay * i + by * j == ty:
                mini = min(i*3 + j*1, mini)
    return mini

out = 0
for inn in input_ls:
    ans = test(inn[0], inn[1], inn[2])
    if ans == 500:
        print('no solution')
        ans = 0
    else:
        print(f'Solution found with cost: {ans}')
    out += ans
print(out)