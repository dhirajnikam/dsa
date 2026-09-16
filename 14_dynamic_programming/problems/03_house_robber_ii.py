"""
Problem: House Robber II
Difficulty: Medium | Pattern: 1D DP on a circle, reduce to linear
Source: LeetCode 213

Same as House Robber, but the houses form a circle: the first and last are adjacent.
Return the maximum amount you can rob.

Example 1:
  nums = [2, 3, 2] -> 3
Example 2:
  nums = [1, 2, 3, 1] -> 4
Example 3:
  nums = [1, 2, 3] -> 3

Constraints:
  1 <= len(nums) <= 100
  0 <= nums[i] <= 1000

Hints:
1. Either house 0 is not robbed or house n-1 is not robbed (possibly both).
2. Answer = max(linear_rob(nums[1:]), linear_rob(nums[:-1])). Handle n == 1 separately.

Expected: O(n) time, O(1) space
"""


def rob(nums: list[int]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert rob([2, 3, 2]) == 3, 'Check: rob([2, 3, 2]) == 3'
    assert rob([1, 2, 3, 1]) == 4, 'Check: rob([1, 2, 3, 1]) == 4'
    assert rob([1, 2, 3]) == 3, 'Check: rob([1, 2, 3]) == 3'
    assert rob([1]) == 1, 'Check: rob([1]) == 1'
    assert rob([1, 2]) == 2, 'Check: rob([1, 2]) == 2'
    assert rob([0]) == 0, 'Check: rob([0]) == 0'
    assert rob([200, 3, 140, 20, 10]) == 340, 'Check: rob([200, 3, 140, 20, 10]) == 340'
    assert rob([1, 3, 1, 3, 100]) == 103, 'Check: rob([1, 3, 1, 3, 100]) == 103'
    print("ok")
