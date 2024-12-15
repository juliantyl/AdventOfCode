import collections
import functools
import re
from collections import Counter
from itertools import cycle, combinations, accumulate, chain
from aoc.helpers import output, read_input_from_file, input_lines
from functools import lru_cache

import sys


filename = "input.txt"

input = read_input_from_file(filename)

input = [int(_) for _ in input.split(" ")]
# 0 becomes 1
# even number of digits splits into 2
# else multiplied by num * 2024

# len stones = len stones - 1 + len (2 digit numbers)
# what is len of 2 digit numbers
sys.setrecursionlimit(10000)
encountered = {}

def getlen(stone, round_remaining):
    if round_remaining == 0:
        return 1
    elif stone == 0:
        if (stone, round_remaining) not in encountered:
            encountered[(stone, round_remaining)] = getlen(1, round_remaining - 1)
        return encountered[(stone, round_remaining)]
    elif len(str(stone)) % 2 == 0:
        mid = int(len(str(stone)) / 2)
        if (stone, round_remaining) not in encountered:
            encountered[(stone, round_remaining)] = getlen(int(str(stone)[:mid]), round_remaining - 1) + getlen(int(str(stone)[mid:]), round_remaining - 1)
        return encountered[(stone, round_remaining)]
    else:
        if (stone, round_remaining) not in encountered:
            encountered[(stone, round_remaining)] = getlen(stone*2024, round_remaining - 1)
        return encountered[(stone, round_remaining)]

out = 0
for stone in input:
    out += getlen(stone, 2000)
print(out)