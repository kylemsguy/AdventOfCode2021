# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

from collections import deque, defaultdict
from copy import deepcopy
from functools import reduce
import string

class Cave:
    def __init__(self, name):
        self.name = name
        self.big = name[0] in string.ascii_uppercase
        self.v = 0
        self.connected = set()

    def visit(self):
        self.v += 1

    def add_neighbour(self, other):
        self.connected.add(other)
        other.connected.add(self)
    
    def get_neighbours(self, visited):
        nnv = []
        for n in list(self.connected):
            if n.big or n not in visited:
                nnv.append(n)
        return nnv

    def get_neighbour2(self, visited):
        nnv = []
        for n in list(self.connected):
            if n.big or visited[n] < 2:
                nnv.append(n)
        return nnv

def construct(data):
    caves = {}
    for line in data:
        c1, c2 = line.split('-')
        if c1 not in caves:
            caves[c1] = Cave(c1)
        if c2 not in caves:
            caves[c2] = Cave(c2)
        caves[c1].add_neighbour(caves[c2])
    return caves

def visit(node, visited=[]):
    node.visit()
    if node.name == 'end':
        return
    neighbours = node.get_neighbours(visited)
    for n in neighbours:
        visit(n, visited + [node])


def part1(caves):
    visit(caves['start'])
    return caves['end'].v

def part2(caves):
    return "See day12p2.py"


if __name__ == "__main__":
    with open("input") as infile:
    # with open("inputsmall") as infile:
        data = [x.strip() for x in infile.readlines()]
    # print(data)
    caves = construct(data)
    print(">>>Day 11<<<")
    c = part1(caves)
    print(f"Part 1: {c}")
    # print(caves)
    c = part2(caves)
    print(f"Part 2: {c}")
