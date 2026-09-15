import heapq


class MedianFinder:
    # O(log n) add, O(1) median, O(n) space
    # low = max-heap (negated) of the smaller half, high = min-heap of the larger half.
    # Invariant: len(low) == len(high) or len(low) == len(high) + 1.
    def __init__(self):
        self.low = []
        self.high = []

    def add_num(self, num):
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def find_median(self):
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2
