import collections
import functools
import re
from collections import Counter
from itertools import cycle, combinations, accumulate, chain
from aoc.helpers import output, read_input_from_file, input_lines


filename = "input.txt"

input = read_input_from_file(filename)
lines = input_lines(input)

board = []
for i, line in enumerate(lines):
    if line == '':
        cutoff = i
        break
    board.append(list(line))

input = list("".join(_ for _ in lines[cutoff+ 1 : len(lines) - 1]))

position = (0,0)
for i, line in enumerate(board):
    for j, c in enumerate(line):
        if c == '@':
            position = (i,j)



xlim = len(board)
ylim = len(board[0])


def left(pos):
    return pos[0], pos[1] - 1

def right(pos):
    return pos[0], pos[1] + 1

def up(pos):
    return pos[0] - 1, pos[1]

def down(pos):
    return pos[0] + 1, pos[1]

def move(board, movement, pos):
    move = up
    if movement == '<':
        move = left
    elif movement == '>':
        move = right
    elif movement == 'v':
        move = down
    elif movement == '^':
        move = up

    target = move(pos)
    target_tile = board[target[0]][target[1]]
    if target_tile == '.':
        board[pos[0]][pos[1]] = '.'
        board[target[0]][target[1]] = '@'
        pos = target
        return board, pos
    elif target_tile == '#':
        return board, pos
    else:
        original_shark = target
        while True:
            target = move(target)
            target_tile = board[target[0]][target[1]]
            if target_tile == '.':
                board[original_shark[0]][original_shark[1]] = '@'
                board[pos[0]][pos[1]] = '.'
                pos = original_shark
                board[target[0]][target[1]] = 'O'
                return board, pos
            elif target_tile == '#':
                return board, pos


for command in input:
    board, position = move(board, command, position)

out = 0
for i, line in enumerate(board):
    for j, c in enumerate(line):
        if board[i][j] == 'O':
            out += 100*i + j

print(out)
