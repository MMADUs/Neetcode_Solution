# solution 1 (python)
# problem ref: https://neetcode.io/problems/range-sum-query-2d-immutable/question?list=neetcode250

# Example:
#
# NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
# numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
# numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
# numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)

from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0

        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                sum += self.matrix[i][j]

        return sum


if __name__ == "__main__":
    m = NumMatrix(
        matrix=[
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5],
        ]
    )

    a = m.sumRegion(2, 1, 4, 3)  # 8
    b = m.sumRegion(1, 1, 2, 2)  # 11
    c = m.sumRegion(1, 2, 2, 4)  # 12

    print(a, b, c)

# time complexity: O(1) easily a constant because direct access, or maybe O(K) where K is the num of element within the square
