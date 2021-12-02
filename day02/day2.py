def part1(data):
    depthc = 0
    distance = 0
    for dirc, dist in data:
        dist = int(dist)
        if dirc == 'up':
            depthc -= dist
        elif dirc == 'down':
            depthc += dist
        elif dirc == 'forward':
            distance += dist
    return depthc*distance

def part2(data):
    aim = 0
    depthc = 0
    distance = 0
    for dirc, dist in data:
        dist = int(dist)
        if dirc == 'up':
            aim -= dist
        elif dirc == 'down':
            aim += dist
        elif dirc == 'forward':
            distance += dist
            depthc += aim * dist
    return depthc*distance


if __name__ == "__main__":
    with open("input") as infile:
        data = [l.strip().split(' ') for l in infile.readlines() if l]
    # print(data)
    print(">>>Day 2<<<")
    c = part1(data)
    print(f"Part 1: {c}")
    c = part2(data)
    print(f"Part 2: {c}")
