import collections
import functools
import re
from collections import Counter
from itertools import cycle, combinations, accumulate, chain
from aoc.helpers import output, read_input_from_file, input_lines


filename = "input.txt"

input = read_input_from_file(filename)
input = list(input)
out = 0

int_list = []
for c in input:
    if c.isnumeric():
        int_list.append(int(c))

new_list = []
pos = 0
pos_id = 0
q = []
while pos < len(int_list):
    if pos % 2 == 0:
        new_list += [pos_id] * int_list[pos]
        pos_id += 1
    else:
        idx = len(new_list) - 1
        for i in range(idx, idx + int_list[pos]):
            q.append(i + 1)
        new_list += [-1] * int_list[pos]

    pos += 1


while q:
    target = new_list.pop()
    if target == -1:
        q.pop()
        continue

    new_list[q.pop(0)] = target

out = 0
for i, val in enumerate(new_list):
    out += i * val
print(out)
