# solution 1 (python)
# problem ref: https://neetcode.io/problems/duplicate-integer/question?list=neetcode250

# Example:
#
# Input: nums = [1, 2, 3, 3]
# Output: true
#
# Input: nums = [1, 2, 3, 4]
# Output: false

from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        return True if len(s) != len(nums) else False


if __name__ == "__main__":
    s = Solution()

    a = s.hasDuplicate(nums=[1, 2, 3, 3])
    b = s.hasDuplicate(nums=[1, 2, 3, 4])

    print(a, b)

# time complexity: O(1)
