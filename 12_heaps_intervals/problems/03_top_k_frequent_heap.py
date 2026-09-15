"""
Problem: Top K Frequent Elements
Difficulty: Medium | Pattern: counter + size-k heap
Source: LeetCode 347

Given an integer array nums and an integer k, return the k most frequent elements in
any order. The answer is guaranteed to be unique.

Example 1:
  nums = [1, 1, 1, 2, 2, 3], k = 2 -> [1, 2]
Example 2:
  nums = [1], k = 1 -> [1]

Constraints:
  1 <= len(nums) <= 10^5
  k is in [1, number of distinct elements]
  Must be better than O(n log n).

Hints:
1. Counter(nums) gives value -> count.
2. Min-heap of (count, value) with size k over the distinct values: O(m log k).
3. Follow-up: bucket sort by count is O(n). Mention it.

Expected: O(n log k) time, O(n) space
"""
import heapq
from collections import Counter


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    raise NotImplementedError


if __name__ == "__main__":
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
    assert sorted(top_k_frequent([4, 4, 4, 5, 5, 6, 7], 1)) == [4]
    assert sorted(top_k_frequent([1, 2, 3, 4], 4)) == [1, 2, 3, 4]
    assert sorted(top_k_frequent([-1, -1, 2, 2, 2], 2)) == [-1, 2]
    assert sorted(top_k_frequent([3, 0, 1, 0], 1)) == [0]
    print("ok")
