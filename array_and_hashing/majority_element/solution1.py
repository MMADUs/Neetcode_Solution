# solution 1 (python)
# problem ref: https://neetcode.io/problems/majority-element/question?list=neetcode250

# Example:
#
# Input: nums = [5,5,1,1,1,5,5]
# Output: 5
#
# Input: nums = [2,2,2]
# Output: 2

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = len(nums) // 2

        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

            if freq[n] > threshold:
                return n

        return next(iter(freq.keys()))


if __name__ == "__main__":
    s = Solution()

    a = s.majorityElement(nums=[5,5,1,1,1,5,5])
    b = s.majorityElement(nums=[2,2,2])

    print(a, b)

# time complexity: O(N)