"""
Problem: Daily Temperatures
Difficulty: Medium | Pattern: monotonic decreasing stack of indices
Source: LeetCode 739

Given an array temperatures, return an array answer such that answer[i] is the number of days
you have to wait after day i to get a warmer temperature. If no future day is warmer, answer[i] = 0.

Example 1:
  temperatures = [73, 74, 75, 71, 69, 72, 76, 73] -> [1, 1, 4, 2, 1, 1, 0, 0]
Example 2:
  temperatures = [30, 40, 50, 60] -> [1, 1, 1, 0]
Example 3:
  temperatures = [30, 60, 90] -> [1, 1, 0]

Constraints:
  1 <= len(temperatures) <= 10^5
  30 <= temperatures[i] <= 100

Hints:
1. Brute force O(n^2): for each day scan forward. Too slow.
2. Keep a stack of indices whose answer is still unknown; their temperatures are decreasing top to bottom.
3. When a new day is warmer than the top's temperature, pop it: its answer is i - popped_index.
   Repeat while warmer. Then push i.

Expected: O(n) time, O(n) space
"""


def daily_temperatures(temperatures: list[int]) -> list[int]:
    raise NotImplementedError


if __name__ == "__main__":
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0], 'Check: daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]'
    assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0], 'Check: daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]'
    assert daily_temperatures([30, 60, 90]) == [1, 1, 0], 'Check: daily_temperatures([30, 60, 90]) == [1, 1, 0]'
    assert daily_temperatures([50]) == [0], 'Check: daily_temperatures([50]) == [0]'
    assert daily_temperatures([50, 50, 50]) == [0, 0, 0], 'Check: daily_temperatures([50, 50, 50]) == [0, 0, 0]'
    assert daily_temperatures([90, 80, 70]) == [0, 0, 0], 'Check: daily_temperatures([90, 80, 70]) == [0, 0, 0]'
    assert daily_temperatures([70, 80, 60, 90]) == [1, 2, 1, 0], 'Check: daily_temperatures([70, 80, 60, 90]) == [1, 2, 1, 0]'
    assert daily_temperatures([55, 38, 53, 81, 61, 93, 97, 32, 43, 78]) == [3, 1, 1, 2, 1, 1, 0, 1, 1, 0], 'Check: daily_temperatures([55, 38, 53, 81, 61, 93, 97, 32, 43, 78]) == [3, 1, 1, 2, 1, 1, 0, 1, 1, 0]'
    print("ok")
