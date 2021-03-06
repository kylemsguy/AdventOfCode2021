# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

def part1(data):
    curr_min = 1e99
    # print(min(data), max(data))
    for i in range(max(data)+1):
        curr_sum = 0
        # print(i)
        for d in data:
            curr_sum += abs(d - i)
        if curr_sum < curr_min:
            curr_min = curr_sum

    return curr_min


def part2(data):
    curr_min = 1e99
    # Or you could just use [n(n+1)]/2
    partial = [0]
    for i in range(1, max(data) + 1):
        partial.append(partial[i - 1] + i)

    for i in range(max(data)+1):
        curr_sum = 0
        # print(i)
        for d in data:
            dist = abs(d - i)
            # Or you could just use [n(n+1)]/2
            cost = partial[dist]
            curr_sum += cost
                
        if curr_sum < curr_min:
            curr_min = curr_sum

    return curr_min


def part2_smart(data):
    curr_min = 1e99
    # Or you could just use [n(n+1)]/2
    partial = [0]
    for i in range(1, max(data) + 1):
        partial.append(partial[i - 1] + i)

    for i in range(max(data)+1):
        curr_sum = 0
        # print(i)
        for d in data:
            dist = abs(d - i)
            cost = (dist * (dist + 1)) // 2
            curr_sum += cost
                
        if curr_sum < curr_min:
            curr_min = curr_sum

    return curr_min


if __name__ == "__main__":
    with open("input") as infile:
        data = [int(x) for x in infile.read().strip().split(',')]
    # print(data)
    print(">>>Day 7<<<")
    c = part1(data)
    print(f"Part 1: {c}")
    c = part2_smart(data)
    print(f"Part 2: {c}")
