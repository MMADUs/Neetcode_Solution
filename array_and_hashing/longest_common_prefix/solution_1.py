# solution 1 (python)
# problem ref: https://neetcode.io/problems/longest-common-prefix/question?list=neetcode250

# Example:
#
# Input: strs = ["bat","bag","bank","band"]
# Output: "ba"
#
# Input: strs = ["dance","dag","danger","damage"]
# Output: "da"
#
# Input: strs = ["neet","feet"]
# Output: ""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min = float("inf")

        for s in strs:
            if min > len(s):
                min = len(s)

        prefix = ""

        for i in range(min):
            char = None

            for s in strs:
                s = list(s)

                if char is None:
                    char = s[i]
                else:
                    if char != s[i]:
                        return prefix

            prefix += char

        return prefix


if __name__ == "__main__":
    s = Solution()

    a = s.longestCommonPrefix(strs=["bat", "bag", "bank", "band"])
    b = s.longestCommonPrefix(strs=["dance", "dag", "danger", "damage"])
    c = s.longestCommonPrefix(strs=["neet", "feet"])

    print(a, b, c)

# time complexity: O(C . N) where C is min of string length, N is num of string
