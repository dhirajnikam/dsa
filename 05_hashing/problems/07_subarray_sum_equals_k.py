"""
Problem: Subarray Sum Equals K
Difficulty: Medium | Pattern: prefix sum + hash map of prefix counts
Source: LeetCode 560

Given an integer array nums and an integer k, return the number of contiguous subarrays
whose sum equals k.

Example 1:
  nums = [1, 1, 1], k = 2 -> 2
Example 2:
  nums = [1, 2, 3], k = 3 -> 2   ([1, 2] and [3])

Constraints:
  1 <= len(nums) <= 2 * 10^4
  -1000 <= nums[i] <= 1000
  -10^7 <= k <= 10^7

Hints:
1. Negatives are allowed, so sliding window does not work. Brute force is O(n^2).
2. sum(nums[i..j]) = prefix[j] - prefix[i - 1]. You need the count of earlier prefixes equal to prefix[j] - k.
3. Keep a dict prefix_sum -> how many times seen, seeded with {0: 1} (empty prefix).
   At each step: ans += seen[cur - k]; then seen[cur] += 1.

Expected: O(n) time, O(n) space
"""


def subarray_sum(nums: list[int], k: int) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert subarray_sum([1, 1, 1], 2) == 2, 'Check: subarray_sum([1, 1, 1], 2) == 2'
    assert subarray_sum([1, 2, 3], 3) == 2, 'Check: subarray_sum([1, 2, 3], 3) == 2'
    assert subarray_sum([1], 1) == 1, 'Check: subarray_sum([1], 1) == 1'
    assert subarray_sum([1], 0) == 0, 'Check: subarray_sum([1], 0) == 0'
    assert subarray_sum([0, 0, 0], 0) == 6, 'Check: subarray_sum([0, 0, 0], 0) == 6'
    assert subarray_sum([1, -1, 1, -1], 0) == 4, 'Check: subarray_sum([1, -1, 1, -1], 0) == 4'
    assert subarray_sum([-1, -1, 1], 0) == 1, 'Check: subarray_sum([-1, -1, 1], 0) == 1'
    assert subarray_sum([3, 4, 7, 2, -3, 1, 4, 2], 7) == 4, 'Check: subarray_sum([3, 4, 7, 2, -3, 1, 4, 2], 7) == 4'
    print("ok")
