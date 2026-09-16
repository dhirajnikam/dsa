"""
Problem: Two Sum
Difficulty: Easy | Pattern: hash map of seen values (complement lookup)
Source: LeetCode 1

Given an array of integers nums and an integer target, return the indices of the two numbers
that add up to target. Exactly one solution exists; you may not use the same element twice.
Return the indices in increasing order.

Example 1:
  nums = [2, 7, 11, 15], target = 9 -> [0, 1]
Example 2:
  nums = [3, 2, 4], target = 6 -> [1, 2]
Example 3:
  nums = [3, 3], target = 6 -> [0, 1]

Constraints:
  2 <= len(nums) <= 10^4
  -10^9 <= nums[i], target <= 10^9

Hints:
1. Brute force: every pair, O(n^2). Say it, then improve it.
2. For each x, you need target - x. A dict from value -> index answers "have I seen it?" in O(1).
3. Check the complement BEFORE inserting x, so [3, 3] does not pair an element with itself.

Expected: O(n) time, O(n) space
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    raise NotImplementedError


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1], 'Check: two_sum([2, 7, 11, 15], 9) == [0, 1]'
    assert two_sum([3, 2, 4], 6) == [1, 2], 'Check: two_sum([3, 2, 4], 6) == [1, 2]'
    assert two_sum([3, 3], 6) == [0, 1], 'Check: two_sum([3, 3], 6) == [0, 1]'
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4], 'Check: two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]'
    assert two_sum([0, 4, 3, 0], 0) == [0, 3], 'Check: two_sum([0, 4, 3, 0], 0) == [0, 3]'
    assert two_sum([1, 5], 6) == [0, 1], 'Check: two_sum([1, 5], 6) == [0, 1]'
    assert two_sum([5, 75, 25], 100) == [1, 2], 'Check: two_sum([5, 75, 25], 100) == [1, 2]'
    # Boundary and misconception checks: predict each result before running.
    assert two_sum([4, 4], 8) == [0, 1], 'Check: two_sum([4, 4], 8) == [0, 1]'
    assert two_sum([8, 1, 4, 3], 7) == [2, 3], 'Check: two_sum([8, 1, 4, 3], 7) == [2, 3]'
    print("ok")
