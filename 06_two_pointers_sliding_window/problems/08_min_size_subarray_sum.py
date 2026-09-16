"""
Problem: Minimum Size Subarray Sum
Difficulty: Medium | Pattern: variable window, shrink while valid
Source: LeetCode 209

Given an array of POSITIVE integers nums and a positive integer target, return the minimal
length of a contiguous subarray whose sum is >= target. Return 0 if none exists.

Example 1:
  target = 7, nums = [2, 3, 1, 2, 4, 3] -> 2   ([4, 3])
Example 2:
  target = 4, nums = [1, 4, 4] -> 1
Example 3:
  target = 11, nums = [1, 1, 1, 1, 1, 1, 1, 1] -> 0

Constraints:
  1 <= target <= 10^9
  1 <= len(nums) <= 10^5
  1 <= nums[i] <= 10^4

Hints:
1. All positives means adding an element never decreases the sum, so a window works.
2. Expand r, adding to the running sum. While sum >= target: record r - l + 1, then remove nums[l], l += 1.
3. The "shrink while VALID" shape is the mirror of Problem 07's "shrink while INVALID". Both are the same template.

Expected: O(n) time, O(1) space
"""


def min_subarray_len(target: int, nums: list[int]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert min_subarray_len(7, [2, 3, 1, 2, 4, 3]) == 2, 'Check: min_subarray_len(7, [2, 3, 1, 2, 4, 3]) == 2'
    assert min_subarray_len(4, [1, 4, 4]) == 1, 'Check: min_subarray_len(4, [1, 4, 4]) == 1'
    assert min_subarray_len(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0, 'Check: min_subarray_len(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0'
    assert min_subarray_len(5, [5]) == 1, 'Check: min_subarray_len(5, [5]) == 1'
    assert min_subarray_len(6, [5]) == 0, 'Check: min_subarray_len(6, [5]) == 0'
    assert min_subarray_len(15, [1, 2, 3, 4, 5]) == 5, 'Check: min_subarray_len(15, [1, 2, 3, 4, 5]) == 5'
    assert min_subarray_len(3, [1, 1, 1, 1]) == 3, 'Check: min_subarray_len(3, [1, 1, 1, 1]) == 3'
    assert min_subarray_len(8, [2, 2, 2, 2, 2, 2]) == 4, 'Check: min_subarray_len(8, [2, 2, 2, 2, 2, 2]) == 4'
    assert min_subarray_len(1, [10, 10]) == 1, 'Check: min_subarray_len(1, [10, 10]) == 1'
    print("ok")
