"""
Problem: Two Sum II - Input Array Is Sorted
Difficulty: Medium | Pattern: opposite-direction pointers on sorted input
Source: LeetCode 167

Given a 1-indexed array of integers numbers sorted in non-decreasing order, find two numbers
that add up to target. Return their 1-based indices [i, j] with i < j. Exactly one solution
exists. Use O(1) extra space.

Example 1:
  numbers = [2, 7, 11, 15], target = 9 -> [1, 2]
Example 2:
  numbers = [2, 3, 4], target = 6 -> [1, 3]
Example 3:
  numbers = [-1, 0], target = -1 -> [1, 2]

Constraints:
  2 <= len(numbers) <= 3 * 10^4
  -1000 <= numbers[i], target <= 1000

Hints:
1. A hash map works but uses O(n) space. Sorted input is the clue for pointers.
2. l = 0, r = n - 1. If the sum is too small, only moving l right can increase it.
   If too big, only moving r left can decrease it.
3. Return 1-based indices: [l + 1, r + 1].

Expected: O(n) time, O(1) space
"""


def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    raise NotImplementedError


if __name__ == "__main__":
    assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2], 'Check: two_sum_sorted([2, 7, 11, 15], 9) == [1, 2]'
    assert two_sum_sorted([2, 3, 4], 6) == [1, 3], 'Check: two_sum_sorted([2, 3, 4], 6) == [1, 3]'
    assert two_sum_sorted([-1, 0], -1) == [1, 2], 'Check: two_sum_sorted([-1, 0], -1) == [1, 2]'
    assert two_sum_sorted([1, 2], 3) == [1, 2], 'Check: two_sum_sorted([1, 2], 3) == [1, 2]'
    assert two_sum_sorted([-5, -3, 0, 2, 8], 5) == [2, 5], 'Check: two_sum_sorted([-5, -3, 0, 2, 8], 5) == [2, 5]'
    assert two_sum_sorted([0, 0, 3, 4], 0) == [1, 2], 'Check: two_sum_sorted([0, 0, 3, 4], 0) == [1, 2]'
    # Boundary and misconception checks: predict each result before running.
    assert two_sum_sorted([1, 1], 2) == [1, 2], 'Check: two_sum_sorted([1, 1], 2) == [1, 2]'
    assert two_sum_sorted([-8, -2, 1, 4, 9], 2) == [2, 4], 'Check: two_sum_sorted([-8, -2, 1, 4, 9], 2) == [2, 4]'
    print("ok")
