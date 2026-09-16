"""
Problem: Merge Intervals
Difficulty: Medium | Pattern: sort by start, extend
Source: LeetCode 56

Given an array of intervals [start, end], merge all overlapping intervals and return
the non-overlapping intervals that cover all the input, sorted by start.
Touching intervals ([1, 4] and [4, 5]) count as overlapping.

Example 1:
  intervals = [[1, 3], [2, 6], [8, 10], [15, 18]] -> [[1, 6], [8, 10], [15, 18]]
Example 2:
  intervals = [[1, 4], [4, 5]] -> [[1, 5]]

Constraints:
  1 <= len(intervals) <= 10^4
  0 <= start <= end <= 10^4

Hints:
1. Sort by start. Then an interval can only overlap the last merged one.
2. If start <= merged[-1][1], set merged[-1][1] = max(merged[-1][1], end). Else append.

Expected: O(n log n) time, O(n) space
"""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    raise NotImplementedError


if __name__ == "__main__":
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]], 'Check: merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]'
    assert merge([[1, 4], [4, 5]]) == [[1, 5]], 'Check: merge([[1, 4], [4, 5]]) == [[1, 5]]'
    assert merge([[1, 4]]) == [[1, 4]], 'Check: merge([[1, 4]]) == [[1, 4]]'
    assert merge([[1, 4], [2, 3]]) == [[1, 4]], 'Check: merge([[1, 4], [2, 3]]) == [[1, 4]]'
    assert merge([[5, 6], [1, 2]]) == [[1, 2], [5, 6]], 'Check: merge([[5, 6], [1, 2]]) == [[1, 2], [5, 6]]'
    assert merge([[1, 4], [0, 4]]) == [[0, 4]], 'Check: merge([[1, 4], [0, 4]]) == [[0, 4]]'
    assert merge([[1, 4], [0, 0]]) == [[0, 0], [1, 4]], 'Check: merge([[1, 4], [0, 0]]) == [[0, 0], [1, 4]]'
    assert merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == [[1, 10]], 'Check: merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == [[1, 10]]'
    print("ok")
