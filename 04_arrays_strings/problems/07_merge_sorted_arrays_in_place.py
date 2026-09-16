"""
Problem: Merge Sorted Array
Difficulty: Easy | Pattern: two-array merge from the back
Source: LeetCode 88

You are given two sorted integer arrays nums1 and nums2 and integers m and n, the number of
real elements in each. nums1 has length m + n; its last n slots are 0 placeholders.
Merge nums2 into nums1 so that nums1 is sorted, IN PLACE (return None).

Example 1:
  nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3 -> nums1 = [1, 2, 2, 3, 5, 6]
Example 2:
  nums1 = [1], m = 1, nums2 = [], n = 0 -> nums1 = [1]
Example 3:
  nums1 = [0], m = 0, nums2 = [1], n = 1 -> nums1 = [1]

Constraints:
  0 <= m, n <= 200,  1 <= m + n <= 200
  -10^9 <= values <= 10^9

Hints:
1. Merging from the front overwrites nums1 values you still need.
2. Fill from the back: compare nums1[i] and nums2[j], write the larger at position k = m + n - 1.
3. When nums1 runs out first, copy the rest of nums2. When nums2 runs out first, nothing left to do.

Expected: O(m + n) time, O(1) space
"""


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    raise NotImplementedError


if __name__ == "__main__":
    a = [1, 2, 3, 0, 0, 0]
    merge(a, 3, [2, 5, 6], 3)
    assert a == [1, 2, 2, 3, 5, 6], 'Check: a == [1, 2, 2, 3, 5, 6]'
    a = [1]
    merge(a, 1, [], 0)
    assert a == [1], 'Check: a == [1]'
    a = [0]
    merge(a, 0, [1], 1)
    assert a == [1], 'Check: a == [1]'
    a = [4, 5, 6, 0, 0, 0]
    merge(a, 3, [1, 2, 3], 3)
    assert a == [1, 2, 3, 4, 5, 6], 'Check: a == [1, 2, 3, 4, 5, 6]'
    a = [1, 2, 3, 0, 0, 0]
    merge(a, 3, [4, 5, 6], 3)
    assert a == [1, 2, 3, 4, 5, 6], 'Check: a == [1, 2, 3, 4, 5, 6]'
    a = [-3, 0, 0]
    merge(a, 1, [-5, -4], 2)
    assert a == [-5, -4, -3], 'Check: a == [-5, -4, -3]'
    a = [2, 2, 0, 0]
    merge(a, 2, [2, 2], 2)
    assert a == [2, 2, 2, 2], 'Check: a == [2, 2, 2, 2]'
    print("ok")
