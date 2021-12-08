# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

def simulate(data, days):
    curr = data[:]
    for i in range(days):
        newfish = 0
        for f in range(len(curr)):
            val = curr[f] - 1
            if val < 0:
                val = 6
                curr.append(8)
                newfish += 1
            curr[f] = val
        print(f"Day {i}: {len(curr) - newfish}, newfish: {newfish}")
    return len(curr)

def simulate2(data, days):
    fishes = [0 for x in range(9)]
    for f in data:
        fishes[f] += 1

    print(fishes)
    
    for i in range(days):
        zero = fishes[0]
        for i in range(8):
            fishes[i] = fishes[i+1]
        fishes[-1] = zero
        fishes[6] += zero
    
    print(fishes)

    return sum(fishes)

def part1(data):
    return simulate(data, 80)

def part2(data):
    return simulate2(data, 256)


if __name__ == "__main__":
    with open("input") as infile:
        data = [int(x) for x in infile.read().strip().split(',')]
    # print(data)
    print(">>>Day 6<<<")
    c = part1(data)
    print(f"Part 1: {c}")
    c = part2(data)
    print(f"Part 2: {c}")
