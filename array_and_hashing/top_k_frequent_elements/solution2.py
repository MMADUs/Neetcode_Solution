# solution 2 (python)
# problem ref: https://neetcode.io/problems/top-k-elements-in-list/question?list=neetcode250

# Example:
#
# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]
#
# Input: nums = [7,7], k = 1
# Output: [7]

from typing import List, Tuple


class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, value: Tuple[int, int]) -> None:
        self.heap.append(value)

        index = len(self.heap) - 1

        # heapify up
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[parent][1] >= self.heap[index][1]:
                break

            # swap
            temp = self.heap[index]
            self.heap[index] = self.heap[parent]
            self.heap[parent] = temp

            index = parent

    def top_k(self, k: int) -> int:
        top_k = []

        for _ in range(k):
            top_k.append(self.heap[0][0])

            self.heap[0] = self.heap[-1]
            self.heap.pop()

            index = 0

            while True:
                left = 2 * index + 1
                right = 2 * index + 2

                if left >= len(self.heap):
                    break

                if right < len(self.heap) and self.heap[right][1] > self.heap[left][1]:
                    largest = right
                else:
                    largest = left

                if self.heap[index][1] >= self.heap[largest][1]:
                    break

                self.heap[index], self.heap[largest] = (
                    self.heap[largest],
                    self.heap[index],
                )

                index = largest

        return top_k


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        max_heap = MaxHeap()

        for n, freq in freq.items():
            max_heap.push((n, freq))

        return max_heap.top_k(k)


if __name__ == "__main__":
    s = Solution()

    a = s.topKFrequent(nums=[1, 2, 2, 3, 3, 3], k=2)
    b = s.topKFrequent(nums=[7, 7], k=1)

    print(a, b)

# time complexity: O(N + U log U + K log U)
