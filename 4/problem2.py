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
        if lines[i][j] == "A":
            if i >= 1 and i < len(lines) - 1 and j >= 1 and j < len(lines[i]) - 1:
                # check verts
                string_vert = lines[i - 1][j] + lines[i + 1][j] + lines[i][j + 1] + lines[i][j - 1]
                vert_count = Counter(string_vert)
                if vert_count['M'] == 2 and vert_count['S'] == 2 and string_vert[0] != string_vert[1]:
                    pass
                    # out += 1
                # check diags
                string_diag = lines[i - 1][j - 1] + lines[i + 1][j + 1] + lines[i - 1][j + 1] + lines[i + 1][j - 1]
                diag_count = Counter(string_diag)
                if diag_count['M'] == 2 and diag_count['S'] == 2 and string_diag[0] != string_diag[1]:
                    out += 1
print(out)