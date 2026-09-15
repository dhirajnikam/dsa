"""
Problem: House Robber
Difficulty: Medium | Pattern: 1D linear DP, take/skip
Source: LeetCode 198

nums[i] is the money in house i. You cannot rob two adjacent houses. Return the maximum
amount you can rob.

Example 1:
  nums = [1, 2, 3, 1] -> 4   (houses 0 and 2)
Example 2:
  nums = [2, 7, 9, 3, 1] -> 12   (houses 0, 2, 4)

Constraints:
  1 <= len(nums) <= 100
  0 <= nums[i] <= 400

Hints:
1. State: dp[i] = max loot from houses 0..i.
2. Recurrence: dp[i] = max(dp[i-1], dp[i-2] + nums[i])  (skip house i, or rob it and skip i-1).
3. Two rolling variables suffice.

Expected: O(n) time, O(1) space
"""


def rob(nums: list[int]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12
    assert rob([5]) == 5
    assert rob([2, 1]) == 2
    assert rob([1, 2]) == 2
    assert rob([0, 0, 0]) == 0
    assert rob([2, 1, 1, 2]) == 4
    assert rob([100, 1, 1, 100, 1, 1, 100]) == 300
    print("ok")
