def part1(data):
    count = 0
    prev = -1e99
    for d in data:
        if d > prev:
            count += 1
        prev = d
    return count - 1


def part2(data):
    count = 0
    part_sum = sum(data[0:3])

    for i in range(3,len(data)):
        next_sum = part_sum - data[i - 3] + data[i]
        if next_sum > part_sum:
            count += 1

    return count


if __name__ == "__main__":
    with open("input") as infile:
        data = [int(l.strip()) for l in infile.readlines() if l]
    print(">>>Day 1<<<")
    c = part1(data)
    print(f"Part 1: {c}")
    c = part2(data)
    print(f"Part 2: {c}")
