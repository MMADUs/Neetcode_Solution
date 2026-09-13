# solution 1 (python)
# problem ref: https://neetcode.io/problems/majority-element-ii/question?list=neetcode250

# Example:
#
# Input: nums = [5,2,3,2,2,2,2,5,5,5]
# Output: [2,5]
#
# Input: nums = [4,4,4,4,4]
# Output: [4]
#
# Input: nums = [1,2,3]
# Output: []

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) // 3

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        result = []

        for k, v in freq.items():
            if v > threshold:
                result.append(k)

        return result


if __name__ == "__main__":
    s = Solution()

    a = s.majorityElement(nums=[5, 2, 3, 2, 2, 2, 2, 5, 5, 5])
    b = s.majorityElement(nums=[4, 4, 4, 4, 4])
    c = s.majorityElement(nums=[1, 2, 3])

    print(a, b, c)

# time complexity: O(N)
