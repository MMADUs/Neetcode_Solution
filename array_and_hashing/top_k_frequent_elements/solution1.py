# solution 1 (python)
# problem ref: https://neetcode.io/problems/top-k-elements-in-list/question?list=neetcode250

# Example:
#
# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]
#
# Input: nums = [7,7], k = 1
# Output: [7]

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        top_k = []

        for _ in range(k):
            biggest = None

            for k, v in freq.items():
                if k in top_k:
                    continue

                if biggest is None:
                    biggest = (k, v)
                else:
                    if v > biggest[1]:
                        biggest = (k, v)

            top_k.append(biggest[0])

        return top_k


if __name__ == "__main__":
    s = Solution()

    a = s.topKFrequent(nums=[1, 2, 2, 3, 3, 3], k=2)
    b = s.topKFrequent(nums=[7, 7], k=1)

    print(a, b)

# time complexity: O(N + KU), where K is top k and U is number of unique numbers
