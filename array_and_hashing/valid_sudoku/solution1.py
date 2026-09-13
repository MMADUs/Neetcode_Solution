# solution 1 (python)
# problem ref: https://neetcode.io/problems/valid-sudoku/question?list=neetcode250

# Example:
#
# Input: board =
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","8",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]
#
# Output: true
#
# Input: board =
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","1",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]
#
# Output: false

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check 3x3 sub grid for duplicates
        for i in range(1, len(board) + 1):
            # only accept every 3 row
            if i % 3 != 0:
                continue

            col = []

            for j in range(1, len(board) + 1):
                # only accept every 3 col
                col.append(j - 1)

                if j % 3 != 0:
                    continue

                hashset = set()

                # THIS IS CONSTANT TO SUB GRID SIZE OF 3 X 3
                for c in col:
                    for r in range(i - 1, i - 1 - 3, -1):
                        v = board[c][r]

                        # ignore pad
                        if v == ".":
                            continue

                        if v not in hashset:
                            hashset.add(v)
                        else:
                            return False

                col.clear()

        def is_duplicate(values):
            hashset = set()

            for v in values:
                # ignore pad
                if v == ".":
                    continue

                if v not in hashset:
                    hashset.add(v)
                else:
                    return True

            return False

        # check each row and col should not contain duplicates
        # diagonal approaches
        for i in range(len(board)):
            vertical = [row[i] for row in board]
            horizontal = board[i][:]

            if is_duplicate(vertical):
                return False 

            if is_duplicate(horizontal):
                return False 

        return True


if __name__ == "__main__":
    s = Solution()

    a = s.isValidSudoku(
        board=[
            ["1", "2", ".", ".", "3", ".", ".", ".", "."],
            ["4", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", ".", "3"],
            ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
            [".", ".", ".", "8", ".", "3", ".", ".", "5"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", ".", ".", ".", ".", ".", "2", ".", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "8"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )

    b = s.isValidSudoku(
        board=[
            ["1", "2", ".", ".", "3", ".", ".", ".", "."],
            ["4", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", "9", "1", ".", ".", ".", ".", ".", "3"],
            ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
            [".", ".", ".", "8", ".", "3", ".", ".", "5"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", ".", ".", ".", ".", ".", "2", ".", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "8"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )

    print(a, b)

# time complexity: O(N^2)
