import heapq
from collections import Counter


def top_k_frequent(nums, k):
    # O(n log k) time, O(n) space
    # Count, then keep a min-heap of the k highest (count, value) pairs.
    h = []
    for val, cnt in Counter(nums).items():
        heapq.heappush(h, (cnt, val))
        if len(h) > k:
            heapq.heappop(h)
    return [val for _, val in h]
