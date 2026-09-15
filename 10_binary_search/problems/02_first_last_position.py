"""
Problem: Find First and Last Position of Element in Sorted Array
Difficulty: Medium | Pattern: Boundary binary search (bisect_left / bisect_right)
Source: LeetCode 34

Given an array of integers nums sorted in non-decreasing order, find the starting and ending
position of a given target value. If target is not found, return [-1, -1]. O(log n) required.

Example 1:
  Input: nums = [5,7,7,8,8,10], target = 8
  Output: [3,4]

Example 2:
  Input: nums = [5,7,7,8,8,10], target = 6
  Output: [-1,-1]

Example 3:
  Input: nums = [], target = 0
  Output: [-1,-1]

Constraints:
  0 <= len(nums) <= 10^5
  -10^9 <= nums[i], target <= 10^9

Hints:
1. Write one helper: first index where nums[i] >= x (that is bisect_left). Use the half-open template.
2. The first position is lower_bound(target). The last position is lower_bound(target + 1) - 1.
3. Check that the first position is in range and actually holds target before returning.

Expected: O(log n) time, O(1) space.
"""


def search_range(nums: list[int], target: int) -> list[int]:
    raise NotImplementedError


if __name__ == "__main__":
    assert search_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert search_range([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert search_range([], 0) == [-1, -1]
    assert search_range([1], 1) == [0, 0]
    assert search_range([2, 2, 2, 2], 2) == [0, 3]
    assert search_range([1, 2, 3], 3) == [2, 2]
    assert search_range([1, 2, 3], 0) == [-1, -1]
    assert search_range([1, 2, 3], 4) == [-1, -1]
    print("ok")
