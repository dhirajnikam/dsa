"""
Problem: Mock interview 5 - Min Cost Climbing Stairs
Difficulty: Medium (Easy on LeetCode; graded on how you derive and explain the DP) | Pattern: 1D DP
Source: LeetCode 746

Interviewer says:
  "There is a staircase, and stepping on each stair costs something. You can climb one or
   two stairs at a time. What is the cheapest way to get to the top?"

Ask about: where do I start (stair 0, stair 1, or before the staircase)? Does "the top"
mean the last stair or one past it? Are costs non-negative? How many stairs? Do I pay for
the stair I stand on when I start?

Hints (constraints you should have asked about):
1. cost has 2 to 1000 entries, each 0..999. You may start on index 0 or index 1 and pay its
   cost when you step on it. "The top" is index n (one past the last stair) and costs 0.
2. Define dp[i] = min cost to stand on stair i. dp[0] = cost[0], dp[1] = cost[1],
   dp[i] = cost[i] + min(dp[i-1], dp[i-2]). Answer = min(dp[n-1], dp[n-2]).
3. Only the last two values are needed: two variables, O(1) space. Say the O(n) array
   version first, then compress; that is the expected narrative.
4. Explain why greedy (always take the cheaper next step) fails: [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
   greedy commits to 1 then must land on 100 later.

Expected: O(n) time, O(1) space
"""


def min_cost_climbing_stairs(cost: list[int]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert min_cost_climbing_stairs([10, 15, 20]) == 15
    assert min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    assert min_cost_climbing_stairs([0, 0]) == 0
    assert min_cost_climbing_stairs([5, 7]) == 5
    assert min_cost_climbing_stairs([7, 5]) == 5
    assert min_cost_climbing_stairs([1, 2, 3]) == 2
    assert min_cost_climbing_stairs([9, 1, 9, 1, 9]) == 2
    assert min_cost_climbing_stairs([999] * 1000) == 999 * 500
    print("ok")
