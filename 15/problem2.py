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
    l = []
    for c in line:
        if c == '#':
            l.append('#')
            l.append('#')
        elif c == '@':
            l.append('@')
            l.append('.')
        elif c == '.':
            l.append('.')
            l.append('.')
        elif c == 'O':
            l.append('[')
            l.append(']')
    board.append(l)


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
        if target_tile == '[':
            box_left = target
            box_right = right(target)
        else:
            box_right = target
            box_left = left(target)
        chunk = {pos, box_left, box_right}


        # establish chunk
        updated_chunk = set()
        while chunk != updated_chunk:
            for item in updated_chunk:
                chunk.add(item)
            updated_chunk = chunk.copy()
            for i, item in enumerate(chunk):
                next_space = move(item)
                target_space = board[next_space[0]][next_space[1]]
                if target_space == '.':
                    continue
                elif target_space == '#':
                    return board, pos
                elif target_space == '[':
                    updated_chunk.add(next_space)
                    updated_chunk.add(right(next_space))
                else:
                    updated_chunk.add(next_space)
                    updated_chunk.add(left(next_space))

        # move
        new_chunk = {}
        for item in chunk:
            if board[item[0]][item[1]] not in new_chunk:
                new_chunk[board[item[0]][item[1]]] = [move(item)]
            else:
                new_chunk[board[item[0]][item[1]]].append(move(item))
            board[item[0]][item[1]] = '.'


        for key in new_chunk.keys():
            for location in new_chunk[key]:
                board[location[0]][location[1]] = key
        return board, move(pos)


for command in input:
    board, position = move(board, command, position)

out = 0
for i, line in enumerate(board):
    for j, c in enumerate(line):
        if board[i][j] == '[':
            out += 100*i + j

print(out)
