"""
Problem: Search in Rotated Sorted Array
Difficulty: Medium | Pattern: Binary search on the sorted half
Source: LeetCode 33

An integer array nums sorted ascending with distinct values was rotated at an unknown pivot,
e.g. [0,1,2,4,5,6,7] became [4,5,6,7,0,1,2]. Given the rotated array and a target, return
the index of target or -1. Must run in O(log n).

Example 1:
  Input: nums = [4,5,6,7,0,1,2], target = 0
  Output: 4

Example 2:
  Input: nums = [4,5,6,7,0,1,2], target = 3
  Output: -1

Example 3:
  Input: nums = [1], target = 0
  Output: -1

Constraints:
  1 <= len(nums) <= 5000
  -10^4 <= nums[i], target <= 10^4
  All values are unique.

Hints:
1. For any mid, at least one of [lo, mid] and [mid, hi] is sorted. nums[lo] <= nums[mid] tells you which.
2. If the left half is sorted and nums[lo] <= target < nums[mid], go left; otherwise go right.
3. Mirror the logic for the case where the right half is the sorted one.

Expected: O(log n) time, O(1) space.
"""


def search(nums: list[int], target: int) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search([1], 0) == -1
    assert search([1], 1) == 0
    assert search([], 5) == -1
    assert search([3, 1], 1) == 1 and search([3, 1], 3) == 0
    assert search([1, 2, 3, 4, 5], 4) == 3   # rotation by 0
    assert search([5, 1, 2, 3, 4], 5) == 0
    assert search([2, 3, 4, 5, 1], 1) == 4
    base = list(range(20))
    for k in range(20):
        rot = base[k:] + base[:k]
        assert all(search(rot, t) == rot.index(t) for t in base)
    print("ok")
