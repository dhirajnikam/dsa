"""
Problem: Number of Connected Components in an Undirected Graph
Difficulty: Medium | Pattern: union-find
Source: LeetCode 323

You have n nodes labeled 0..n-1 and a list of undirected edges. Return the number of
connected components.

Example 1:
  n = 5, edges = [[0, 1], [1, 2], [3, 4]] -> 2
Example 2:
  n = 5, edges = [[0, 1], [1, 2], [2, 3], [3, 4]] -> 1

Constraints:
  1 <= n <= 2000
  No duplicate edges, no self-loops.

Hints:
1. Start with n components. Each successful union (different roots) reduces the count by 1.
2. Union-find with path compression and union by rank. Or DFS from every unvisited node.

Expected: O((V + E) * alpha(V)) time, O(V) space
"""


def count_components(n: int, edges: list[list[int]]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert count_components(5, [[0, 1], [1, 2], [3, 4]]) == 2, 'Check: count_components(5, [[0, 1], [1, 2], [3, 4]]) == 2'
    assert count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1, 'Check: count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1'
    assert count_components(1, []) == 1, 'Check: count_components(1, []) == 1'
    assert count_components(4, []) == 4, 'Check: count_components(4, []) == 4'
    assert count_components(3, [[0, 1], [1, 2], [0, 2]]) == 1, 'Check: count_components(3, [[0, 1], [1, 2], [0, 2]]) == 1'
    assert count_components(6, [[0, 1], [2, 3], [4, 5]]) == 3, 'Check: count_components(6, [[0, 1], [2, 3], [4, 5]]) == 3'
    assert count_components(6, [[0, 1], [2, 3], [4, 5], [1, 2], [3, 4]]) == 1, 'Check: count_components(6, [[0, 1], [2, 3], [4, 5], [1, 2], [3, 4]]) == 1'
    print("ok")
