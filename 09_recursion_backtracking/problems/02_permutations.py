"""
Problem: Permutations
Difficulty: Medium | Pattern: Backtracking (used array)
Source: LeetCode 46

Given an array nums of distinct integers, return all possible permutations in any order.

Example 1:
  Input: nums = [1,2,3]
  Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
  Input: nums = [0,1]
  Output: [[0,1],[1,0]]

Example 3:
  Input: nums = [1]
  Output: [[1]]

Constraints:
  1 <= len(nums) <= 6
  -10 <= nums[i] <= 10
  All integers are unique.

Hints:
1. At each level pick any element not yet used. Depth n, n! leaves.
2. Track used elements with a boolean list (or a set) and restore it on the way back.
3. The path is complete when len(path) == len(nums).

Expected: O(n * n!) time, O(n) extra space.
"""


def permute(nums: list[int]) -> list[list[int]]:
    raise NotImplementedError


if __name__ == "__main__":
    assert sorted(permute([1, 2, 3])) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]], 'Check: sorted(permute([1, 2, 3])) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]'
    assert sorted(permute([0, 1])) == [[0, 1], [1, 0]], 'Check: sorted(permute([0, 1])) == [[0, 1], [1, 0]]'
    assert permute([1]) == [[1]], 'Check: permute([1]) == [[1]]'
    assert permute([]) == [[]], 'Check: permute([]) == [[]]'
    out = permute([1, 2, 3, 4])
    assert len(out) == 24 and len(set(map(tuple, out))) == 24, 'Check: len(out) == 24 and len(set(map(tuple, out))) == 24'
    assert all(sorted(p) == [1, 2, 3, 4] for p in out), 'Check: all(sorted(p) == [1, 2, 3, 4] for p in out)'
    print("ok")
