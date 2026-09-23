# solution 2 (python)
# problem ref: https://neetcode.io/problems/longest-consecutive-sequence/question

# Example:
#
# Input: nums = [2,20,4,10,3,4,5]
# Output: 4
#
# Input: nums = [0,3,2,5,4,6,1,1]
# Output: 7

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        count = 0

        for n in hashset:
            if n - 1 not in hashset:
                curr = n
                while curr in hashset:
                    curr += 1
                count = max(count, curr - n)

        return count


if __name__ == "__main__":
    s = Solution()

    a = s.longestConsecutive(nums=[2, 20, 4, 10, 3, 4, 5])
    b = s.longestConsecutive(nums=[0, 3, 2, 5, 4, 6, 1, 1])

    print(a, b)

# time complexity: O(N)
