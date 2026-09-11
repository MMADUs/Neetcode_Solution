# solution 1 (python)
# problem ref: https://neetcode.io/problems/anagram-groups/question?list=neetcode250

# Example:
#
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
#
# Input: strs = ["x"]
# Output: [["x"]]
#
# Input: strs = [""]
# Output: [[""]]

import string

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashes = []

        alphabet = list(string.ascii_lowercase)

        for s in strs:
            freq = {k: 0 for k in alphabet}  # alphabet freq

            for ch in s:
                freq[ch.lower()] = freq.get(ch.lower(), 0) + 1

            hashes.append(self.hash(freq))

        groups = {}

        for hash, str in zip(hashes, strs):
            if hash not in groups.keys():
                groups[hash] = []

            groups[hash].append(str)

        return [v for v in groups.values()]

    def hash(self, freq: dict[str, int]) -> str:
        return "|".join(str(v) for v in freq.values())


if __name__ == "__main__":
    s = Solution()

    freq = {
        "a": 1,
        "b": 3,
        "c": 2,
    }
    print(f"example hash: {s.hash(freq)}")

    a = s.groupAnagrams(strs=["act", "pots", "tops", "cat", "stop", "hat"])
    b = s.groupAnagrams(strs=["x"])
    c = s.groupAnagrams(strs=[""])

    print(a, b, c)


# time complexity: O(N + K), where N is num sample, and K is the max length of string
