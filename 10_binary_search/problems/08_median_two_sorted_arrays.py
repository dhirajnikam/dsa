"""
Problem: Median of Two Sorted Arrays
Difficulty: Hard | Pattern: Binary search on a partition
Source: LeetCode 4

Given two sorted arrays nums1 and nums2 of sizes m and n, return the median of the two
sorted arrays combined. The overall run time complexity should be O(log(m + n)).

Example 1:
  Input: nums1 = [1,3], nums2 = [2]
  Output: 2.0

Example 2:
  Input: nums1 = [1,2], nums2 = [3,4]
  Output: 2.5   (merged = [1,2,3,4], median = (2 + 3) / 2)

Constraints:
  0 <= m, n <= 1000
  1 <= m + n <= 2000
  -10^6 <= nums1[i], nums2[i] <= 10^6

Hints:
1. Make nums1 the shorter array. Binary search i = how many elements of nums1 go in the left
   half; then j = (m + n + 1) // 2 - i elements of nums2 go left too.
2. The partition is correct when nums1[i-1] <= nums2[j] and nums2[j-1] <= nums1[i]. Use
   -inf / +inf for out-of-range neighbors.
3. If nums1[i-1] > nums2[j], i is too big (move hi left); otherwise i is too small.
   Odd total: median = max of left halves. Even: average of max-left and min-right.

Expected: O(log(min(m, n))) time, O(1) space.
"""


def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    raise NotImplementedError


if __name__ == "__main__":
    assert find_median_sorted_arrays([1, 3], [2]) == 2.0
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5
    assert find_median_sorted_arrays([], [1]) == 1.0
    assert find_median_sorted_arrays([2], []) == 2.0
    assert find_median_sorted_arrays([], [1, 2, 3, 4]) == 2.5
    assert find_median_sorted_arrays([1, 2, 3], [4, 5, 6]) == 3.5
    assert find_median_sorted_arrays([4, 5, 6], [1, 2, 3]) == 3.5
    assert find_median_sorted_arrays([1, 1, 1], [1, 1]) == 1.0
    assert find_median_sorted_arrays([-5, 3, 6, 12, 15], [-12, -10, -6, -3, 4, 10]) == 3.0
    import random
    rng = random.Random(4)
    for _ in range(200):
        a = sorted(rng.randint(-50, 50) for _ in range(rng.randint(0, 8)))
        b = sorted(rng.randint(-50, 50) for _ in range(rng.randint(1 if not a else 0, 8)))
        merged = sorted(a + b)
        k = len(merged)
        expected = float(merged[k // 2]) if k % 2 else (merged[k // 2 - 1] + merged[k // 2]) / 2
        assert find_median_sorted_arrays(a, b) == expected, (a, b)
    print("ok")
