"""
Problem: Assign Cookies
Difficulty: Easy | Pattern: Greedy (sort both, two pointers)
Source: LeetCode 455

Child i has greed factor g[i]; cookie j has size s[j]. A child is content if assigned a
cookie with s[j] >= g[i]. Each child gets at most one cookie and each cookie goes to at
most one child. Return the maximum number of content children.

Example 1: g = [1, 2, 3], s = [1, 1] -> 1
Example 2: g = [1, 2], s = [1, 2, 3] -> 2

Hints:
1. Sort both arrays.
2. Give the smallest cookie that satisfies the least greedy unsatisfied child; otherwise
   discard that cookie (it satisfies nobody).
3. Exchange argument: using a bigger cookie on the least greedy child can only waste capacity.

Expected: O(n log n + m log m) time, O(1) extra space (ignoring sort)
"""


def find_content_children(g: list[int], s: list[int]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert find_content_children([1, 2, 3], [1, 1]) == 1, 'Check: find_content_children([1, 2, 3], [1, 1]) == 1'
    assert find_content_children([1, 2], [1, 2, 3]) == 2, 'Check: find_content_children([1, 2], [1, 2, 3]) == 2'
    assert find_content_children([], [1, 2]) == 0, 'Check: find_content_children([], [1, 2]) == 0'
    assert find_content_children([1, 2], []) == 0, 'Check: find_content_children([1, 2], []) == 0'
    assert find_content_children([10, 9, 8], [5, 6, 7]) == 0, 'Check: find_content_children([10, 9, 8], [5, 6, 7]) == 0'
    assert find_content_children([1, 1, 1], [1]) == 1, 'Check: find_content_children([1, 1, 1], [1]) == 1'
    assert find_content_children([3, 1, 2], [1, 3, 2]) == 3, 'Check: find_content_children([3, 1, 2], [1, 3, 2]) == 3'
    assert find_content_children([2, 2, 2], [3, 3, 3, 3]) == 3, 'Check: find_content_children([2, 2, 2], [3, 3, 3, 3]) == 3'
    print("ok")
