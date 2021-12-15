# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0
import sys
import string
import heapq
from collections import defaultdict

class Node:
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = int(cost) if isinstance(cost, str) else cost
        self.prev = None
    
    def __lt__(self, other):
        return self.cost < other.cost

    def __repr__(self):
        return f"{self.x}, {self.y}; {self.cost} <- {self.prev}"


def get_adjacent(grid, row, col):
    curr = grid[row][col]
    adjacents = set()
    if row > 0:
        adjacents.add((row - 1, col))

    if row < len(grid)-1:
        adjacents.add((row + 1, col))

    if col > 0:
        adjacents.add((row, col - 1))
    if col < len(grid)-1:
        adjacents.add((row, col + 1))
    return adjacents


def part1(data):
    start = Node(0, 0, data[0][0])

    openset = []
    allpoints = []

    for r, row in enumerate(data):
        curr_r = []
        for c, col in enumerate(row):
            p = Node(r, c, float('inf'))
            openset.append(p)
            curr_r.append(p)
        allpoints.append(curr_r)
    allpoints[0][0].cost = 0
    heapq.heapify(openset)
    while openset:
        curr = heapq.heappop(openset)
        # print(curr)
        allpoints[curr.x][curr.y] = None
        if curr.x == len(data) - 1 and curr.y == len(data) - 1:
            return curr.cost
        for x, y in get_adjacent(data, curr.x, curr.y):
            if allpoints[x][y] is None:
                continue
            # print(x, y)
            cost = curr.cost + int(data[x][y])
            if cost < allpoints[x][y].cost:
                allpoints[x][y].cost = cost
                allpoints[x][y].prev = curr
                heapq.heapify(openset)




def part2(data):
    pass


if __name__ == "__main__":
    with open("input") as infile:
    # with open("inputsmall.txt") as infile:
        data = [x.strip() for x in infile.readlines() if x]
    # print(data)
    print(">>>Day 15<<<")
    c = part1(data)
    print(f"Part 1: {c}")
    c = part2(data)
    print(f"Part 2: {c}")
