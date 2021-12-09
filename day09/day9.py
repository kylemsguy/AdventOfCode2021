# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

from collections import deque
from functools import reduce

def check_adjacent(grid, row, col):
    curr = grid[row][col]
    if row > 0:
        if grid[row-1][col] <= curr:
            return False
    if row < 99:
        if grid[row+1][col] <= curr:
            return False

    if col > 0:
        if grid[row][col-1] <= curr:
            return False
    if col < 99:
        if grid[row][col+1] <= curr:
            return False
    return True


def part1(data):
    danger_sum = 0
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            if check_adjacent(data, r, c):
                danger = col + 1
                danger_sum += danger
    return danger_sum

def get_low_points(data):
    low_points = []
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            if check_adjacent(data, r, c):
                low_points.append((r, c))
    return low_points


def get_adjacent(grid, row, col):
    curr = grid[row][col]
    adjacents = set()
    if row > 0:
        adjacents.add((row - 1, col))

    if row < 99:
        adjacents.add((row + 1, col))

    if col > 0:
        adjacents.add((row, col - 1))
    if col < 99:
        adjacents.add((row, col + 1))
    return adjacents


def traverse_basin(grid, start):
    os = deque([start])
    cs = set()
    size = 0

    while os:
        row, col = os.pop()
        curr = grid[row][col]
        
        if curr < 9:
            size += 1
            # find neighbours
            n = get_adjacent(grid, row, col)
            for r, c in n:
                if (r, c) not in os and (r, c) not in cs:
                    os.appendleft((r, c))
        cs.add((row, col))

    return size


def part2(grid):
    basins = []
    low_points = get_low_points(grid)
    for r, c in low_points:
        count = traverse_basin(grid, (r, c))
        basins.append(count)
    basins.sort()
    return reduce(lambda x, y: x * y, basins[-3:])


if __name__ == "__main__":
    with open("input") as infile:
        data = [l.strip() for l in infile.readlines() if l]
    data = [[int(x) for x in line] for line in data]
    # print(data)
    print(">>>Day 9<<<")
    c = part1(data)
    print(f"Part 1: {c}")
    c = part2(data)
    print(f"Part 2: {c}")
