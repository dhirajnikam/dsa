"""
Problem: Mock interview 2 - Kth Largest Element in a Stream
Difficulty: Medium (Easy on LeetCode; the design conversation is the medium part) | Pattern: Heap
Source: LeetCode 703

Interviewer says:
  "Numbers keep arriving one at a time. After each one, I want to know the k-th largest
   number seen so far. Design something for that."

Ask about: how many numbers total, the range of k, whether the initial batch can have
fewer than k numbers, duplicates, negative values, what k-th largest means with duplicates
(k-th in sorted order, not k-th distinct).

Hints (constraints you should have asked about):
1. k >= 1. Up to 10^4 calls to add. Values fit in 32-bit signed ints. The initial list may
   have fewer than k elements, but add is only queried when at least k have been seen.
   Duplicates count separately: k-th largest of [4, 4, 3] with k = 2 is 4.
2. Sorting on every add is O(n log n) per call. Keep only the k largest seen so far in a
   min-heap of size k; the root is the k-th largest.
3. add(v): heappush, then heappop if the heap exceeds k. Return heap[0].
4. Follow-up they may ask: k-th smallest (max-heap by negation), or sliding window
   (needs a balanced structure or lazy deletion).

Expected: O(log k) per add, O(n log k) to build, O(k) space
"""
import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]) -> None:
        raise NotImplementedError

    def add(self, val: int) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    s = KthLargest(3, [4, 5, 8, 2])
    assert s.add(3) == 4, 'Check: s.add(3) == 4'
    assert s.add(5) == 5, 'Check: s.add(5) == 5'
    assert s.add(10) == 5, 'Check: s.add(10) == 5'
    assert s.add(9) == 8, 'Check: s.add(9) == 8'
    assert s.add(4) == 8, 'Check: s.add(4) == 8'

    e = KthLargest(1, [])
    assert e.add(-3) == -3, 'Check: e.add(-3) == -3'
    assert e.add(-2) == -2, 'Check: e.add(-2) == -2'
    assert e.add(-4) == -2, 'Check: e.add(-4) == -2'

    d = KthLargest(2, [0])
    assert d.add(-1) == -1, 'Check: d.add(-1) == -1'
    assert d.add(1) == 0, 'Check: d.add(1) == 0'
    assert d.add(-2) == 0, 'Check: d.add(-2) == 0'
    assert d.add(-4) == 0, 'Check: d.add(-4) == 0'
    assert d.add(3) == 1, 'Check: d.add(3) == 1'

    dup = KthLargest(2, [4, 4, 3])
    assert dup.add(1) == 4, 'Check: dup.add(1) == 4'
    print("ok")
