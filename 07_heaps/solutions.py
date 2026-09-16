"""07 · Heaps — reference solutions.

Honor rule: 40 minutes on a problem first. Read one function, close the file, rewrite it cold,
add it to redo.txt. Run `python solutions.py` to prove these pass exercises.py's tests.
"""
import heapq
import random
from collections import Counter


class KthLargest:
    def __init__(self, k: int, nums: list[int]) -> None:
        self.k = k
        self.heap: list[int] = []
        for x in nums:
            self.add(x)
        # O(n log k) to build.

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)   # the smallest survivor can never be the kth largest
        return self.heap[0]
        # O(log k) per add, O(k) space.


def kth_largest(nums: list[int], k: int) -> int:
    heap: list[int] = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
    # O(n log k) time, O(k) space. heapq.nlargest(k, nums)[-1] is the one-liner.


def _kth_largest_quickselect(nums: list[int], k: int) -> int:
    """Average O(n), worst O(n^2) with a random pivot making the worst case negligible.
    Not used by the tests; here so you can read it and explain it."""
    target = len(nums) - k             # index of the answer in ascending order
    lo, hi = 0, len(nums) - 1
    while True:
        pivot = nums[random.randint(lo, hi)]
        i, j = lo, hi
        while i <= j:                  # partition: < pivot left, > pivot right
            while nums[i] < pivot:
                i += 1
            while nums[j] > pivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        if target <= j:
            hi = j
        elif target >= i:
            lo = i
        else:
            return nums[target]


def last_stone_weight(stones: list[int]) -> int:
    heap = [-s for s in stones]        # negate for a max-heap
    heapq.heapify(heap)                # O(n)
    while len(heap) > 1:
        a, b = -heapq.heappop(heap), -heapq.heappop(heap)
        if a != b:
            heapq.heappush(heap, -(a - b))
    return -heap[0] if heap else 0
    # O(n log n): each smash removes at least one stone.


def k_closest_points(points: list[list[int]], k: int) -> list[list[int]]:
    heap: list[tuple[int, int, int]] = []     # (-dist^2, x, y): max-heap on distance
    for x, y in points:
        heapq.heappush(heap, (-(x * x + y * y), x, y))
        if len(heap) > k:
            heapq.heappop(heap)        # evict the farthest
    return [[x, y] for _, x, y in heap]
    # O(n log k). Squared distance avoids sqrt and stays in integers.


def top_k_frequent_heap(nums: list[int], k: int) -> list[int]:
    counts = Counter(nums)
    heap: list[tuple[int, int]] = []          # (count, value), min-heap of size k
    for val, c in counts.items():
        heapq.heappush(heap, (c, val))
        if len(heap) > k:
            heapq.heappop(heap)
    return [val for _, val in heap]
    # O(n log k). Equivalent: heapq.nlargest(k, counts, key=counts.get).


def task_scheduler(tasks: list[str], n: int) -> int:
    heap = [-c for c in Counter(tasks).values()]   # max-heap of remaining counts
    heapq.heapify(heap)
    time = 0
    while heap:
        round_tasks: list[int] = []
        for _ in range(n + 1):         # one "cycle": n + 1 slots, all distinct tasks
            if heap:
                round_tasks.append(heapq.heappop(heap) + 1)   # run one unit (count is negative)
        for c in round_tasks:
            if c < 0:
                heapq.heappush(heap, c)                       # still has work left
        time += n + 1 if heap else len(round_tasks)           # last round: no idle padding
    return time
    # O(T log 26) = O(T). Closed form: max(len(tasks), (max_count - 1) * (n + 1) + num_max).


class MedianFinder:
    def __init__(self) -> None:
        self.low: list[int] = []       # max-heap (negated): the smaller half
        self.high: list[int] = []      # min-heap: the larger half

    def add_num(self, num: int) -> None:
        heapq.heappush(self.low, -num)                            # 1. into low
        heapq.heappush(self.high, -heapq.heappop(self.low))       # 2. low's max moves up
        if len(self.high) > len(self.low):                        # 3. low is never smaller
            heapq.heappush(self.low, -heapq.heappop(self.high))
        # O(log n).

    def find_median(self) -> float:
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2
        # O(1).


def merge_k_sorted(lists: list[list[int]]) -> list[int]:
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]   # one head per list
    heapq.heapify(heap)
    out: list[int] = []
    while heap:
        val, li, ei = heapq.heappop(heap)
        out.append(val)
        if ei + 1 < len(lists[li]):
            heapq.heappush(heap, (lists[li][ei + 1], li, ei + 1))
    return out
    # O(N log k). The indices are tie-breakers AND tell us where the next element lives.


def reorganize_string(s: str) -> str:
    counts = Counter(s)
    if max(counts.values()) > (len(s) + 1) // 2:
        return ""                      # the most common char cannot be spaced out
    heap = [(-c, ch) for ch, c in counts.items()]
    heapq.heapify(heap)
    out: list[str] = []
    prev: tuple[int, str] | None = None        # held back: the char we just placed
    while heap:
        c, ch = heapq.heappop(heap)
        out.append(ch)
        if prev is not None:
            heapq.heappush(heap, prev)         # previous char is allowed again
        prev = (c + 1, ch) if c + 1 < 0 else None
    return "".join(out)
    # O(n log 26) = O(n). Always place the most frequent remaining char that is not prev.


def meeting_rooms_ii(intervals: list[list[int]]) -> int:
    ends: list[int] = []               # min-heap of end times of meetings in progress
    for start, end in sorted(intervals):
        if ends and ends[0] <= start:
            heapq.heapreplace(ends, end)       # reuse the room that frees up earliest
        else:
            heapq.heappush(ends, end)          # need a new room
    return len(ends)
    # O(n log n). Heap size never shrinks below the peak concurrency, so len(ends) is the answer.


def kth_smallest_in_sorted_matrix(matrix: list[list[int]], k: int) -> int:
    n = len(matrix)
    heap = [(matrix[r][0], r, 0) for r in range(min(n, k))]   # one head per row
    heapq.heapify(heap)
    val = matrix[0][0]
    for _ in range(k):
        val, r, c = heapq.heappop(heap)
        if c + 1 < n:
            heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))
    return val
    # O(k log n). Same as merge_k_sorted stopped after k pops. Binary search on the value is also O(n log range).


def smallest_range_covering_k_lists(lists: list[list[int]]) -> list[int]:
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists)]   # one pointer per list
    heapq.heapify(heap)
    cur_max = max(lst[0] for lst in lists)
    best = [heap[0][0], cur_max]
    while True:
        lo, li, ei = heapq.heappop(heap)                    # the range is [lo, cur_max]
        if cur_max - lo < best[1] - best[0]:
            best = [lo, cur_max]
        if ei + 1 == len(lists[li]):
            return best                # this list is exhausted: no smaller lo can cover it
        nxt = lists[li][ei + 1]
        cur_max = max(cur_max, nxt)
        heapq.heappush(heap, (nxt, li, ei + 1))
    # O(N log k). Advancing the minimum is the only move that can shrink the range.


if __name__ == "__main__":
    import exercises
    for _k, _v in list(globals().items()):
        if not _k.startswith("_") and _k != "exercises":
            setattr(exercises, _k, _v)
    exercises._check()
