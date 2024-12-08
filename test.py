### SCAFFOLD ###

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

### END ###


if __name__ == '__main__':
    print('This is the repository for my advent of code stuffs.. yay me. Do ur best !')
