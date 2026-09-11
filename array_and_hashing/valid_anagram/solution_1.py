# solution 1 (python)
# problem ref: https://neetcode.io/problems/is-anagram/question?list=neetcode250

# Example:
#
# Input: s = "racecar", t = "carrace"
# Output: true
#
# Input: s = "jar", t = "jam"
# Output: false
#
# Input: s = "x", t = "x"
# Output: true


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s, t = list(s), list(t)
        s.sort()
        t.sort()
        return True if s == t else False


if __name__ == "__main__":
    print(list("hello"))

    s = Solution()

    a = s.isAnagram(s="racecar", t="carrace")
    b = s.isAnagram(s="jar", t="jam")
    c = s.isAnagram(s="x", t="x")

    print(a, b, c)

# time complexity: O(N . log(N)) if sort is merge sort