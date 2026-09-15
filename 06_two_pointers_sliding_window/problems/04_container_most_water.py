"""
Problem: Container With Most Water
Difficulty: Medium | Pattern: opposite pointers, move the shorter side
Source: LeetCode 11

You are given an array height of length n. There are n vertical lines; the i-th line goes
from (i, 0) to (i, height[i]). Find two lines that together with the x-axis form a container
holding the most water. Return the maximum amount. Water = min(height[l], height[r]) * (r - l).

Example 1:
  height = [1, 8, 6, 2, 5, 4, 8, 3, 7] -> 49   (lines at index 1 and 8)
Example 2:
  height = [1, 1] -> 1

Constraints:
  2 <= n <= 10^5
  0 <= height[i] <= 10^4

Hints:
1. Brute force O(n^2) over pairs. Too slow at 10^5.
2. Start with the widest container (l = 0, r = n - 1). Shrinking width can only help if the
   limiting (shorter) side gets taller, so move the pointer at the shorter line.
3. Prove it to yourself: moving the taller side never increases min(h[l], h[r]).

Expected: O(n) time, O(1) space
"""


def max_area(height: list[int]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([4, 3, 2, 1, 4]) == 16
    assert max_area([1, 2, 1]) == 2
    assert max_area([0, 0]) == 0
    assert max_area([5, 5, 5, 5]) == 15
    assert max_area([1, 2, 4, 3]) == 4
    assert max_area([2, 3, 4, 5, 18, 17, 6]) == 17
    print("ok")
