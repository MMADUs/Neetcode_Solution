# solution 2 (python)
# problem ref: https://neetcode.io/problems/subarray-sum-equals-k/question

# Example:
#
# Input: nums = [2,-1,1,2], k = 2
# Output: 4
#
# Input: nums = [4,4,4,4,4,4], k = 4
# Output: 6

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {}

        curr = 0
        total = 0

        for num in nums:
            freq[curr] = freq.get(curr, 0) + 1
            curr += num
            total += freq.get(curr - k, 0)

        return total


if __name__ == "__main__":
    s = Solution()

    a = s.subarraySum(nums=[2, -1, 1, 2], k=2)
    b = s.subarraySum(nums=[4, 4, 4, 4, 4, 4], k=4)

    print(a, b)

# time complexity: O(N)
