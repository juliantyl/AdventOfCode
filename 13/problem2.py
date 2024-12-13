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

input_ls = []

for i, line in enumerate(lines):
    if i % 4 == 0:
        inner = []
        inner.append((int(line.split("+")[1].strip(", Y")), int(line.split("+")[2])))
        inner.append((int(lines[i+1].split("+")[1].strip(", Y")), int(lines[i+1].split("+")[2])))
        inner.append((int(lines[i+2].split("=")[1].strip(", Y")), int(lines[i+2].split("=")[2])))
        input_ls.append(inner)



def test(a, b, target):
    ax, ay = a
    bx, by = b
    tx, ty = target
    tx += 10000000000000
    ty += 10000000000000
    start_B_ls = []
    for B in range(ax):
        if (tx - bx*B) % ax == 0:
            start_B_ls.append(B)

    starts = len(start_B_ls)
    if starts == 0:
        print("No solution")
        return 0
    start_B = min(start_B_ls)


    # basically do a binary search
    # if ay > by then adding more ay will increase val of the compare that is tryna reach ty
    # if not, then adding more ay will decrease val of compare


    lowest = 0
    mult = ax // starts
    # print(f'stepping by {mult} instead of {ax}')
    max_B = (tx//bx + 1) // mult + 1
    B = (lowest + max_B) // 2


    b = B
    true_B = start_B + b * mult
    A = (tx - bx * true_B) // ax
    before = A * ay + true_B * by
    b -= 1
    true_B = start_B + b * mult
    A = (tx - bx * true_B) // ax
    after = A * ay + true_B * by

    if before >= after:
        flipped = False
    else:
        flipped = True

    # print('-------')

    while True:

        true_B = start_B + B*mult
        A = (tx - bx*true_B) // ax
        compare = A * ay + true_B * by
        # print('-------')
        # print(f'lowest: {lowest}, current: {B}, max: {max_B}')
        # print(f'A: {A}, B: {true_B}')
        # print(f'YVal: {compare}, Target: {ty}')

        if compare == ty:
            print(f'Solution found with cost: {A * 3 + true_B}')
            # print('-------')
            return (A * 3 + true_B)
        if max_B - lowest == 1:
            print('no solution')
            # print('-------')
            return 0
        elif compare < ty:
            # need more Y
            if flipped:
                # need more A > less B
                max_B = B
                B = (lowest + max_B) // 2
            else:
                # need less A > more B
                lowest = B
                B = (lowest + max_B) // 2
        elif compare > ty:
            # need less Y
            if flipped:
                # need less A > more B
                lowest = B
                B = (lowest + max_B) // 2
            else:
                # need more A > less B
                max_B = B
                B = (lowest + max_B) // 2
        # print('-------')




    # for B in range(start_B, tx//bx + 1, ax):
    #     print(ty)
    #
    #     A = (tx - bx*B) // ax
    #     print('----------------------')
    #     print(A * ay + B * by)
    #     if A >= 0 and (A*ay + B*by == ty):
    #         print(A, B)
    #         ls.append((A, B))


    lowest = float('inf')
    for item in ls:
        cost = item[0] * 3 + item[1]
        lowest = min(lowest, cost)
    if lowest == float('inf'):
        return 0
    print(lowest)
    return lowest

out = 0
for inn in input_ls:
    ans = test(inn[0], inn[1], inn[2])
    out += ans
print(out)