"""
Problem: Combination Sum
Difficulty: Medium | Pattern: Backtracking with reuse + pruning
Source: LeetCode 39

Given an array of distinct integers candidates and a target integer target, return a list of
all unique combinations of candidates where the chosen numbers sum to target. The same number
may be chosen an unlimited number of times. Two combinations are unique if the frequency of
at least one chosen number differs. Return in any order.

Example 1:
  Input: candidates = [2,3,6,7], target = 7
  Output: [[2,2,3],[7]]

Example 2:
  Input: candidates = [2,3,5], target = 8
  Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
  Input: candidates = [2], target = 1
  Output: []

Constraints:
  1 <= len(candidates) <= 30
  2 <= candidates[i] <= 40, all distinct
  1 <= target <= 40

Hints:
1. Like subsets, but recurse with the same index i (not i + 1) to allow reuse.
2. Pass the remaining target down; record the path when it hits 0.
3. Sort candidates; once a candidate exceeds the remaining target, break out of the loop.

Expected: O(n^(target/min_candidate)) time worst case, O(target/min) depth.
"""


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    raise NotImplementedError


def _norm(res):
    return sorted(sorted(c) for c in res)


if __name__ == "__main__":
    assert _norm(combination_sum([2, 3, 6, 7], 7)) == [[2, 2, 3], [7]], 'Check: _norm(combination_sum([2, 3, 6, 7], 7)) == [[2, 2, 3], [7]]'
    assert _norm(combination_sum([2, 3, 5], 8)) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]], 'Check: _norm(combination_sum([2, 3, 5], 8)) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]'
    assert combination_sum([2], 1) == [], 'Check: combination_sum([2], 1) == []'
    assert _norm(combination_sum([1], 2)) == [[1, 1]], 'Check: _norm(combination_sum([1], 2)) == [[1, 1]]'
    assert _norm(combination_sum([7, 3, 2], 7)) == [[2, 2, 3], [7]], 'Check: _norm(combination_sum([7, 3, 2], 7)) == [[2, 2, 3], [7]]'
    assert len(combination_sum([2, 3, 5, 7], 20)) == 18, 'Check: len(combination_sum([2, 3, 5, 7], 20)) == 18'
    print("ok")
