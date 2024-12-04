import collections
import functools
import re
from collections import Counter
from itertools import cycle, combinations, accumulate, chain
from aoc.helpers import output, read_input_from_file, input_lines


filename = "input.txt"

input = read_input_from_file(filename)
lines = input_lines(input)


final_in = []
out = 0

for line in lines:
    line = line.split(" ")
    # print(line)
    if line == ['']: continue
    final_in.append([int(item) for item in line] )


def is_safe(report):

    if report[1] == report[0]:
        return False
    decreasing = report[1] < report[0]
    if decreasing:
        allowed = {-1, -2, -3}
    else:
        allowed = {1, 2, 3}
    valid = True
    pos = 0
    while valid and pos < len(report) - 1:
        if report[pos + 1] - report[pos] not in allowed:
            valid = False
        else:
            pos = pos + 1
        if pos == len(report) - 1:
            return True
    return False


def is_safe_with_dampener(report):

    if is_safe(report):
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True

    return False


def count_safe_reports_with_dampener(reports):
    return sum(is_safe_with_dampener(report) for report in reports)

safe_count = count_safe_reports_with_dampener(final_in)


print(safe_count)