"""
Problem: Combinations
Difficulty: Medium | Pattern: Backtracking (start index + size)
Source: LeetCode 77

Given two integers n and k, return all possible combinations of k numbers chosen from the
range [1, n]. Return the answer in any order.

Example 1:
  Input: n = 4, k = 2
  Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

Example 2:
  Input: n = 1, k = 1
  Output: [[1]]

Constraints:
  1 <= n <= 20
  1 <= k <= n

Hints:
1. Same as subsets with a start index, but only record paths of length exactly k.
2. Prune: if the remaining numbers (n - i + 1) cannot fill the remaining slots (k - len(path)), stop.
3. Loop upper bound can be n - (k - len(path)) + 1 to skip hopeless branches.

Expected: O(k * C(n, k)) time, O(k) extra space.
"""


def combine(n: int, k: int) -> list[list[int]]:
    raise NotImplementedError


if __name__ == "__main__":
    assert sorted(combine(4, 2)) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert combine(1, 1) == [[1]]
    assert sorted(combine(3, 3)) == [[1, 2, 3]]
    assert sorted(combine(3, 1)) == [[1], [2], [3]]
    out = combine(10, 5)
    assert len(out) == 252 and len(set(map(tuple, out))) == 252
    assert all(len(c) == 5 and c == sorted(c) for c in out)
    assert len(combine(20, 1)) == 20
    print("ok")
