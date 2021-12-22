"""Day 04"""
from typing import List


class BingoBoard:
    rows: List[List[int]]
    marks: List[List[str]]
    row_strs: List[str]

    def __init__(self, row_strs: List[str]):
        self.row_strs = row_strs
        self.rows = [[int(x) for x in row.strip().split()] for row in row_strs]
        self.marks = [[' ' for _ in range(5)] for _ in range(5)]

    def __repr__(self):
        reps = []
        for idx, mark_row in enumerate(self.marks):
            rep_row = []
            for midx, mark in enumerate(mark_row):
                num = self.rows[idx][midx]
                if mark == 'x':
                    rep_row.append(f"*{num}*")
                else:
                    rep_row.append(str(num))
            reps.append(rep_row)
        results = []
        for rep in reps:
            results.append(("{:<5}"*5).format(*rep))
        return '\n'.join(results)

    def copy(self) -> 'BingoBoard':
        result = BingoBoard(row_strs=self.row_strs)
        result.marks = self.marks.copy()
        return result
   
    def mark(self, num: int):
        for idx, row in enumerate(self.rows):
            if num in row:
                self.marks[idx][row.index(num)] = 'x'
 
    def check(self) -> bool:
        for idx, mark in enumerate(self.marks):
            vertical = [self.marks[i][idx] for i in range(5)]
            if ['x']*5 in [mark, vertical]:
                return True
        return False
    
    def unmarked_sum(self) -> int:
        total = 0
        for row_idx, mark_row in enumerate(self.marks):
            for idx, mark in enumerate(mark_row):
                if mark == ' ':
                    total += self.rows[row_idx][idx]
        return total


def process(filename):
    boards = []
    tmp_lines = []
    with open(filename) as infile:
        numbers = [int(x) for x in infile.readline().strip().split(',')]
        for line in infile.readlines():
            if line.strip() == '':
                if len(tmp_lines) == 5:
                    boards.append(BingoBoard(tmp_lines))
                tmp_lines = []
            else:
                tmp_lines.append(line)
        if len(tmp_lines) == 5:
            boards.append(BingoBoard(tmp_lines))

    wins = [False for _ in range(len(boards))]
    last_winner = None
    last_winning_number = None
    for idx, number in enumerate(numbers):
        for bidx, board in enumerate(boards):
            if wins[bidx]:
                continue
            board.mark(number)
            if board.check():
                wins[bidx] = True
                last_winner = board.copy()
                last_winning_number = number
                print(f"Found winning board on idx: {idx} with {number}\n", board)
                print(f"Sum of unmarked numbers: {board.unmarked_sum()} * {number} == {number * board.unmarked_sum()}")
    
    print(f"Last winner with {last_winning_number}: \n{last_winner}")
    print(f"Sum of unmarked numbers: {last_winner.unmarked_sum()} * {last_winning_number} == {last_winning_number * last_winner.unmarked_sum()}")
    

if __name__ == '__main__':
    process('test.txt')
    process('input.txt')
