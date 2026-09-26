# solution 2 (python)
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

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result


if __name__ == "__main__":
    s = Solution()

    a = s.productExceptSelf(nums=[1, 2, 4, 6])
    b = s.productExceptSelf(nums=[-1, 0, 1, 2, 3])

    print(a, b)

# time complexity: O(N)
