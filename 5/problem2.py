import collections
import functools
import re
from collections import Counter
from itertools import cycle, combinations, accumulate, chain
from aoc.helpers import output, read_input_from_file, input_lines


filename = "input.txt"

input = read_input_from_file(filename)
lines = input_lines(input)

orders = []
pages = []
switch = True
for line in lines:
    if line == "":
        switch = False
    elif switch:
        orders.append([int(item) for item in line.split("|")])
    else:
        pages.append([int(item) for item in line.split(",")])
# print(orders)
# print(pages)
before = {}
after = {}
for order_l, order_r in orders:
    if order_l not in before:
        before[order_l] = [order_r]
    else:
        before[order_l].append(order_r)
    if order_r not in after:
        after[order_r] = [order_l]
    else:
        after[order_r].append(order_l)

def correctly_order(ls):
    outy = ls.copy()
    j = 0
    while j < len(outy):
        if outy[j] in after and any(x in after[outy[j]] for x in outy[j + 1:]):
            outy = outy[:j] + outy[j + 1:] + [outy[j]]
        else:
            j += 1
    print(outy)
    return outy


out = 0
count = 0
for page in pages:
    count += 1
    for i in range(len(page)):
        if page[i] in after and any(x in after[page[i]] for x in page[i+1:]):
            temp = correctly_order(page)
            out += temp[len(page)//2]
            break
        elif page[i] in before and any(x in before[page[i]] for x in page[:i]):
            temp = correctly_order(page)
            out += temp[len(page) // 2]
            break
        elif i == len(page) - 1:
            break

print(out)