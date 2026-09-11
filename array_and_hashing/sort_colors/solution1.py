# solution 1 (python)
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
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        idx = 0

        # needs to sort the reconstruction
        for k in range(3):
            for _ in range(freq.get(k, 0)):
                nums[idx] = k
                idx += 1

        return nums


# my solution uses frequencies instead of sorting algorithm because the element is known (0, 1, and 2) only

if __name__ == "__main__":
    s = Solution()

    a = s.sortColors(nums=[1, 0, 1, 2])
    b = s.sortColors(nums=[2, 1, 0])

    print(a, b)

# time complexity: O(N)
