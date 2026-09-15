import heapq


def k_closest(points, k):
    # O(n log k) time, O(k) space
    # Max-heap (negated squared distance) of size k: the root is the farthest kept point,
    # so once the heap has k items the pop removes whichever is farthest.
    h = []
    for x, y in points:
        heapq.heappush(h, (-(x * x + y * y), x, y))
        if len(h) > k:
            heapq.heappop(h)
    return [[x, y] for _, x, y in h]
