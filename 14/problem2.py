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

def print_board(b, f):
    for line in b:
        print("".join(["." if _ == 0 else "X" for _ in line]))
        f.write("".join(["." if _ == 0 else "X" for _ in line]))
        f.write("\n")

robots = []

for line in lines:
    obj = re.match('p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line)
    p1, p2, v1, v2 = obj.groups()
    robots.append(([int(p1), int(p2)], [int(v1), int(v2)]))

board = []
for i in range(103):
    board.append([0] * 101)

for robot in robots:
    x = robot[0][0]
    y = robot[0][1]
    board[y][x] += 1

file1 = open("output.txt", "w")
for i in range(10000):
    for robot in robots:
        x = robot[0][0]
        y = robot[0][1]
        board[y][x] -= 1
        x = (robot[0][0] + robot[1][0]) % 101
        y = (robot[0][1] + robot[1][1]) % 103
        board[y][x] += 1
        robot[0][0] = x
        robot[0][1] = y
    if (i+1) % 101 == 52:
        print(f'-------- AFTER {i + 1} ROUNDS --------')
        file1.write(f'-------- AFTER {i + 1} ROUNDS --------\n\n')
        print_board(board, file1)
file1.close()


mid_y = 103//2
mid_x = 101//2
q_1 = 0
q_2 = 0
q_3 = 0
q_4 = 0

for y in range(103):
    for x in range(101):
        if y < mid_y and x < mid_x:
            q_1 += board[y][x]
        elif y > mid_y and x < mid_x:
            q_3 += board[y][x]
        elif y > mid_y and x > mid_x:
            q_4 += board[y][x]
        elif y < mid_y and x > mid_x:
            q_2 += board[y][x]

print(q_1 * q_2 * q_3 * q_4)
