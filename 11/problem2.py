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
    out = []
    for stone in ls:
        if stone == 0:
            out.append(1)
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            mid = len(stone_str) // 2
            out.append(int(stone_str[:mid]))
            out.append(int(stone_str[mid:]))
        else:
            out.append(2024 * stone)
    return out


def blink25(ls, encountered, flag):
    oa = 0
    out = []
    for stone in ls:
        if stone in encountered:
            if flag == 2:
                oa += len(encountered[stone])
            for result in encountered[stone]:
                out.append(result)
        else:
            inner_out = [stone]
            for _ in range(25):
                inner_out = blink(inner_out)
            encountered[stone] = inner_out
            for result in inner_out:
                out.append(result)
    return out, oa


out = input
answer = 0
offset = 0
for item in out:
    print(item)
    curr = [item]
    for i in range(3):
        print(i)
        curr, offset = blink25(curr, encountered, i)
    answer += len(curr) + offset
    print(answer)
print('final')
print(answer)