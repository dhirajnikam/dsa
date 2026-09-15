"""
Problem: Coin Change
Difficulty: Medium | Pattern: unbounded knapsack, minimize
Source: LeetCode 322

Given coin denominations and an amount, return the fewest coins needed to make that
amount, or -1 if it cannot be made. You have unlimited coins of each denomination.

Example 1:
  coins = [1, 2, 5], amount = 11 -> 3   (5 + 5 + 1)
Example 2:
  coins = [2], amount = 3 -> -1
Example 3:
  coins = [1], amount = 0 -> 0

Constraints:
  1 <= len(coins) <= 12
  1 <= coins[i] <= 2^31 - 1
  0 <= amount <= 10^4

Hints:
1. State: dp[a] = fewest coins to make amount a. dp[0] = 0, others start at infinity.
2. Recurrence: dp[a] = min(dp[a - c] + 1 for c in coins if c <= a).
3. Greedy (largest coin first) fails: coins [1, 3, 4], amount 6.

Expected: O(amount * len(coins)) time, O(amount) space
"""


def coin_change(coins: list[int], amount: int) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
    assert coin_change([1, 3, 4], 6) == 2
    assert coin_change([2, 5, 10, 1], 27) == 4
    assert coin_change([186, 419, 83, 408], 6249) == 20
    assert coin_change([5], 5) == 1
    assert coin_change([3, 7], 1) == -1
    print("ok")
