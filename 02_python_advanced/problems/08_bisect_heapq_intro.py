"""
Problem: bisect and heapq warm-up
Difficulty: Easy | Topic: bisect_left/right, insort, heapify, heappush/pop, nsmallest, merge
Source: LeetCode 215, 23 (list version), 1287-ish

1. insert_sorted(a, x) -> insert x into the already-sorted list a in place (bisect.insort) and
   return a.
2. count_in_range(a, lo, hi) -> number of items in sorted list a with lo <= x <= hi, in O(log n).
3. k_smallest(nums, k) -> the k smallest items in ascending order (heapq.nsmallest or heapify+pop).
4. kth_largest(nums, k) -> k-th largest element. Keep a min-heap of size k: O(n log k).
   Do not sort the whole list.
5. merge_sorted(*lists) -> one sorted list from any number of sorted lists via heapq.merge.
6. running_top3(nums) -> list where the i-th element is the 3 largest values seen so far (sorted
   descending), for i >= 2. Use a min-heap of size 3. [5,1,9,3,7] -> [[9,5,1],[9,5,3],[9,7,5]].

Hints:
2. bisect_right(a, hi) - bisect_left(a, lo)
4. for x in nums: heappush(h, x); if len(h) > k: heappop(h). Answer is h[0].
6. Same pattern as 4 with k = 3; record sorted(h, reverse=True) once len(h) == 3.
"""
import bisect
import heapq


def insert_sorted(a: list[int], x: int) -> list[int]:
    raise NotImplementedError


def count_in_range(a: list[int], lo: int, hi: int) -> int:
    raise NotImplementedError


def k_smallest(nums: list[int], k: int) -> list[int]:
    raise NotImplementedError


def kth_largest(nums: list[int], k: int) -> int:
    raise NotImplementedError


def merge_sorted(*lists: list[int]) -> list[int]:
    raise NotImplementedError


def running_top3(nums: list[int]) -> list[list[int]]:
    raise NotImplementedError


if __name__ == "__main__":
    a = [1, 3, 5]
    assert insert_sorted(a, 4) is a and a == [1, 3, 4, 5]
    assert insert_sorted([], 1) == [1] and insert_sorted([2, 2], 2) == [2, 2, 2]
    s = [1, 3, 3, 5, 8, 8, 9]
    assert count_in_range(s, 3, 8) == 5 and count_in_range(s, 4, 4) == 0
    assert count_in_range(s, -10, 100) == 7 and count_in_range([], 0, 1) == 0
    assert k_smallest([5, 1, 9, 3, 7], 3) == [1, 3, 5]
    assert k_smallest([2, 2, 1], 5) == [1, 2, 2] and k_smallest([1], 0) == []
    assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4 and kth_largest([1], 1) == 1
    assert merge_sorted([1, 4, 7], [2, 5], [3, 6, 8, 9]) == list(range(1, 10))
    assert merge_sorted() == [] and merge_sorted([], [1]) == [1]
    assert running_top3([5, 1, 9, 3, 7]) == [[9, 5, 1], [9, 5, 3], [9, 7, 5]]
    assert running_top3([1, 2]) == []
    assert running_top3([4, 4, 4, 4]) == [[4, 4, 4], [4, 4, 4]]
    print("ok")
