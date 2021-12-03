def get_bit_score(data, idx):
    score = 0
    for val in data:
        bit = val[idx]
        if bit == '0':
            score -= 1
        else:
            score += 1
    return score


def part1(data):
    gamma = [0 for _ in data[0]]
    for i, val in enumerate(data):
        for j, bit in enumerate(val):
            if bit == '0':
                gamma[j] -= 1
            else:
                gamma[j] += 1
    g = ''.join(['1' if x > 0 else '0' for x in gamma])
    l = ''.join(['0' if x > 0 else '1' for x in gamma])

    # print(g, l)

    return int(g, 2) * int(l, 2)


def part2(data):
    bits = len(data[0])

    left_o = data[:]
    for i in range(bits):
        score = get_bit_score(left_o, i)
        most_common = '1' if score >= 0 else '0'
        left_o = [x for x in left_o if x[i] == most_common]
        if len(left_o) == 1:
            break
    o = int(left_o[0], 2)
    

    left_c = data[:]
    for i in range(bits):
        score = get_bit_score(left_c, i)
        least_common = '0' if score >= 0 else '1'
        left_c = [x for x in left_c if x[i] == least_common]
        if len(left_c) == 1:
            break
    c = int(left_c[0], 2)

    return o * c    


if __name__ == "__main__":
    with open("input") as infile:
        data = [l.strip() for l in infile.readlines() if l]
    # print(data)
    print(">>>Day 3<<<")
    c = part1(data)
    print(f"Part 1: {c}")
    c = part2(data)
    print(f"Part 2: {c}")
