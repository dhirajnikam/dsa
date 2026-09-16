"""
Problem: Remove Duplicates from Sorted Array
Difficulty: Easy | Pattern: same-direction (read/write) pointers
Source: LeetCode 26

Given a sorted integer array nums, remove duplicates IN PLACE so each element appears once,
preserving relative order. Return the number k of unique elements; the first k slots of nums
must hold them. Content beyond k does not matter.

Example 1:
  nums = [1, 1, 2] -> 2, nums[:2] = [1, 2]
Example 2:
  nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] -> 5, nums[:5] = [0, 1, 2, 3, 4]

Constraints:
  1 <= len(nums) <= 3 * 10^4
  -100 <= nums[i] <= 100
  sorted non-decreasing

Hints:
1. Because it is sorted, duplicates are adjacent. Compare each element with the last kept one.
2. Write pointer w = 1 (first element always kept). For each read index r, if nums[r] != nums[w - 1]: nums[w] = nums[r]; w += 1.
3. Same template solves "remove element", "move zeroes", "remove duplicates allowing 2 copies" (compare with nums[w - 2]).

Expected: O(n) time, O(1) space
"""


def remove_duplicates(nums: list[int]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    a = [1, 1, 2]
    k = remove_duplicates(a)
    assert k == 2 and a[:k] == [1, 2], 'Check: k == 2 and a[:k] == [1, 2]'
    a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates(a)
    assert k == 5 and a[:k] == [0, 1, 2, 3, 4], 'Check: k == 5 and a[:k] == [0, 1, 2, 3, 4]'
    a = [7]
    k = remove_duplicates(a)
    assert k == 1 and a[:k] == [7], 'Check: k == 1 and a[:k] == [7]'
    a = [2, 2, 2, 2]
    k = remove_duplicates(a)
    assert k == 1 and a[:k] == [2], 'Check: k == 1 and a[:k] == [2]'
    a = [1, 2, 3]
    k = remove_duplicates(a)
    assert k == 3 and a[:k] == [1, 2, 3], 'Check: k == 3 and a[:k] == [1, 2, 3]'
    a = [-3, -3, -1, 0, 0]
    k = remove_duplicates(a)
    assert k == 3 and a[:k] == [-3, -1, 0], 'Check: k == 3 and a[:k] == [-3, -1, 0]'
    a = []
    assert remove_duplicates(a) == 0, 'Check: remove_duplicates(a) == 0'
    print("ok")
