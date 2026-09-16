"""
Problem: Minimum Number of Arrows to Burst Balloons
Difficulty: Medium | Pattern: Greedy (interval scheduling, sort by end)
Source: LeetCode 452

Each balloon is a horizontal interval [x_start, x_end]. An arrow shot vertically at x
bursts every balloon with x_start <= x <= x_end. Return the minimum number of arrows.

Example 1: points = [[10, 16], [2, 8], [1, 6], [7, 12]] -> 2
Example 2: points = [[1, 2], [3, 4], [5, 6], [7, 8]] -> 4
Example 3: points = [[1, 2], [2, 3], [3, 4], [4, 5]] -> 2   (touching counts as overlap)

Hints:
1. Sort by end. Shoot the first arrow at the first end.
2. Every balloon whose start <= that arrow position is burst. The next balloon that starts
   after it needs a new arrow, placed at its end.
3. Exchange argument: shooting earlier than the earliest end cannot burst more balloons.
4. Coordinates may be large negatives/positives; do not assume they fit in a fixed range.

Expected: O(n log n) time, O(1) extra space
"""


def find_min_arrow_shots(points: list[list[int]]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert find_min_arrow_shots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2, 'Check: find_min_arrow_shots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2'
    assert find_min_arrow_shots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4, 'Check: find_min_arrow_shots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4'
    assert find_min_arrow_shots([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2, 'Check: find_min_arrow_shots([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2'
    assert find_min_arrow_shots([[1, 2]]) == 1, 'Check: find_min_arrow_shots([[1, 2]]) == 1'
    assert find_min_arrow_shots([]) == 0, 'Check: find_min_arrow_shots([]) == 0'
    assert find_min_arrow_shots([[1, 10], [2, 3], [4, 5]]) == 2, 'Check: find_min_arrow_shots([[1, 10], [2, 3], [4, 5]]) == 2'
    assert find_min_arrow_shots([[-2147483648, 2147483647], [0, 0]]) == 1, 'Check: find_min_arrow_shots([[-2147483648, 2147483647], [0, 0]]) == 1'
    assert find_min_arrow_shots([[3, 3], [3, 3], [3, 3]]) == 1, 'Check: find_min_arrow_shots([[3, 3], [3, 3], [3, 3]]) == 1'
    print("ok")
