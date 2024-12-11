import collections
import functools
import re
from collections import Counter
from itertools import cycle, combinations, accumulate, chain
from aoc.helpers import output, read_input_from_file, input_lines


filename = "input.txt"

input = read_input_from_file(filename)

input = [int(_) for _ in input.split(" ")]
# 0 becomes 1
# even number of digits splits into 2
# else multiplied by num * 2024

encountered = {}


def blink(ls):
    new_items = {}
    for i, stone in enumerate(ls):
        if stone == 0:
            ls[i] = 1
        elif len(str(stone)) % 2 == 0:

            stone_str = str(stone)
            mid = int(len(stone_str) / 2)
            new_items[i] = [int(stone_str[:mid]) , int(stone_str[mid:])]
        else:
            ls[i] = 2024 * stone

    out = []
    for i, stone in enumerate(ls):
        if i not in new_items:
            out += [ls[i]]
        else:
            out += new_items[i]
    return out

def blink25(ls, encountered, flag, go):
    out = []
    for i, stone in enumerate(ls):
        inner_out = [stone]
        if stone in encountered:
            if flag == 2:
                go += len(encountered[stone])
            else:
                out += encountered[stone]
        else:
            for j in range(25):
                inner_out = blink(inner_out)
            encountered[stone] = inner_out
            out += inner_out
    return out, go


out = input
global_offset = 0
for i in range(3):
    print(i)
    out, global_offset = blink25(out, encountered, i, global_offset)
print(len(out) + global_offset)