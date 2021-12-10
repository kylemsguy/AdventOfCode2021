# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0

close_map = {
    '(': ')',
    '[': ']',
    '<': '>',
    '{': '}',
}
invalid_score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
completion_score = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

def score_corrupted(line):
    open_stack = []
    score = 0

    is_corrupted = False
    for c in line:
        if c in close_map:
            open_stack.append(close_map[c])
        elif open_stack[-1] == c:
            open_stack.pop()
        else:
            is_corrupted = True
            break
    if is_corrupted:
        return invalid_score[c]
    return 0
    
def score_completion(line):
    open_stack = []

    score = 0
    for c in line:
        if c in close_map:
            open_stack.append(close_map[c])
        elif open_stack[-1] == c:
            open_stack.pop()
        else:
            return 0

    while open_stack:
        score = score * 5 + completion_score[open_stack.pop()]
    return score

def part1(data):
    score = 0
    for line in data:
        score += score_corrupted(line)
    return score


def part2(data):
    scores = []
    for line in data:
        score = score_completion(line)
        if score:
            scores.append(score)
    scores.sort()
    # print(scores)
    return scores[len(scores)//2]



if __name__ == "__main__":
    with open("input") as infile:
    # with open("inputsmall") as infile:
        data = [l.strip() for l in infile.readlines() if l]
    # print(data)
    print(">>>Day 10<<<")
    c = part1(data)
    print(f"Part 1: {c}")
    c = part2(data)
    print(f"Part 2: {c}")
