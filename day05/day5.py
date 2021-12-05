def is_horizontal(beg, end):
    return beg[0] == end[0] or beg[1] == end[1]

def mark_grid(grid, beg, end):
    if beg[0] == end[0]:
        start = min(beg[1], end[1])
        end = max(beg[1], end[1])
        for c in range(start, end+1):
            grid[beg[0]][c] += 1
    else:
        start = min(beg[0], end[0])
        end = max(beg[0], end[0])
        for r in range(start, end+1):
            grid[r][beg[1]] += 1
    # print(start, end)

def mark_grid_diagonal(grid, beg, end):
    x, y = beg
    xe, ye = end
    while x != xe and y != ye:
        grid[x][y] += 1
        x += 1 if x < xe else -1
        y += 1 if y < ye else -1
    grid[xe][ye] += 1

def part1(data):
    lines = []
    for x in data:
        parts = x.split(' -> ')
        x1, y1 = parts[0].split(',')
        x2, y2 = parts[1].split(',')

        lines.append((
            (int(x1), int(y1)),
            (int(x2), int(y2)),
        ))

    cardinal = [x for x in lines if is_horizontal(x[0], x[1])]

    grid = [[0 for y in range(1000)] for x in range(1000)]

    for b, e in cardinal:
        mark_grid(grid, b, e)

    overlap = 0
    for r in grid:
        for c in r:
            if c > 1:
                overlap += 1
    return overlap


def part2(data):
    lines = []
    for x in data:
        parts = x.split(' -> ')
        x1, y1 = parts[0].split(',')
        x2, y2 = parts[1].split(',')

        lines.append((
            (int(x1), int(y1)),
            (int(x2), int(y2)),
        ))

    cardinal = [x for x in lines if is_horizontal(x[0], x[1])]
    others = [x for x in lines if not is_horizontal(x[0], x[1])]

    grid = [[0 for y in range(1000)] for x in range(1000)]

    for b, e in cardinal:
        mark_grid(grid, b, e)

    for b, e in others:
        mark_grid_diagonal(grid, b, e)

    overlap = 0
    for r in grid:
        for c in r:
            if c > 1:
                overlap += 1
    return overlap


if __name__ == "__main__":
    with open("input") as infile:
        data = [l.strip() for l in infile.readlines() if l]
    # print(data)
    print(">>>Day 5<<<")
    c = part1(data)
    print(f"Part 1: {c}")
    c = part2(data)
    print(f"Part 2: {c}")
