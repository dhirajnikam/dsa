"""
Problem: Binary Search
Difficulty: Easy | Pattern: Binary search (closed interval)
Source: LeetCode 704

Given a sorted (ascending) array of distinct integers nums and an integer target, return the
index of target if it exists, otherwise -1. Must run in O(log n).

Example 1:
  Input: nums = [-1,0,3,5,9,12], target = 9
  Output: 4

Example 2:
  Input: nums = [-1,0,3,5,9,12], target = 2
  Output: -1

Constraints:
  1 <= len(nums) <= 10^4
  -10^4 < nums[i], target < 10^4
  All integers in nums are unique and sorted ascending.

Hints:
1. lo, hi = 0, len(nums) - 1; loop while lo <= hi.
2. If nums[mid] < target the answer is to the right: lo = mid + 1. Else hi = mid - 1.
3. Both pointers must always skip mid, otherwise the loop can spin forever.

Expected: O(log n) time, O(1) space.
"""


def search(nums: list[int], target: int) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert search([5], 5) == 0
    assert search([5], -5) == -1
    assert search([], 1) == -1
    assert search([1, 3], 1) == 0 and search([1, 3], 3) == 1
    assert search([-1, 0, 3, 5, 9, 12], -1) == 0
    assert search([-1, 0, 3, 5, 9, 12], 12) == 5
    assert search(list(range(0, 20000, 2)), 9998) == 4999
    print("ok")
