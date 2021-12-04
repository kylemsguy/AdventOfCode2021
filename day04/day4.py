class Board:
    def __init__(self, board):
        self.unmarked_sum = 0
        self.board = board
        self.number_map = {}
        self.marked = [[False for c in r] for r in self.board]

        for r, row in enumerate(board):
            for c, item in enumerate(row):
                if item in self.number_map:
                    print("invalid board: no repeats allowed!!!", board)
                    exit(1)
                self.number_map[item] = r, c
                self.unmarked_sum += item
    
    def mark(self, num):
        if num in self.number_map:
            row, col = self.number_map[num]
            self.marked[row][col] = True
            self.unmarked_sum -= num

            return row, col
        return None

    def check_row_col(self, row, col):
        return self.check_col(col) or self.check_row(row)

    def check_col(self, col):
        for r in self.marked:
            if not r[col]:
                return False
        return True

    def check_row(self, row):
        for c in self.marked[row]:
            if not c:
                return False
        return True



def part1(data):
    called = [int(x) for x in data[0].split(',')]

    boards = []
    curr = []
    for i in range(2, len(data)):
        if not data[i]:
            boards.append(Board(curr))
            curr = []
        else:
            curr.append([int(x) for x in data[i].strip().split()])
    
    for n in called:
        for b in boards:
            result = b.mark(n)
            if result:
                if b.check_row_col(*result):
                    return b.unmarked_sum * n


def part2(data):
    called = [int(x) for x in data[0].split(',')]

    boards = []
    curr = []
    for i in range(2, len(data)):
        if not data[i]:
            boards.append(Board(curr))
            curr = []
        else:
            curr.append([int(x) for x in data[i].strip().split()])

    notwon = set(boards)
    for n in called:
        for b in list(notwon):
            result = b.mark(n)
            if result:
                if b.check_row_col(*result):
                    notwon = notwon - {b}
                if len(notwon) == 0:
                    return b.unmarked_sum * n


if __name__ == "__main__":
    with open("input") as infile:
        data = [l.strip() for l in infile.readlines() if l]
    # print(data)
    print(">>>Day 4<<<")
    c = part1(data)
    print(f"Part 1: {c}")
    c = part2(data)
    print(f"Part 2: {c}")
