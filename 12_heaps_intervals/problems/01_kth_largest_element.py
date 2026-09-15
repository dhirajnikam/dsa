"""
Problem: Kth Largest Element in an Array
Difficulty: Medium | Pattern: size-k min-heap
Source: LeetCode 215

Given an integer array nums and an integer k, return the k-th largest element in the
array (in sorted order, not the k-th distinct element). Solve it without fully sorting.

Example 1:
  nums = [3, 2, 1, 5, 6, 4], k = 2 -> 5
Example 2:
  nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4 -> 4

Constraints:
  1 <= k <= len(nums) <= 10^5
  -10^4 <= nums[i] <= 10^4

Hints:
1. A min-heap of size k holds the k largest seen so far. What is at the root?
2. Push every number; when the heap exceeds k, pop the smallest.
3. Follow-up: quickselect gives O(n) average. Mention it, code the heap.

Expected: O(n log k) time, O(k) space
"""
import heapq


def find_kth_largest(nums: list[int], k: int) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert find_kth_largest([1], 1) == 1
    assert find_kth_largest([2, 1], 2) == 1
    assert find_kth_largest([5, 5, 5], 2) == 5
    assert find_kth_largest([-1, -2, -3], 1) == -1
    assert find_kth_largest(list(range(100)), 100) == 0
    print("ok")
