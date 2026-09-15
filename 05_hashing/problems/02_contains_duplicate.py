"""
Problem: Contains Duplicate
Difficulty: Easy | Pattern: set membership
Source: LeetCode 217

Given an integer array nums, return True if any value appears at least twice, False if every
element is distinct.

Example 1:
  nums = [1, 2, 3, 1] -> True
Example 2:
  nums = [1, 2, 3, 4] -> False
Example 3:
  nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2] -> True

Constraints:
  1 <= len(nums) <= 10^5
  -10^9 <= nums[i] <= 10^9

Hints:
1. Sorting then checking neighbours is O(n log n). Fine, but hashing is faster.
2. len(set(nums)) < len(nums) is the one-liner.
3. To return early on the first duplicate, insert into a set as you go and check membership first.

Expected: O(n) time, O(n) space
"""


def contains_duplicate(nums: list[int]) -> bool:
    raise NotImplementedError


if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    assert contains_duplicate([7]) is False
    assert contains_duplicate([]) is False
    assert contains_duplicate([-1, 1, -1]) is True
    assert contains_duplicate([0, 0]) is True
    print("ok")
