"""
Problem: Find Minimum in Rotated Sorted Array
Difficulty: Medium | Pattern: Boundary binary search on rotation
Source: LeetCode 153

A sorted array of unique integers was rotated between 1 and n times. Return the minimum
element. Must run in O(log n).

Example 1:
  Input: nums = [3,4,5,1,2]
  Output: 1

Example 2:
  Input: nums = [4,5,6,7,0,1,2]
  Output: 0

Example 3:
  Input: nums = [11,13,15,17]
  Output: 11

Constraints:
  1 <= len(nums) <= 5000
  -5000 <= nums[i] <= 5000
  All integers are unique.

Hints:
1. Compare nums[mid] with nums[hi]. If nums[mid] > nums[hi], the drop (minimum) is to the right.
2. Otherwise the minimum is at mid or to the left: hi = mid (keep mid).
3. Use lo < hi so the loop ends with lo == hi pointing at the minimum.

Expected: O(log n) time, O(1) space.
"""


def find_min(nums: list[int]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert find_min([3, 4, 5, 1, 2]) == 1
    assert find_min([4, 5, 6, 7, 0, 1, 2]) == 0
    assert find_min([11, 13, 15, 17]) == 11
    assert find_min([1]) == 1
    assert find_min([2, 1]) == 1
    assert find_min([1, 2]) == 1
    assert find_min([5, 1, 2, 3, 4]) == 1
    assert find_min([2, 3, 4, 5, 1]) == 1
    base = list(range(-10, 10))
    assert all(find_min(base[k:] + base[:k]) == -10 for k in range(20))
    print("ok")
