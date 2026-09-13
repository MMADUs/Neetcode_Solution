# solution 2 (python)
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


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def push(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children.keys():
                node.children[ch] = TrieNode()

            node = node.children[ch]

        node.is_end = True

    def lcs(self) -> str:
        node = self.root

        prefix = ""

        while not node.is_end:
            if len(node.children) == 1:
                ch = next(iter(node.children.keys()))
                prefix += ch
                node = node.children[ch]
            else:
                break

        return prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()

        for s in strs:
            trie.push(s)

        return trie.lcs()


if __name__ == "__main__":
    s = Solution()

    a = s.longestCommonPrefix(strs=["bat", "bag", "bank", "band"])
    b = s.longestCommonPrefix(strs=["dance", "dag", "danger", "damage"])
    c = s.longestCommonPrefix(strs=["neet", "feet"])

    print(a, b, c)

# time complexity: O(L + M), where M (lcs len) <= L (num or char on all string), 
