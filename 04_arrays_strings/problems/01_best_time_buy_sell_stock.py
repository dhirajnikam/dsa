"""
Problem: Best Time to Buy and Sell Stock
Difficulty: Easy | Pattern: single pass, track running minimum
Source: LeetCode 121

You are given an array prices where prices[i] is the price of a stock on day i.
Choose one day to buy and a later day to sell. Return the maximum profit.
If no profit is possible, return 0.

Example 1:
  prices = [7, 1, 5, 3, 6, 4] -> 5   (buy at 1, sell at 6)
Example 2:
  prices = [7, 6, 4, 3, 1] -> 0      (prices only fall)

Constraints:
  1 <= len(prices) <= 10^5
  0 <= prices[i] <= 10^4

Hints:
1. Brute force checks every (buy, sell) pair: O(n^2). Too slow.
2. Walking left to right, the best sell today uses the cheapest buy seen so far.
3. Keep min_so_far and best; update both in one pass.

Expected: O(n) time, O(1) space
"""


def max_profit(prices: list[int]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([5]) == 0
    assert max_profit([3, 3, 3]) == 0
    assert max_profit([1, 2]) == 1
    assert max_profit([2, 1, 4]) == 3
    assert max_profit([2, 4, 1]) == 2
    assert max_profit([1, 10000, 0, 5000]) == 9999
    print("ok")
