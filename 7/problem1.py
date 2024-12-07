import collections
import functools
import itertools
import re
from collections import Counter
from itertools import cycle, combinations, accumulate, chain
from aoc.helpers import output, read_input_from_file, input_lines


filename = "input.txt"

input = read_input_from_file(filename)
lines = input_lines(input)
lines = lines[:len(lines)-1]


data = [(int(line.split(": ")[0]), [int(_) for _ in line.split(": ")[1].split(" ")]) for line in lines]


def check_if_possible(target, ls):
    combinations_len = len(ls) - 1
    combs = list(itertools.product("+*", repeat=combinations_len))
    combs = [''.join(comb) for comb in combs]
    return any([test_solution(target, ls, c) for c in combs])


def test_solution_according_to_prec(target, ls, combinations):
    subject = ls.copy()
    for i, c in enumerate(combinations):
        if c == "*":
            subject[i+1] = subject[i]*subject[i+1]
            subject[i] = 0
    return target == sum(subject)

def test_solution(target, ls, combinations):
    subject = ls.copy()
    for i, c in enumerate(combinations):
        if c == "*":
            subject[i + 1] = subject[i] * subject[i + 1]
            subject[i] = 0
        elif c == "+":
            subject[i + 1] = subject[i] + subject[i + 1]
            subject[i] = 0
    return target == sum(subject)


out = 0
for datum in data:
    if check_if_possible(datum[0], datum[1]):

        out += datum[0]

print(out)
