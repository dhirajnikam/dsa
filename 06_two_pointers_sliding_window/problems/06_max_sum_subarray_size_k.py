"""
Problem: Maximum Sum Subarray of Size K
Difficulty: Easy | Pattern: fixed-size sliding window
Source: classic (LeetCode 643 Maximum Average Subarray I is the same window)

Given an integer array nums and an integer k, return the maximum sum of any contiguous
subarray of exactly length k. If len(nums) < k, return 0.

Example 1:
  nums = [2, 1, 5, 1, 3, 2], k = 3 -> 9   ([5, 1, 3])
Example 2:
  nums = [2, 3, 4, 1, 5], k = 2 -> 7      ([3, 4])
Example 3:
  nums = [1, 2], k = 3 -> 0

Constraints:
  0 <= len(nums) <= 10^5
  1 <= k <= 10^5
  -10^4 <= nums[i] <= 10^4

Hints:
1. Recomputing sum(nums[i:i+k]) for each i is O(n*k).
2. Slide: add the entering element nums[i], subtract the leaving element nums[i - k].
3. Start tracking the best only once the window has k elements (i >= k - 1). Negatives are fine.

Expected: O(n) time, O(1) space
"""


def max_sum_subarray_k(nums: list[int], k: int) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert max_sum_subarray_k([2, 1, 5, 1, 3, 2], 3) == 9, 'Check: max_sum_subarray_k([2, 1, 5, 1, 3, 2], 3) == 9'
    assert max_sum_subarray_k([2, 3, 4, 1, 5], 2) == 7, 'Check: max_sum_subarray_k([2, 3, 4, 1, 5], 2) == 7'
    assert max_sum_subarray_k([1, 2], 3) == 0, 'Check: max_sum_subarray_k([1, 2], 3) == 0'
    assert max_sum_subarray_k([], 1) == 0, 'Check: max_sum_subarray_k([], 1) == 0'
    assert max_sum_subarray_k([5], 1) == 5, 'Check: max_sum_subarray_k([5], 1) == 5'
    assert max_sum_subarray_k([-1, -2, -3], 2) == -3, 'Check: max_sum_subarray_k([-1, -2, -3], 2) == -3'
    assert max_sum_subarray_k([4, 4, 4, 4], 2) == 8, 'Check: max_sum_subarray_k([4, 4, 4, 4], 2) == 8'
    assert max_sum_subarray_k([1, 2, 3, 4, 5], 5) == 15, 'Check: max_sum_subarray_k([1, 2, 3, 4, 5], 5) == 15'
    assert max_sum_subarray_k([-5, 10, -5, 10], 3) == 15, 'Check: max_sum_subarray_k([-5, 10, -5, 10], 3) == 15'
    # Boundary and misconception checks: predict each result before running.
    assert max_sum_subarray_k([-9, -1, -8], 1) == -1, 'Check: max_sum_subarray_k([-9, -1, -8], 1) == -1'
    assert max_sum_subarray_k([0, 0, 0], 2) == 0, 'Check: max_sum_subarray_k([0, 0, 0], 2) == 0'
    print("ok")
