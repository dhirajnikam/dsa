"""
Problem: Maximum Subarray
Difficulty: Medium | Pattern: Kadane's algorithm (running best-ending-here)
Source: LeetCode 53

Given an integer array nums, find the contiguous subarray (at least one element)
with the largest sum and return that sum.

Example 1:
  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> 6   ([4, -1, 2, 1])
Example 2:
  nums = [1] -> 1
Example 3:
  nums = [5, 4, -1, 7, 8] -> 23

Constraints:
  1 <= len(nums) <= 10^5
  -10^4 <= nums[i] <= 10^4

Hints:
1. Let cur = best sum of a subarray ENDING at index i.
2. cur = max(nums[i], cur + nums[i]): either extend the previous run or start fresh.
3. Answer is the max of cur over all i. Handle all-negative arrays (answer is the largest element).

Expected: O(n) time, O(1) space
"""


def max_subarray(nums: list[int]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6, 'Check: max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6'
    assert max_subarray([1]) == 1, 'Check: max_subarray([1]) == 1'
    assert max_subarray([5, 4, -1, 7, 8]) == 23, 'Check: max_subarray([5, 4, -1, 7, 8]) == 23'
    assert max_subarray([-3, -1, -2]) == -1, 'Check: max_subarray([-3, -1, -2]) == -1'
    assert max_subarray([-5]) == -5, 'Check: max_subarray([-5]) == -5'
    assert max_subarray([0, 0, 0]) == 0, 'Check: max_subarray([0, 0, 0]) == 0'
    assert max_subarray([2, -1, 2, -1, 2]) == 4, 'Check: max_subarray([2, -1, 2, -1, 2]) == 4'
    assert max_subarray([-1, 10, -1]) == 10, 'Check: max_subarray([-1, 10, -1]) == 10'
    print("ok")
