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
        if len(s) != len(t):
            return False 

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in t:
            if ch not in freq or freq[ch] == 0:
                return False 
            freq[ch] -= 1

        return True


if __name__ == "__main__":
    print(list("hello"))

    s = Solution()

    a = s.isAnagram(s="racecar", t="carrace")
    b = s.isAnagram(s="jar", t="jam")
    c = s.isAnagram(s="x", t="x")

    print(a, b, c)

# time complexity: o(n)