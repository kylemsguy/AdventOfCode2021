def part2():
    with open("input") as infile:
        data = [int(l.strip()) for l in infile.readlines() if l]
    count = 0
    part_sum = sum(data[0:3])

    for i in range(3,len(data)):
        next_sum = part_sum - data[i - 3] + data[i]
        if next_sum > part_sum:
            count += 1

    return count

if __name__ == "__main__":
    c = part2()
    print(c)
