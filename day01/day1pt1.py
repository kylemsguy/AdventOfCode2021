def part1():
    with open("input") as infile:
        data = [int(l.strip()) for l in infile.readlines() if l]
    count = 0
    prev = -1e99
    for d in data:
        if d > prev:
            count += 1
        prev = d
    return count - 1

if __name__ == "__main__":
    c = part1()
    print(c)
