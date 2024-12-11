import collections
import functools
import re
from collections import Counter
from itertools import cycle, combinations, accumulate, chain
from aoc.helpers import output, read_input_from_file, input_lines
from functools import lru_cache


filename = "input.txt"

input = read_input_from_file(filename)

input = [int(_) for _ in input.split(" ")]
# 0 becomes 1
# even number of digits splits into 2
# else multiplied by num * 2024

encountered = {}


def blink(ls):
    for stone in ls:
        if stone == 0:
            yield 1
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            mid = len(stone_str) // 2
            yield int(stone_str[:mid])
            yield int(stone_str[mid:])
        else:
            yield 2024 * stone


def blink25(ls, encountered):
    for stone in ls:
        if stone in encountered:
            for result in encountered[stone]:
                yield result
        else:
            inner_out = [stone]
            for _ in range(15):
                inner_out = list(blink(inner_out))
            encountered[stone] = inner_out
            for result in inner_out:
                yield result


out = input
for i in range(5):
    print(i)
    out = blink25(out, encountered)
total_length = sum(1 for _ in out)
print(total_length)