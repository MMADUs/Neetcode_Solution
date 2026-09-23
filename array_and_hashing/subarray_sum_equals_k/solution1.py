# solution 1 (python)
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
        count = 0

        for i in range(len(nums)):
            sum = 0

            for j in range(i, len(nums)):
                sum += nums[j]

                if sum == k:
                    count += 1

        return count


if __name__ == "__main__":
    s = Solution()

    a = s.subarraySum(nums=[2, -1, 1, 2], k=2)
    b = s.subarraySum(nums=[4, 4, 4, 4, 4, 4], k=4)

    print(a, b)

# time complexity: O(N^2)
