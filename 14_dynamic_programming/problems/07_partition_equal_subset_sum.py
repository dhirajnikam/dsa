"""
Problem: Partition Equal Subset Sum
Difficulty: Medium | Pattern: boolean 0/1 knapsack
Source: LeetCode 416

Return True if nums can be split into two subsets with equal sums.

Example 1:
  nums = [1, 5, 11, 5] -> True   ([1, 5, 5] and [11])
Example 2:
  nums = [1, 2, 3, 5] -> False

Constraints:
  1 <= len(nums) <= 200
  1 <= nums[i] <= 100

Hints:
1. If the total is odd, False. Otherwise target = total // 2: can some subset sum to target?
2. State: dp[s] = can we make sum s with the items seen so far. dp[0] = True.
   Recurrence: for each x, for s from target down to x: dp[s] = dp[s] or dp[s - x].
   Iterate s downward so x is used at most once.
3. A set of reachable sums, or a Python int as a bitset (bits |= bits << x), also works.

Expected: O(n * target) time, O(target) space
"""


def can_partition(nums: list[int]) -> bool:
    raise NotImplementedError


if __name__ == "__main__":
    assert can_partition([1, 5, 11, 5]) is True
    assert can_partition([1, 2, 3, 5]) is False
    assert can_partition([1]) is False
    assert can_partition([2, 2]) is True
    assert can_partition([1, 1, 1, 1]) is True
    assert can_partition([3, 3, 3, 4, 5]) is True
    assert can_partition([1, 2, 5]) is False
    assert can_partition([100] * 200) is True
    assert can_partition([100] * 199) is False
    print("ok")
