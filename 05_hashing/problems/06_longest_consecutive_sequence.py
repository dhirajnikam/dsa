"""
Problem: Longest Consecutive Sequence
Difficulty: Medium | Pattern: set lookups, only start from sequence heads
Source: LeetCode 128

Given an unsorted array of integers nums, return the length of the longest run of consecutive
integers (values, not positions). Must run in O(n).

Example 1:
  nums = [100, 4, 200, 1, 3, 2] -> 4   (1, 2, 3, 4)
Example 2:
  nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1] -> 9

Constraints:
  0 <= len(nums) <= 10^5
  -10^9 <= nums[i] <= 10^9

Hints:
1. Sorting gives O(n log n). The interviewer will ask for O(n).
2. Put everything in a set. For each x, extend upward x+1, x+2, ... while present.
3. Only start counting from x when x - 1 is NOT in the set. Then each element is visited
   at most twice, so total work is O(n).

Expected: O(n) time, O(n) space
"""


def longest_consecutive(nums: list[int]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive([]) == 0
    assert longest_consecutive([1]) == 1
    assert longest_consecutive([2, 2, 2]) == 1
    assert longest_consecutive([-2, -1, 0, 1]) == 4
    assert longest_consecutive([10, 5, 6, 12, 11]) == 3
    assert longest_consecutive([1, 3, 5, 7]) == 1
    print("ok")
