"""
Problem: Longest Increasing Subsequence
Difficulty: Medium | Pattern: LIS (dp ending at i; patience sorting)
Source: LeetCode 300

Return the length of the longest strictly increasing subsequence of nums.

Example 1:
  nums = [10, 9, 2, 5, 3, 7, 101, 18] -> 4   (2, 3, 7, 101)
Example 2:
  nums = [0, 1, 0, 3, 2, 3] -> 4
Example 3:
  nums = [7, 7, 7, 7] -> 1

Constraints:
  1 <= len(nums) <= 2500
  -10^4 <= nums[i] <= 10^4

Hints:
1. State: dp[i] = length of the longest increasing subsequence that ENDS at index i.
2. Recurrence: dp[i] = 1 + max(dp[j] for j < i if nums[j] < nums[i]), default 1. Answer = max(dp).
3. Follow-up O(n log n): tails[k] = smallest tail of any increasing subsequence of length k+1.
   For each x, i = bisect_left(tails, x); if i == len(tails) append, else tails[i] = x.

Expected: O(n^2) time, O(n) space  (O(n log n) with bisect)
"""
from bisect import bisect_left


def length_of_lis(nums: list[int]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4
    assert length_of_lis([7, 7, 7, 7]) == 1
    assert length_of_lis([1]) == 1
    assert length_of_lis([5, 4, 3, 2, 1]) == 1
    assert length_of_lis([1, 2, 3, 4, 5]) == 5
    assert length_of_lis([4, 10, 4, 3, 8, 9]) == 3
    assert length_of_lis([-1, 3, 4, 5, 2, 2, 2, 2]) == 4
    assert length_of_lis(list(range(2000)) + list(range(2000))) == 2000
    print("ok")
