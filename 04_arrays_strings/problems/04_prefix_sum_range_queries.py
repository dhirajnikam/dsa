"""
Problem: Range Sum Query - Immutable
Difficulty: Easy | Pattern: prefix sums
Source: LeetCode 303

Design a class NumArray that is initialized with an integer array and answers many
queries of the form sum_range(left, right) = nums[left] + ... + nums[right], inclusive.
Queries must be O(1) each after O(n) preprocessing.

Example:
  na = NumArray([-2, 0, 3, -5, 2, -1])
  na.sum_range(0, 2) -> 1
  na.sum_range(2, 5) -> -1
  na.sum_range(0, 5) -> -3

Constraints:
  1 <= len(nums) <= 10^4
  -10^5 <= nums[i] <= 10^5
  0 <= left <= right < len(nums)
  up to 10^4 calls to sum_range

Hints:
1. Precompute prefix[i] = sum of nums[:i], so prefix has length n + 1 and prefix[0] = 0.
2. sum(nums[l..r]) = prefix[r + 1] - prefix[l].
3. itertools.accumulate builds prefix sums in one line.

Expected: O(n) build, O(1) per query, O(n) space
"""


class NumArray:
    def __init__(self, nums: list[int]):
        raise NotImplementedError

    def sum_range(self, left: int, right: int) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    na = NumArray([-2, 0, 3, -5, 2, -1])
    assert na.sum_range(0, 2) == 1, 'Check: na.sum_range(0, 2) == 1'
    assert na.sum_range(2, 5) == -1, 'Check: na.sum_range(2, 5) == -1'
    assert na.sum_range(0, 5) == -3, 'Check: na.sum_range(0, 5) == -3'
    assert na.sum_range(3, 3) == -5, 'Check: na.sum_range(3, 3) == -5'
    single = NumArray([7])
    assert single.sum_range(0, 0) == 7, 'Check: single.sum_range(0, 0) == 7'
    same = NumArray([2, 2, 2, 2])
    assert same.sum_range(1, 2) == 4, 'Check: same.sum_range(1, 2) == 4'
    assert same.sum_range(0, 3) == 8, 'Check: same.sum_range(0, 3) == 8'
    neg = NumArray([-1, -1, -1])
    assert neg.sum_range(0, 2) == -3, 'Check: neg.sum_range(0, 2) == -3'
    # Boundary and misconception checks: predict each result before running.
    mixed = NumArray([0, -4, 4, 0])
    assert mixed.sum_range(0, 0) == 0, 'Check: mixed.sum_range(0, 0) == 0'
    assert mixed.sum_range(1, 2) == 0, 'Check: mixed.sum_range(1, 2) == 0'
    assert mixed.sum_range(3, 3) == 0, 'Check: mixed.sum_range(3, 3) == 0'
    print("ok")
