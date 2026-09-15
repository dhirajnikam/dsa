"""
Problem: Coin Change II
Difficulty: Medium | Pattern: unbounded knapsack, count combinations
Source: LeetCode 518

Given coin denominations and an amount, return the number of COMBINATIONS of coins that
make up that amount (order does not matter). Unlimited coins of each kind.

Example 1:
  amount = 5, coins = [1, 2, 5] -> 4   (5, 2+2+1, 2+1+1+1, 1+1+1+1+1)
Example 2:
  amount = 3, coins = [2] -> 0
Example 3:
  amount = 10, coins = [10] -> 1

Constraints:
  1 <= len(coins) <= 300
  0 <= amount <= 5000
  Answer fits in a 32-bit int.

Hints:
1. State: dp[a] = number of combinations making amount a using the coins processed so far.
2. Recurrence: for each coin c (OUTER loop), for a from c to amount: dp[a] += dp[a - c].
   Coins outside = each combination counted once regardless of order.
3. Swapping the loops counts permutations (wrong here). Know why.

Expected: O(amount * len(coins)) time, O(amount) space
"""


def change(amount: int, coins: list[int]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert change(5, [1, 2, 5]) == 4
    assert change(3, [2]) == 0
    assert change(10, [10]) == 1
    assert change(0, [1, 2]) == 1
    assert change(4, [1, 2]) == 3
    assert change(3, [1, 2, 3]) == 3
    assert change(500, [3, 5, 7, 8, 9, 10, 11]) == 35502874
    print("ok")
