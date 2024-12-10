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
files_dic = {}
files_locs = {}
dic = {}
while pos < len(int_list):
    if pos % 2 == 0:
        idx = len(new_list)
        files_locs[pos_id] = idx
        new_list += [pos_id] * int_list[pos]
        files_dic[pos_id] = int_list[pos]
        pos_id += 1
    else:
        idx = len(new_list)
        dic[idx] = int_list[pos]
        new_list += [-1] * int_list[pos]
    pos += 1

for i in range(len(files_dic.keys()) - 1, -1, -1):
    print(i)
    for j in dic.keys():
        if dic[j] >= files_dic[i] and files_locs[i] > j:
            files_locs[i] = j
            # new_list[j:j+files_dic[i]] = [i] * files_dic[i]
            new_length = dic.pop(j) - files_dic[i]
            new_key = j + files_dic[i]
            dic[new_key] = new_length
            dic = dict(sorted(dic.items()))
            break



out = 0
for key in files_locs.keys():
    for i in range(files_dic[key]):
        out += key * (files_locs[key] + i)
print(out)
