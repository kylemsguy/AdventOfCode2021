# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

from collections import deque
from copy import deepcopy

def print_grid(data):
    for r in data:
        print(''.join(str(x) for x in r))
    print()

def flash_adjacent(grid, row, col, to_flash, flashed):
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            r = row + i
            c = col + j
            if r == row and c == col:
                continue
            if r < 0 or r > 9 or c < 0 or c > 9:
                continue
            grid[r][c] += 1
            if grid[r][c] > 9:
                if (r, c) not in to_flash and (r, c) not in flashed:
                    to_flash.append((r, c))

def simulate(data, iter):
    flashes = 0
    for i in range(iter):
        to_flash = deque()
        flashed = set()
        for r, row in enumerate(data):
            for c, oct in enumerate(row):
                data[r][c] += 1
                # print(data[r][c])
                if data[r][c] > 9:
                    to_flash.append((r, c))
        while to_flash:
            r, c = to_flash.popleft()
            flash_adjacent(data, r, c, to_flash, flashed)
            flashed.add((r, c))
            flashes += 1
        for r, c in list(flashed):
            data[r][c] = 0
    print_grid(data)
    return flashes

def simulate2(data):
    iter = 0
    while True:
        iter += 1
        to_flash = deque()
        flashed = set()
        for r, row in enumerate(data):
            for c, oct in enumerate(row):
                data[r][c] += 1
                # print(data[r][c])
                if data[r][c] > 9:
                    to_flash.append((r, c))
        while to_flash:
            r, c = to_flash.popleft()
            flash_adjacent(data, r, c, to_flash, flashed)
            flashed.add((r, c))
        for r, c in list(flashed):
            data[r][c] = 0
        # print_grid(data)
        if len(flashed) == 100:
            # print(data)
            return iter


def part1(data):
    return simulate(deepcopy(data), 100)

def part2(data):
    return simulate2(deepcopy(data))

if __name__ == "__main__":
    with open("input") as infile:
    # with open("inputsmall") as infile:
        data = [[int(o) for o in l.strip()] for l in infile.readlines() if l]
    # print(data)
    print(">>>Day 10<<<")
    c = part1(data)
    print(f"Part 1: {c}")
    c = part2(data)
    print(f"Part 2: {c}")
