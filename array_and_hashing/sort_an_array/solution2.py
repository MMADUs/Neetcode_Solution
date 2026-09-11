# solution 2 (python)
# problem ref: https://neetcode.io/problems/sort-an-array/question?list=neetcode250

# Example:
#
# Input: nums = [10,9,1,1,1,2,3,1]
# Output: [1,1,1,1,2,3,9,10]
#
# Input: nums = [5,10,2,1,3]
# Output: [1,2,3,5,10]

from typing import List


def merge(nums: List[int], left: int, mid: int, right: int):
    left_size = mid - left + 1
    right_size = right - mid

    left_nums = [nums[left + i] for i in range(left_size)]
    right_nums = [nums[mid + i + 1] for i in range(right_size)]

    idx, left_idx, right_idx = left, 0, 0

    while left_idx < left_size and right_idx < right_size:
        if left_nums[left_idx] < right_nums[right_idx]:
            nums[idx] = left_nums[left_idx]
            idx += 1
            left_idx += 1
        else:
            nums[idx] = right_nums[right_idx]
            idx += 1
            right_idx += 1

    while left_idx < left_size:
        nums[idx] = left_nums[left_idx]
        idx += 1
        left_idx += 1

    while right_idx < right_size:
        nums[idx] = right_nums[right_idx]
        idx += 1
        right_idx += 1


def divide(nums: List[int], left: int, right: int):
    if left >= right:
        return

    mid = (left + right) // 2

    divide(nums, left, mid)
    divide(nums, mid + 1, right)

    merge(nums, left, mid, right)


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        divide(nums, left=0, right=len(nums) - 1)
        return nums


if __name__ == "__main__":
    s = Solution()

    a = s.sortArray(nums=[10, 9, 1, 1, 1, 2, 3, 1])
    b = s.sortArray(nums=[5, 10, 2, 1, 3])

    print(a, b)

# time complexity: O(N . log(N))
