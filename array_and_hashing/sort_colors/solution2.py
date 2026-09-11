# solution 2 (python)
# problem ref: https://neetcode.io/problems/sort-colors/question?list=neetcode250

# Example:
#
# Input: nums = [1,0,1,2]
# Output: [0,1,1,2]
#
# Input: nums = [2,1,0]
# Output: [0,1,2]

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            # low region own by 0
            if nums[mid] == 0:
                tmp_low = nums[low]
                nums[low] = nums[mid]
                nums[mid] = tmp_low

                low += 1
                mid += 1

            # mid region own by 1
            elif nums[mid] == 1:
                mid += 1

            # high region own by 2
            elif nums[mid] == 2:
                tmp_high = nums[mid]
                nums[mid] = nums[high]
                nums[high] = tmp_high

                high -= 1

        return nums


# solution with Dutch National Flag algorithm (three-pointers) because the element is known (0, 1, and 2) only

if __name__ == "__main__":
    s = Solution()

    a = s.sortColors(nums=[1, 0, 1, 2])
    b = s.sortColors(nums=[2, 1, 0])

    print(a, b)

# time complexity: O(N)
