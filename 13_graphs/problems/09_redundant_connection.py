"""
Problem: Redundant Connection
Difficulty: Medium | Pattern: union-find cycle edge
Source: LeetCode 684

A tree with n nodes (1..n) had one extra edge added, producing a graph with exactly one
cycle. edges is that graph's edge list. Return the edge that can be removed to make it a
tree again. If several answers exist, return the one that appears last in the input.

Example 1:
  edges = [[1, 2], [1, 3], [2, 3]] -> [2, 3]
Example 2:
  edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]] -> [1, 4]

Constraints:
  3 <= n <= 1000
  No repeated edges.

Hints:
1. Process edges in order with union-find. The first edge whose endpoints are already
   connected closes the cycle.
2. Because it is the last such edge in input order that we need, and only one cycle
   exists, the first failing union is exactly that edge.

Expected: O(n * alpha(n)) time, O(n) space
"""


def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    raise NotImplementedError


if __name__ == "__main__":
    assert find_redundant_connection([[1, 2], [1, 3], [2, 3]]) == [2, 3], 'Check: find_redundant_connection([[1, 2], [1, 3], [2, 3]]) == [2, 3]'
    assert find_redundant_connection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4], 'Check: find_redundant_connection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]'
    assert find_redundant_connection([[1, 2], [2, 3], [1, 3]]) == [1, 3], 'Check: find_redundant_connection([[1, 2], [2, 3], [1, 3]]) == [1, 3]'
    assert find_redundant_connection([[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]]) == [2, 5], 'Check: find_redundant_connection([[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]]) == [2, 5]'
    assert find_redundant_connection([[1, 4], [3, 4], [1, 3], [1, 2], [4, 5]]) == [1, 3], 'Check: find_redundant_connection([[1, 4], [3, 4], [1, 3], [1, 2], [4, 5]]) == [1, 3]'
    assert find_redundant_connection([[2, 3], [3, 4], [4, 5], [5, 2], [1, 2]]) == [5, 2], 'Check: find_redundant_connection([[2, 3], [3, 4], [4, 5], [5, 2], [1, 2]]) == [5, 2]'
    print("ok")
