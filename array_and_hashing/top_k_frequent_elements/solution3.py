# solution 3 (python)
# problem ref: https://neetcode.io/problems/top-k-elements-in-list/question?list=neetcode250

# Example:
#
# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]
#
# Input: nums = [7,7], k = 1
# Output: [7]

from typing import List


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class PQLL:
    def __init__(self):
        self.head = None

    def push(self, key: int, value: int):
        new_node = Node(key, value)

        if self.head is None or new_node.value > self.head.value:
            new_node.next = self.head
            self.head = new_node
            return

        curr_head = self.head

        while curr_head.next is not None and new_node.value <= curr_head.next.value:
            curr_head = curr_head.next

        new_node.next = curr_head.next
        curr_head.next = new_node

    def top_k(self, k: int):
        top_k = []

        curr_head = self.head

        for _ in range(k):
            top_k.append(curr_head.key)
            curr_head = curr_head.next

        return top_k


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        queue = PQLL()

        for n, freq in freq.items():
            queue.push(n, freq)

        return queue.top_k(k)


# i think linked list is pretty inefficient, PQLL = priority queue linked list


if __name__ == "__main__":
    s = Solution()

    a = s.topKFrequent(nums=[1, 2, 2, 3, 3, 3], k=2)
    b = s.topKFrequent(nums=[7, 7], k=1)

    print(a, b)

# time complexity: O(N^2)
