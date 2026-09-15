"""
Problem: Top K Frequent Elements
Difficulty: Medium | Pattern: frequency map + bucket sort (or heap)
Source: LeetCode 347

Given an integer array nums and an integer k, return the k most frequent elements,
in any order. The answer is guaranteed to be unique.

Example 1:
  nums = [1, 1, 1, 2, 2, 3], k = 2 -> [1, 2]
Example 2:
  nums = [1], k = 1 -> [1]

Constraints:
  1 <= len(nums) <= 10^5
  -10^4 <= nums[i] <= 10^4
  1 <= k <= number of distinct elements

Hints:
1. Counter(nums).most_common(k) solves it in one line (O(n log n)). Know it, then beat it.
2. heapq.nlargest(k, counts, key=counts.get) is O(n log k).
3. O(n): bucket by frequency. buckets[f] = list of values with frequency f (f <= n).
   Walk buckets from high to low until you have k items.

Expected: O(n) time, O(n) space
"""


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    raise NotImplementedError


if __name__ == "__main__":
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
    assert sorted(top_k_frequent([4, 4, 4, 5, 5, 6], 1)) == [4]
    assert sorted(top_k_frequent([1, 2, 3], 3)) == [1, 2, 3]
    assert sorted(top_k_frequent([-1, -1, 2], 1)) == [-1]
    assert sorted(top_k_frequent([5, 5, 5, 5], 1)) == [5]
    assert sorted(top_k_frequent([3, 0, 1, 0, 3, 3, 1, 2], 2)) == [0, 3]
    print("ok")
