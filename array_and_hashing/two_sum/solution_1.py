# solution 1 (python)
# problem ref: https://neetcode.io/problems/two-integer-sum/question?list=neetcode250

# Example:
#
# Input: nums = [3,4,5,6], target = 7
# Output: [0,1]
#
# Input: nums = [4,5,6], target = 10
# Output: [0,2]
#
# Input: nums = [5,5], target = 10
# Output: [0,1]

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]
        return []


if __name__ == "__main__":
    s = Solution()

    a = s.twoSum(nums=[3, 4, 5, 6], target=7)
    b = s.twoSum(nums=[4, 5, 6], target=10)
    c = s.twoSum(nums=[5, 5], target=10)

    print(a, b, c)

# time complexity: O(N^2)
