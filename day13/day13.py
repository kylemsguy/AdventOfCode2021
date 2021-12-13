# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

import sys

def print_grid(data):
    for r in data:
        print(''.join(str(x) for x in r))
    print()

def parse(data):
    dots = set()
    instructions = []

    for l in data:
        if not l:
            continue
        if l.startswith("fold"):
            instructions.append(l[11:])
        else:
            x,y = l.split(",")
            dots.add((int(x), int(y)))
    return dots, instructions

def fold(dots, instruction):
    axis, fold_line = instruction.split('=')
    fold_line = int(fold_line)

    points = set()
    
    for x, y in list(dots):
        newx = x
        newy = y
        if axis == 'x':
            if x > fold_line:
                newx = fold_line - (x - fold_line)
        else: # axis = x
            if y > fold_line:
                newy = fold_line - (y - fold_line)
        points.add((newx, newy))
        # print(x, y, "->", newx, newy)
    return points

def part1(dots, instructions):
    # up, 655
    # fold_line = 655
    return len(fold(dots, instructions[0]))

def part2(dots, instructions):
    for i in instructions:
        dots = fold(dots, i)
    render_grid(dots)
    return "See stderr"


def render_grid(dots):
    max_x = max([x[0] for x in dots]) + 1
    max_y = max([x[1] for x in dots]) + 1

    grid = [[False for y in range(max_y)] for x in range(max_x)]

    for x, y in list(dots):
        # print(x, y)
        grid[x][y] = True
    for y in range(max_y):    
        for x in range(max_x):
            if grid[x][y]:
                print("x", end=' ', file=sys.stderr)
            else:
                print('.', end=' ', file=sys.stderr)
        print(file=sys.stderr)


if __name__ == "__main__":
    with open("input") as infile:
    # with open("inputsmall.txt") as infile:
        rawdata = [x.strip() for x in infile.readlines()]
    data = parse(rawdata)
    # print(data)
    print(">>>Day 13<<<")
    c = part1(*data)
    print(f"Part 1: {c}")
    c = part2(*data)
    print(f"Part 2: {c}")
