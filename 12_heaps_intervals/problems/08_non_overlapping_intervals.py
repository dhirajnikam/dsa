"""
Problem: Non-overlapping Intervals
Difficulty: Medium | Pattern: sort by end, greedy keep
Source: LeetCode 435

Given an array of intervals [start, end), return the minimum number of intervals you
need to remove so the rest do not overlap. Intervals that only touch ([1, 2] and [2, 3])
do not overlap.

Example 1:
  intervals = [[1, 2], [2, 3], [3, 4], [1, 3]] -> 1   (remove [1, 3])
Example 2:
  intervals = [[1, 2], [1, 2], [1, 2]] -> 2
Example 3:
  intervals = [[1, 2], [2, 3]] -> 0

Constraints:
  1 <= len(intervals) <= 10^5
  -5 * 10^4 <= start < end <= 5 * 10^4

Hints:
1. Maximizing kept intervals = classic activity selection. Sort by END.
2. Keep an interval if its start >= the end of the last kept one. Everything else is removed.
3. Why end and not start? The interval that finishes earliest leaves the most room.

Expected: O(n log n) time, O(1) extra space
"""


def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1, 'Check: erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1'
    assert erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]) == 2, 'Check: erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]) == 2'
    assert erase_overlap_intervals([[1, 2], [2, 3]]) == 0, 'Check: erase_overlap_intervals([[1, 2], [2, 3]]) == 0'
    assert erase_overlap_intervals([[1, 100]]) == 0, 'Check: erase_overlap_intervals([[1, 100]]) == 0'
    assert erase_overlap_intervals([[1, 100], [11, 22], [1, 11], [2, 12]]) == 2, 'Check: erase_overlap_intervals([[1, 100], [11, 22], [1, 11], [2, 12]]) == 2'
    assert erase_overlap_intervals([[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]) == 2, 'Check: erase_overlap_intervals([[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]) == 2'
    assert erase_overlap_intervals([[-5, -1], [-3, 0], [0, 2]]) == 1, 'Check: erase_overlap_intervals([[-5, -1], [-3, 0], [0, 2]]) == 1'
    print("ok")
