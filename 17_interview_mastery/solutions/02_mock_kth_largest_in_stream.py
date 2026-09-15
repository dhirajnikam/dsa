# What a strong candidate says:
# "Is k fixed for the object's lifetime, and is add only queried once k numbers exist?
#  Do duplicates count separately? Then I only ever need the k largest values seen so far.
#  A min-heap of size k keeps exactly those and its root is the k-th largest. Each add is
#  O(log k); resorting every time would be O(n log n) per call. Space O(k), not O(n)."
import heapq


class KthLargest:
    # O(n log k) build, O(log k) per add, O(k) space
    # Min-heap holding the k largest values seen; the smallest of them (the root) is the answer.
    def __init__(self, k, nums):
        self.k = k
        self.heap = []
        for x in nums:
            self.add(x)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
