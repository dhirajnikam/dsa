import bisect
import heapq


def insert_sorted(a, x):  # O(n) because of the shift, O(log n) to find the spot
    bisect.insort(a, x)
    return a


def count_in_range(a, lo, hi):  # O(log n)
    return bisect.bisect_right(a, hi) - bisect.bisect_left(a, lo)


def k_smallest(nums, k):  # O(n log k)
    return heapq.nsmallest(k, nums)


def kth_largest(nums, k):  # O(n log k) time, O(k) space
    h = []
    for x in nums:
        heapq.heappush(h, x)
        if len(h) > k:
            heapq.heappop(h)
    return h[0]


def merge_sorted(*lists):  # O(N log k)
    return list(heapq.merge(*lists))


def running_top3(nums):  # O(n log 3) = O(n)
    h, out = [], []
    for x in nums:
        heapq.heappush(h, x)
        if len(h) > 3:
            heapq.heappop(h)
        if len(h) == 3:
            out.append(sorted(h, reverse=True))
    return out
