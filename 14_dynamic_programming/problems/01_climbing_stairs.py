"""
Problem: Climbing Stairs
Difficulty: Easy | Pattern: 1D linear DP
Source: LeetCode 70

You are climbing a staircase with n steps. Each move you climb 1 or 2 steps. In how many
distinct ways can you reach the top?

Example 1:
  n = 2 -> 2   (1+1, 2)
Example 2:
  n = 3 -> 3   (1+1+1, 1+2, 2+1)

Constraints:
  1 <= n <= 45

Hints:
1. State: dp[i] = number of ways to reach step i.
2. Recurrence: the last move was 1 or 2 steps, so dp[i] = dp[i-1] + dp[i-2]. dp[0] = dp[1] = 1.
3. Only two previous values are needed: O(1) space.

Expected: O(n) time, O(1) space
"""


def climb_stairs(n: int) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(4) == 5
    assert climb_stairs(5) == 8
    assert climb_stairs(10) == 89
    assert climb_stairs(45) == 1836311903
    print("ok")
