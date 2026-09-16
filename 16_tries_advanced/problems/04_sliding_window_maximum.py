"""
Problem: Sliding Window Maximum
Difficulty: Hard | Pattern: Monotonic deque
Source: LeetCode 239

Given an integer array nums and a window size k, return the maximum of each contiguous
window of size k as the window slides from left to right.

Example 1: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3 -> [3, 3, 5, 5, 6, 7]
Example 2: nums = [1], k = 1 -> [1]

Hints:
1. Keep a deque of indices whose values decrease from front to back; the front is the max.
2. Before pushing index i, pop from the back while nums[back] <= nums[i] (they are dominated).
3. Pop the front if it is out of the window (front <= i - k). Emit once i >= k - 1.
4. A heap solution is O(n log n) and acceptable as a first answer; the deque is the follow-up.

Expected: O(n) time, O(k) space
"""
from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    raise NotImplementedError


if __name__ == "__main__":
    assert max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7], 'Check: max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]'
    assert max_sliding_window([1], 1) == [1], 'Check: max_sliding_window([1], 1) == [1]'
    assert max_sliding_window([1, -1], 1) == [1, -1], 'Check: max_sliding_window([1, -1], 1) == [1, -1]'
    assert max_sliding_window([9, 8, 7, 6], 2) == [9, 8, 7], 'Check: max_sliding_window([9, 8, 7, 6], 2) == [9, 8, 7]'
    assert max_sliding_window([1, 2, 3, 4], 2) == [2, 3, 4], 'Check: max_sliding_window([1, 2, 3, 4], 2) == [2, 3, 4]'
    assert max_sliding_window([4, 4, 4], 2) == [4, 4], 'Check: max_sliding_window([4, 4, 4], 2) == [4, 4]'
    assert max_sliding_window([5, 3, 1, 2, 8], 5) == [8], 'Check: max_sliding_window([5, 3, 1, 2, 8], 5) == [8]'
    assert max_sliding_window([1, 3, 1, 2, 0, 5], 3) == [3, 3, 2, 5], 'Check: max_sliding_window([1, 3, 1, 2, 0, 5], 3) == [3, 3, 2, 5]'
    print("ok")
