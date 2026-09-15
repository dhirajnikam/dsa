"""
Problem: Burst Balloons
Difficulty: Hard | Pattern: interval DP, choose the last
Source: LeetCode 312

You have n balloons with numbers nums[i]. Bursting balloon i earns nums[i-1] * nums[i] *
nums[i+1] coins (out-of-range neighbors count as 1). After bursting, the neighbors become
adjacent. Return the maximum coins you can collect by bursting all balloons.

Example 1:
  nums = [3, 1, 5, 8] -> 167
  (burst 1: 3*1*5=15, then 5: 3*5*8=120, then 3: 1*3*8=24, then 8: 1*8*1=8)
Example 2:
  nums = [1, 5] -> 10

Constraints:
  1 <= len(nums) <= 300
  0 <= nums[i] <= 100

Hints:
1. Choosing the FIRST balloon to burst breaks the array in a way that couples the two sides.
   Choose the LAST balloon k in range (i, j) instead: when k bursts, its neighbors are
   exactly the fixed boundaries i and j.
2. Pad with 1s. State: dp[i][j] = max coins from bursting everything strictly between i and j.
   Recurrence: dp[i][j] = max over i < k < j of dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j].
3. Fill by increasing gap j - i. Answer is dp[0][n+1].

Expected: O(n^3) time, O(n^2) space
"""


def max_coins(nums: list[int]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert max_coins([3, 1, 5, 8]) == 167
    assert max_coins([1, 5]) == 10
    assert max_coins([7]) == 7
    assert max_coins([0]) == 0
    assert max_coins([1, 1, 1]) == 3
    assert max_coins([9, 76, 64, 21]) == 116718
    assert max_coins([3, 1, 5, 8, 2, 4]) == 315
    assert max_coins([1, 2, 3, 4, 5]) == 110
    print("ok")
