# solution 1 (python)
# problem ref: https://neetcode.io/problems/best-time-to-buy-and-sell-stock-ii/question

# Example:
#
# Input: prices = [7,1,5,3,6,4]
# Output: 7
#
# Input: prices = [1,2,3,4,5]
# Output: 4

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit


if __name__ == "__main__":
    s = Solution()

    a = s.maxProfit(prices=[7, 1, 5, 3, 6, 4])
    b = s.maxProfit(prices=[1, 2, 3, 4, 5])

    print(a, b)

# time complexity: O(N)
