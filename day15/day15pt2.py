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
        self.actual_cost = 0
        self.prev = None
    
    def __lt__(self, other):
        return self.cost < other.cost

    def __repr__(self):
        return f"{self.x}, {self.y}; {self.cost} <- {self.prev.x if self.prev else None},{self.prev.y if self.prev else None}"


def get_cost(grid, row, col):
    repeat_right = row // len(grid)
    offset_right = row % len(grid)

    repeat_down = col // len(grid)
    offset_down = col % len(grid)

    return (int(grid[offset_right][offset_down]) + (repeat_right + repeat_down) - 1) % 9 + 1


def heuristic(data, x, y, multiplier=1):
    limit = len(data) * multiplier
    return limit - x + limit - y
    # cost = 0
    # for i in range(x+1, len(data) * multiplier):
    #     # print(i, y)
    #     cost += get_cost(data, i, y)
    # for i in range(y+1, len(data) * multiplier):
    #     # print((len(data) * multiplier - 1, i))
    #     cost += get_cost(data, len(data) * multiplier - 1, i)
    # return cost


def get_adjacent(grid, row, col):
    adjacents = set()
    limit = len(grid) * 5
    if row > 0:
        adjacents.add((row - 1, col))

    if row < limit - 1:
        adjacents.add((row + 1, col))

    if col > 0:
        adjacents.add((row, col - 1))
    if col < limit - 1:
        adjacents.add((row, col + 1))
    return adjacents


def astar(data):
    openq = [Node(0, 0, 0)]
    openset = {(0, 0): openq[0]}
    seen = {(0, 0): openq[0]}

    iter = 0
    while openq:
        curr = heapq.heappop(openq)
        iter += 1
        if iter % 10000 == 0:
            print(iter, curr)
        del openset[(curr.x, curr.y)]
        # if curr.x == len(data) - 1 and curr.y == len(data) - 1:
        if curr.x == (len(data) * 5) - 1 and curr.y == (len(data) * 5) - 1:
            # print(curr.x, curr.y, curr.actual_cost, curr.cost)
            print(iter)
            return curr.actual_cost
        for x, y in get_adjacent(data, curr.x, curr.y):
            if (x, y) in seen:
                neighbour = seen[(x, y)]
            else:
                neighbour = Node(x, y, float('inf'))
                neighbour.actual_cost = float('inf')
                seen[(x, y)] = neighbour
            cost = curr.actual_cost + get_cost(data, x, y)

            if cost < neighbour.actual_cost:
                neighbour.cost = cost + heuristic(data, x, y, 5)
                neighbour.actual_cost = cost
                neighbour.prev = curr
                if (x,y) not in openset:
                    openset[(x, y)] = neighbour
                    openq.append(neighbour)
                heapq.heapify(openq)


def part2(data):
    return astar(data)
    # 4196 is too high
    # 4220 is too high        


if __name__ == "__main__":
    with open("input") as infile: # 3033
    # with open("inputsmall.txt") as infile: # 40  # 315
        data = [x.strip() for x in infile.readlines() if x]

    # print(heuristic(data, 0, 0, 5))

    # for i in range(50):
    #     for j in range(50):
    #         print(get_cost(data, i, j), end=',')
    #     print()
    # print(data)
    print(">>>Day 15<<<")
    # c = part1(data)
    # print(f"Part 1: {c}")
    c = part2(data)
    print(f"Part 2: {c}")
