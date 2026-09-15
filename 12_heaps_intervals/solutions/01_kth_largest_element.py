import heapq


def find_kth_largest(nums, k):
    # O(n log k) time, O(k) space
    # Min-heap of the k largest values seen; its root is the k-th largest.
    h = []
    for x in nums:
        heapq.heappush(h, x)
        if len(h) > k:
            heapq.heappop(h)
    return h[0]
