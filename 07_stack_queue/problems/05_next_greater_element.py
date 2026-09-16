"""
Problem: Next Greater Element I
Difficulty: Easy | Pattern: monotonic stack + hash map
Source: LeetCode 496

nums1 is a subset of nums2 (both have distinct integers). For each nums1[i], find its position
in nums2 and return the first element to the RIGHT of it in nums2 that is greater. If none,
return -1. Return the answers in the order of nums1.

Example 1:
  nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2] -> [-1, 3, -1]
Example 2:
  nums1 = [2, 4], nums2 = [1, 2, 3, 4] -> [3, -1]

Constraints:
  1 <= len(nums1) <= len(nums2) <= 1000
  0 <= values <= 10^4, all distinct in each array

Hints:
1. Compute the next greater element for EVERY value in nums2 once, then look up nums1 values.
2. Monotonic stack: iterate nums2; while the top is smaller than the current value, pop it and
   record next_greater[popped] = current.
3. Values are distinct, so a dict value -> next greater works. Default -1.

Expected: O(n + m) time, O(n) space
"""


def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    raise NotImplementedError


if __name__ == "__main__":
    assert next_greater_element([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1], 'Check: next_greater_element([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]'
    assert next_greater_element([2, 4], [1, 2, 3, 4]) == [3, -1], 'Check: next_greater_element([2, 4], [1, 2, 3, 4]) == [3, -1]'
    assert next_greater_element([5], [5]) == [-1], 'Check: next_greater_element([5], [5]) == [-1]'
    assert next_greater_element([1, 2, 3], [3, 2, 1]) == [-1, -1, -1], 'Check: next_greater_element([1, 2, 3], [3, 2, 1]) == [-1, -1, -1]'
    assert next_greater_element([1, 2, 3], [1, 2, 3]) == [2, 3, -1], 'Check: next_greater_element([1, 2, 3], [1, 2, 3]) == [2, 3, -1]'
    assert next_greater_element([3], [1, 3, 2, 5]) == [5], 'Check: next_greater_element([3], [1, 3, 2, 5]) == [5]'
    assert next_greater_element([2, 1], [1, 2]) == [-1, 2], 'Check: next_greater_element([2, 1], [1, 2]) == [-1, 2]'
    print("ok")
