"""
Problem: Largest Rectangle in Histogram
Difficulty: Hard | Pattern: monotonic increasing stack with sentinel
Source: LeetCode 84

Given an array heights of bar heights (each bar width 1), return the area of the largest
rectangle that fits inside the histogram.

Example 1:
  heights = [2, 1, 5, 6, 2, 3] -> 10   (bars 5 and 6, height 5 * width 2)
Example 2:
  heights = [2, 4] -> 4

Constraints:
  1 <= len(heights) <= 10^5
  0 <= heights[i] <= 10^4

Hints:
1. For each bar, the best rectangle using its full height extends left and right until a
   shorter bar. Brute force finding those bounds is O(n^2).
2. Monotonic increasing stack of indices. When heights[i] < heights[top], the top's right
   bound is i and its left bound is the new top (after popping) + 1. Area = h * (i - left - 1).
3. Append a 0 sentinel to heights (or loop to n inclusive with height 0) so every bar is popped.

Expected: O(n) time, O(n) space
"""


def largest_rectangle_area(heights: list[int]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert largest_rectangle_area([2, 1, 5, 6, 2, 3]) == 10, 'Check: largest_rectangle_area([2, 1, 5, 6, 2, 3]) == 10'
    assert largest_rectangle_area([2, 4]) == 4, 'Check: largest_rectangle_area([2, 4]) == 4'
    assert largest_rectangle_area([7]) == 7, 'Check: largest_rectangle_area([7]) == 7'
    assert largest_rectangle_area([0]) == 0, 'Check: largest_rectangle_area([0]) == 0'
    assert largest_rectangle_area([3, 3, 3]) == 9, 'Check: largest_rectangle_area([3, 3, 3]) == 9'
    assert largest_rectangle_area([1, 2, 3, 4, 5]) == 9, 'Check: largest_rectangle_area([1, 2, 3, 4, 5]) == 9'
    assert largest_rectangle_area([5, 4, 3, 2, 1]) == 9, 'Check: largest_rectangle_area([5, 4, 3, 2, 1]) == 9'
    assert largest_rectangle_area([2, 1, 2]) == 3, 'Check: largest_rectangle_area([2, 1, 2]) == 3'
    assert largest_rectangle_area([0, 9]) == 9, 'Check: largest_rectangle_area([0, 9]) == 9'
    assert largest_rectangle_area([4, 2, 0, 3, 2, 5]) == 6, 'Check: largest_rectangle_area([4, 2, 0, 3, 2, 5]) == 6'
    print("ok")
