# Note to anyone who looks at this before I clean it up: I'm sorry
# 1 = 2
# 4 = 4
# 7 = 3
# 8 = 7
from collections import defaultdict
def part1(data):
    count = 0
    for line in data:
        d, o = line.strip().split(' | ')
        o = [x for x in o.strip().split(' ') if x]
        for x in o:
            if len(x) in [2, 4, 3, 7]:
                count += 1

    return count

def part2(data):
    output_sum = 0
    for line in data:
        d, o = line.strip().split(' | ')
        d = [x for x in d.strip().split(' ') if x]
        o = [x for x in o.strip().split(' ') if x]

        final_mapping = {x: None for x in range(10)}

        print(len(d))

        d_map = defaultdict(list)
        for x in d:
            d_map[len(x)].append(x)

        l_mapping = {x: set("abcdefg") for x in ['a','b','c','d','e','f','g']}

        # 1 (len 2)
        digit = d_map[2][0]
        final_mapping[1] = digit
        l_mapping['c'] = set(digit)
        l_mapping['f'] = set(digit)

        for key, val in l_mapping.items():
            if key not in 'cf':
                val.difference_update(set(digit))

        # 4 (len 4)
        digit = d_map[4][0]
        final_mapping[4] = digit
        l_mapping['b'] = set(digit)
        l_mapping['d'] = set(digit)
        # l_mapping['c'].update(digit)
        # l_mapping['f'].update(digit)

        for key, val in l_mapping.items():
            if key not in 'bdcf':
                val.difference_update(set(digit))

        # 7 (len 3)
        digit = d_map[3][0]
        final_mapping[7] = digit
        l_mapping['a'] = set(digit) - l_mapping['c']

        for key, val in l_mapping.items():
            if key not in 'acf':
                val.difference_update(set(digit))

        # 6
        sixs = d_map[6]
        eight = d_map[7][0]
        final_mapping[8] = eight
        for num in sixs:
            (num_diff,) = set(eight) - set(num)
            if num_diff in l_mapping['f']:
                # number is 6
                final_mapping[6] = num
                l_mapping['c'] = {num_diff}
                l_mapping['f'].difference_update([num_diff])
                
                for key, val in l_mapping.items():
                    if key != 'c':
                        val.difference_update([num_diff])
                break
        sixs.remove(final_mapping[6])

        # differentiating 0 from 9
        x = sixs[0]

        is_zero = False
        for letter in final_mapping[4]:
            if letter not in x:
                is_zero = True
                break

        if is_zero:
            # this number is 0, and the letter is d
            final_mapping[0] = x
            l_mapping['d'] = set(letter)
            for key, val in l_mapping.items():
                if key != 'd':
                    val.difference_update([letter])
            final_mapping[9] = sixs[1]
        else:
            final_mapping[0] = sixs[1]
            final_mapping[9] = sixs[0]
            x = sixs[1]
            for letter in final_mapping[4]:
                if letter not in x:
                    l_mapping['d'] = set(letter)
                    for key, val in l_mapping.items():
                        if key != 'd':
                            val.difference_update([letter])
                    break

        # print(l_mapping)
        # Subtract 8 from 9 to get e
        print(final_mapping[8])
        letter_e = set(final_mapping[8]) - set(final_mapping[9])
        l_mapping['e'] = set(letter_e)
        l_mapping['g'].difference_update(set(letter_e))
        
        # print(l_mapping, final_mapping)

        # Final
        final_l_mapping = {l: ''.join(s) for l, s in l_mapping.items()}
        # print(final_mapping)

        # two
        mapped_two = set()
        mapped_three = set()
        mapped_five = set()
        for i in "acdfg":
            mapped_three.add(final_l_mapping[i])
        for i in "acdeg":
            mapped_two.add(final_l_mapping[i])
        for i in "abdfg":
            mapped_five.add(final_l_mapping[i])
        for item in d_map[5]:
            if set(item) == mapped_two:
                final_mapping[2] = item
            elif set(item) == mapped_three:
                final_mapping[3] = item
            elif set(item) == mapped_five:
                final_mapping[5] = item

        print(final_mapping)
        reverse_mapping = {frozenset(v): str(k) for k, v in final_mapping.items()}

        digits = []
        for item in o:
            digits.append(reverse_mapping[frozenset(item)])
        output_sum += int(''.join(digits))

    return output_sum

helper = 0


if __name__ == "__main__":
    with open("input") as infile:
        data = [x.strip() for x in infile.readlines() if x]
    # print(data)
    print(">>>Day 6<<<")
    c = part1(data)
    print(f"Part 1: {c}")
    c = part2(data)
    print(f"Part 2: {c}")
