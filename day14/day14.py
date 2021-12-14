# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0
import sys
import string
from collections import defaultdict


def parse(data):
    template = data[0].strip()
    rules = {}
    for line in data[2:]:
        match, insert = line.split(" -> ")
        if match in rules:
            print("Duplicate rule", line)
            exit(1)
        rules[match] = insert
    return template, rules


def part1(template, rules):
    counts = {l: 0 for l in string.ascii_uppercase}

    for s in template:
        counts[s] += 1
    
    for i in range(10):
        # do the insert
        next_t = [template[0]]
        for i in range(1, len(template)):
            p = template[i-1:i+1]
            if p in rules:
                counts[rules[p]] += 1
                next_t.append(rules[p])
            next_t.append(p[1])
        template = ''.join(next_t)
    print(counts)
    finalcounts = [x for x in counts.values() if x > 0]
    return max(finalcounts) - min(finalcounts)


def part2(template, rules):
    counts = {l: 0 for l in string.ascii_uppercase}

    for s in template:
        counts[s] += 1
    pair_counts = defaultdict(int)
    for i in range(1, len(template)):
        pair = template[i-1: i+1]
        pair_counts[pair] += 1
    
    for i in range(40):
        new_pair_counts = defaultdict(int)
        for pair, count in pair_counts.items():
            if pair in rules:
                c1, c2 = pair
                addi = rules[pair]
                new_pair_counts[c1 + addi] += count
                new_pair_counts[addi + c2] += count
                counts[addi] += count
        pair_counts = new_pair_counts
    
    finalcounts = [x for x in counts.values() if x > 0]
    return max(finalcounts) - min(finalcounts)


if __name__ == "__main__":
    with open("input") as infile:
    # with open("inputsmall") as infile:
        rawdata = [x.strip() for x in infile.readlines() if x]
    data = parse(rawdata)
    # print(data)
    print(">>>Day 13<<<")
    c = part1(*data)
    print(f"Part 1: {c}")
    c = part2(*data)
    print(f"Part 2: {c}")
