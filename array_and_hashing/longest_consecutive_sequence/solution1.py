# solution 1 (python)
# problem ref: https://neetcode.io/problems/longest-consecutive-sequence/question

# Example:
#
# Input: nums = [2,20,4,10,3,4,5]
# Output: 4
#
# Input: nums = [0,3,2,5,4,6,1,1]
# Output: 7

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
            left_idx += 1
            idx += 1
        else:
            nums[idx] = right_nums[right_idx]
            right_idx += 1
            idx += 1

    while left_idx < left_size:
        nums[idx] = left_nums[left_idx]
        left_idx += 1
        idx += 1

    while right_idx < right_size:
        nums[idx] = right_nums[right_idx]
        right_idx += 1
        idx += 1


def divide(nums: List[int], left: int, right: int):
    if left >= right:
        return

    mid = (left + right) // 2

    divide(nums, left, mid)
    divide(nums, mid + 1, right)

    merge(nums, left, mid, right)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        divide(nums, left=0, right=len(nums) - 1)

        freq = 1
        max_freq = 1

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue

            if nums[i] + 1 == nums[i + 1]:
                freq += 1
            else:
                freq = 1

            max_freq = max(max_freq, freq)

        return max_freq


if __name__ == "__main__":
    s = Solution()

    a = s.longestConsecutive(nums=[2, 20, 4, 10, 3, 4, 5])
    b = s.longestConsecutive(nums=[0, 3, 2, 5, 4, 6, 1, 1])

    print(a, b)

# time complexity: O(N . log(N))
