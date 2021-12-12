# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

# NOTE: A bunch of this code is unnecessary, but it works.
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
        self.current_v = 0

    def visit(self):
        self.v += 1
        if not self.big:
            self.current_v += 1
            if self.current_v > 1:
                return True
        return False
    
    def unvisit(self):
        if self.big:
            return False
        self.current_v -= 1
        if self.current_v > 0:
            return True
        return False


    def add_neighbour(self, other):
        self.connected.add(other)
        other.connected.add(self)
    
    def get_neighbours(self, curr_path=[], allow_repeat=True):
        nnv = []
        for n in list(self.connected):
            if n.name == 'start':
                continue
            if n.big:
                nnv.append(n)
            elif n not in curr_path:
                nnv.append(n)
            elif allow_repeat:
                nnv.append(n)
        return nnv

    def __repr__(self):
        return self.name


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

def visit(start):
    curr_path = [start]
    to_search = [(True, start.get_neighbours())]
    count = 0
    while curr_path:
        # print(curr_path)
        # print(to_search)
        if curr_path[-1].name == 'end':
            count += 1
            # print(curr_path)
            curr = curr_path.pop()
            to_search.pop()
        if not to_search[-1][1]:
            curr = curr_path.pop()
            curr.unvisit()
            to_search.pop()
            continue
        allow_repeat, left = to_search[-1]
        n = left.pop()
        if n.name == 'end':
            n.visit()
        if n.visit():
            allow_repeat = False
        curr_path.append(n)
        n_neighbours = n.get_neighbours(curr_path, allow_repeat)
        to_search.append((allow_repeat, n_neighbours))
    return count


def part1(caves):
    visit(caves['start'])
    return caves['end'].v

def part2(caves):
    return visit(caves['start'])
    # return caves['end'].v


if __name__ == "__main__":
    with open("input") as infile:
    # with open("inputsmall") as infile:
        data = [x.strip() for x in infile.readlines()]
    # print(data)
    # caves = construct(data)
    print(">>>Day 11<<<")
    # c = part1(caves)
    # print(f"Part 1: {c}")
    caves = construct(data)
    # print(caves)
    c = part2(caves)
    print(f"Part 2: {c}")
