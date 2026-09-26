# solution 1 (python)
# problem ref: https://neetcode.io/problems/products-of-array-discluding-self/question?list=neetcode250

# Example:
#
# Input: nums = [1,2,4,6]
# Output: [48,24,12,8]
#
# Input: nums = [-1,0,1,2,3]
# Output: [0,-6,0,0,0]

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        for i in range(len(nums)):
            for j, num in enumerate(nums):
                if i != j:
                    result[i] *= num

        return result


if __name__ == "__main__":
    s = Solution()

    a = s.productExceptSelf(nums=[1, 2, 4, 6])
    b = s.productExceptSelf(nums=[-1, 0, 1, 2, 3])

    print(a, b)

# time complexity: O(N^2)
