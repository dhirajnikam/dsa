"""
Problem: Subsets
Difficulty: Medium | Pattern: Backtracking (include/exclude)
Source: LeetCode 78

Given an integer array nums of unique elements, return all possible subsets (the power set)
in any order. The solution set must not contain duplicate subsets.

Example 1:
  Input: nums = [1,2,3]
  Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
  Input: nums = [0]
  Output: [[],[0]]

Constraints:
  1 <= len(nums) <= 10
  -10 <= nums[i] <= 10
  All numbers are unique.

Hints:
1. Every element is either in or out of the subset: a binary tree of depth n with 2^n leaves.
2. Or: at each call, record the current path, then try adding each element from a start index onward.
3. Append a copy of path, never path itself.

Expected: O(n * 2^n) time, O(n) extra space (excluding output).
"""


def subsets(nums: list[int]) -> list[list[int]]:
    raise NotImplementedError


def _norm(res: list[list[int]]) -> list[list[int]]:
    return sorted(sorted(s) for s in res)


if __name__ == "__main__":
    assert _norm(subsets([1, 2, 3])) == _norm([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
    assert _norm(subsets([0])) == [[], [0]]
    assert _norm(subsets([])) == [[]]
    assert len(subsets([1, 2, 3, 4, 5])) == 32
    assert len(set(map(tuple, map(sorted, subsets([1, 2, 3, 4]))))) == 16
    assert _norm(subsets([-1, 2])) == _norm([[], [-1], [2], [-1, 2]])
    print("ok")
