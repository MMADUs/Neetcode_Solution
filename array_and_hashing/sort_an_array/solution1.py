# solution 1 (python)
# problem ref: https://neetcode.io/problems/sort-an-array/question?list=neetcode250

# Example:
#
# Input: nums = [10,9,1,1,1,2,3,1]
# Output: [1,1,1,1,2,3,9,10]
#
# Input: nums = [5,10,2,1,3]
# Output: [1,2,3,5,10]

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp
        return nums


if __name__ == "__main__":
    s = Solution()

    a = s.sortArray(nums=[10, 9, 1, 1, 1, 2, 3, 1])
    b = s.sortArray(nums=[5, 10, 2, 1, 3])

    print(a, b)

# time complexity: O(N^2)
