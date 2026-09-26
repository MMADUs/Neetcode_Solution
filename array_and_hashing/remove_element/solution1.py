# solution 1 (python)
# problem ref: https://neetcode.io/problems/remove-element/question?list=neetcode250

# Custom judge:
#
# int[] nums = [...]; // Input array
# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
#                             // It is sorted with no values equaling val.
#
# int k = removeElement(nums, val); // Calls your implementation
#
# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }

# Example:
#
# Input: nums = [3,2,2,3], val = 3
# Output: k = 2, nums = [2,2,_,_]
#
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: k = 5, nums = [0,1,3,0,4,_,_,_]

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)


if __name__ == "__main__":
    s = Solution()

    a = s.removeElement(nums=[3, 2, 2, 3], val=3)
    b = s.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2)

    print(a, b)

# time complexity: O(K) where K is number of only `val` value