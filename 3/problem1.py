import collections
import functools
import re
from collections import Counter
from itertools import cycle, combinations, accumulate, chain
from aoc.helpers import output, read_input_from_file, input_lines


filename = "input.txt"

input = read_input_from_file(filename)
lines = input_lines(input)


string = str(input)
pattern = r'mul\(\d{1,3},\d{1,3}\)'
matches = re.findall(pattern, string)
out = 0
for match in matches:
    match = match.strip("mul(").strip(")")
    m1, m2 = int(match.split(',')[0]), int(match.split(',')[1])
    out += m1 * m2
print(out)