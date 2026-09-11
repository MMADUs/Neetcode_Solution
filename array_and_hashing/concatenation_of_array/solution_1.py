# solution 1 (python)
# problem ref: https://neetcode.io/problems/concatenation-of-array/question?list=neetcode250

# Example:
#
# Input: nums = [1,4,1,2]
# Output: [1,4,1,2,1,4,1,2]
#
# Input: nums = [22,21,20,1]
# Output: [22,21,20,1,22,21,20,1]

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


if __name__ == "__main__":
    s = Solution()

    a = s.getConcatenation(nums=[1, 4, 1, 2])
    b = s.getConcatenation(nums=[22, 21, 20, 1])

    print(a, b)

# time complexity: O(1)