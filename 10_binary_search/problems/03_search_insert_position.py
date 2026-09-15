"""
Problem: Search Insert Position
Difficulty: Easy | Pattern: Boundary binary search (half-open)
Source: LeetCode 35

Given a sorted array of distinct integers and a target value, return the index if the target
is found. If not, return the index where it would be inserted to keep the array sorted.
Must run in O(log n).

Example 1:
  Input: nums = [1,3,5,6], target = 5
  Output: 2

Example 2:
  Input: nums = [1,3,5,6], target = 2
  Output: 1

Example 3:
  Input: nums = [1,3,5,6], target = 7
  Output: 4

Constraints:
  1 <= len(nums) <= 10^4
  -10^4 <= nums[i], target <= 10^4
  nums contains distinct values sorted ascending.

Hints:
1. This is exactly "first index i where nums[i] >= target", which can be len(nums).
2. lo, hi = 0, len(nums); while lo < hi: ... hi = mid or lo = mid + 1; return lo.
3. Compare with bisect.bisect_left to check your implementation.

Expected: O(log n) time, O(1) space.
"""


def search_insert(nums: list[int], target: int) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert search_insert([1, 3, 5, 6], 5) == 2
    assert search_insert([1, 3, 5, 6], 2) == 1
    assert search_insert([1, 3, 5, 6], 7) == 4
    assert search_insert([1, 3, 5, 6], 0) == 0
    assert search_insert([1], 0) == 0 and search_insert([1], 1) == 0 and search_insert([1], 2) == 1
    assert search_insert([], 3) == 0
    from bisect import bisect_left
    a = list(range(0, 100, 3))
    assert all(search_insert(a, t) == bisect_left(a, t) for t in range(-2, 105))
    print("ok")
